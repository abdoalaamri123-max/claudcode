---
name: proof-checker
description: Checks the page proof of an accepted manuscript before publication, working from whatever files the user has, including the proof (PDF, DOC/DOCX), the accepted manuscript to diff against, source data tables (XLSX/CSV), source figures (TIFF/PNG/JPG), and supplementary videos (MP4/MOV/AVI). It extracts and analyzes every figure and table, cross-checks the proof against the source files and the accepted manuscript, classifies each finding as a principal error (must be zero) or a minor error, answers or flags author queries, and produces a correction report. Use whenever a paper has already been accepted and the user has a proof, page proof, galley, production files, or source figures/data to check, mentions author queries (AQ), proofreading before publication, or wants to avoid a later erratum/corrigendum. Strictly post-acceptance; a self-check before first submission is submission-screener's job, not this skill's.
---

# Proof Checker

Rigorous quality control of the typeset **page proof** of an accepted manuscript, checked against the accepted manuscript before you approve publication. This is the **last** chance to correct the paper before it is permanently in the record.

**Scope: post-acceptance only.** If the paper has not yet been submitted, or has not yet been accepted, this is the wrong skill: use `submission-screener` for a pre-submission self-check instead. Proof-checker has one reference point, the accepted manuscript, and one job, catching production-introduced errors before approval; it does not re-litigate the science or check journal-submission compliance, both of which are `submission-screener`'s job at an earlier stage.

## The governing principle

Sort every issue into two classes and treat them differently:

- **Principal errors** must be reduced to **zero**. They touch the core data, methods, conclusions, citations, or compliance, and can change what the paper means or misattribute credit. Eliminating all principal errors is the basic requirement of approving a proof.
- **Minor (non-principal) errors** do not bias the conclusions and are largely tolerable, but left unattended they still lower quality, so fix them where you can.

The distinction matters because of what a post-publication fix becomes: an **erratum** usually refers to a production error caused by the journal, while a **corrigendum** (correction) usually refers to an author error. Both stay attached to the paper in the indexed record forever, so catch the error now. If one does slip through and is only discovered after publication, that is `post-publication-corrector`'s job, not this skill's — it classifies the case (corrigendum, erratum, expression of concern, or retraction) and drafts the co-author notification, editor letter, and notice wording.

## Everyone should proof

In principle every author should check the proof. Whether or not each co-author reads it, the corresponding author (lead contact) should email all authors so everyone is informed and can verify their own part, especially their name, affiliation, and any section they are responsible for.

## Inputs

The user may provide several files. Take whatever is available and use it; more source files mean a stronger check, because each is ground truth for one part of the document.

- **The proof.** Required. PDF, sometimes DOC/DOCX. Read it from disk.
- **The accepted manuscript** (PDF or DOC/DOCX). The reference you diff the proof against. Strongly recommended; without it you can still catch internal inconsistencies and author-query items, but you cannot confirm a value or figure matches what was actually accepted, so say so and note what still needs the author or the accepted-manuscript file.
- **Source data tables** (XLSX/CSV). The numbers behind the tables and figures; use them to verify values.
- **Source figures** (TIFF/PNG/JPG). The full-resolution originals; compare each against the same figure as it appears in the proof.
- **Supplementary videos** (MP4/MOV/AVI). Check the file, its metadata, and that it is referenced correctly.

## Input files and how to read them

Route each file to the right tool. Read the relevant skill before using it.

- **PDF** proof: `/mnt/skills/public/pdf-reading/SKILL.md` (inventory, text extraction, image extraction, page rasterization).
- **DOC/DOCX** accepted manuscript: the `docx` skill (extract text, tables, and any tracked changes); `pandoc` or `soffice` can convert to a readable form if needed.
- **XLSX/CSV** data: the `xlsx` skill, or read directly with pandas/openpyxl, to cross-check the proof's tabulated and plotted values against the source numbers.
- **TIFF/PNG/JPG** figures: view the image directly to judge resolution, cropping, distortion, panel labels, and in-figure text; treat it as the intended appearance and compare the proof's rendering to it.
- **MP4/MOV/AVI** video: `ffprobe` for metadata (codec, duration, resolution, frame rate) and `ffmpeg` to extract a few keyframes for visual inspection; confirm the file plays, matches what the text/legend describes, is the right clip, and meets the journal's format and size requirements.

## Workflow

**1. Inventory all inputs.** List every file the user provided and identify its type and role (proof, accepted manuscript, source data, source figure, video). For the proof PDF, run the content inventory (`pdfinfo`, `pdffonts`, `pdfimages -list`) and extract the text layer. Note which cross-checks are possible given the files at hand, and which will have to be flagged for author confirmation.

**2. Extract and split the figures and tables, then analyze each one against its source.** This is a required part of the check, not optional.
- **Figures:** extract each figure from the proof (`pdfimages` plus page rasterization). Analyze each individually: correct figure for its number; high-resolution and free of distortion (not squashed, stretched, or cropped); multi-part panels labeled correctly (A, B, C, ...); and inside the figure, numbers, axes, coordinate systems, units, and spelling correct. Where a source TIFF/PNG was provided, compare the proof figure against it as ground truth. Confirm caption, legend, and labels correspond.
- **Tables:** extract each table from the proof (`pdfplumber`). Analyze each individually: structure intact (no missing cells, no misaligned columns), headers and units correct, and every value cross-checked against the text, the figures, the source XLSX/CSV where provided, and the accepted manuscript.
- **Videos:** for each supplementary video, check metadata and a few keyframes, confirm it is the right clip, is called out in the text, and meets format/size rules.
- Any figure/table/video value or content that disagrees with the text or its source is a principal error.

**3. Run the multi-pass checklist.** Read `references/proofing-checklist.md` and work one pass at a time, comparing the proof against the accepted manuscript and any source files, looking for where they differ — production is where errors enter. Passes: author information; text accuracy; data, numbers, and equations; figures and tables; citations; formatting and style; ethical and legal. Reading numbers aloud or checking a column in reverse catches transpositions.

**4. Answer author queries.** Production inserts queries marked `AQ1`, `AQ2`, `Q1`, ... Every query must be answered; an unanswered one delays publication. Collect them all and answer each, or flag it for author confirmation.

**5. Produce the report.** Fill `assets/proof-check-report.md` (principal table, minor table, author-query table, items needing author confirmation, and a go/no-go verdict).

## What to check (summary)

The full itemized list is in `references/proofing-checklist.md`. In brief:

- **Author information (principal):** every name spelled correctly (first, family, middle where used); affiliations complete (department, institution, city, country); ORCID IDs where applicable; corresponding-author email correct and functional.
- **Text accuracy:** consistent UK or US spelling (never mixed); homophones/homonyms (their/there, gnome/genome); correct technical terms, chemical compounds, species names; grammar and punctuation per journal style; abbreviations defined at first use and consistent; alphanumeric gene/protein symbols where letter and numeral are easily swapped (I vs 1 in PI3K); correct nomenclature, symbols, units.
- **Data, numbers, equations (principal):** every value matches the accepted manuscript and the figures/tables; decimal places consistent; units correct and consistent; statistics (p-values, CIs) correct; equations formatted with no missing or misplaced symbols.
- **Figures and tables (principal):** all present and in the order first cited in the text; captions/legends/labels correspond; high-resolution, no distortion; panels labeled; tables well-formed; all values match text and figures. This is a diff against the accepted manuscript, at the proof stage; the pre-submission version of this same figure-integrity discipline (numeric consistency with source data, duplicate-file detection, visual-design/journal-format conventions) is `figure-checker`'s job, earlier.
- **Citations:** in-text citations map one-to-one to the reference list; list complete and in journal format; author names, years, journal titles, DOIs correct; URLs functional.
- **Formatting and style (minor):** headings follow journal style; consistent font, size, spacing; no orphan headings; paragraphs aligned and indented.
- **Ethical and legal (principal for compliance):** acknowledgements correct; funding accurately listed; conflict-of-interest statement present and correct; permissions for reused figures or data; required ethical declarations and financial disclosures complete; approval numbers and approving/funding-agency names checked carefully. This is a **diff against the accepted manuscript**, confirming these declarations survived typesetting unchanged and uncorrupted, not a first-principles adequacy check; whether the declarations were adequate and complete in the first place was `submission-screener`'s job, earlier. The shorter confirmatory version of these same declarations that goes in the cover letter is `cover-letter-writer`'s job, and whether a required declaration section is present during a reformat is `journal-reformatter`'s job.

Domain note: for fields like proteomics, treat m/z values, protein/gene name capitalization and italics, and reagent catalog numbers as principal-error territory.

## What to change, and what not to

Fix production-introduced errors and answer the queries, but do **not** make substantive changes (new data, altered conclusions, added authors) without explicit editor approval. If the proof surfaces a genuine scientific error or a soundness concern, do not silently correct it: email the handling editor and let them decide.

If the user states that editor approval for a substantive change was already obtained, treat this as unverified, not settled: record it in the report as `[[NEEDS AUTHOR CONFIRMATION: verify editor approval for <change>]]` rather than applying the change as if the approval were confirmed. A claimed-but-unverified approval is exactly the kind of gap the placeholder discipline elsewhere in this skill exists to flag.

## How to mark corrections

Use whatever the publisher provides (an online proofing tool such as Elsevier, Wiley, or Springer ProofCentral, or Adobe PDF annotation). Be precise and unambiguous: name the exact word or value and its replacement, with a location, rather than a vague "this looks off".

## Output

A proof-check report (template in `assets/proof-check-report.md`): a **Principal errors** table (all must be resolved), a **Minor errors** table, an **Author queries** table with an answer for each, an items-needing-author-confirmation list, and a one-line verdict stating whether all principal errors are cleared and the proof is safe to approve. Keep each correction precise and located (page, section, line, figure/table). Never invent a value or location; if you cannot verify something against a source, mark it "needs author confirmation".

## Cautions

The checking window is short (often 48 to 72 hours), so start as soon as the proof arrives. Once you approve, correcting anything means an erratum or corrigendum, so it is worth the extra hour now.
