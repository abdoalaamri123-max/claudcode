#!/usr/bin/env python3
"""Shared helpers for the table-checker skill.

Same good-faith philosophy as the figure-checker: assume the authors acted in
good faith, catch honest formatting slips before submission, and phrase every
item with a benign explanation and a concrete fix. Status vocabulary only:
must_fix (deterministic error) / check (worth a glance) / note (reminder).
There is no risk score.
"""
# Attribution: adapted from the "academic-integrity-skill" project by lanj
# (GitHub @1anj), MIT License, Copyright (c) 2026 lanj.
# Source: https://github.com/1anj/academic-integrity-skill @ 135073a
# The load_table/parse_float helpers derive from scripts/integrity_common.py.
# The status/benign-explanation model, the markdown/stdin table reader and the
# decimals helper are original. See ATTRIBUTION.md for the full upstream license.
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

STATUS_ORDER = {"note": 0, "check": 1, "must_fix": 2}


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Optional output file")


def make_item(*, check: str, status: str, message: str, location: str = "",
              benign_explanation: str = "", fix: str = "",
              details: Optional[Dict[str, object]] = None) -> Dict[str, object]:
    status = status.lower()
    if status not in STATUS_ORDER:
        raise ValueError(f"status must be one of {list(STATUS_ORDER)}, got {status!r}")
    return {
        "check": check, "status": status, "location": location, "message": message,
        "benign_explanation": benign_explanation, "fix": fix, "details": details or {},
    }


def summarize(items: Sequence[Dict[str, object]]) -> Dict[str, int]:
    counts = {"must_fix": 0, "check": 0, "note": 0}
    for it in items:
        s = str(it.get("status", "note")).lower()
        if s in counts:
            counts[s] += 1
    return counts


def make_result(*, tool: str, input_value: object, items: Sequence[Dict[str, object]],
                limitations: Optional[Sequence[str]] = None,
                metadata: Optional[Dict[str, object]] = None) -> Dict[str, object]:
    return {
        "tool": tool, "input": input_value, "summary": summarize(items),
        "items": list(items), "limitations": list(limitations or []),
        "metadata": metadata or {},
        "note": "Self-check for honest formatting slips. Items are prompts to verify, not accusations.",
    }


def _fmt(value: object) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def result_to_markdown(result: Dict[str, object]) -> str:
    order = {"must_fix": 0, "check": 1, "note": 2}
    items = sorted(result.get("items", []), key=lambda it: order.get(it.get("status", "note"), 3))
    summary = result.get("summary", {})
    label = {"must_fix": "Must fix", "check": "Double-check", "note": "Note"}
    lines = [
        f"# {result.get('tool', 'Table check')}",
        "",
        f"- Input: `{_fmt(result.get('input', ''))}`",
        f"- Must fix: {summary.get('must_fix', 0)} | Double-check: {summary.get('check', 0)} | Notes: {summary.get('note', 0)}",
        "",
    ]
    if not items:
        lines.append("Nothing flagged. Every table checked was internally consistent.")
    for it in items:
        lines.append(f"## [{label.get(it['status'], it['status'])}] {it.get('check', '')}")
        if it.get("location"):
            lines.append(f"- Where: `{it['location']}`")
        lines.append(f"- What: {it.get('message', '')}")
        if it.get("benign_explanation"):
            lines.append(f"- Could be innocent because: {it['benign_explanation']}")
        if it.get("fix"):
            lines.append(f"- Fix: {it['fix']}")
        for k, v in (it.get("details") or {}).items():
            lines.append(f"  - {k}: {_fmt(v)}")
        lines.append("")
    limits = result.get("limitations") or []
    if limits:
        lines.append("## Limitations")
        for lim in limits:
            lines.append(f"- {lim}")
        lines.append("")
    return "\n".join(lines)


def emit_result(result: Dict[str, object], fmt: str, output: Optional[str]) -> str:
    text = json.dumps(result, ensure_ascii=False, indent=2) if fmt == "json" else result_to_markdown(result)
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        try:
            print(text)
        except BrokenPipeError:
            pass
    return text


def parse_float(value: object) -> Optional[float]:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    if text.startswith("(") and text.endswith(")"):
        text = "-" + text[1:-1]
    try:
        return float(text)
    except ValueError:
        return None


def decimals_of(value: object) -> Optional[int]:
    """Decimal places of a plain numeric string, or None if not plain-numeric.

    Scientific notation returns None (its precision is not comparable this way).
    A trailing-unit token (e.g. '5.20 mg') is ignored for the count.
    """
    text = str(value).strip().replace(",", "")
    m = re.match(r"^[-+]?(\d+(?:\.\d+)?|\.\d+)", text)
    if not m:
        return None
    if "e" in text.lower():
        return None
    num = m.group(1)
    return len(num.split(".", 1)[1]) if "." in num else 0


def _parse_markdown(text: str) -> List[Dict[str, object]]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    table_lines = [ln for ln in lines if ln.count("|") >= 1]
    if len(table_lines) < 2:
        return []

    def cells(ln: str) -> List[str]:
        ln = ln.strip()
        if ln.startswith("|"):
            ln = ln[1:]
        if ln.endswith("|"):
            ln = ln[:-1]
        return [c.strip() for c in ln.split("|")]

    header = cells(table_lines[0])
    body = table_lines[1:]
    if body and re.fullmatch(r"[\s:|-]+", body[0].replace("|", "|")):
        body = body[1:]
    rows = []
    for ln in body:
        vals = cells(ln)
        rows.append({header[i]: (vals[i] if i < len(vals) else "") for i in range(len(header))})
    return rows


def read_table(path: str, delimiter: Optional[str] = None) -> List[Dict[str, object]]:
    """Load a table from CSV/TSV/XLSX/Markdown, or '-' for stdin."""
    if path == "-":
        text = sys.stdin.read()
        if "|" in text:
            md = _parse_markdown(text)
            if md:
                return md
        try:
            dialect = csv.Sniffer().sniff(text[:4096])
        except csv.Error:
            dialect = csv.excel
        return list(csv.DictReader(text.splitlines(), dialect=dialect))

    suffix = Path(path).suffix.lower()
    if suffix in {".md", ".markdown"}:
        return _parse_markdown(Path(path).read_text(encoding="utf-8"))
    if suffix in {".xlsx", ".xlsm"}:
        try:
            from openpyxl import load_workbook
        except ImportError as exc:
            raise SystemExit("XLSX input needs openpyxl: python3 -m pip install openpyxl") from exc
        wb = load_workbook(path, data_only=True, read_only=True)
        sheet = wb.worksheets[0]
        it = sheet.iter_rows(values_only=True)
        try:
            header = next(it)
        except StopIteration:
            return []
        cols = [str(c).strip() if c is not None else "" for c in header]
        rows = []
        for raw in it:
            rows.append({cols[i]: c for i, c in enumerate(raw) if i < len(cols) and cols[i]})
        return rows
    with open(path, newline="", encoding="utf-8-sig") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        if delimiter is not None:
            return list(csv.DictReader(handle, delimiter=delimiter))
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            dialect = csv.excel_tab if path.endswith(".tsv") else csv.excel
        return list(csv.DictReader(handle, dialect=dialect))


def columns_of(rows: Sequence[Dict[str, object]]) -> List[str]:
    seen: List[str] = []
    for row in rows:
        for k in row.keys():
            if k not in seen and str(k).strip():
                seen.append(k)
    return seen
