#!/usr/bin/env python3
"""Deterministic arithmetic self-consistency of the summary table behind a figure.

A bar/point in a figure is only as trustworthy as the mean/SD/SEM/n it stands
for. This checks that those reported numbers are mutually possible. Only rules
that are mathematically always true are flagged as must_fix, so a clean table
produces no output and nothing assumes bad faith.

Rules on a summary table (columns: group/label, mean, sd, sem, n, min, max):
  - n must be a positive integer            (must_fix if not)
  - sd, sem must be >= 0                     (must_fix if negative)
  - min <= mean <= max                       (must_fix: transcription error)
  - reported sem ~= sd / sqrt(n)             (check: SD/SEM often swapped)

Optional GRIM (--integer-columns): for means computed from INTEGER items only
(counts, Likert), verifies the mean is achievable at its stated precision. This
does NOT apply to continuous measurements (protein intensities etc.), so it is
off by default to avoid false positives.
"""
# Attribution: adapted from the "academic-integrity-skill" project by lanj
# (GitHub @1anj), MIT License, Copyright (c) 2026 lanj.
# Source: https://github.com/1anj/academic-integrity-skill @ 135073a
# The recompute-and-flag concept comes from scripts/stats_consistency_check.py.
# The min<=mean<=max range check, the SEM=SD/sqrt(n) consistency check and the
# GRIM check are original. See ATTRIBUTION.md for the full upstream license.
from __future__ import annotations

import argparse
from typing import Dict, List, Optional

from figurecheck_common import add_common_args, emit_result, load_table, make_item, make_result, parse_float


def find_col(row: Dict[str, object], names: List[str]) -> Optional[str]:
    lower = {str(k).lower(): k for k in row.keys()}
    for name in names:
        if name in lower:
            return lower[name]
    return None


def decimals(value: object) -> int:
    text = str(value).strip()
    if "." in text and "e" not in text.lower():
        return len(text.split(".", 1)[1])
    return 0


def grim_ok(reported_mean: float, n: int, ndec: int) -> bool:
    if n <= 0:
        return True
    scale = 10 ** ndec
    target = round(reported_mean * scale)
    for total in (int(reported_mean * n), int(reported_mean * n) + 1, round(reported_mean * n)):
        if round((total / n) * scale) == target:
            return True
    return False


def run(path: str, integer_columns: List[str]) -> Dict[str, object]:
    rows = load_table(path)
    items: List[Dict[str, object]] = []
    int_cols = {c.lower() for c in integer_columns}

    for row in rows:
        gcol = find_col(row, ["group", "label", "name", "condition", "column"])
        loc = str(row.get(gcol)) if gcol else "row"

        n = parse_float(row.get(find_col(row, ["n", "sample_size"]) or ""))
        mean_v = parse_float(row.get(find_col(row, ["mean", "average", "avg"]) or ""))
        sd_v = parse_float(row.get(find_col(row, ["sd", "std", "standard_deviation"]) or ""))
        sem_v = parse_float(row.get(find_col(row, ["sem", "se", "stderr"]) or ""))
        min_v = parse_float(row.get(find_col(row, ["min", "minimum"]) or ""))
        max_v = parse_float(row.get(find_col(row, ["max", "maximum"]) or ""))

        if n is not None and (n <= 0 or abs(n - round(n)) > 1e-9):
            items.append(make_item(
                check="stats_sanity", status="must_fix", location=loc,
                message="n is not a positive integer.",
                benign_explanation="Likely a typo or a merged cell read wrong.",
                fix="Enter n as a positive whole number.",
                details={"n": n},
            ))
        for label, val in (("SD", sd_v), ("SEM", sem_v)):
            if val is not None and val < 0:
                items.append(make_item(
                    check="stats_sanity", status="must_fix", location=loc,
                    message=f"{label} is negative.",
                    benign_explanation="A stray minus sign or a subtraction error.",
                    fix=f"{label} cannot be negative; recompute.",
                    details={label.lower(): val},
                ))
        if mean_v is not None and min_v is not None and max_v is not None:
            if not (min_v - 1e-9 <= mean_v <= max_v + 1e-9):
                items.append(make_item(
                    check="stats_sanity", status="must_fix", location=loc,
                    message="Mean lies outside the reported [min, max] range.",
                    benign_explanation="Usually a transcription error in one of the three numbers.",
                    fix="Recheck mean, min and max against the source data.",
                    details={"mean": mean_v, "min": min_v, "max": max_v},
                ))
        if sd_v is not None and sem_v is not None and n is not None and n > 0:
            implied = sd_v / (n ** 0.5)
            if abs(implied - sem_v) > max(1e-6, 5e-2 * max(abs(implied), abs(sem_v))):
                items.append(make_item(
                    check="stats_sanity", status="check", location=loc,
                    message="Reported SEM is not consistent with SD/sqrt(n).",
                    benign_explanation="SD and SEM are commonly swapped, or one predates a change in n.",
                    fix="Decide which the figure shows and make SD, SEM and n mutually consistent.",
                    details={"reported_sem": sem_v, "sd_over_sqrt_n": round(implied, 6), "n": int(n)},
                ))
        if gcol and str(row.get(gcol)).lower() in int_cols and mean_v is not None and n is not None and n > 0:
            mcol = find_col(row, ["mean", "average", "avg"])
            ndec = decimals(row.get(mcol))
            if ndec > 0 and not grim_ok(mean_v, int(round(n)), ndec):
                items.append(make_item(
                    check="stats_sanity_grim", status="check", location=loc,
                    message="Mean of integer-valued items is not achievable at its stated precision (GRIM).",
                    benign_explanation="Rounding during reporting, or n counted differently; only meaningful for count/Likert data.",
                    fix="Confirm n and recompute the mean, or report decimals consistently.",
                    details={"mean": mean_v, "n": int(round(n)), "decimals": ndec},
                ))

    return make_result(
        tool="stats_sanity",
        input_value=path,
        items=items,
        limitations=[
            "Only checks arithmetic self-consistency of reported summaries; it does not judge the analysis.",
            "GRIM applies to integer-item means only and is off unless columns are named with --integer-columns.",
        ],
        metadata={"rows": len(rows), "integer_columns": integer_columns},
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic sanity check of the statistics table behind a figure.")
    p.add_argument("input", help="Summary table CSV/TSV/XLSX")
    p.add_argument("--integer-columns", default="", help="Comma-separated group labels whose items are integers (enables GRIM)")
    add_common_args(p)
    a = p.parse_args()
    cols = [c.strip() for c in a.integer_columns.split(",") if c.strip()]
    emit_result(run(a.input, cols), a.format, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
