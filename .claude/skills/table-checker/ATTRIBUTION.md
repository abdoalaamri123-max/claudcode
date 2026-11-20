# Attribution and licensing

This skill reuses a small amount of code from an upstream open-source project.
Parts adapted from it are attributed below; original parts carry no upstream
obligation.

## Upstream source

- Project: academic-integrity-skill ("耿同学 Skill")
- Author: lanj (GitHub [@1anj](https://github.com/1anj))
- Repository: https://github.com/1anj/academic-integrity-skill
- Commit referenced: 135073a
- License: MIT (reproduced in full below)

## What was adapted vs original

| File | Status | Basis |
| --- | --- | --- |
| `scripts/tablecheck_common.py` | Partly adapted | The `load_table`/`parse_float` helpers derive from upstream `integrity_common.py`. The status vocabulary (must_fix/check/note), benign-explanation model, the Markdown/stdin table reader and the decimals helper are original. |
| `scripts/table_check.py` | Original | The table-format rules (decimal consistency, units-in-header, abbreviation footnote cross-check, size/placement) are original. It imports the shared helpers above. |
| `SKILL.md` | Original | Original content. |

The upstream project's numeric fingerprint screening, image forensics and risk
scoring were not carried over.

## Your own copyright

Add your own copyright line for the modifications, for example:

```
Copyright (c) 2026 <your name>
```

The combined work can be distributed under MIT (recommended, to stay compatible
with the upstream license) or another license, provided the upstream MIT notice
below is retained.

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
