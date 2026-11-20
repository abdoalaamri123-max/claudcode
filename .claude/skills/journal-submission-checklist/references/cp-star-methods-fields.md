# Cell Press STAR Methods — Structure + Field Inventory

Source: Cell Press "STAR Methods guide for authors" (April 2026) and the Key Resources Table
template. STAR Methods (Structured, Transparent, Accessible Reporting) is required for acceptance
at Cell Press life-science journals, iScience, and the partner journal Stem Cell Reports.

## Scope / routing (which Cell Press journals use STAR Methods)
- **Applies:** Cell Press life-science journals (Cell, Cancer Cell, Cell Chemical Biology, Cell
  Genomics, Cell Host & Microbe, Cell Metabolism, Cell Reports, Cell Reports Medicine, Cell Stem
  Cell, Cell Systems, Current Biology, Developmental Cell, Immunity, Med, Molecular Cell, Neuron,
  Structure, Cell Reports Methods, STAR Protocols) plus iScience and Stem Cell Reports (partner).
- **Likely different / check the journal guide:** Cell Press physical-science titles (Chem, Joule,
  Matter, Newton, Device, Cell Reports Physical Science, Chem Catalysis, Matter & Light, etc.) and
  the Trends review journals, which are not STAR-Methods life-science journals. If the target is one
  of these, note that STAR Methods may not apply and point the author to that journal's guide.
- **Section 1 (Experimental Model and Study Participant Details) is omitted** for computational or
  physical-science studies with no life-science experimental models.

There is no word count limit; STAR Methods is typeset but not copyedited. It must be a Word
document, placed after the figure legends if in the main file. References cited in STAR Methods and
the KRT go in the single main reference list. Do not include complex/numbered tables or figures
(other than chemical reaction schemes) in STAR Methods; those go to supplemental.

Status codes for the report: `✅ Covered` / `⚠️ Partial` / `❌ Missing` / `➖ N/A` /
`👤 Author-only` (formatting/rendering the author must verify, e.g. subheading typeface).

STAR Methods has four headings (2 is required; 1, 3, 4 are omitted when not applicable) plus a KRT:
1. Experimental Model and Study Participant Details
2. Method Details (required)
3. Quantification and Statistical Analysis
4. Additional Resources
5. Key Resources Table (KRT)

The editor **reference sheet** below is the checklist reviewers apply. Assess each item.

---

## General format requirements
- No more than two levels of customized subheadings organizing the STAR Methods text.
- Subheadings are under 45 characters, not numbered, and free of reference/figure/table citations;
  each subheading level uses a typeface different from body text (`👤 Author-only` for typeface).
- Enough method/analysis detail that a reader can understand and reproduce without other papers.
- All references cited in STAR Methods and the KRT appear in the main reference list.

## §1. Experimental Model and Study Participant Details  *(omit if no life-science models)*
List every model under a separate heading (human, animal, plant, cell line, primary culture,
microbe strain). Report the influence/association of sex and/or gender on results, or discuss its
absence as a limitation.
- **Human participants/samples:** committee approval + informed-consent statement; sex, gender,
  ancestry, race, ethnicity, socioeconomic status, and age reported (or where to find them), else a
  statement of why plus a generalizability-limitation discussion; sample size + how allocated to
  groups; for sensitive materials under ISSCR category 1a/2, a specific ethics statement.
- **Human embryos/gametes/stem cells (ISSCR 1b, 2):** an ethics statement citing ISSCR 2021
  compliance and category, review process, procurement/donation conditions, informed consent,
  future-use discussion; for category 2, the approving EMRO/committee name and affiliation.
- **Live vertebrates / animal studies:** approving committee identified + confirmation experiments
  conform to regulatory standards; sex, genotype, age/developmental stage, health/immune status,
  previous procedures, and other ARRIVE parameters; housing and husbandry; allocation to groups.
- **Sex as a variable:** for studies with both sexes (animal or human), an analysis of the
  influence/association of sex (and, for humans, gender/ancestry/race/ethnicity/SES) on results, or
  a statement of why not plus a generalizability discussion; include negative results.
- **Cell lines / primary cultures:** culture/growth conditions incl. temperature; sex of cells
  (animal origin) or sex + gender (human origin), or a statement of why not; authentication info.
- **In vitro / non-human source organisms:** culture conditions/maintenance; source organism
  details (strain, growth/husbandry, sex, age).
- **Plants:** growth conditions (chamber make/model, temperature, light intensity/period, substrate,
  fertilizer, humidity; farm location + season/years for field); seed sterilization, stratification,
  germination, vernalization with solutions/media/temperatures/times.
- RRIDs recommended for all models and as the KRT identifier.

## §2. Method Details  *(required)*
- Method-specific descriptive subheadings (<45 chars, no numbering, no citations).
- Precise, full details of every procedure (how, when, where, why); do not defer to other papers.
- Temperature reported where it can affect results (electrophysiology, behavior, binding assays,
  chemical reactions, materials synthesis/characterization).
- Experimental-design information (per NIH/ARRIVE): replication; randomization/stratification
  strategy; whether done anonymized/blinded; inclusion/exclusion criteria; sample-size estimation.
- All datasets, program code, and methods cited in text and listed in references (publication or a
  persistent identifier such as a DOI).

## §3. Quantification and Statistical Analysis  *(omit if none)*
- Explanation of the statistical analysis used to quantify data, and the software used.
- Where the statistical details live (figure legends, results, etc.): tests used, exact value of n
  and what n represents, definition of center, dispersion/precision (mean, median, SD, SEM, CI),
  how significance was defined.
- Whether methods were used to test that data met the assumptions of the statistical approach;
  randomization/stratification, sample-size estimation, and inclusion/exclusion methods.

## §4. Additional Resources  *(omit if none)*
- Links to websites/resources created or expanded by the study (protocol download, forum, etc.),
  each briefly described as "Description: URL".
- Clinical trial registry numbers and links, if relevant.

## §5. Key Resources Table (KRT)
Three columns: **REAGENT or RESOURCE | SOURCE | IDENTIFIER**. Use the official Cell Press KRT
template (download from the STAR Methods author resources, https://www.cell.com/star-methods) or the KRT webform. Standard
subheadings only (do not add custom ones): Antibodies; Bacterial and virus strains; Biological
samples; Chemicals, peptides, and recombinant proteins; Critical commercial assays; Deposited data;
Experimental models: Cell lines; Experimental models: Organisms/strains; Oligonucleotides;
Recombinant DNA; Software and algorithms; Other.
Checklist:
- No custom headings/subheadings added (prohibited).
- Every KRT item is also described in Method Details / main text in the context of its use.
- Every paper cited in the KRT is in the main reference list.
- Source and identifier given for each resource ("N/A" if none).
- Unique identifiers labeled and prepended (Cat#, Lot, Clone, RRID, GEO, PDB, etc.).
- All standardized data types deposited with accession numbers (Deposited data section).
- All original code included with a DOI; all published code with a DOI or reference to its paper.
- If more than 10 oligonucleotides/RNA sequences, provide a supplemental table and cite it in KRT.
- One item per row; descriptions intuitive and informative.
- For software/algorithms, provide the version; RRIDs recommended for antibodies and model organisms.

## Proteomics / MS notes (common for this author)
- Software and algorithms rows need versions (DIA-NN, Spectronaut, MaxQuant, Perseus, QuPath, R
  packages, custom code) and, for custom code, a DOI (Zenodo/GitHub release).
- Deposited data rows need accessions: ProteomeXchange/PRIDE PXD (raw MS), plus any PDB/GEO/Zenodo.
- Human FFPE/patient tissue turns on §1 human-participant reporting: ethics committee + consent
  statement and the demographic fields, or a documented reason for their absence.
