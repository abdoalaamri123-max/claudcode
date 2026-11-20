#!/usr/bin/env python3
"""Figure-legend self-check.

A good figure legend must let the figure stand alone. This checks a legend (or a
file of many legends) for the elements a reviewer routinely asks for, but only
fires when the legend text itself gives a concrete signal, so it stays quiet on
legends that are already complete and never invents problems.

What a strong data-figure legend contains (used as the reference here):
  1. A descriptive title sentence stating the key takeaway.
  2. Enough method context to interpret the figure (cells, treatment, etc.).
  3. Error-bar / statistic definitions with n (e.g. "mean +/- s.e.m., n = 6").
  4. Definitions of colors, symbols, line styles and abbreviations shown.
Plus: microscopy panels state a scale bar; any image adjustment is disclosed;
spliced blots/gels are declared; review/schematic legends walk through the idea.

Title quality is a human judgement and is left to manual review, not auto-graded.

Input: one or more legend text files (.txt/.md), or '-' for stdin. Multiple
legends in one file are split on "Figure N" / "Fig. N" headings.
"""
# Attribution: this module is original. It imports shared helpers from
# figurecheck_common, which is adapted from the "academic-integrity-skill" project
# by lanj (GitHub @1anj), MIT License, Copyright (c) 2026 lanj
# (https://github.com/1anj/academic-integrity-skill @ 135073a). The legend rules
# implemented here are original.
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from figurecheck_common import add_common_args, emit_result, make_item, make_result

FIG_HEADER_RE = re.compile(r"(?im)^\s*(?:figure|fig\.?)\s+([0-9]+[a-z]?)\b")
ABBREV_RE = re.compile(r"\b([A-Za-z0-9]*[A-Z]{2,}[A-Za-z0-9]*)\b")

STANDARD_ABBREV = {
    "SD", "SEM", "SE", "CI", "IQR", "N", "ID", "NA", "ND", "NS", "P", "DF", "CV",
    "DNA", "RNA", "MRNA", "CDNA", "PCR", "QPCR", "RT", "GFP", "RFP", "YFP", "WT",
    "KO", "KD", "ATP", "GTP", "ADP", "PBS", "SDS", "EDTA", "DAPI", "FACS", "3D", "2D",
}
UNIT_TOKENS = {"mm", "cm", "um", "nm", "kda", "da", "ml", "ul", "nl", "mg", "ng",
               "pg", "mol", "mm", "kb", "bp", "rpm", "hz"}

ERROR_TYPE_RE = re.compile(r"(?i)\b(s\.?\s*d\.?|standard deviation|s\.?\s*e\.?\s*m\.?|"
                           r"standard error|s\.?\s*e\.?|c\.?\s*i\.?|confidence interval|"
                           r"iqr|interquartile|range|whisker|min.?max)\b")
ERROR_SIGNAL_RE = re.compile(r"(?i)(±|\+/-|\berror bars?\b|\berror\b)")
CENTRAL_RE = re.compile(r"(?i)\b(mean|average|median|geometric mean)\b")
N_RE = re.compile(r"(?i)(\bn\s*=\s*\d+|\bn\s*of\s*\d+|independent (?:experiment|replicate)|"
                  r"biological replicate|technical replicate)")
STAR_RE = re.compile(r"\*")
P_RE = re.compile(r"(?i)(p\s*[<=>]\s*0?\.\d+|p[\- ]?value|p\s*<|p\s*=)")
SIG_WORD_RE = re.compile(r"(?i)significan")
TEST_RE = re.compile(r"(?i)(t[- ]?test|anova|mann[- ]?whitney|wilcoxon|kruskal|"
                     r"chi[- ]?squared?|fisher|tukey|dunnett|bonferroni|log[- ]?rank|"
                     r"kolmogorov|spearman|pearson|regression|mixed[- ]model|\btest\b)")

METHOD_KW_RE = re.compile(r"(?i)(cell|line|treat|induc|incubat|stain|buffer|assay|"
                          r"perform|transfect|infect|concentration|dose|"
                          r"antibod|probe|primer|culture|\bfix|wash|hours?\b|days?\b|"
                          r"passage|medium|reagent|\bkit\b|instrument|microscop)")
COLOR_STYLE_RE = re.compile(r"(?i)(colou?r|\bred\b|\bblue\b|\bgreen\b|\bblack\b|\bgr[ae]y\b|"
                            r"\borange\b|\bpurple\b|\bcyan\b|\bmagenta\b|\byellow\b|dashed|"
                            r"dotted|solid line|\bsymbol|\bmarker|\bshaded|\bfill|legend key)")
SCALE_RE = re.compile(r"(?i)(scale ?bar|µm|um\b|magnificat|objective|\b\d+\s?x\b)")
ADJUST_RE = re.compile(r"(?i)(bright|contrast|gamma|pseudo[- ]?colou?r|threshold|deconvol|"
                       r"crop|adjust|process|linear adjustment|level)")
SPLICE_RE = re.compile(r"(?i)(splic|non[- ]?adjacent|same (?:membrane|gel|blot)|"
                       r"separated by|dividing line|lanes were run|reprobed)")

BLOT_RE = re.compile(r"(?i)(blot|western|immunoblot|\bgel\b|\blane)")
MICRO_RE = re.compile(r"(?i)(micrograph|microscop|immunofluoresc|confocal|\bstain|"
                      r"histolog|fluoresc|dapi|h&e|scale ?bar|µm|imag(?:e|ing))")
REVIEW_RE = re.compile(r"(?i)(schematic|graphical abstract|workflow|pipeline|cartoon|"
                       r"overview of|model of|illustrat|concept)")


def split_legends(text: str) -> List[Tuple[str, str]]:
    matches = list(FIG_HEADER_RE.finditer(text))
    if not matches:
        return [("figure", text.strip())] if text.strip() else []
    out = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((f"Figure {m.group(1)}", text[start:end].strip()))
    return out


def detect_type(text: str, override: Optional[str]) -> str:
    if override and override != "auto":
        return override
    if REVIEW_RE.search(text) and not (CENTRAL_RE.search(text) or ERROR_SIGNAL_RE.search(text)):
        return "review"
    if BLOT_RE.search(text):
        return "blot"
    if MICRO_RE.search(text):
        return "microscopy"
    return "plot"


def undefined_abbrevs(text: str) -> List[str]:
    cands = {c for c in ABBREV_RE.findall(text)
             if c.upper() not in STANDARD_ABBREV and c.lower() not in UNIT_TOKENS}
    undef = []
    for c in sorted(cands):
        in_parens = re.search(r"\(\s*" + re.escape(c) + r"\s*\)", text)
        spelled_after = re.search(re.escape(c) + r"\s*\([^)]*[a-z]{3,}", text)
        if not (in_parens or spelled_after):
            undef.append(c)
    return undef


def check_legend(fig_id: str, text: str, ftype: str) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    words = len(text.split())
    is_data = ftype in {"plot", "microscopy", "blot"}

    if words < 15:
        items.append(make_item(
            check="legend_too_brief", status="note", location=fig_id,
            message=f"Legend is short ({words} words) and may not stand alone.",
            benign_explanation="A simple panel can have a short legend; only expand if a reader would be left guessing.",
            fix="Add a descriptive title, brief methods, and definitions so the figure reads without the main text.",
        ))

    has_error = bool(ERROR_SIGNAL_RE.search(text)) or bool(ERROR_TYPE_RE.search(text))
    error_defined = bool(ERROR_TYPE_RE.search(text))
    has_central = bool(CENTRAL_RE.search(text))
    has_n = bool(N_RE.search(text))

    if is_data:
        if has_error and not error_defined:
            items.append(make_item(
                check="error_bar_undefined", status="check", location=fig_id,
                message="Error bars are mentioned but their meaning is not defined.",
                benign_explanation="It may be defined in a shared 'Statistics' section, but a standalone legend should say it too.",
                fix="State whether error bars are SD, SEM or a confidence interval.",
            ))
        if (has_error or has_central) and not has_n:
            items.append(make_item(
                check="n_missing", status="check", location=fig_id,
                message="A mean/error is reported but n is not stated.",
                benign_explanation="n may be given elsewhere, but a standalone legend should state it.",
                fix="State n and whether replicates are biological or technical.",
            ))

    has_star = bool(STAR_RE.search(text))
    has_p = bool(P_RE.search(text))
    has_sig = bool(SIG_WORD_RE.search(text))
    has_test = bool(TEST_RE.search(text))
    if has_star and not has_p:
        items.append(make_item(
            check="significance_symbol_undefined", status="check", location=fig_id,
            message="An asterisk is used but the significance thresholds are not defined.",
            benign_explanation="Readers cannot tell what * means without the p-value key.",
            fix="Define the thresholds, e.g. *p<0.05, **p<0.01, and 'ns' for not significant.",
        ))
    if (has_star or has_p or has_sig) and not has_test:
        items.append(make_item(
            check="statistical_test_unnamed", status="check", location=fig_id,
            message="Significance is reported but the statistical test is not named.",
            benign_explanation="The test may be in Methods, but a standalone legend should name it.",
            fix="Name the test and any multiple-comparison correction used.",
        ))

    undef = undefined_abbrevs(text)
    if undef:
        items.append(make_item(
            check="abbreviation_undefined_in_legend", status="note", location=fig_id,
            message="Some abbreviations may not be defined within this legend.",
            benign_explanation="They may be field-standard or defined in a global abbreviation list; the legend should still stand alone.",
            fix="Spell out each non-standard abbreviation on first use in the legend.",
            details={"candidates": undef},
        ))

    if ftype == "microscopy":
        if not SCALE_RE.search(text):
            items.append(make_item(
                check="scale_bar_missing", status="check", location=fig_id,
                message="Microscopy legend does not mention a scale bar or magnification.",
                benign_explanation="Fine if a scale bar is drawn in the panel and stated elsewhere; better to state it here.",
                fix="State the scale bar length or the magnification.",
            ))
        if not ADJUST_RE.search(text):
            items.append(make_item(
                check="image_adjustment_disclosure", status="note", location=fig_id,
                message="No image-adjustment disclosure found.",
                benign_explanation="Only needed if brightness/contrast/gamma/pseudocolor/threshold were changed.",
                fix="If any adjustment was applied, state it (and that it was applied to the whole image).",
            ))

    if ftype == "blot" and not SPLICE_RE.search(text):
        items.append(make_item(
            check="splice_disclosure", status="note", location=fig_id,
            message="No splice/cropping disclosure found for a blot/gel figure.",
            benign_explanation="Only needed if lanes are non-adjacent or the blot was spliced/cropped.",
            fix="If lanes were spliced or non-adjacent, mark and state it in the legend.",
        ))

    if ftype == "plot" and not COLOR_STYLE_RE.search(text):
        items.append(make_item(
            check="encoding_undefined", status="note", location=fig_id,
            message="No color/symbol/line-style description found for a data plot.",
            benign_explanation="Fine if the panel has an in-figure key; otherwise define the encodings.",
            fix="Define what each color, symbol and line style represents.",
        ))

    if ftype == "review":
        items.append(make_item(
            check="review_walkthrough", status="note", location=fig_id,
            message="Schematic/overview figure: make sure the legend walks the reader through it.",
            benign_explanation="Conceptual figures need narrative guidance rather than n and error bars.",
            fix="Describe what each part of the schematic shows and the take-home message.",
        ))

    if is_data and not has_n and not has_error and not METHOD_KW_RE.search(text):
        items.append(make_item(
            check="legend_essentials_reminder", status="note", location=fig_id,
            message="Legend looks thin for a data figure.",
            benign_explanation="Some panels genuinely need little; expand only if a reader would struggle.",
            fix="Consider a descriptive title, brief methods, error/stat definitions with n, and encoding definitions.",
        ))

    return items


def run(paths: List[str], ftype: Optional[str]) -> Dict[str, object]:
    items: List[Dict[str, object]] = []
    processed = 0
    for path in paths:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        for fig_id, legend in split_legends(text):
            if not legend:
                continue
            processed += 1
            t = detect_type(legend, ftype)
            src = fig_id if path == "-" else f"{Path(path).name}:{fig_id}"
            items.extend(make_item_relocate(check_legend(fig_id, legend, t), src))
    return make_result(
        tool="legend_check",
        input_value=paths,
        items=items,
        limitations=[
            "Legend quality (especially the title) is a human judgement; this only checks detectable elements.",
            "Checks fire only on signals in the legend text, so a missing element with no signal is not caught.",
            "Figure type is auto-detected from keywords; override with --figure-type.",
        ],
        metadata={"legends_processed": processed},
    )


def make_item_relocate(items: List[Dict[str, object]], location: str) -> List[Dict[str, object]]:
    for it in items:
        it["location"] = location
    return items


def main() -> int:
    p = argparse.ArgumentParser(description="Self-check figure legends for standalone completeness.")
    p.add_argument("paths", nargs="+", help="Legend text files (.txt/.md) or '-' for stdin")
    p.add_argument("--figure-type", choices=["auto", "plot", "microscopy", "blot", "review"], default="auto")
    add_common_args(p)
    a = p.parse_args()
    emit_result(run(a.paths, a.figure_type), a.format, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
