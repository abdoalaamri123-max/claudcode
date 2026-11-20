---
name: journal-submission-checklist
description: >-
  Assesses a manuscript against mandatory submission checklists and produces a fill-in report. Two kinds, which can combine: (1) publisher families, each a separate report, Nature Portfolio/NP (Reporting Summary + Editorial Policy Checklist), Molecular and Cellular Proteomics/MCP-ASBMB (MS checklists by study type), Cell Press/CP (STAR Methods + Key Resources Table); (2) universal reporting guidelines chosen by study design, not publisher, often required alongside a publisher family, CONSORT (randomised trials), STROBE (cohort/case-control/cross-sectional), ARRIVE 2.0 (animal research), PRISMA 2020 (systematic reviews/meta-analyses). Auto-routes by target journal and by study design, and assesses every item with evidence, never certifying compliance. Cues: reporting summary, editorial policy checklist, STAR Methods, KRT, CONSORT, STROBE, ARRIVE, PRISMA, flow diagram. Ask which journal or study design if unstated.
---

# Journal Submission Checklist Assessor

Some journals require structured submission checklists that verify a manuscript reports enough
detail to be reproducible and policy-compliant. This skill reads a manuscript, walks every field
of the relevant checklist(s), decides what the manuscript already covers, flags gaps, drafts
answers, and produces a report the author uses to fill the actual forms.

It supports two kinds of checklist, which can combine on the same manuscript:

- **Publisher families**, each with its OWN separate report, routed by the target journal:
  - **Nature Portfolio (NP)**: Reporting Summary + Editorial Policy Checklist.
  - **Molecular & Cellular Proteomics (MCP / ASBMB)**: study-type-specific MS checklists.
  - **Cell Press (CP)**: STAR Methods (four sections) + a Key Resources Table (KRT).
- **Universal reporting guidelines**, each with its OWN separate report, routed by **study
  design**, not by publisher — many journals across many publishers require these in addition to,
  not instead of, whatever publisher family also applies:
  - **CONSORT 2010**: randomised controlled trials.
  - **STROBE**: cohort, case-control, or cross-sectional observational studies.
  - **ARRIVE 2.0**: *in vivo* animal research.
  - **PRISMA 2020**: systematic reviews and meta-analyses.

The skill assists; it does not certify. The author remains responsible for the final signed
answers. Never claim a requirement is satisfied without evidence in the text, and clearly mark
items only the author can confirm (signatures, figure-rendering choices, the flow-diagram graphic
itself).

## Inputs
- A manuscript (`.pdf`, `.docx`, `.txt`, or `.md`), or pasted manuscript text.
- The target/aim journal (needed to pick the publisher family, if any; ask if unstated and
  unclear). Not needed to pick a universal guideline — that follows from the study design.
- Optional: which checklist(s) to assess (default: everything that applies).

If no manuscript is provided, ask for one before proceeding. The assessment is evidence-based and
cannot be done from memory.

## Step 0 — Classify the study design and identify the journal family, then route

These two questions are independent. A manuscript can need a publisher family only, a universal
guideline only, both, or neither; do every track that applies this pass rather than stopping at the
first one found.

**A. Study design — drives a universal guideline, regardless of publisher:**
- **Randomised controlled trial** (parallel, factorial, or other randomised design): go to the
  **CONSORT track** below. Non-inferiority/equivalence, cluster, and pragmatic trials use CONSORT
  extensions with extra items not covered here; note if one applies.
- **Observational study** (cohort, case-control, or cross-sectional): go to the **STROBE track**
  below, and determine which of the three designs it is (several items differ by design).
- **In vivo animal research** (live, non-human animals): go to the **ARRIVE track** below.
  Cell-culture or purely computational work does not trigger this even if animal-derived material
  is used elsewhere.
- **Systematic review or meta-analysis**: go to the **PRISMA track** below. A narrative review with
  no reproducible search-and-selection method does not trigger this.
- **None of the above** (e.g. a purely computational or in vitro discovery paper with no clinical,
  observational, animal, or review component): no universal guideline applies; go straight to B.
- A manuscript can combine designs (e.g. a trial with an embedded systematic-review section); assess
  each applicable track independently and say so. For an observational study with an embedded
  randomised sub-study (e.g. a cohort study containing a small randomised sub-analysis), run STROBE
  on the full cohort and CONSORT on the randomised sub-study, but state explicitly, per item, which
  population its evidence covers ("participant flow: full cohort N=..." vs. "randomised sub-study
  n=...") — do not let the same item label imply one shared assessment when the two tracks actually
  describe different populations.

**B. Journal family — drives NP / MCP / CP, if any:**
- **Nature Portfolio** (Nature and any Nature-branded journal, plus Springer Nature titles that use
  these forms): go to the **Nature Portfolio (NP) track** below.
- **Molecular & Cellular Proteomics / MCP**: go to the **MCP track** below.
- **Cell Press**: any Cell Press life-science journal (Cell, Cancer Cell, Cell Reports, Molecular
  Cell, Neuron, Immunity, Cell Metabolism, Cell Systems, Current Biology, Developmental Cell, Med,
  Structure, Cell Reports Methods, STAR Protocols, etc.) plus iScience and Stem Cell Reports: go to
  the **Cell Press (CP) track** below. Note: Cell Press physical-science titles (Chem, Joule,
  Matter, Newton, Device, Cell Reports Physical Science, etc.) and Trends review journals are not
  STAR-Methods journals; if the target is one of those, say STAR Methods may not apply and point to
  that journal's guide.
- **Another publisher with no bundled family** (Science/AAAS, PLOS, eLife, Elsevier, Wiley, MDPI,
  Frontiers, etc.): say this skill has no publisher-family checklist for that journal, but still do
  any applicable universal-guideline track from A — those apply regardless of publisher.
- **Unstated and unclear**: ask which journal, unless only a universal-guideline track applies, in
  which case the journal is not needed to proceed. If the user names specific forms (e.g. "the
  reporting summary," "CONSORT," "the DIA checklist"), infer the track from that directly.

Example combinations: a Nature Medicine RCT needs both NP (Reporting Summary + Editorial Policy
Checklist) and CONSORT; a PLOS Medicine RCT needs CONSORT only (PLOS's own checklist forms are out
of this skill's scope); a Cell Press animal study needs both STAR Methods/KRT and ARRIVE; a
Molecular & Cellular Proteomics discovery paper with no clinical/animal/review component needs MCP
only.

## Step 1 — Get the manuscript text (both tracks)
If given a file path, extract text with the bundled script:
```bash
python scripts/extract_manuscript.py <manuscript_path>
```
(The script auto-installs `pdfplumber` / `python-docx` if needed. If it warns that a PDF yielded
almost no text, the file is likely scanned or image-only: ask the user to OCR it or supply a
text/docx version before assessing, since otherwise there is nothing to read.) If the user pasted
text, use it directly. Read the whole manuscript, with special attention to **Methods / Experimental
Procedures**, figure legends, and end-matter (Data/Code availability, Competing interests, Author
contributions, Ethics, Acknowledgements).

---

## Nature Portfolio (NP) track

### N1. Load the field inventories
Read both before assessing so no field is skipped:
- `references/np-reporting-summary-fields.md`
- `references/np-editorial-policy-fields.md`

### N2. Classify the study (drives conditional sections)
Determine: the field-specific track (Life sciences is the default for molecular/cell/proteomics/
tissue work; otherwise Behavioural & social or Ecological); human involvement (participants, human
data, or human biological material such as patient tissue); which materials/systems/methods are
involved (antibodies, cell lines, animals, plants, clinical data, dual-use, ChIP-seq, flow
cytometry, MRI, macromolecular structures, stem cells); any custom code/algorithms; and deposited
data types (proteomics PRIDE/ProteomeXchange PXD, MassIVE, jPOST; sequencing GEO/SRA; structures
PDB/EMDB; generic Zenodo/Figshare). Only deep-dive sections that apply; mark the rest N/A with a
one-line basis. Do not invent involvement.

### N3. Assess every field and produce the report
Assign each field a status (`✅ Covered` / `⚠️ Partial` / `❌ Missing` / `➖ N/A` /
`👤 Author-only`) with a short quote and location. Draft ready-to-paste answers for missing or
partial items using the manuscript's own details. Fill `assets/np-report-template.md` exactly, lead
with the coverage summary and prioritized action items, and end with the draft-statements appendix.

Save to `/mnt/user-data/outputs/` as `np-checklist-report_<short-title>.md` and present it.
The official Nature Portfolio forms (Reporting Summary and Editorial Policy
Checklist) are **not** bundled with this skill; the author downloads the
current versions from the journal's online submission system (Nature Portfolio
provides them there and on its reporting-standards policy page,
https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards)
and completes them using this report.

---

## MCP track

### M1. Select which MCP checklists apply (auto-assign)
Read `references/mcp-checklist-fields.md` and use its routing table. The **Peptide & Protein
Identification** checklist is the base for essentially all MS proteomics papers. Then add:
- **DIA** if DIA/SWATH/diaPASEF or library-based/spectrum-centric analysis is used (DIA-NN,
  Spectronaut, library-free are strong cues).
- **Targeted MS** if MRM/PRM/SRM (Skyline/Panorama, transitions, heavy peptides, Tier 1/2/3).
- **Glycomic** if glycans/glycopeptides/glycolipids.
- **Clinical Proteomics** if human clinical/biomarker samples (patient, biobank, IRB, FFPE tumor);
  this also requires the MS checklist(s) for the identification data.

State the selection explicitly in the report and only assess the selected checklists. A typical MS
discovery paper needs one to three of these.

### M2. Assess every item
For each item of each selected checklist, assign a status (`✅ Covered` / `⚠️ Partial` /
`❌ Missing` / `➖ N/A` / `👤 Author-only`). MCP requires a **page number** next to each satisfied
item, so record the manuscript page/section where the evidence sits (or note "add to Methods").
MCP items are mostly Yes/N/A confirmations tied to specific Experimental Procedures / Results
content, so check for the exact required detail (for example, software with version, mass
tolerances, FDR method, replicate type distinction, exact n as a number not a range).

### M3. Produce the report
Fill `assets/mcp-report-template.md`, rendering only the checklist sections that apply. Lead with
the "which checklists apply" table and prioritized action items; end with the draft-text appendix
(Experimental Design and Statistical Rationale subsection, search-parameters block, repository
statement, ethics statement if clinical, and a cover-letter note for reviewer credentials plus
Tier level if targeted).

Save to `/mnt/user-data/outputs/` as `mcp-checklist-report_<short-title>.md` and present it. The
official MCP/ASBMB checklists are not bundled with this skill; direct the author to download
the ones that apply from the MCP author guidelines (https://www.mcponline.org/) and complete them
using this report.

---

## Cell Press (CP) track

### C1. Load the field inventory and decide which sections apply
Read `references/cp-star-methods-fields.md`. STAR Methods has four headings plus a KRT:
1. Experimental Model and Study Participant Details, 2. Method Details (required),
3. Quantification and Statistical Analysis, 4. Additional Resources, 5. Key Resources Table.
Section 2 and the KRT always apply. Include Section 1 only if the study uses life-science
experimental models/participants (omit for purely computational/physical-science work); include
Sections 3 and 4 only if the study has statistics/quantification or a new resource/clinical trial.
Confirm the target is a STAR-Methods journal (life-science title, iScience, or Stem Cell Reports).

### C2. Assess every reference-sheet item
Walk the general format requirements and each applicable section, plus the KRT checklist, assigning
a status (`✅ Covered` / `⚠️ Partial` / `❌ Missing` / `➖ N/A` / `👤 Author-only`) with evidence
and location. STAR Methods is prose-based (not a Yes/N/A form), so check that required content is
actually present and detailed enough to reproduce. Human tissue turns on the Section 1 human
reporting (ethics committee + informed consent, and the demographic fields, or a documented reason
plus a generalizability-limitation note). For the KRT, draft rows from items the manuscript
mentions (software with versions and RRIDs/DOIs, deposited data with accessions, antibodies,
biological samples), and flag custom subheadings, missing identifiers, or code without a DOI.

### C3. Produce the report
Fill `assets/cp-report-template.md`, rendering only the sections that apply. Lead with the
structure check + coverage summary and prioritized action items; include draft KRT rows and an
appendix of paste-ready text (experimental-design paragraph, statistics statement, ethics
statement if human, data/code + KRT accessions/DOIs).

Save to `/mnt/user-data/outputs/` as `cp-checklist-report_<short-title>.md` and present it. The
official Cell Press Key Resources Table template and STAR Methods guide are not bundled with this
skill; direct the author to the Cell Press STAR Methods author resources
(https://www.cell.com/star-methods) to download the current KRT template and fill it directly using
the draft rows in this report.

---

## CONSORT track

### T1. Load the field inventory and confirm scope
Read `references/consort-fields.md`. Confirm the manuscript is a parallel-group randomised trial;
if it is a non-inferiority/equivalence, cluster, or pragmatic design, note that CONSORT extension
items exist beyond this reference's 25-item base checklist and are not covered here.

### T2. Assess every item and the flow diagram
Assign a status to each of the 25 items with evidence and location. A CONSORT flow diagram is
expected alongside the checklist; confirm one is present and consistent with the participant-flow
text (item 13), and mark the diagram graphic itself `👤 Author-only` since building it is out of
scope. Registration number, protocol availability, and funding (items 23–25) are common gaps; check
them explicitly.

### T3. Produce the report
Fill `assets/reporting-guideline-report-template.md`, §A only. Lead with the coverage summary and
top action items. Save to `/mnt/user-data/outputs/` as `consort-checklist-report_<short-title>.md`.

---

## STROBE track

### S1. Load the field inventory and confirm the design variant
Read `references/strobe-fields.md`. Determine and state explicitly which of cohort, case-control,
or cross-sectional applies, since items 6, 12, 14, and 15 have design-specific wording; assess only
the matching variant.

### S2. Assess every item
Assign a status to each of the 22 items with evidence and location. Confirm the participant-flow
numbers (item 13) and whether a flow diagram is used; check that missing-data and confounding
handling (items 11–12) are explicit, since these are common gaps.

### S3. Produce the report
Fill `assets/reporting-guideline-report-template.md`, §B only, noting the assessed design variant
at the top. Save to `/mnt/user-data/outputs/` as `strobe-checklist-report_<short-title>.md`.

---

## ARRIVE track

### R1. Load the field inventory and confirm scope
Read `references/arrive-fields.md`. Confirm the study involves live, non-human animals *in vivo*;
cell-culture-only or purely computational work does not belong here even if animal-derived material
appears elsewhere.

### R2. Assess the Essential 10, then the Recommended Set
Assess items 1–10 (Essential 10) first and treat any gap there as principal; a manuscript reporting
animal research should not have an Essential-10 item missing. Then assess items 11–21 (Recommended
Set) as lower-severity gaps. Ethical approval (item 14) and exact n per group with a stated method
for handling exclusions (items 2–3) are common gaps; check them explicitly.

### R3. Produce the report
Fill `assets/reporting-guideline-report-template.md`, §C only, with the two sub-tables (Essential
10, Recommended Set). Save to `/mnt/user-data/outputs/` as `arrive-checklist-report_<short-title>.md`.

---

## PRISMA track

### P1. Load the field inventory and confirm scope
Read `references/prisma-fields.md`. Confirm the manuscript is a systematic review (with or without
meta-analysis); note if a related extension (PRISMA-P for a protocol, PRISMA-ScR for a scoping
review) would be more appropriate instead, since their item sets differ.

### P2. Assess every item, the abstract checklist, and the flow diagram
Assign a status to each of the 27 main items with evidence and location, then the separate 12-item
abstract checklist if the journal expects a structured abstract. A PRISMA flow diagram is expected
for item 16a; confirm one is present and its counts are consistent with the narrative, and mark the
diagram graphic itself `👤 Author-only`. Registration/protocol (item 24) and risk-of-bias / certainty
assessment (items 11, 15, 18, 22) are common gaps; check them explicitly.

### P3. Produce the report
Fill `assets/reporting-guideline-report-template.md`, §D only, including the abstract-checklist
block if applicable. Save to `/mnt/user-data/outputs/` as `prisma-checklist-report_<short-title>.md`.

---

## Judgement notes (all tracks)
- **Do not over-claim.** "Covered" needs evidence. When unsure, use `⚠️ Partial` and say why.
- **Versions and links matter.** Software without a version, a database without a version/entry
  count, or custom code without a public repo is `⚠️ Partial` at best; reviewers check these.
- **Raw data / repository.** MS work must deposit raw data (ProteomeXchange/PRIDE/MassIVE/jPOST).
  For MCP, reviewer credentials for private data go in the cover letter, not the form.
- **Ethics for human tissue.** Patient/biobank material triggers the Nature human-participants
  blocks, and on the MCP side both the Clinical Proteomics ethics/IRB item and the Targeted
  Clinical Compliance check. Flag a missing approval number.
- **Statistics.** If a study has no inferential statistics, mark the relevant items N/A once with a
  basis rather than flagging each as a gap.
- **Consistency.** Where the same fact appears on multiple forms (data availability, statistics,
  software), assess once and keep the wording consistent across the report.
- **Version caveat.** Bundled Nature PDFs are the April 2023 revision; MCP checklist versions vary
  by study type; the Cell Press STAR Methods guide referenced here reflects the April 2026 revision;
  CONSORT is built on the 2010 checklist (a CONSORT 2025 revision is emerging via
  consort-spirit.org — confirm which the target journal currently asks for); STROBE (2007) and
  ARRIVE 2.0 (2020) are unrevised and current. Tell the author to confirm the current version on
  the journal's submission system before final submission.
- **Universal guidelines stack with publisher families, they don't replace them.** Running a
  CONSORT/STROBE/ARRIVE/PRISMA track never substitutes for an applicable NP/MCP/CP track, or vice
  versa; do both if both apply, and say so in the top-level summary handed to the author.
- **Complements, doesn't compete with, `review-simulator`.** That skill's simulated editor desk
  review gives a first-pass compliance-and-completeness impression as part of a broader mock peer
  review; this skill's evidence-quoted, field-by-field verdict is the authoritative one for
  compliance specifically — if the two disagree on a compliance item, this skill's verdict governs.
- **Flow diagrams (CONSORT, PRISMA) are a required artifact, not just a checklist item.** The
  skill checks that the manuscript states one is included and that its narrative numbers are
  internally consistent, but does not draw the diagram itself; that stays `👤 Author-only`.
- **Essential vs. recommended (ARRIVE).** Grade the Essential 10 more strictly than the
  Recommended Set; a gap in the Essential 10 is the animal-research equivalent of a principal
  error elsewhere in this skill.
- **Bilingual users.** Keep drafted statements in English (the forms are English); the surrounding
  report explanation can be in the user's language if they are writing in it.

## Example triggers
- "Here is my manuscript, help me with the Nature reporting summary and editorial policy checklist."
- "Pre-check my paper for Nature Protocols reproducibility requirements before I submit."
- "Getting this DIA proteomics paper ready for Molecular & Cellular Proteomics, what do I need?"
- "Fill the MCP DIA checklist from my Methods section."
- "Which MCP checklists apply to my clinical FFPE proteomics study?"
- "Check my randomised trial manuscript against CONSORT before I submit to Nature Medicine."
- "Is my cohort study STROBE-compliant? Here's the draft."
- "Fill the ARRIVE checklist for this mouse knockout study."
- "Assess my systematic review against PRISMA 2020, including the flow diagram numbers."
- "Set up STAR Methods and the key resources table for my Molecular Cell submission."
- "Pre-check my Cell Reports Methods paper against the STAR Methods reference sheet."
