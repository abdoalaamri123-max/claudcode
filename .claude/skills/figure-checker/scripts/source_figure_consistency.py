#!/usr/bin/env python3
"""Check that the mean / SD / SEM / n written into a figure or table actually
match the numbers recomputed from the source data.

This is the single most useful honest-error catcher: it finds stale values left
over after re-running an analysis, a wrong column plotted, SEM accidentally
labeled as SD, or a mistyped n. Every mismatch is deterministic, so there are
essentially no false positives once the tolerance is set sensibly.

Source data may be in either layout, auto-detected (override with --layout):
  wide : one column per group, values stacked down each column.
  long : one row per observation, with a group/label column and a value column.

Reported table must have one row per group with columns named (case-insensitive)
some of: group/label/condition, mean, sd, sem, n.
"""
# Attribution: adapted from the "academic-integrity-skill" project by lanj
# (GitHub @1anj), MIT License, Copyright (c) 2026 lanj.
# Source: https://github.com/1anj/academic-integrity-skill @ 135073a
# Derived from scripts/graph_source_consistency.py. The good-faith reframing,
# status/benign-explanation model, the SD-vs-SEM swap heuristic and the
# wide/long layout auto-detection are original.
# See ATTRIBUTION.md for the full upstream license.
from __future__ import annotations

import argparse
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from figurecheck_common import (
    add_common_args, emit_result, load_table, make_item, make_result,
    mean, numeric_columns, parse_float, sample_sd,
)

GROUP_HINTS = {"group", "label", "condition", "name", "class", "category",
               "sample", "protein", "gene", "feature", "region", "compartment"}
VALUE_HINTS = {"value", "intensity", "abundance", "expression", "level",
               "measurement", "reading", "signal", "quant", "lfq", "ratio"}


def find_col(row: Dict[str, object], names: List[str]) -> Optional[str]:
    lower = {str(k).lower(): k for k in row.keys()}
    for name in names:
        if name in lower:
            return lower[name]
    return None


def numeric_fraction(rows, col) -> float:
    total = num = 0
    for r in rows:
        v = r.get(col)
        if v is None or str(v).strip() == "":
            continue
        total += 1
        if parse_float(v) is not None:
            num += 1
    return num / total if total else 0.0


def has_repeats(rows, col) -> bool:
    vals = [str(r.get(col)).strip() for r in rows if str(r.get(col)).strip()]
    uniq = set(vals)
    return 2 <= len(uniq) < len(vals)


def detect_layout(rows, layout, group_col, value_col):
    """Return (layout, meta). meta carries chosen group_col/value_col for long."""
    if not rows:
        return "wide", {}
    cols = list(rows[0].keys())
    fracs = {c: numeric_fraction(rows, c) for c in cols}
    numeric_cols = [c for c in cols if fracs[c] >= 0.8]
    cat_cols = [c for c in cols if fracs[c] < 0.5]
    lower = {c: str(c).lower() for c in cols}

    if layout == "wide":
        return "wide", {"numeric_cols": numeric_cols}

    gkey = group_col
    if gkey is None:
        named = [c for c in cols if lower[c] in GROUP_HINTS and (c in cat_cols or has_repeats(rows, c))]
        gkey = named[0] if named else next((c for c in cat_cols if has_repeats(rows, c)), None)

    vcol = value_col
    ambiguous = False
    if vcol is None:
        vnamed = [c for c in numeric_cols if lower[c] in VALUE_HINTS]
        if vnamed:
            vcol = vnamed[0]
        elif len(numeric_cols) == 1:
            vcol = numeric_cols[0]
        elif numeric_cols:
            vcol = numeric_cols[0]
            ambiguous = True

    if layout == "long":
        return "long", {"group_col": gkey, "value_col": vcol, "ambiguous_value": ambiguous, "numeric_cols": numeric_cols}

    if gkey is not None and vcol is not None:
        return "long", {"group_col": gkey, "value_col": vcol, "ambiguous_value": ambiguous, "numeric_cols": numeric_cols}
    return "wide", {"numeric_cols": numeric_cols}


def build_group_values(rows, layout, meta):
    if layout == "long":
        gcol, vcol = meta.get("group_col"), meta.get("value_col")
        gv = defaultdict(list)
        if gcol and vcol:
            for r in rows:
                g = str(r.get(gcol)).strip()
                v = parse_float(r.get(vcol))
                if g and v is not None:
                    gv[g].append(v)
        return dict(gv)
    return {c: vals for c, vals in numeric_columns(rows, min_n=1).items()}


def run(source, reported, rel_tol, abs_tol, layout, group_col, value_col):
    source_rows = load_table(source)
    reported_rows = load_table(reported)

    detected, meta = detect_layout(source_rows, layout, group_col, value_col)
    group_values = build_group_values(source_rows, detected, meta)
    stats = {g: {"n": len(v), "mean": mean(v), "sd": sample_sd(v)} for g, v in group_values.items()}

    items = []

    if detected == "long":
        items.append(make_item(
            check="layout_detected", status="note", location=source,
            message=f"Source read as LONG format: group column '{meta.get('group_col')}', value column '{meta.get('value_col')}'.",
            benign_explanation="Detected automatically. Override with --layout/--group-col/--value-col if this is wrong.",
            details={"groups_found": list(stats.keys())},
        ))
        if meta.get("ambiguous_value"):
            items.append(make_item(
                check="layout_detected", status="check", location=source,
                message="Several numeric columns exist; the value column was guessed.",
                benign_explanation="The guess may be wrong when a table has multiple numeric columns.",
                fix="Pass --value-col to name the measurement column explicitly.",
                details={"numeric_columns": meta.get("numeric_cols")},
            ))
    else:
        items.append(make_item(
            check="layout_detected", status="note", location=source,
            message="Source read as WIDE format: each numeric column treated as one group.",
            benign_explanation="Detected automatically. Use --layout long if your data is one row per observation.",
            details={"groups_found": list(stats.keys())},
        ))

    def mismatch(a, b):
        return abs(a - b) > max(abs_tol, rel_tol * max(abs(a), abs(b)))

    for row in reported_rows:
        gcol = find_col(row, ["group", "column", "name", "label", "condition"])
        if gcol is None:
            continue
        group = str(row.get(gcol))
        if group not in stats:
            items.append(make_item(
                check="source_figure_consistency", status="check", location=group,
                message=f"Reported group '{group}' has no matching group in the source data.",
                benign_explanation="The group may be named differently in the source table, or aggregated from several columns.",
                fix="Align the group label with the source-data group/column name, or point the tool at the right source file.",
            ))
            continue
        s = stats[group]

        mcol = find_col(row, ["mean", "average", "avg"])
        if mcol is not None:
            rep = parse_float(row.get(mcol))
            if rep is not None and mismatch(rep, s["mean"]):
                items.append(make_item(
                    check="source_figure_consistency", status="must_fix", location=group,
                    message="Reported mean does not match the mean recomputed from source data.",
                    benign_explanation="Often a stale number left after re-running the analysis, or the wrong source column.",
                    fix="Recompute from the current source data and update the figure/table.",
                    details={"reported_mean": rep, "source_mean": round(s["mean"], 6)},
                ))

        scol = find_col(row, ["sd", "std", "standard_deviation"])
        if scol is not None:
            rep = parse_float(row.get(scol))
            if rep is not None and mismatch(rep, s["sd"]):
                sem = s["sd"] / (s["n"] ** 0.5) if s["n"] else 0.0
                looks_like_sem = abs(rep - sem) <= max(abs_tol, rel_tol * max(abs(rep), abs(sem)))
                items.append(make_item(
                    check="source_figure_consistency", status="must_fix", location=group,
                    message="Reported SD does not match source data.",
                    benign_explanation=("The reported value equals the SEM, so SD and SEM may simply be swapped in the label."
                                        if looks_like_sem else
                                        "May be a stale value or a different variance definition (population vs sample SD)."),
                    fix="Confirm whether the bar shows SD or SEM and relabel/recompute accordingly.",
                    details={"reported_sd": rep, "source_sd": round(s["sd"], 6), "source_sem": round(sem, 6)},
                ))

        secol = find_col(row, ["sem", "se", "stderr", "standard_error"])
        if secol is not None and s["n"]:
            rep = parse_float(row.get(secol))
            src_sem = s["sd"] / (s["n"] ** 0.5)
            if rep is not None and mismatch(rep, src_sem):
                items.append(make_item(
                    check="source_figure_consistency", status="must_fix", location=group,
                    message="Reported SEM does not match SD/sqrt(n) from source data.",
                    benign_explanation="SD and SEM are easy to mix up, or n changed after the figure was made.",
                    fix="Recompute SEM as SD/sqrt(n) with the final n.",
                    details={"reported_sem": rep, "source_sem": round(src_sem, 6)},
                ))

        ncol = find_col(row, ["n", "sample_size"])
        if ncol is not None:
            rep = parse_float(row.get(ncol))
            if rep is not None and int(rep) != s["n"]:
                items.append(make_item(
                    check="source_figure_consistency", status="check", location=group,
                    message="Reported n differs from the number of source-data points.",
                    benign_explanation="Source table may include excluded outliers or count replicates differently.",
                    fix="Confirm the counting convention (biological vs technical replicates, exclusions) and state it.",
                    details={"reported_n": int(rep), "source_n": s["n"]},
                ))

    return make_result(
        tool="source_figure_consistency",
        input_value={"source": source, "reported": reported},
        items=items,
        limitations=[
            "Reported table must name source groups. P-values are not recomputed here.",
            "n mismatches are flagged as double-check, not errors, because replicate-counting conventions vary legitimately.",
            "Layout is auto-detected; check the layout_detected note if results look off.",
        ],
        metadata={"layout": detected,
                  "layout_meta": {k: v for k, v in meta.items() if k != "numeric_cols"},
                  "source_groups": list(stats.keys()), "reported_rows": len(reported_rows)},
    )


def main():
    p = argparse.ArgumentParser(description="Check reported summary values against source data (wide or long).")
    p.add_argument("--source", required=True, help="Source data CSV/TSV/XLSX")
    p.add_argument("--reported", required=True, help="Reported summaries with group/mean/sd/sem/n columns")
    p.add_argument("--layout", choices=["auto", "wide", "long"], default="auto")
    p.add_argument("--group-col", help="Long format: name of the group/label column")
    p.add_argument("--value-col", help="Long format: name of the value column")
    p.add_argument("--rel-tol", type=float, default=1e-2, help="Relative tolerance (default 1%)")
    p.add_argument("--abs-tol", type=float, default=1e-9, help="Absolute tolerance floor")
    add_common_args(p)
    a = p.parse_args()
    emit_result(run(a.source, a.reported, a.rel_tol, a.abs_tol, a.layout, a.group_col, a.value_col), a.format, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
