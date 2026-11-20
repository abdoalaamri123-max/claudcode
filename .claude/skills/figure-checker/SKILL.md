---
name: figure-checker
description: Good-faith pre-submission check of a manuscript's figures. Catches honest figure mistakes before you submit, such as numbers plotted in a figure that no longer match the source data, mislabeled SD/SEM, accidentally reused image files, low resolution or lossy formats, and undisclosed image adjustments. Also checks figure-legend standalone completeness (error/n/stats definitions, scale bar, splice/adjustment disclosure, abbreviations) and a visual-design and journal-format checklist covering vector vs. raster format by content type, font and panel-label conventions, colorblind-safe palette, on-figure statistics/n annotation, and journal column width. Assumes the authors acted in good faith; it produces a fix-it list, never an accusation. Use before submitting or resubmitting, when tidying a figure package, or asking about figure fonts, panel labels, colors, scale bars, legends, or sizing. Do NOT use it to judge whether someone else committed misconduct.
---

# Figure checker

## What this is (and is not)

This skill helps an author find and fix their own honest figure mistakes before a
manuscript goes out. It assumes good faith throughout. Every item is a prompt to
verify, phrased with a plausible innocent explanation and a concrete fix. It does
not score "risk", does not use "investigation" language, and does not do
accusatory image forensics: perceptual-similarity "reuse detection" produces too
many false positives on legitimately similar images and reads as an allegation.

Three status levels only:
- **must_fix**: a deterministic error, e.g. a plotted value that does not match
  the source data. Almost certainly a real mistake.
- **check**: worth a second look; often legitimate.
- **note**: an informational reminder.

If a check cannot point to a concrete fix, it does not fire. That rule is what
keeps false positives low.

A clean automated report clears only the good-faith slips these checks actually test for
(byte-identical duplicate files, arithmetic inconsistency in a stats table, mismatched
plotted-vs-source numbers). It is not evidence that no image was deliberately duplicated,
rotated, cropped, or reprocessed to disguise reuse — reliably catching that needs
perceptual-similarity forensics, which this skill deliberately does not do (see Design notes
below). Say this plainly if a clean report risks being read as "no manipulation happened."

## When to run it

- Before first submission or a resubmission/revision.
- After re-running an analysis, to catch stale numbers left in figures.
- While assembling the figure and source-data package for a journal.

## Workflow

### 1. Automated checks (scripts)

All scripts share `--format markdown|json` and `--output`. Clean inputs produce
no items.

```
# Do the numbers in a figure/table match the source data? (highest-value check)
# Source data may be wide (one column per group) or long (group column + value
# column); the layout is auto-detected and reported back in a note.
python3 scripts/source_figure_consistency.py \
    --source source_data.csv --reported reported_summaries.csv \
    --format json --output src.json
#   Long data with several numeric columns: name the value column explicitly, e.g.
#   --layout long --group-col compartment --value-col intensity

# Is the statistics table behind the figure arithmetically self-consistent?
# (min<=mean<=max, SD/SEM>=0, SEM~=SD/sqrt(n), n a positive integer)
python3 scripts/stats_sanity.py reported_summaries.csv --format json --output stat.json
#   For count/Likert columns only, enable GRIM: --integer-columns "Grade,ScoreA"

# Image files: exact-duplicate detection, resolution/format notes, disclosure reminders
python3 scripts/figure_hygiene.py figures/ source_images/ \
    --format json --output fig.json

# Figure legends: standalone completeness (error/n/stats definitions, scale bar,
# splice/adjustment disclosure, abbreviations). One file may hold many legends.
python3 scripts/legend_check.py legends.txt --format json --output leg.json
#   Force the figure type when auto-detection is wrong: --figure-type microscopy

# One combined fix-it list
python3 scripts/assemble_report.py src.json stat.json fig.json leg.json --output figure-fixlist.md
```

`source_figure_consistency` expects a reported table with one row per group and
columns named (case-insensitive) from: group/label/condition, mean, sd, sem, n.
Source layout is auto-detected: wide means one numeric column per group; long
means one row per observation with a group column and a value column. Detection
is announced in a `layout_detected` note so a misread is visible; force it with
`--layout wide|long` and name columns with `--group-col`/`--value-col`.
Tolerances default to ~1% so ordinary 2-3 significant-figure rounding never nags;
tighten with `--rel-tol`.

`figure_hygiene` options: `--no-reminders` to skip the disclosure checklist,
`--no-resolution` to skip resolution/format notes, `--min-edge` to set the
short-edge pixel threshold (default 600). Resolution/format checks need Pillow;
without it the script says so and continues.

### 2. Human review of figures (the scripts cannot do this)

Read each figure and legend. Frame every item as "is this a slip I should fix?".

- Does every quantified panel state n, what error bars mean, and the test used?
- Does every microscopy panel have a scale bar or stated magnification?
- Are all crops, splices, brightness/contrast/gamma, pseudocolor and threshold
  changes disclosed in the legend or Methods?
- Do axis choices avoid accidental distortion (e.g. an unintended truncated
  y-axis, unequal tick spacing, missing units)?
- Does each panel's caption match what the panel actually shows (right group,
  right magnification, right channel)?
- Are composite panels (spliced lanes, assembled grids) assembled from the
  correct, current source images?

### 3. Legend quality (human judgement the script leaves alone)

`legend_check.py` verifies detectable elements, but the legend's title and
overall clarity are yours to judge. A legend must let the figure stand alone
without the main text. A strong data-figure legend has four elements:

1. A descriptive title stating the key takeaway, not a bare "X over time".
2. Enough method context to interpret it (which cells, what treatment).
3. Error-bar/statistic definitions with n.
4. Definitions of colors, symbols, line styles and abbreviations.

Before (weak): "Bacterial expression of three fibrillizing peptides tagged with
GFP, over time (minutes)."

After (strong): "Temporal variation in protein expression of the three GFP-tagged
peptides, Pep 1-3, in BL21(DE3) cells. The x axis shows timing relative to IPTG
induction. Means (+/- s.e.) of n=6 independent experiments."

Also: any microscopy post-processing must be stated in the legend; spliced
blots/gels must be declared; and a review/schematic figure's legend should walk
the reader through the concept rather than report n and error bars.

### 4. Visual design and journal-format check (human review)

The scripts above catch numeric and file-level slips; they do not judge design
quality. Read each figure with these questions in mind, in the same spirit as
section 2 — "is this a slip I should fix?", not an accusation:

- **One figure, one message.** Does each panel convey a single, clear point,
  rather than crowding several unrelated comparisons into one panel?
- **Consistent visual grammar across every figure.** The same color palette,
  font, font size, and line width used throughout the manuscript — not
  drifting figure to figure, a common consequence of figures assembled by
  different co-authors or at different times.
- **Vector format for line art, charts, and schematics** (PDF, SVG, AI, or
  EPS), not a raster export, so they stay crisp at the journal's final print
  size.
- **High-resolution TIFF for microscopy and imaging panels**, not a
  compressed JPEG.
- **Sans-serif font (Arial/Helvetica), sized for the figure's final printed
  width**, not the screen/draft canvas — body and axis text generally no
  smaller than 5-7 pt at final size.
- **Panel labels (a, b, c, ...) bold**, and consistently placed and sized
  across every figure.
- **Colorblind-friendly palette**, avoiding a red-green-only encoding for any
  comparison that needs to be told apart.
- **Statistical significance and exact n annotated directly on the figure
  itself** (not only described in the legend) — e.g. asterisks/n.s. markers
  and the sample size on or beside each relevant panel.
- **Figure width matches the target journal's column specification** at
  final print size (commonly ~85 mm single column and ~170 mm double column;
  Nature specifically uses 89 mm and 183 mm). Confirm the current, exact
  figures against the target journal's own author guidelines (`journal-reformatter`
  fetches these) rather than assuming the commonly cited defaults above still
  hold for that journal.
- **No 3D bar/pie charts, and no decorative clutter** (gradients, drop
  shadows, unnecessary gridlines) that carries no information.

### 5. Target-journal image policy pass

Before submitting, re-read the current image-integrity and figure-preparation
policy of the target journal (they change), and confirm the figures match their
specific format, resolution and disclosure requirements.

## Relationship to sister skills

- `submission-screener` — Pass 6 (wet-lab raw-data/source-data) and Pass 1 (internal consistency) check that source data and figure-referenced numbers are present and consistent at a general level; this skill goes deeper on figure-specific numeric consistency, image-file hygiene, and the visual-design/journal-format checklist above.
- `proof-checker` — the post-acceptance counterpart: re-applies figure scrutiny (resolution, distortion, panel labeling, caption correspondence) to the typeset production proof against the accepted manuscript. This skill is the pre-submission version of that same discipline.
- `journal-reformatter` — fetches the target journal's current author guidelines and handles figure/table *callout* format (numbering, legend placement); it does not judge figure design quality or numeric integrity, which are this skill's job.
- `table-checker` — the equivalent good-faith, non-accusatory self-check for tables, sharing the same three-tier status vocabulary and philosophy. Run both together when assembling a submission package.

## Design notes for maintainers

Scope is figures and images, plus the arithmetic self-consistency of the
statistics table a figure stands for and the standalone completeness of figure
legends. Kept: source-vs-reported numeric consistency (wide or long source
data), the stats sanity table check, exact-duplicate file detection,
resolution/format hygiene, disclosure reminders, and signal-driven legend
checks. Dropped on purpose: perceptual image-similarity forensics
(false-positive heavy and accusatory), numeric fingerprint screening and risk
scoring. Any new check must (a) point to a concrete fix, (b) carry a benign
explanation, and (c) stay silent on clean input.

The visual-design and journal-format checklist (section 4) is deliberately
human-review only, not scripted: reliably classifying "is this raster file
actually a chart that should be vector" or "is this palette colorblind-safe"
from pixel data alone is failure-prone, and a wrong automated call there would
break the concrete-fix/benign-explanation/silent-on-clean-input bar the
scripted checks hold themselves to. Legend *title* quality and overall clarity
(section 3) are the same kind of judgement call, which is why `legend_check.py`
only verifies detectable elements and leaves the title itself to human review.

## Attribution

Parts of this skill are adapted from the MIT-licensed academic-integrity-skill
by lanj (GitHub @1anj), https://github.com/1anj/academic-integrity-skill. See
`ATTRIBUTION.md` for the per-file breakdown of what was adapted versus original
and for the retained upstream license.
