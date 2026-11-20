# MCP (Molecular & Cellular Proteomics) — Checklist Routing + Field Inventory

Source: ASBMB / Molecular & Cellular Proteomics author checklists and MS data guidelines.
MCP is NOT Nature Portfolio. It uses study-type-specific checklists completed on the submission
site, plus underlying data guidelines. Authors note the manuscript page where each item appears.

Unlike Nature, MCP items are mostly Yes / N/A confirmations tied to specific Experimental
Procedures / Results content. The compliance check verifies that required information is present,
not scientific quality. Missing required information causes delays or rejection until fixed.

## How to route (which checklist(s) apply)
Almost every MS proteomics paper needs the **Peptide & Protein Identification** checklist as the
base. Then ADD checklists by study type. A single manuscript often needs 2 to 3 of these.

| If the manuscript involves... | Apply this checklist |
|---|---|
| Any MS-based protein / peptide / PTM identification + quantification (DDA/discovery) | Peptide & Protein Identification (base, §A) |
| Data Independent Acquisition (DIA / SWATH; library-based or spectrum-centric) | DIA (§B) — plus the base checklist for any DDA library work |
| Targeted MS (MRM / PRM / SRM), Tier 1/2/3 assays | Targeted MS (§C) |
| Glycans, glycopeptides, glycolipids | Glycomic (§D) |
| Human clinical samples / biomarker or clinical study | Clinical Proteomics (§E) — plus the relevant MS checklist(s) |

Detection cues: "DIA", "SWATH", "diaPASEF", "library-free", DIA-NN, Spectronaut → DIA.
"MRM"/"PRM"/"SRM"/"Skyline"/"Panorama"/"heavy peptide"/"transitions" → Targeted.
"glycan"/"glycopeptide"/"glycosylation profiling" → Glycomic.
"patient"/"biobank"/"IRB"/"clinical cohort"/"FFPE tumor" → Clinical (and note IRB/ethics).

Status codes for the report: `✅ Covered` / `⚠️ Partial` / `❌ Missing` / `➖ N/A` / `👤 Author-only`.
For MCP, "Page" is required next to each satisfied item — record the manuscript page/section where
the evidence sits so the author can transcribe it into the form.

Raw data note (applies to all MS checklists): raw vendor-format data must be deposited at first
submission in a public repository (ProteomeXchange / PRIDE / MassIVE / jPOST); reviewer
username/password go in the cover letter if data are private during review.

---

## §A. Peptide & Protein Identification (base MS checklist)

### A1. Experimental Procedures — Experimental Design and Statistical Rationale
Requires a subsection with the exact header "Experimental Design and Statistical Rationale".
- Sample size (n) for each experiment, as a number (ranges are not acceptable).
- Rationale for that n (statistical power of detection or similar).
- Numbers and types of controls employed.
- Number of replicates, with a clear distinction between biological (independent), process, and
  technical replicates, and the rationale.
- Criteria for inclusion/exclusion of data points (if relevant).
- Description of the statistical methods used for analysis.
- Justification for the statistical methods (e.g. normality of the dataset).

### A2. Experimental Procedures — Search Parameters and Acceptance Criteria (MS/MS and/or PMF)
- Name + release version/date of peak-list-generating software.
- Name + release version/date of the search engine.
- Name + release version/date of sequence database / spectral library searched.
- If database generated in-house: source of sequences + software used to compile.
- Number of entries actually searched.
- Specificity of all proteases used.
- Number of missed and/or non-specific cleavages permitted.
- List of all fixed modifications (with residue specificity).
- List of all variable modifications (with residue specificity).
- Mass tolerance for precursor ions.
- Mass tolerance for fragment ions (not required for PMF).
- Known contaminants excluded (primarily PMF).
- Threshold score / expectation value for accepting individual spectra.
- Justification of that threshold.
- FDR estimation for large datasets + how it was calculated.

### A3. Results/Supplemental — Peptide and Protein Identification
- Table of all peptide sequences assigned (note deviations from expected cleavage).
- Precursor charge and m/z per assignment.
- All modifications observed.
- Number of matched/unmatched masses (PMF).
- Peptide identification score(s).
- Protein accession # + source database.
- Number of distinct peptides per protein.
- % coverage per protein (or derived identification probability).
- Single-peptide + PMF identifications: annotated spectra provided (public repository with entry
  number, or as supplemental material).

### A4. Results/Supplemental — Post-Translational Modifications (if PTMs reported)
- Site(s) of modification clearly located within each peptide.
- Justification of any localization score threshold.
- Separate table for peptides with ambiguous site assignments.
- Annotated, mass-labeled spectra for all modified peptides (public repository or supplemental).

### A5. Results/Supplemental — Protein Inference (if protein groups reported)
- Accession numbers for all proteins combined into a group.
- Which peptides are distinct vs shared within a group.
- Any proteins identified from a different species than studied (by homology).

### A6. Results/Supplemental — Quantification (if quantitative)
- Quantification measurements for each peptide and protein.
- How raw MS data were processed to yield quantification.
- Analytical reliability (technical replicates + statistical treatment).
- Biological reliability (biological replicates, independent experiments, statistics). Single
  biological experiments are generally not acceptable.
- Adjustments for systematic errors.
- Random-error handling (outliers, exclusion thresholds).
- Estimates of uncertainty for individual proteins.
- How analyte identity was verified for non-database identifications.
- How multiple isoforms in a group were quantified.
- Spectral counting (if used): number of peptides/spectra counted; inclusion of modified,
  semi-tryptic, or shared peptides.

### A7. Raw Data Submission
- Raw MS data deposited (Y).
- Location + identifying info (repository URL, deposit ID, username, hash/identifier, password).
- Reviewer login also in the cover letter.

---

## §B. DIA (Data Independent Acquisition)
Not all items apply to every DIA strategy; pick spectrum-centric and/or peptide-centric as used.
Read the full DIA guidelines too; the checklist is a subset.

### B1. Experimental Design and Statistical Rationale
- Subsection header present.
- Numbers and types of sample conditions.
- Methods for sample acquisition-order randomization (if appropriate).
- Whether retention-time standards or spiked protein/peptide standards were used.
- Whether MS1 data were acquired.
- Whether the m/z range was fractionated for fragmentation; if so, separation parameter (m/z,
  mobility), number of windows, whether overlapping windows were acquired, total cycle time.
- If a library was created: number and type (biological/technical) of samples used.
- Description or reference to the statistical tests used.
- Justification for the choice of statistical tests.

### B2. Spectrum-Centric DIA — Peak List Generation
- Software used to create peak lists.
- Parameters (thresholding, de-multiplexing, de-isotoping).
- How retention/drift time and intensity were assigned to peaks.
- Maximum number of precursor peak lists an observed fragment ion could be included in.

### B3. Spectrum-Centric DIA — Search Engine
- Name + version of search software.
- Name + release version/date of sequence databases / spectral libraries.
- If library generated in-house: source of sequences + software.
- Number of entries searched + number of proteins covered.
- Enzyme specificity + missed/non-specific cleavages.
- Fixed modifications (residue specificity).
- Variable modifications (residue specificity).
- Mass tolerance for precursor (if relevant) and fragment ions.
- Threshold score / expectation value.
- Estimated FDR at peptide / protein / batch level.
- Description of how FDR was calculated.

### B4. Peptide-Centric DIA — Spectral Library
- Source of library stated.
- If created in this study: DDA MS/MS (base checklist) completed.
- Software used for library generation + parameters (handling of multiple spectra per precursor,
  any thresholding/peak removal).
- Estimated FDR of library entries + estimation method.
- If public library: version/release + download location.
- Number of entries searched + number of proteins.
- Whether metadata (retention time, ion mobility) was associated with spectra.
- If decoys created: how, how many searched, protein-level FDR assignment.

### B5. Peptide-Centric DIA — Matching of Data to Spectral Library
- Name + version of search software.
- If precursor-ion detection attempted: how used + mass tolerance.
- If RT / ion mobility used: tolerances + alignment across acquisitions.
- Number of peaks considered for identifying peptides + selection criteria.
- Mass tolerance for matching library vs experimental data.
- If modifications reported: how site localization was evaluated.
- Estimated FDR at peptide / protein / batch level + how calculated.

### B6. Results/Supplemental
Protein level: accession number; number of distinct peptide sequences per protein; if library
searching, number of distinct peptides from that protein in the library; single-peptide proteins
have annotated spectra or chromatograms.
Peptide level: accession number; all peptide sequences + modifications; observed precursor m/z and
z (if MS1 used); spectrum-centric score/statistical measure; for a biological modification, a
reliability measure or ambiguity indication for site localization; annotated spectra/chromatograms
for biologically-modified peptides and single-peptide proteins.

### B7. Quantification + Raw Data
Quantification measures in the table + how derived; post-processing (outlier rejection, minimum
intensity thresholds); number of peptides used for quantification if different from identification;
statistics for technical + biological reliability; how isoforms in a group were quantified (if
relevant). Raw data deposited with location + identifying info.

---

## §C. Targeted MS (MRM / PRM / SRM)

### C1. Section I — General (all targeted papers)
- Tier level stated (Tier 1, 2, 3, or combination).
- Names of databases + access codes for raw data (and chromatogram files if not uploaded as
  supplement).
- If human samples (other than established cell lines): Clinical Compliance check completed
  (IRB approval + how biofluids/tissue collected and handled).

### C2. Section II — Chromatograms (Tiers 1 and 2 only)
- All chromatograms used in quantification provided (Skyline/Panorama link or PDF), with database
  names + access codes if applicable.
- If integration boundaries were manually adjusted: noted, with methods described.

### C3. Section III — Experimental Design and Rationale
- Subsection with header "Experimental Design and Rationale".
- Criteria used to select target peptides (uniqueness to proteoform, PTM-site avoidance).
- Sample size (n) per experiment, as a number (no ranges).
- Rationale for that n (e.g. statistical power).
- Numbers and types of controls.
- Number of replicates with biological/process/technical distinction.
- Whether samples were processed/run blinded.
- Inclusion/exclusion criteria for data points (if relevant).
- Methods used for analysis + statistical cutoffs (p-value, FDR) for identification AND
  quantification.
- Justification of statistical methods.
- Software described with versions + explicit options/parameters; in-house source code provided
  if applicable.

### C4. Section IV — Development and Analytical Validation of the Assay
- Type of targeted experiment (PRM, MRM/SRM).
- How precursor ions + transitions were selected (in silico, discovery, database/library/lit).
- Methods to optimize transition ion abundance.
- Methods to identify interferences.
- Transitions monitored per analyte (supplementary table).
- Precision of measurements determined/reported.
- Response-to-concentration behavior (linearity), curve-fitting algorithm, response curves.
- Chromatography/desalting methods (packing, column dimensions, flow rates, mobile phases).
- Internal standards identified + use fully described.
- Methods to characterize internal standards (AAA, MALDI/ESI MS, HPLC-UV).
- Concentration + stability of heavy peptide standards / labeled proteins over the study.
- LOD/LOQ values + calculations (if determined).
- System suitability evaluation (robustness, reproducibility, stability, carryover).
- For studies over weeks/months: QC of overall system performance + reproducibility over time.

### C5. Section V — Methods of Data Collection and Analysis
- Software for peak picking + peak-area-ratio determination.
- How transitions were selected/used for quantification + any data filtering.
- Whether single or multiple peptides used for protein concentration + how qualifiers used.
- If external calibration used: calibrators, curve-fitting equations, QC samples, acceptance
  criteria.
- Precision (SD, CV, SE) reported per peptide/protein.

---

## §D. Glycomic (glycans / glycopeptides / glycolipids)

### D1. Experimental Procedures — Section I
- Clearly defined degree of analysis supporting reported structures (assumptions on linkage,
  monosaccharide identity, etc.).

### D2. Experimental Procedures — Section II
- Peak-list-generating software + release version.
- Parameters/thresholds used, including exclusion of contaminant peaks / degradation products.
- Search engine name + release version.
- Database/spectral library version + number of entries searched.
- Search parameters: fixed/variable modifications considered.
- Enzyme/chemical release specificity + efficiency (if measured).
- Justification of the assignment threshold, including for isobaric/isomeric species.
- For quantitative data: rationale for quantification of isobaric/isomeric structures.

### D3. Results/Supplemental — Section III (per glycan, in a table)
- Glycan assignment (symbol nomenclature per Essentials of Glycobiology).
- Precursor m/z + charge observed.
- Deviation between experimental and theoretical mass.
- Modifications observed (reducing end, adducts, etc.).
- Number of matched fragments above threshold (MS).
- Number of assigned/unassigned mass values above threshold (MS-only data).
- Relevant scores if software used for assignment.
- MS/MS (and full MS) annotated spectra for all assignments.
- For quantitative studies: measurement + accuracy (mean and error).

---

## §E. Clinical Proteomics (human clinical / biomarker studies)

### E1. Ethics Approvals (required, no exception)
- Statement of institutional Ethics/Animal Committee (IRB/ACUC) approval in the article text.

### E2. Study Goals and Design
- Stage/phase of the study (discovery / verification / validation) and the candidate stage.
- Flow of subjects/samples: initial cases, numbers at each analysis stage, dropout reasons
  (diagram recommended for larger studies).

### E3. Subject Sources and Description
- Source of biospecimens (centralized/internal biobank, clinical-trial collection, surgery).
- Inclusion/exclusion criteria for study + reference cohorts.
- Disease definition: description (subtype, stage, grade, histology, clinical score).
- Disease type in standard terminology (ICD codes where known).
- Known confounders relative to sampling time (intra/pre-operative status, drugs/anesthetics).
- Intrinsic factors + demographics + clinical characteristics (age, sex/gender, disease stage,
  comorbidities) for study and control subjects.

### E4. Biospecimen Qualifications
Tissue: processing type (formalin, ethanol, embedding medium, freezing, lysis); post-cutting
fixation for frozen tissue; enrichment methods (microdissection, fractionation); any histological
review.
Biofluids: SOPs referenced; if not, method of collection (for urine specify 24-h/first
morning/etc.), tube type/size, additives (anticoagulants, preservatives, protease inhibitors),
processing conditions (time to separation, centrifugation, temperature, time to freezing).
Primary cell lines: clinical details of subject/biospecimen of origin; generation/characterization
protocol including passage number + number of clones.

### E5. Statistical Considerations
- Central hypothesis tested.
- Model building and validation.
- Clear definition of the statistical algorithm.
- Rationale for cut-off thresholds and other model parameters.
- Independence of exploratory (training) vs confirmative (test) analyses.
- Point estimates, p-values, and/or confidence intervals.

### E6. Technical Considerations
- Performance characteristics (technical + process: fractionation, digestion, etc.) of the
  analytical process/assay(s) described in Experimental Procedures. MS-based identifications must
  additionally meet the base Peptide & Protein Identification criteria (§A).
