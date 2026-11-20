---
name: submission-screener
description: Pre-submission quality control for a manuscript before it is first submitted, working from whatever files the user has. Checks internal consistency (numbers, citations, figure/table order), completeness of required sections and declarations, the target journal's author guidelines (formatting, limits, reference style), ethics approval and informed consent adequacy, research-integrity red flags (confidentiality breaches, authorship disputes, undeclared competing interests), statistical justification materials, wet-lab raw/source-data upload requirements, and data/code deposition (PRIDE/ProteomeXchange, GEO/SRA, PDB/EMDB, Zenodo, code archival) with DAS wording. Classifies findings as principal (must fix before submitting) or minor. Use whenever preparing a first submission and wanting a pre-submission self-check. Strictly pre-submission; checking a post-acceptance page proof is proof-checker's job, not this skill's.
---

# Submission Screener

Rigorous quality control of a manuscript **before its first submission**: check what a careful reviewer or editor would catch first, so it never reaches them. This is the self-check pass; the goal is to avoid desk rejection, reviewer friction, and a compliance bounce-back, not to critique the science in depth.

**Scope: pre-submission only.** If the paper has already been accepted and there is a typeset proof to check against, this is the wrong skill: use `proof-checker` instead, which diffs the proof against the accepted manuscript. This skill has no accepted-manuscript reference point; everything here is a first-principles adequacy check against the target journal's requirements and general scientific-reporting norms.

## The governing principle

Sort every finding into two classes:

- **Principal** — would likely cause a desk rejection, a required-resubmission bounce, or a compliance failure: a missing or inadequate ethics approval, no consent statement where one is required, no data deposition where the journal mandates one, a required declaration entirely absent, a word/reference limit substantially exceeded, an undeclared competing interest, a confidentiality breach, or an authorship dispute papered over rather than genuinely settled. Fix all of these before submitting.
- **Minor** — stylistic, cosmetic, or easily fixed at any later stage: formatting inconsistencies, small reference-style deviations, minor wording.

Unlike `proof-checker`, everything found here is fixed now; this is exactly the stage where substantive changes are expected and cheap. There is no editor to defer to yet.

## Relationship to sister skills

This skill is the **general, journal-agnostic pass**: it applies to any manuscript regardless of target. Several sister skills go deeper on specific pieces, and should be run alongside this one where they apply, not instead of it:

- `journal-submission-checklist` — deep, field-by-field assessment against a *specific* journal family's mandatory form (Nature Portfolio, MCP/ASBMB, Cell Press STAR Methods) or a study-design guideline (CONSORT, STROBE, ARRIVE, PRISMA). Run this skill first for the general pass, then that one if the target journal or study design requires a structured form.
- `review-simulator` — the deep version of Pass 8's light scientific-soundness catch-net: a full simulated editor desk assessment plus 2-3 reviewer reports. Run this skill's Pass 8 as a quick self-check; run `review-simulator` for the real pre-submission stress test.
- `statistical-rigor-helper` — the deep version of Pass 5's statistical-justification check: whether the specific test, correction, and design are actually rigorous (confounding, pseudoreplication, distributional assumptions, CV/data leakage), using rules distilled from *Modern Statistics for Modern Biology*. Run this skill's Pass 5 as a quick presence/naming check; run `statistical-rigor-helper` for the real statistics rigor check whenever the manuscript has a statistics section.
- `figure-checker` — the deep version of Pass 6's raw-data presence check: whether the figures themselves are numerically consistent with their source data, free of accidental duplicate image files, and meet visual-design/journal-format conventions. Run this skill's Pass 6 as a quick presence check; run `figure-checker` for the actual figure-integrity and design pass. It also has a `legend_check.py` script that automates the mechanical part of Pass 5's figure-legend-statistics check (undefined error bars, missing *n*, unnamed test) — run it alongside Pass 5 for a manuscript with figures.
- `table-checker` — the deep version of Pass 1's cross-manuscript consistency check, applied to a table's own internal formatting (decimal uniformity, units in header vs. cells, footnote-defined abbreviations, main-text vs. supplement placement).
- `cover-letter-writer` — drafts the *short confirmatory* version of these same declarations for the cover letter. This skill checks the manuscript's own, full declarations; keep the underlying fact (COI status, ethics approval, data availability) consistent between the two.
- `journal-reformatter` — checks only whether a required declaration section is *present and labeled* during a reformat; this skill checks whether its *content* is actually adequate.
- `authorship-credit` — CRediT roles, ICMJE authorship eligibility, and resolving a genuine authorship dispute; this skill's Pass 9 only confirms a dispute has actually been settled (every author has seen and approved the final list and order), not who should be an author or in what order — hand off to `authorship-credit` if a real dispute surfaces.
- `citation-auditor` — verifies citation accuracy and finds missing citations for claims; this skill's internal-consistency pass checks citation *mapping* (does every in-text citation resolve), not citation *correctness*.
- `proof-checker` — the same disciplined checking style, applied post-acceptance to the typeset proof instead of the manuscript.

## Inputs

Take whatever is available; more source files make a stronger check.

- **The manuscript** (PDF/DOC/DOCX), or pasted text. Required.
- **The target journal's author guidelines** (any format, or a URL) — lets you check formatting, limits, reference style, and required sections/statements against what the journal actually asks for. If not supplied, ask for the journal name and fetch its current guidelines from the web rather than guessing from memory (requirements change).
- **Source data tables** (XLSX/CSV) — to verify reported values, and to plan what needs depositing.
- **Ethics/IRB/IACUC approval documentation**, if the user has it — to confirm the manuscript's approval number and approving body are stated correctly.
- **Existing repository accessions**, if data was already deposited — to check the DAS references them correctly.

If only the manuscript is given, you can still check internal consistency, completeness, and the declarations already present, but not confirm reported values against source data or draft a deposition plan with real accessions; say so and note what still needs the author.

## Workflow

**1. Inventory and classify.** Identify the manuscript's field, study type (see `references/pre-submission-checklist.md` for the classification this drives), and target journal. Extract text (via the `docx`/`pdf` skills as needed) and identify every section: abstract, methods, results, discussion, and every end-matter declaration (ethics, consent, funding, COI, author contributions, data/code availability, acknowledgments).

**2. Run the multi-pass checklist.** Read `references/pre-submission-checklist.md` and work one pass at a time: internal consistency; completeness; journal-guideline compliance; ethics and informed consent; statistical justification materials; wet-lab raw-data and source-data upload requirements; scientific-soundness catch-net; research-integrity red flags (confidentiality breaches, authorship disputes, undeclared competing interests). Classify every finding principal or minor with evidence and location; never claim something is adequate without a quote from the text.

**3. Assess data and code deposition, and draft the Data Availability Statement.** Read `references/data-deposition-guide.md`. Identify every dataset and code artifact the study produced, match each to the repository it belongs in (PRIDE/ProteomeXchange for MS proteomics, GEO/SRA for sequencing, PDB/EMDB for structures, Zenodo/Figshare for generic data, a Zenodo-archived DOI snapshot for code), and determine whether it is already deposited, needs depositing, or is exempt with a stated reason. For anything not yet deposited, walk the author through the submission process for that repository and what an accession number and reviewer-access link look like once obtained. Draft the DAS in the target journal's expected wording, using real accessions where available and `[[NEEDS AUTHOR INPUT: <accession pending deposition>]]` where not.

**4. Produce the report.** Fill `assets/submission-readiness-report.md`: coverage summary, principal-findings table, minor-findings table, deposition-status table, draft declaration text, the research-integrity red-flags section, and a ready-to-submit verdict.

## The one rule that cannot be broken

**Never invent.** Do not fabricate an ethics approval number, a repository accession, a consent statement, or a statistical justification the manuscript does not actually contain. Where something is missing, say so and flag it — `[[NEEDS AUTHOR INPUT: <what is missing>]]` — rather than drafting confident-sounding text with no basis. A flagged gap costs a question; an invented approval number is research misconduct waiting to be discovered.

## What to check (summary)

The full itemized checklist is in `references/pre-submission-checklist.md`. In brief:

- **Internal consistency:** numbers agree across text, tables, and figures; every in-text citation maps to the reference list; figures/tables called out in the order first cited.
- **Completeness:** every section and declaration the journal requires is present (abstract, methods, results, discussion, ethics, consent, funding, COI, author contributions, data/code availability). This checks *presence* only; see the research-integrity pass below for a *content* audit of the COI statement.
- **Journal-guideline compliance:** word/figure/table/reference/title limits; reference style; formatting (line numbering, structured vs. unstructured abstract).
- **Ethics and informed consent:** the right approval type for the study (human, animal, human tissue/biobank), an actual approval/protocol number, the approving body named, consent obtained and documented (including separate consent for identifiable images), a stated exemption reason where ethics review was not required.
- **Statistical justification materials:** sample-size/power justification present, the statistical test named and appropriate in the Methods (not folded into one generic sentence), every figure legend independently stating its own test and an exact, specific replicate number (not "repeated multiple times"), multiple-comparison correction addressed, and whether supporting statistical material (full model output, code) should be prepared for submission. This is a presence/naming/consistency check; for whether the test, correction, and design are actually rigorous, run `statistical-rigor-helper`.
- **Wet-lab raw-data / source-data upload requirements:** unprocessed images (uncropped blots/gels, raw micrographs) and a source-data file prepared where the journal requires one, distinct from the deposited datasets in Step 3.
- **Data/code deposition and DAS:** see `references/data-deposition-guide.md` and Step 3 above.
- **Scientific soundness (light catch-net):** statistical method suits the data and design; every conclusion traces to a specific result; no over-interpretation beyond what the data show; claims of fact or prior work carry a citation. This is a self-check catch-net, not a full peer review; for the real stress test (a simulated editor desk assessment plus 2-3 reviewer reports), use `review-simulator`.
- **Research-integrity red flags:** the three COPE-style categories that, caught after publication instead of now, become a public correction or worse — breach of confidentiality (participant identifiability beyond consent-to-publish, unauthorized use of a third party's unpublished data, peer-review confidentiality), an authorship dispute papered over rather than genuinely settled (hand off to `authorship-credit` if real), and an undeclared competing interest (financial ties, IP, funder role, personal relationships) beyond the mere presence of a COI statement. Missing or inadequate ethical approval is covered in depth above, not repeated here. Treat any finding in this pass as principal by default.

Domain note: for fields like proteomics, treat m/z values, protein/gene name capitalization and italics, and reagent catalog numbers as principal-error territory, same as `proof-checker` does at the proof stage.

## Output

A submission-readiness report (template in `assets/submission-readiness-report.md`): a **principal findings** table (must all be resolved before submitting), a **minor findings** table, a **deposition status** table (dataset/artifact, repository, status, accession if available), draft declaration text ready to paste (ethics, consent, data/code availability), and a one-line verdict on whether the manuscript is ready to submit. Keep each finding precise and located (section, page, figure/table). Never invent a value, approval number, or accession; mark anything unverifiable "needs author confirmation."

## Cautions

Journal guidelines, repository submission steps, and reporting norms all change; fetch the target journal's current guidelines rather than relying on memory, and confirm the deposition steps in `references/data-deposition-guide.md` against the repository's current documentation for anything time-sensitive. This is a self-check, not certification — the author remains responsible for the final submitted version, and a deep scientific critique is a human reviewer's job, not this skill's.
