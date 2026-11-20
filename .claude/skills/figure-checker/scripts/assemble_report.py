#!/usr/bin/env python3
"""Merge JSON outputs from the other checks into one pre-submission fix-it list.

Output is grouped by action level (Must fix / Double-check / Notes), not by a
risk score. There is no "investigation threshold" here by design.
"""
# Attribution: the aggregation concept is adapted from scripts/report_assembler.py
# in the "academic-integrity-skill" project by lanj (GitHub @1anj), MIT License,
# Copyright (c) 2026 lanj (https://github.com/1anj/academic-integrity-skill @
# 135073a). The implementation and the action-level (not risk-score) grouping are
# rewritten. See ATTRIBUTION.md for the full upstream license.
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


def load(path: str) -> Dict[str, object]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run(paths: List[str]) -> str:
    buckets: Dict[str, List[str]] = {"must_fix": [], "check": [], "note": []}
    totals = {"must_fix": 0, "check": 0, "note": 0}
    tools = []
    for p in paths:
        try:
            result = load(p)
        except Exception as exc:
            buckets["check"].append(f"- Could not read `{p}`: {exc}")
            continue
        tool = result.get("tool", Path(p).stem)
        tools.append(tool)
        for item in result.get("items", []):
            status = str(item.get("status", "note")).lower()
            if status not in buckets:
                status = "note"
            totals[status] += 1
            line = f"- **{item.get('check', tool)}** ({item.get('location', '') or 'general'}): {item.get('message', '')}"
            if item.get("fix"):
                line += f"\n  - Fix: {item['fix']}"
            if item.get("benign_explanation"):
                line += f"\n  - Could be innocent: {item['benign_explanation']}"
            buckets[status].append(line)

    lines = [
        "# Pre-submission self-check summary",
        "",
        f"Checks run: {', '.join(tools) if tools else 'none'}",
        f"Must fix: {totals['must_fix']} | Double-check: {totals['check']} | Notes: {totals['note']}",
        "",
        "This is a self-audit for honest mistakes. Items are prompts to verify before submission, not accusations.",
        "",
        "## Must fix (deterministic errors)",
        "",
    ]
    lines += buckets["must_fix"] or ["- None."]
    lines += ["", "## Double-check (probably fine, worth a glance)", ""]
    lines += buckets["check"] or ["- None."]
    lines += ["", "## Notes and reminders", ""]
    lines += buckets["note"] or ["- None."]
    lines += [""]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Assemble check JSONs into one fix-it list.")
    p.add_argument("inputs", nargs="+", help="JSON outputs from the other scripts")
    p.add_argument("--output", help="Optional output .md path")
    a = p.parse_args()
    text = run(a.inputs)
    if a.output:
        Path(a.output).write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
