# Attribution and licensing

This skill reuses and reframes code from an upstream open-source project. Parts
that were adapted from it are attributed below; parts that are original are noted
as such and carry no upstream obligation.

## Upstream source

- Project: academic-integrity-skill ("耿同学 Skill")
- Author: lanj (GitHub [@1anj](https://github.com/1anj))
- Repository: https://github.com/1anj/academic-integrity-skill
- Commit referenced: 135073a
- License: MIT (reproduced in full below)

## What was adapted vs original

| File | Status | Basis |
| --- | --- | --- |
| `scripts/figurecheck_common.py` | Adapted | Reframed derivative of upstream `integrity_common.py`. The status vocabulary (must_fix/check/note) and the benign-explanation model are original. |
| `scripts/source_figure_consistency.py` | Adapted | Derived from upstream `graph_source_consistency.py`. The good-faith reframing, the SD-vs-SEM swap heuristic and the wide/long layout auto-detection are original. |
| `scripts/stats_sanity.py` | Adapted | Recompute-and-flag concept from upstream `stats_consistency_check.py`. The min<=mean<=max range check, the SEM=SD/sqrt(n) check and the GRIM check are original. |
| `scripts/assemble_report.py` | Adapted (concept) | Aggregation idea from upstream `report_assembler.py`; implementation and action-level grouping rewritten. |
| `scripts/figure_hygiene.py` | Mostly original | Uses the SHA-256 helper from the adapted common module. Duplicate-file grouping, resolution/format checks and disclosure reminders are original. |
| `scripts/legend_check.py` | Original | Figure-legend standalone-completeness rules are original. Imports the adapted common module for output helpers. |
| `SKILL.md` | Mostly original | Domain review checklist draws on upstream README/SKILL; the good-faith framing, status model and workflow are original. |

The upstream project's numeric fingerprint screening, perceptual image-similarity
forensics, risk scoring and package-completeness checklist were intentionally not
carried over.

## Your own copyright

Add your own copyright line for the modifications, for example:

```
Copyright (c) 2026 <your name>
```

The combined work can be distributed under MIT (recommended, to stay compatible
with the upstream license) or another license of your choosing, provided the
upstream MIT notice below is retained.

## Upstream license (retained per MIT terms)

```
MIT License

Copyright (c) 2026 lanj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
