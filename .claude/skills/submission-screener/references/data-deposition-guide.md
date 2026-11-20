# Data and Code Deposition Guide

Read this for Pass 7 of the pre-submission checklist: matching every dataset and code artifact the study produced to the repository it belongs in, walking the author through depositing it, and drafting the Data Availability Statement (DAS).

**Never invent an accession number.** An accession is issued by the repository at the moment of submission, not before. If deposition has not happened yet, say so and use `[[NEEDS AUTHOR INPUT: accession pending deposition]]` rather than a placeholder that reads as if it already exists.

**Version caution.** Repository submission tools and interfaces change; the workflow below is the general shape as of this writing. Confirm the current submission steps on the repository's own documentation before depositing, especially for a time-sensitive submission.

## Matching data type to repository

| Data type | Repository | Accession format |
|---|---|---|
| MS proteomics (raw files, search results) | PRIDE, via the ProteomeXchange (PX) consortium | `PXD0xxxxx` |
| Alternative proteomics repositories | MassIVE (UCSD), jPOST (Japan), iProX (China) — all issue a PX accession too, via ProteomeXchange | `PXD0xxxxx` (same namespace) |
| Sequencing / transcriptomics (RNA-seq, ChIP-seq, scRNA-seq, etc.) | GEO (processed data + metadata) and/or SRA (raw reads) | `GSExxxxx` (GEO series), `SRPxxxxxx` / `SRRxxxxxx` (SRA) |
| Macromolecular structures (X-ray, cryo-EM, NMR) | PDB (atomic coordinates), EMDB (cryo-EM maps) | `PDB xxxx` (4-character), `EMD-xxxxx` |
| Flow cytometry | FlowRepository | `FRxxxxxx` |
| Generic datasets, images, supplementary files with no field-specific home | Zenodo, Figshare, Dryad | a DOI (`10.5281/zenodo.xxxxxxx`) |
| Custom analysis code / pipelines | A version-controlled host (GitHub/GitLab) for development, **archived as a citable, versioned snapshot** for the paper | a Zenodo-archived DOI (or Software Heritage / GitHub-native release DOI) pointing to the exact code version used |

If a study spans more than one data type (e.g. a proteogenomics paper), deposit each type in its own matching repository and list every accession in the DAS.

## PRIDE / ProteomeXchange (MS proteomics)

PRIDE is the proteomics member of the ProteomeXchange (PX) consortium; other PX members (MassIVE, jPOST, iProX) issue the same `PXD` accession namespace, so the workflow is equivalent regardless of which member repository is used.

**What to submit:**
- Raw instrument files (vendor-native, e.g. `.raw`, `.d`, `.wiff`) or an open format (`.mzML`).
- Search/identification result files (e.g. the search engine's native output, or `mzIdentML`).
- The FASTA database(s) used for the search.
- A completed metadata form: species, sample type, instrument, experiment type (e.g. shotgun, DIA, targeted), modifications searched, and a brief project description.

**Process (general shape):**
1. Submit via the PRIDE submission tool or the web-based upload interface at the EBI PRIDE Archive.
2. A `PXD` accession is issued at submission time, before curation completes — the dataset starts in a **private** state.
3. A **reviewer account** (a reviewer-specific username/password, or a reviewer URL) is generated automatically, so editors and reviewers can access the private dataset during review without it being public. Include this reviewer access in the cover letter, not the manuscript itself.
4. On acceptance, the submitter (or the PRIDE team, on request) makes the dataset public; the `PXD` accession then resolves publicly and should be cited in the DAS and, if the journal asks, in the reference list as the last item before supplementary references.

**Common gaps to flag:** raw files not actually uploaded (only a summary spreadsheet); no reviewer access account generated ahead of submission; FASTA database missing (identification cannot be reproduced without it); modifications searched not stated in the metadata.

## GEO / SRA (sequencing and transcriptomics)

**What to submit:**
- Raw sequencing reads (SRA) and/or processed data matrices (GEO): counts tables, normalized expression values, peak calls, as appropriate to the assay.
- A completed metadata (MIAME/MINSEQE-compliant) description: sample source, processing pipeline, platform, and experimental design linking samples to conditions.

**Process (general shape):**
1. Register and submit via the GEO submission portal.
2. A `GSE` accession is typically approved within about 5 business days of a complete submission; incomplete submissions (missing raw files or metadata) are not assigned promptly, so submit well before the deadline.
3. Records can be kept **private until a linked manuscript is published**, with an option to grant **reviewers anonymous private access** during review — request this at submission and include the reviewer link in the cover letter.
4. On publication, release the record to public (GEO does this automatically at the requested date, or on author request); the `GSE` accession is then cited in the DAS.

**Common gaps to flag:** raw reads deposited to SRA but no corresponding GEO series linking them with sample metadata (or vice versa); the experimental-design metadata insufficiently describes which sample is which condition/replicate; reviewer access not requested ahead of submission.

## PDB / EMDB (structures)

- Atomic coordinates go to the PDB; cryo-EM density maps go to EMDB (a structure solved by cryo-EM typically needs both: the map in EMDB and the fitted model in PDB, cross-referenced).
- A wwPDB **validation report** is required alongside the deposition (many journals, including Nature Portfolio, explicitly require this at submission — see the "Additional policy considerations" section a `journal-submission-checklist` NP assessment would also check).
- Depositions can be held on-hold pending publication; request a specific release date or "on publication" release, and include the reviewer-access details the repository provides for embargoed structures.

## Zenodo / Figshare / Dryad (generic data, and code archival)

- Use for datasets with no field-specific repository, and for **archiving a citable snapshot of analysis code** even when the live development repository is on GitHub/GitLab.
- The common pattern: link a GitHub repository to Zenodo, then create a tagged release; Zenodo automatically archives that release and mints a DOI. Cite the **Zenodo DOI**, not just the GitHub URL, in the code availability statement — a live repository can change or disappear, a versioned DOI-archived snapshot cannot.
- Figshare and Dryad work similarly for datasets (upload, receive a DOI); Dryad is common for datasets tied to a specific publication and is sometimes journal-mandated (e.g. by evolution/ecology journals).

## Drafting the Data Availability Statement

Match the wording to the actual situation; never claim a status that is not yet true.

**All data already public, with accessions:**
> "The [mass spectrometry proteomics / RNA-seq] data generated in this study have been deposited in [PRIDE / GEO] under accession [PXDxxxxxx / GSExxxxxx] and are publicly available as of the date of publication."

**Deposited but embargoed until publication:**
> "The data generated in this study are deposited in [repository] under accession [accession], and will be made publicly available upon publication. Reviewer access is provided via [reviewer link/credentials] (see cover letter)."

**Not yet deposited (flag for the author, do not present as done):**
> `[[NEEDS AUTHOR INPUT: deposit the raw MS data to PRIDE and insert the PXD accession here before submission]]`

**Restricted data (e.g. patient data under a data-use agreement):**
> "Due to [patient privacy / data-use agreement] restrictions, the [dataset] cannot be made publicly available. Access may be requested from [the corresponding author / a named data-access committee], subject to [the specific governance process, e.g. an approved data-use agreement with the originating institution]."

**No new data generated, or all data already in the paper:**
> "All data supporting the findings of this study are available within the article and its supplementary information."

**Code availability (separate statement, where the journal asks for one):**
> "The analysis code used in this study is available at [Zenodo DOI], archived from [GitHub repository URL] at the version used for this manuscript ([commit/tag])."

Always check the target journal's own required phrasing (some, e.g. Nature Portfolio, have a specific expected sentence structure covered in more depth by `journal-submission-checklist`'s NP track); use the templates above as a starting point, not a substitute for the journal's own instructions.
