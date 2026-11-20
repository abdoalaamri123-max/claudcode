#!/usr/bin/env python3
"""Figure hygiene check (good-faith version).

Deliberately does NOT do perceptual-similarity forensics: under a good-faith
assumption, "these two blots look similar" is mostly noise (serial images of the
same sample legitimately look alike) and reads as an accusation. It sticks to
low-false-positive, self-service checks:

  1. Exact-duplicate file detection via SHA-256. If the identical image file is
     used in two different figure slots, that is almost always an accidental
     copy-paste worth catching before submission.
  2. Resolution and format notes (needs Pillow). Flags images that look too small
     for print, or lossy JPEGs where lossless art is usually expected. Emitted as
     notes, never as errors.
  3. A disclosure reminder listing the standard items reviewers expect stated
     (scale bars, error-bar definition, n, adjustment disclosure).
"""
# Attribution: this module is largely original. It imports shared helpers from
# figurecheck_common, which is adapted from the "academic-integrity-skill"
# project by lanj (GitHub @1anj), MIT License, Copyright (c) 2026 lanj
# (https://github.com/1anj/academic-integrity-skill @ 135073a). The SHA-256
# file-hashing helper originates there; the duplicate-file grouping, the
# resolution/format checks and the disclosure reminders are original.
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from figurecheck_common import (
    IMAGE_EXTS, add_common_args, emit_result, iter_files, make_item, make_result, sha256_file,
)

DISCLOSURE_REMINDERS = [
    ("scale_bar", "Every microscopy panel should carry a scale bar or state the magnification."),
    ("error_bars", "State what error bars represent (SD, SEM or CI) and the n, in each legend."),
    ("n_reported", "Report n (biological vs technical replicates) for every quantified panel."),
    ("adjustments", "Disclose any crop, splice, brightness/contrast, gamma, pseudocolor or threshold change."),
    ("stats_test", "Name the statistical test and correction used for each comparison shown."),
]

LOSSY_EXTS = {".jpg", ".jpeg"}


def resolution_notes(files, min_edge: int) -> List[Dict[str, object]]:
    try:
        from PIL import Image
    except ImportError:
        return [make_item(
            check="resolution", status="note", location="all figures",
            message="Pillow is not installed, so resolution and format were not checked.",
            benign_explanation="Install Pillow (pip install Pillow) to enable these self-checks.",
        )]
    items: List[Dict[str, object]] = []
    for f in files:
        try:
            with Image.open(f) as img:
                w, h = img.width, img.height
        except Exception:
            continue
        if min(w, h) < min_edge:
            items.append(make_item(
                check="resolution", status="note", location=str(f),
                message=f"Image is {w}x{h}px; its short edge is below {min_edge}px.",
                benign_explanation="Fine for a thumbnail or a screen-only panel; only a problem if it prints blurry.",
                fix="Re-export from the source at higher resolution if this panel goes to print.",
                evidence_files=[str(f)],
                details={"width": w, "height": h},
            ))
        if f.suffix.lower() in LOSSY_EXTS:
            items.append(make_item(
                check="format", status="note", location=str(f),
                message="Panel is a lossy JPEG.",
                benign_explanation="Acceptable for some photographic panels; less ideal for line art, blots or gels.",
                fix="Prefer lossless TIFF or PNG for blots, gels, plots and line art.",
                evidence_files=[str(f)],
            ))
    return items


def run(paths: List[str], with_reminders: bool, min_edge: int, check_resolution: bool) -> Dict[str, object]:
    files = iter_files(paths, IMAGE_EXTS)
    by_hash: Dict[str, List[str]] = defaultdict(list)
    for f in files:
        by_hash[sha256_file(f)].append(str(f))

    items: List[Dict[str, object]] = []
    for digest, group in by_hash.items():
        if len(group) > 1:
            items.append(make_item(
                check="duplicate_image_file", status="check", location=group[0],
                message="The identical image file appears in more than one location.",
                benign_explanation="A shared logo/template, or the same panel legitimately reused with a clear caption. Only a problem if two different results point to one file.",
                fix="Confirm each result has its own source image; remove accidental copy-paste.",
                evidence_files=group,
                details={"sha256": digest[:16], "count": len(group)},
            ))

    if check_resolution:
        items.extend(resolution_notes(files, min_edge))

    if with_reminders:
        for key, text in DISCLOSURE_REMINDERS:
            items.append(make_item(
                check=f"disclosure_{key}", status="note", location="all figures",
                message=text,
                benign_explanation="A reminder, not a finding; tick off each one against your legends and Methods.",
            ))

    return make_result(
        tool="figure_hygiene",
        input_value=paths,
        items=items,
        limitations=[
            "Detects byte-identical files only; it does not and should not judge visual similarity.",
            "Resolution is judged by pixel dimensions alone; true print adequacy also depends on physical size and DPI.",
            "Disclosure items are reminders to self-verify against legends and Methods.",
        ],
        metadata={"image_count": len(files), "unique_files": len(by_hash)},
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Figure hygiene: duplicate files, resolution/format, disclosure reminders.")
    p.add_argument("paths", nargs="+", help="Figure/image directories or files")
    p.add_argument("--no-reminders", action="store_true", help="Skip the disclosure checklist")
    p.add_argument("--no-resolution", action="store_true", help="Skip resolution/format checks")
    p.add_argument("--min-edge", type=int, default=600, help="Short-edge pixel threshold for the resolution note")
    add_common_args(p)
    a = p.parse_args()
    emit_result(run(a.paths, not a.no_reminders, a.min_edge, not a.no_resolution), a.format, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
