#!/usr/bin/env python3
"""Shared helpers for the pre-submission self-check skill.

Philosophy: assume the authors acted in good faith. The job is to catch honest
mistakes (transcription errors, stale numbers, missing files, mislabeled
statistics) BEFORE submission, not to accuse anyone of manipulation.

Every item therefore uses a neutral status vocabulary and always carries a
plain-language benign explanation:

  must_fix : a deterministic error. The math does not work, or a required file
             is absent. This is almost certainly a mistake worth correcting.
  check    : worth a second look. May well be legitimate; needs a human glance.
  note     : informational only. No action implied.

There is no risk score and no "investigation" language by design.
"""
# Attribution: adapted from the "academic-integrity-skill" project by lanj
# (GitHub @1anj), MIT License, Copyright (c) 2026 lanj.
# Source: https://github.com/1anj/academic-integrity-skill @ 135073a
# This module is a reframed derivative of scripts/integrity_common.py.
# The status vocabulary (must_fix/check/note) and benign_explanation model are
# original additions. See ATTRIBUTION.md for the full upstream license.
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
TABLE_EXTS = {".csv", ".tsv", ".xlsx", ".xlsm"}

STATUS_ORDER = {"note": 0, "check": 1, "must_fix": 2}


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Optional output file")


def make_item(
    *,
    check: str,
    status: str,
    message: str,
    location: str = "",
    benign_explanation: str = "",
    fix: str = "",
    evidence_files: Optional[Sequence[str]] = None,
    details: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    status = status.lower()
    if status not in STATUS_ORDER:
        raise ValueError(f"status must be one of {list(STATUS_ORDER)}, got {status!r}")
    return {
        "check": check,
        "status": status,
        "location": location,
        "message": message,
        "benign_explanation": benign_explanation,
        "fix": fix,
        "evidence_files": list(evidence_files or []),
        "details": details or {},
    }


def summarize(items: Sequence[Dict[str, object]]) -> Dict[str, int]:
    counts = {"must_fix": 0, "check": 0, "note": 0}
    for item in items:
        status = str(item.get("status", "note")).lower()
        if status in counts:
            counts[status] += 1
    return counts


def make_result(
    *,
    tool: str,
    input_value: object,
    items: Sequence[Dict[str, object]],
    limitations: Optional[Sequence[str]] = None,
    metadata: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    return {
        "tool": tool,
        "input": input_value,
        "summary": summarize(items),
        "items": list(items),
        "limitations": list(limitations or []),
        "metadata": metadata or {},
        "note": "Self-check for honest errors. Items are prompts to verify, not accusations.",
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
        f"# {result.get('tool', 'Self-check')}",
        "",
        f"- Input: `{_fmt(result.get('input', ''))}`",
        f"- Must fix: {summary.get('must_fix', 0)} | Double-check: {summary.get('check', 0)} | Notes: {summary.get('note', 0)}",
        "",
    ]
    if not items:
        lines.append("Nothing flagged. Everything checked was internally consistent.")
    for item in items:
        lines.append(f"## [{label.get(item['status'], item['status'])}] {item.get('check', '')}")
        if item.get("location"):
            lines.append(f"- Where: `{item['location']}`")
        lines.append(f"- What: {item.get('message', '')}")
        if item.get("benign_explanation"):
            lines.append(f"- Could be innocent because: {item['benign_explanation']}")
        if item.get("fix"):
            lines.append(f"- Fix: {item['fix']}")
        ev = item.get("evidence_files") or []
        if ev:
            lines.append(f"- Files: {', '.join(f'`{e}`' for e in ev)}")
        det = item.get("details") or {}
        if det:
            for k, v in det.items():
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
        print(text)
    return text


def iter_files(paths: Sequence[str], exts: Optional[Set[str]] = None) -> List[Path]:
    files: List[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            if exts is None or path.suffix.lower() in exts:
                files.append(path)
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and (exts is None or child.suffix.lower() in exts):
                    files.append(child)
    return sorted(files)


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(block_size), b""):
            digest.update(block)
    return digest.hexdigest()


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


def load_table(path: str, delimiter: Optional[str] = None) -> List[Dict[str, object]]:
    suffix = Path(path).suffix.lower()
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
        rows: List[Dict[str, object]] = []
        for raw in it:
            row = {cols[i]: c for i, c in enumerate(raw) if i < len(cols) and cols[i]}
            rows.append(row)
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


def numeric_columns(rows: Sequence[Dict[str, object]], min_n: int = 2) -> Dict[str, List[float]]:
    values: Dict[str, List[float]] = {}
    for row in rows:
        for col, raw in row.items():
            f = parse_float(raw)
            if f is None:
                continue
            values.setdefault(col, []).append(f)
    return {c: v for c, v in values.items() if len(v) >= min_n}


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def sample_sd(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((x - m) ** 2 for x in values) / (len(values) - 1))
