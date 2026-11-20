---
name: table-checker
description: Lightweight good-faith self-check of manuscript tables (main-text, supplementary, source-data files, or a pasted table). Catches honest table-formatting slips before submission, such as decimal places that are not uniform within a column, units buried in data cells instead of the header, abbreviations or statistics not defined in a footnote, and large data tables left in the main text that belong in the supplement. Assumes good faith and produces a fix-it list, never an accusation. Works on CSV, TSV, XLSX, Markdown and stdin. Do NOT use it to judge someone else's work for misconduct.
---

# Table checker

## What this is

A small companion to `figure-checker` for the tables in a manuscript. It
assumes the authors acted in good faith and only flags things a reviewer would
routinely ask an author to tidy. Same status vocabulary, no risk score:

- **must_fix**: a deterministic error.
- **check**: worth a second look; often a legitimate style choice.
- **note**: an informational reminder.

Every item carries a plausible innocent explanation and a concrete fix. A clean,
well-formatted table produces no items.

**What this is not:** this skill checks formatting only. It does not verify that a table's
numbers are accurate or match a source-data file or the manuscript text — a table where a
value was changed but the decimal precision stayed uniform within its column produces no
items here. For numeric accuracy, run `figure-checker`'s `source_figure_consistency.py`
against the table's underlying data, or `submission-screener` Pass 1.

## The rules it checks

1. **Decimal places uniform within a column.** Mixed decimals in one numeric
   column are flagged (check); integers mixed with decimals are a gentler note
   (usually stripped trailing zeros).
2. **Units in the header, not in cells.** A unit token inside data cells (e.g.
   "5 mm") is flagged so it can move into the header, e.g. `Tumor size (mm)`. A
   dimensional-looking numeric column with no unit in its header gets a note.
3. **Abbreviations and statistics defined in a footnote.** Detected
   abbreviations are listed as a reminder; pass `--footnotes FILE` to cross-check
   which ones are not yet defined. Standard ones (SD, SEM, CI, n, IQR) are
   ignored.
4. **Small essential tables in the main text; large data tables in the
   supplement.** A table over the size limits whose placement is the main text is
   flagged; the same table placed in the supplement or source data is not.

It also notes empty cells (state what a blank means: ND, NA).

## Usage

```
# One table
python3 scripts/table_check.py path/to/table1.csv

# Several tables at once (placement inferred from filename tokens like
# main/table1, supp/S1, source/raw)
python3 scripts/table_check.py main_table1.csv supplementary_S1.xlsx source_data.csv

# Cross-check abbreviations against a footnotes file
python3 scripts/table_check.py main_table1.csv --footnotes footnotes.txt

# A pasted Markdown table
printf '| Gene | Conc | logFC |\n|--|--|--|\n| TP53 | 5 mM | 1.2 |\n' \
    | python3 scripts/table_check.py -

# JSON output, custom main-text size limits
python3 scripts/table_check.py table.csv --placement main \
    --max-rows 15 --max-cols 8 --format json --output table_check.json
```

Options: `--placement main|supplement|source|unknown` overrides the filename
guess; `--max-rows`/`--max-cols` set the main-text size limits (default 15 x 8);
`--footnotes` enables the abbreviation cross-check; `--format` and `--output` as
usual.

## Notes and limits

- Decimal checks read the stored text; an XLSX may already have lost display
  formatting, so prefer CSV/Markdown export when checking decimals.
- Placement is inferred from the filename unless `--placement` is given; the size
  limits are guidelines, not hard rules.
- Unit and abbreviation detection are heuristic reminders, not exhaustive; they
  under-report rather than raise false alarms.

## Relationship to sister skills

- `figure-checker` — the equivalent good-faith, non-accusatory self-check for figures and images, sharing the same three-tier status vocabulary (must_fix/check/note) and never-invent, benign-explanation-first philosophy. Run both together when assembling a submission package.
- `submission-screener` — Pass 1 (internal consistency) checks that numbers agree across text/tables/figures at a general level and every table is called out in order; this skill goes deeper on a table's own internal formatting (decimal uniformity, units in header vs. cells, abbreviation footnotes, main-text vs. supplement placement).
- `manuscript-copyeditor` — number formatting (spelling out one to twenty, comma thresholds, SI unit spacing) applies to numbers in prose; this skill applies the analogous formatting discipline to numbers inside a table.

## Attribution

The shared helper module is adapted from the MIT-licensed academic-integrity-skill
by lanj (GitHub @1anj), https://github.com/1anj/academic-integrity-skill. The
table-format rules themselves are original. See `ATTRIBUTION.md` for the per-file
breakdown and the retained upstream license.
