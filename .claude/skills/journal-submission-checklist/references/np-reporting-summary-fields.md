# Reporting Summary — Field Inventory

Source: Nature Portfolio `nr-reporting-summary` (XFA form, April 2023 revision).
This is the authoritative list of what the form asks. Walk every field. For each,
find manuscript evidence, assign a status, and draft an answer.

## Table of contents
1. Header
2. Statistics (10 confirmation items)
3. Software and code
4. Data
5. Research involving human participants, their data, or biological material
6. Field-specific reporting (choose ONE track)
7. Reporting for specific materials, systems and methods (conditional deep-dives)

Status codes to use in the report: `✅ Covered` / `⚠️ Partial` / `❌ Missing` / `➖ N/A` / `👤 Author-only` (cannot be judged from text, e.g. a signed confirmation or a figure-rendering property).

---

## 1. Header
- **Corresponding author(s)** — free text. Pull from manuscript author block / correspondence line.
- **Last updated by author(s)** — date, `YYYY-MM-DD`. Author fills; leave a placeholder.

## 2. Statistics
Prompt: "For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section." Each is a **Confirmed** checkbox. Only assess the ones that apply to the study; if the paper has no inferential statistics, most are `➖ N/A` and note that in the report.

1. Exact sample size (n) for each experimental group/condition, as a discrete number and unit of measurement.
2. Statement on whether measurements were from distinct samples or the same sample measured repeatedly.
3. The statistical test(s) used AND whether one- or two-sided. (Common tests by name; complex ones described in Methods.)
4. Description of all covariates tested.
5. Description of any assumptions or corrections (e.g. normality tests, multiple-comparison adjustment).
6. Full description of statistical parameters: central tendency (means) or estimates (regression coefficient) AND variation (SD) or uncertainty (CI).
7. For null-hypothesis testing: test statistic (F, t, r) with CIs, effect sizes, degrees of freedom, and P value; P as exact values where suitable.
8. For Bayesian analysis: choice of priors and MCMC settings.
9. For hierarchical/complex designs: appropriate level for tests and full reporting of outcomes.
10. Estimates of effect sizes (Cohen's d, Pearson's r) and how calculated.

Evidence to look for: Methods "Statistical analysis" subsection; figure legends; words like *t-test, ANOVA, Wilcoxon, PERMANOVA, limma, DEqMS, FDR, Benjamini-Hochberg, permutation, n =, mean ± SD, 95% CI, p <*.

## 3. Software and code
Policy note: custom algorithms/software central to the research but not yet published must be made available to editors/reviewers; code deposition in a community repo (e.g. GitHub) is strongly encouraged.

- **Data collection** — free text. Name every instrument-control / acquisition software with **version**. (e.g. microscope acquisition software, mass-spec control software, plate readers.)
- **Data analysis** — free text. Name every analysis tool/package with **version** and, for custom code, a repository link. (e.g. DIA-NN, MaxQuant, Spectronaut, Perseus, R + specific packages, Python libs, QuPath, ImageJ/Fiji, custom scripts.)

Evidence to look for: Methods; "Reporting summary"/"Software" lines; version numbers; GitHub/Zenodo URLs. Flag any custom tool that lacks a public link.

## 4. Data
Policy note: all manuscripts must include a **data availability statement** covering, where applicable: accession codes / unique identifiers / web links for public datasets; description of any restrictions; and for clinical or third-party data, adherence to policy.

- **Data availability** — free text; assess whether the manuscript's data availability statement is present and complete.

Evidence to look for: a "Data availability" heading; repository accessions (for proteomics: **PRIDE / ProteomeXchange PXD…**, MassIVE, jPOST; for sequencing: GEO/SRA/ArrayExpress; PDB; Zenodo/Figshare DOI); restriction language ("available upon reasonable request", controlled access).

## 5. Research involving human participants, their data, or biological material
Only if the study uses human participants, human data, or human biological material (e.g. patient tissue). Otherwise mark the whole block `➖ N/A`.

- **Reporting on sex and gender** — how sex and/or gender was determined, considered, and reported.
- **Reporting on race, ethnicity, or other socially relevant groupings** — categories used, why, and their source.
- **Population characteristics** — relevant covariates of the cohort (age, sex, disease stage, etc.).
- **Recruitment** — how participants/samples were recruited and any resulting bias.
- **Ethics oversight** — the board/committee that approved the protocol. (Full approval info must also be in the manuscript.)

Evidence to look for: cohort/patient tables; "IRB", "ethics committee", "informed consent", approval numbers; tissue-bank/biobank sourcing; age/sex demographics.

## 6. Field-specific reporting
Prompt: "Please select the one below that is the best fit for your research." Choose exactly one and complete only that track.
- **Life sciences** (default for molecular biology, proteomics, cell/tissue work)
- **Behavioural & social sciences**
- **Ecological, evolutionary & environmental sciences**

Recommend the track in the report and complete its design questions.

### 6a. Life sciences study design
"All studies must disclose on these points even when the disclosure is negative."
- **Sample size** — how it was determined; state if no power calculation was done and give the rationale.
- **Data exclusions** — whether any data were excluded and the pre-established criteria.
- **Replication** — how many times experiments were replicated and whether replications were successful.
- **Randomization** — how samples/organisms were allocated; if not relevant, explain why.
- **Blinding** — whether investigators were blinded; if not relevant, explain why.

### 6b. Behavioural & social sciences study design
Study description; Research sample; Sampling strategy; Data collection; Timing; Data exclusions; Non-participation; Randomization.

### 6c. Ecological, evolutionary & environmental sciences study design
Study description; Research sample; Sampling strategy; Data collection; Timing and spatial scale; Data exclusions; Reproducibility; Randomization; Blinding; Did the study involve field work? (if yes: Field conditions, Location, Access & import/export, Disturbance.)

## 7. Reporting for specific materials, systems and methods
For each item, first decide **Involved in the study: yes/no** by scanning the manuscript. Only deep-dive the ones that are involved; list the rest as "not involved".

### Materials & experimental systems
- **Antibodies** → if involved: **Antibodies used** (each antibody, supplier, catalogue #, clone, lot, dilution) and **Validation** (how each was validated for the application/species).
- **Eukaryotic cell lines** → **Cell line source(s)**; **Authentication** (STR etc.); **Mycoplasma contamination** (tested? result); **Commonly misidentified lines** (any used, per ICLAC register).
- **Palaeontology and archaeology** → Specimen provenance; Specimen deposition; Dating methods; confirm raw/calibrated dates available.
- **Animals and other organisms** → Laboratory animals (species/strain/sex/age/housing); Wild animals; Reporting on sex; Field-collected samples; ethics.
- **Clinical data** → follow ICMJE; a completed CONSORT checklist required. Clinical trial registration; Study protocol; Data collection; Outcomes.
- **Dual use research of concern** → Hazards (public health / national security / crops & livestock / ecosystems / other); Experiments of concern; precautions, oversight, benefits.
- **Plants** → Seed stocks; Novel plant genotypes; Authentication.

### Methods
- **ChIP-seq** → Data deposition (raw + processed in public db e.g. GEO; called-peak files e.g. BED); Data access links; Files in database submission; Genome browser session; Replicates; Sequencing depth; Antibodies; Peak calling parameters; Data quality; Software.
- **Flow cytometry** → Plots confirmations (axis labels marker+fluorochrome, scales visible, contour/pseudocolor, numeric counts); Sample preparation; Instrument; Software; Cell population abundance; Gating strategy (+ figure).
- **MRI-based neuroimaging** → Experimental design (type, specifications, behavioral measures); Acquisition (imaging type, field strength, sequence & parameters, area, diffusion MRI); Preprocessing (software, normalization, template, noise/artifact removal, volume censoring); Statistical modeling & inference (model type/settings, effects tested, whole-brain/ROI, anatomical location, statistic type, correction); Models & analysis (connectivity, graph analysis, multivariate/predictive).

Evidence to look for (proteomics/imaging papers commonly trigger): **Antibodies** (immunofluorescence / IHC markers with catalogue numbers) and **Eukaryotic cell lines** (if any cultured lines). Flow/ChIP/MRI usually not involved for LC-MS/spatial-proteomics work — confirm from text before marking N/A.
