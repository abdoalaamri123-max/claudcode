#!/usr/bin/env python3
"""Lightweight table self-check for manuscript tables.

Assumes good faith; catches honest table-formatting slips before submission,
following four common journal expectations plus a size/placement guideline:

  1. Decimal places should be uniform within a numeric column.
  2. Units belong in the column header, not inside data cells.
  3. Abbreviations and statistics (SD, SEM, tests) should be defined in a
     footnote; provide --footnotes to cross-check, otherwise get a reminder.
  4. Keep only small, essential tables in the main text; move large data tables
     to the supplement.

Works on CSV / TSV / XLSX / Markdown tables and on '-' (stdin), so a pasted
table can be checked directly. Every finding carries a benign explanation and a
concrete fix; clean tables produce no items.
"""
# Attribution: this module is original. It imports shared helpers from
# tablecheck_common, which is adapted from the "academic-integrity-skill" project
# by lanj (GitHub @1anj), MIT License, Copyright (c) 2026 lanj
# (https://github.com/1anj/academic-integrity-skill @ 135073a). The table-format
# rules implemented here are original.
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional

from tablecheck_common import (
    add_common_args, columns_of, decimals_of, emit_result, make_item, make_result,
    parse_float, read_table,
)

# unit tokens that may appear in headers or (wrongly) in cells
UNIT_TOKENS = {
    "%", "mg", "g", "kg", "ug", "µg", "ng", "pg", "kda", "da",
    "m", "cm", "mm", "um", "µm", "nm", "km",
    "mol", "mmol", "µmol", "umol", "nmol", "pmol",
    "molar", "mm", "mM", "µM", "uM", "nM", "pM",
    "l", "ml", "µl", "ul", "nl",
    "s", "sec", "min", "h", "hr", "hrs", "day", "days", "week", "weeks", "year", "years",
    "bp", "kb", "mb", "rpm", "xg", "hz", "khz",
    "v", "mv", "a", "ma", "w", "j", "cal", "kcal",
    "fold", "x", "°c", "c", "k", "ph", "au", "rfu", "cpm", "ppm",
}
# tokens that read as dimensionless, so a missing unit is expected, not a problem
UNITLESS_HEADER_HINTS = {
    "n", "count", "number", "num", "ratio", "fold", "index", "score", "rank",
    "id", "p", "pvalue", "p-value", "q-value", "qvalue", "fdr", "padj", "adj.p",
    "log2fc", "logfc", "log2", "log10", "zscore", "z", "t", "df", "cv", "auc",
    "percent", "percentage", "proportion", "fraction", "correlation", "r", "r2",
    "rho", "coefficient", "odds", "hr", "or", "rr", "slope", "intercept",
}
# abbreviations understood without a footnote
STANDARD_ABBREV = {"SD", "SEM", "CI", "SE", "N", "ID", "NA", "ND", "P", "DF",
                   "CV", "FDR", "NS", "IQR", "SEM", "AUC", "OR", "HR", "RR"}
ABBREV_RE = re.compile(r"\b([A-Za-z0-9]*[A-Z]{2,}[A-Za-z0-9]*)\b")
CELL_UNIT_RE = re.compile(r"^[-+]?[\d.,]+\s*([A-Za-zµ%°/]+)\s*$")

MAIN_HINTS = {"main", "maintext", "main-text", "table1", "table2", "table3", "tab1", "tab2"}
SUPP_HINTS = {"supp", "suppl", "supplement", "supplementary", "si", "s1", "s2", "s3", "extended"}
SOURCE_HINTS = {"source", "sourcedata", "source-data", "raw", "original"}


def infer_placement(path: str) -> str:
    if path == "-":
        return "unknown"
    parts = re.split(r"[\\/_\-. ]+", path.lower())
    tokens = set(parts)
    if tokens & SUPP_HINTS:
        return "supplement"
    if tokens & SOURCE_HINTS:
        return "source"
    if tokens & MAIN_HINTS:
        return "main"
    return "unknown"


def header_has_unit(header: str) -> bool:
    h = str(header)
    if "%" in h or "(" in h or "[" in h or "/" in h:
        return True
    tokens = re.split(r"[\s,()\[\]/]+", h.lower())
    return any(tok in UNIT_TOKENS for tok in tokens if tok)


def header_is_unitless(header: str) -> bool:
    h = str(header).lower()
    tokens = re.split(r"[\s,()\[\]/]+", h)
    return any(tok in UNITLESS_HEADER_HINTS for tok in tokens if tok)


def is_numeric_column(values: List[str]) -> bool:
    nonempty = [v for v in values if str(v).strip()]
    if not nonempty:
        return False
    parsed = sum(1 for v in nonempty if parse_float(v) is not None)
    return parsed / len(nonempty) >= 0.8


def check_table(path: str, rows: List[Dict[str, object]], placement: str,
                max_rows: int, max_cols: int, abbrev_bag: set) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    cols = columns_of(rows)
    loc = f"{Path(path).name if path != '-' else 'stdin'}"

    # size vs placement
    n_rows, n_cols = len(rows), len(cols)
    too_big = n_rows > max_rows or n_cols > max_cols
    if too_big and placement in {"main", "unknown"}:
        items.append(make_item(
            check="table_size_placement",
            status="check" if placement == "main" else "note",
            location=loc,
            message=f"Table has {n_rows} rows x {n_cols} columns"
                    + (" and sits in the main text." if placement == "main" else "; placement was not detected."),
            benign_explanation="Some main-text summary tables are legitimately large; only move it if it is really a full data dump.",
            fix="Keep a compact essential table in the main text and move the full data to the supplement.",
            details={"rows": n_rows, "cols": n_cols, "max_rows": max_rows, "max_cols": max_cols, "placement": placement},
        ))

    for col in cols:
        raw_values = [row.get(col) for row in rows]
        values = [v for v in raw_values if str(v).strip() != "" and v is not None]

        # units embedded in cells
        cell_units = Counter()
        for v in values:
            m = CELL_UNIT_RE.match(str(v).strip())
            if m and m.group(1).lower().strip(".") in UNIT_TOKENS:
                cell_units[m.group(1)] += 1
        if cell_units:
            items.append(make_item(
                check="unit_in_cell", status="check", location=f"{loc} :: {col}",
                message="A unit appears inside data cells rather than in the column header.",
                benign_explanation="Sometimes a column legitimately mixes units, but usually the unit should sit in the header.",
                fix=f"Move the unit into the header, e.g. '{col} ({list(cell_units)[0]})', and keep cells numeric.",
                details={"units_seen": dict(cell_units)},
            ))

        numeric = is_numeric_column([str(v) for v in values])
        if numeric:
            dcounts = [decimals_of(v) for v in values]
            dcounts = [d for d in dcounts if d is not None]
            nonint = [d for d in dcounts if d > 0]
            distinct_nonint = sorted(set(nonint))
            has_int = any(d == 0 for d in dcounts)
            if len(distinct_nonint) > 1:
                items.append(make_item(
                    check="decimal_consistency", status="check", location=f"{loc} :: {col}",
                    message="Decimal places vary within this numeric column.",
                    benign_explanation="Different magnitudes may need different significant figures; a spreadsheet may also have stripped trailing zeros.",
                    fix="Report the column to a single, consistent number of decimals (or state the sig-fig rule).",
                    details={"decimal_places_seen": distinct_nonint},
                ))
            elif distinct_nonint and has_int:
                items.append(make_item(
                    check="decimal_consistency", status="note", location=f"{loc} :: {col}",
                    message="Column mixes integers with decimals.",
                    benign_explanation="Often trailing zeros were dropped (e.g. 10 shown instead of 10.0), which is usually harmless.",
                    fix="Pad to a uniform decimal count if the column is a single continuous quantity.",
                    details={"decimal_places": distinct_nonint[0]},
                ))

            # missing unit in header for a dimensional-looking numeric column
            if not header_has_unit(col) and not header_is_unitless(col):
                items.append(make_item(
                    check="unit_missing_header", status="note", location=f"{loc} :: {col}",
                    message="Numeric column header has no unit.",
                    benign_explanation="Fine if the quantity is dimensionless (a count, ratio, score, p-value, etc.).",
                    fix="Add the unit to the header if this quantity is dimensional.",
                ))

        # missing values
        n_missing = sum(1 for v in raw_values if v is None or str(v).strip() == "")
        if n_missing:
            items.append(make_item(
                check="missing_values", status="note", location=f"{loc} :: {col}",
                message=f"{n_missing} empty cell(s) in this column.",
                benign_explanation="Blanks are fine if intentional, but readers cannot tell blank from missing.",
                fix="State what a blank means (e.g. ND = not determined, NA = not applicable) in a footnote.",
            ))

        # collect abbreviation candidates from header and string cells
        for text in [str(col)] + [str(v) for v in values if parse_float(v) is None]:
            for cand in ABBREV_RE.findall(text):
                if cand.upper() not in STANDARD_ABBREV and cand not in UNIT_TOKENS:
                    abbrev_bag.add(cand)

    return items


def run(paths: List[str], placement_override: Optional[str], footnotes: Optional[str],
        max_rows: int, max_cols: int) -> Dict[str, object]:
    items: List[Dict[str, object]] = []
    abbrev_bag: set = set()
    placements: Dict[str, str] = {}

    for path in paths:
        rows = read_table(path)
        if not rows:
            items.append(make_item(
                check="empty_table", status="check", location=path,
                message="No rows were parsed from this input.",
                benign_explanation="The file may be empty, or a Markdown/delimiter mismatch.",
                fix="Confirm the file has a header row and data, or pass --delimiter.",
            ))
            continue
        placement = placement_override or infer_placement(path)
        placements[path] = placement
        items.extend(check_table(path, rows, placement, max_rows, max_cols, abbrev_bag))

    # abbreviation footnote cross-check, done once across all inputs
    if abbrev_bag:
        if footnotes:
            fn_text = Path(footnotes).read_text(encoding="utf-8")
            undefined = sorted(a for a in abbrev_bag if a not in fn_text)
            if undefined:
                items.append(make_item(
                    check="abbreviation_footnote", status="check", location=footnotes,
                    message="Abbreviations appear in the tables but are not found in the footnotes file.",
                    benign_explanation="Some may be defined in the main text or be standard in the field.",
                    fix="Define each non-standard abbreviation in a table footnote.",
                    details={"undefined_abbreviations": undefined},
                ))
        else:
            items.append(make_item(
                check="abbreviation_footnote", status="note", location="all tables",
                message="Abbreviations detected; confirm each is defined in a footnote.",
                benign_explanation="Standard ones (SD, SEM, CI, n) need no definition; this is a reminder for the rest.",
                fix="Add a footnote defining non-standard abbreviations, or pass --footnotes to cross-check.",
                details={"abbreviations_detected": sorted(abbrev_bag)},
            ))

    return make_result(
        tool="table_check",
        input_value=paths,
        items=items,
        limitations=[
            "Decimal checks reflect the stored text; XLSX may already have dropped display formatting.",
            "Placement is inferred from the filename unless --placement is given; size limits are guidelines.",
            "Unit and abbreviation detection are heuristic reminders, not exhaustive.",
        ],
        metadata={"placements": placements, "max_rows": max_rows, "max_cols": max_cols,
                  "abbreviations_detected": sorted(abbrev_bag)},
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Lightweight self-check of manuscript tables.")
    p.add_argument("paths", nargs="+", help="Table files (CSV/TSV/XLSX/Markdown) or '-' for stdin")
    p.add_argument("--placement", choices=["main", "supplement", "source", "unknown"],
                   help="Override placement for all inputs (else inferred from filename)")
    p.add_argument("--footnotes", help="Text/markdown file with table footnotes, to cross-check abbreviations")
    p.add_argument("--max-rows", type=int, default=15, help="Row limit before a main-text table is flagged as large")
    p.add_argument("--max-cols", type=int, default=8, help="Column limit before a main-text table is flagged as large")
    add_common_args(p)
    a = p.parse_args()
    emit_result(run(a.paths, a.placement, a.footnotes, a.max_rows, a.max_cols), a.format, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
