# Pre-Submission Checklist (pass by pass)

Read this for the line-by-line pre-submission check. Work one pass at a time. Classify each finding principal (must fix before submitting) or minor (fix where reasonable). Unlike a proof-stage check, every finding here gets fixed now — this is the cheapest point in the whole process to catch a problem.

## Pass 0 - Classify the study first

Before the rest of the checklist, determine:
- **Field and study type**: which of human-subjects research, animal research, human-tissue/biobank work, a clinical trial, an observational study, a systematic review, or a purely computational/in-vitro study this is. This drives which of Passes 4-5 apply and at what depth (mirrors the classification `journal-submission-checklist` uses for its own routing; if a structured guideline like CONSORT/STROBE/ARRIVE/PRISMA or a publisher form like NP/MCP/CP applies, note it and point the author to `journal-submission-checklist` for the deep version).
- **What data and code the study produced**: raw instrument output, processed datasets, custom analysis code, structural coordinates, images. This feeds Pass 7's deposition assessment.

Do not invent involvement in a category the manuscript does not support; mark it N/A with a one-line basis.

## Pass 1 - Internal consistency

- Every numerical value agrees across the text, tables, and figures.
- Every in-text citation maps to an entry in the reference list, and every reference-list entry is cited at least once.
- Figures and tables are called out in the text in the order they are numbered (Fig. 2 not cited before Fig. 1).
- Units and decimal places are consistent throughout.
- Abbreviations are defined at first use and used consistently thereafter.
- This checks agreement across the whole manuscript; a table's own internal formatting (decimal uniformity within a column, units in the header vs. buried in cells, abbreviations defined in a table footnote, main-text vs. supplement placement) is `table-checker`'s job, and the equivalent for figures and images is `figure-checker`'s.

## Pass 2 - Completeness

Confirm every section and declaration the manuscript needs is present, using the target journal's guidelines where available:
- Title, abstract, keywords, main text sections (introduction, methods, results, discussion).
- Author list, affiliations, corresponding-author contact.
- Acknowledgments, funding statement, conflict-of-interest/competing-interests statement (presence only here — see Pass 9 for whether its content is actually complete).
- Author-contributions statement.
- Ethics/consent statement (see Pass 4), data availability statement and code availability statement (see Pass 7).
- Any journal-specific required statement (e.g. an AI-use disclosure, a inclusion-and-diversity statement).

Anything absent is flagged with what section is missing and, where possible, a draft the author can fill in (never invented content, a placeholder to write from).

## Pass 3 - Journal-guideline compliance

Where the target journal's author guidelines are available (fetch live if not supplied; do not rely on remembered conventions):
- Word count, abstract length, figure/table count, and reference count within the stated limits.
- Reference style matches the journal's format.
- Formatting requirements: line numbering, structured vs. unstructured abstract, title-page contents.
- File and figure specifications (formats, resolution, size) the journal states for initial submission.

If the target journal has a structured mandatory form (Nature Portfolio, MCP/ASBMB, Cell Press STAR Methods) or requires a study-design guideline (CONSORT, STROBE, ARRIVE, PRISMA), name it here and hand off to `journal-submission-checklist` for the field-by-field version; do not attempt to replicate that depth in this pass.

## Pass 4 - Ethics and informed consent

- **Approval type matches the study.** Human-subjects research and human-tissue/biobank work need IRB/ethics-committee approval; animal research needs IACUC (or equivalent) approval; purely computational or public-data-only studies may be exempt, but the manuscript should state the exemption and its basis rather than being silent.
- **Approval is specific, not generic.** The approving committee or institution is named; a protocol or approval number is given (not just "approval was obtained"); the approval covers the actual procedures described, not a related-but-different protocol.
- **Informed consent, where required.** A statement that informed consent was obtained from participants (or their legal guardians); for identifiable images or case details, a **separate**, explicit consent-to-publish statement — a general research-consent form does not cover this on its own, and its absence is a common, serious gap.
- **Clinical trial registration**, if applicable: a registration number and registry name, given before or at the time of first participant enrollment (a trial registered only after the fact is itself often flagged).
- **Animal welfare specifics**, if applicable: species, strain, sex, numbers, and housing/husbandry stated (see ARRIVE Essential 10 in `journal-submission-checklist` for the full version); humane endpoints stated or their absence justified.
- Flag any approval number, committee name, or consent claim you cannot find text supporting; never assume it exists because the study type implies it should.
- **Approval actually covers the data used.** Retrospective analysis of existing records, secondary use of a biobank sample, or reuse of a previously collected dataset each needs its own approval or a documented waiver — the original collection's approval does not automatically extend to a new analysis or a new publication. Multi-site studies need approval (or a documented reliance agreement) at every site that contributed data, not just the coordinating site.
- See Pass 9 for confidentiality risks that go beyond consent-to-publish, and for undeclared competing interests and authorship disputes — none of which belong in this pass.

## Pass 5 - Statistical justification materials

- **Sample size justified.** A stated rationale for n (a priori power calculation, a precedent, or an explicit statement that no formal calculation was done and why).
- **Test choice named and appropriate.** The exact statistical test used is named (not just "statistical analysis was performed"), and it suits the data type, distribution, and study design.
- **Statistical methods complete in the Methods section.** Every test actually used anywhere in the paper is named specifically, not folded into one generic sentence ("appropriate statistical tests were used" or "data were analyzed using GraphPad Prism" with no test named); the software/package and version are given; and it is clear, for each analysis in the Results, which named test produced it.
- **Every figure legend states its own statistical method and exact replicate number, not just the Methods section.** Legends are read independently of the main text, and most journals require this explicitly. For each figure/panel that reports a statistical comparison: the specific test is named in the legend itself (not only inferable from Methods), and the replicate number is an exact count with what it counts stated — "n = 3 biological replicates" or "n = 3 independent experiments," never a vague substitute like "experiments were repeated multiple times" or "representative of several independent experiments." Cross-check: if a figure's legend names a different test than Methods states for that same comparison, flag the inconsistency rather than assuming one of the two is right. `figure-checker`'s `legend_check.py` automates the detectable part of this (undefined error bars, missing n, unnamed test when significance is reported) — run it for the mechanical pass, but still read each legend, since title quality and overall standalone clarity stay a human judgement.
- **Multiple-comparison correction** addressed where many comparisons are made, or an explicit statement that none was needed and why.
- **Exact values, not ranges**: n given as an exact number per group, not "3-5"; exact p-values rather than only "p < 0.05" where the journal expects them.
- **Supporting statistical materials.** Note whether the journal or the complexity of the analysis warrants preparing supplementary statistical material for submission (full model output, a statistics-and-reproducibility checklist, analysis code) beyond what is narrated in the Methods; flag if this looks like it will be needed and is not yet prepared.
- **This pass checks presence and naming, not rigor.** Whether the named test actually suits the design (confounding, pseudoreplication, distributional assumptions, multiple-testing correction appropriateness, CV/data leakage) is `statistical-rigor-helper`'s job — run it on the manuscript's statistics/methods section whenever one exists, alongside this pass.

## Pass 6 - Wet-lab raw-data and source-data upload requirements

Distinct from Pass 7 (repository deposition of full datasets): this is about the **unprocessed originals behind published figures**, which many journals require as a "Source Data" file or supplementary raw-image set at submission, separate from any external repository.

- **Unprocessed blots and gels.** Full-length, uncropped, unadjusted images behind every cropped blot/gel figure, ideally with molecular-weight markers visible.
- **Raw microscopy and imaging.** Original files (not just the exported figure panel) for micrographs, with acquisition metadata where the journal asks for it.
- **Raw flow cytometry / instrument output**, where a figure derives from it (e.g. FCS files behind a flow plot).
- **A "Source Data" file**, if the target journal uses this convention (common at Nature-family and some other journals): the exact numeric values behind every graph and every uncropped image behind every blot/gel figure, organized by figure/panel.
- Flag any figure with a cropped blot/gel or a processed image where the unprocessed original was not supplied, since this is a common source of post-publication image-integrity concerns.
- This pass checks presence of the raw material; whether the figures themselves are numerically consistent with their source data, free of accidental duplicate image files, and meet visual-design/journal-format conventions (vector vs. raster by content type, font/panel-label conventions, colorblind-safe palette, on-figure stats/n annotation, column width) is `figure-checker`'s job.

## Pass 7 - Data and code deposition, and the Data Availability Statement

Read `references/data-deposition-guide.md` for the full repository-by-repository workflow. In brief:
- Every dataset type the study produced is matched to the repository it belongs in and its deposition status determined (already deposited with an accession / needs depositing / exempt with a reason).
- Every custom analysis script or pipeline central to the conclusions is matched to a code-hosting and archival plan (a live repository is not sufficient on its own; a versioned, citable archival snapshot is usually expected).
- The Data Availability Statement (and Code Availability Statement, if the journal separates them) is drafted in the target journal's expected wording, using real accessions where deposition is already done and a clearly flagged placeholder where it is not.

## Pass 8 - Scientific soundness (light catch-net)

A self-check catch-net for the science, lighter than a full peer review — a human reviewer's deep critique is not this skill's job. For a genuine pre-submission stress test (a simulated editor desk assessment plus 2-3 reviewer reports, each with major/minor comments and a recommendation), run `review-simulator` instead of relying on this pass alone.

- **Statistical method appropriate:** the test suits the data type and study design; assumptions are reasonable; multiple-comparison correction is applied where needed (links to Pass 5).
- **Conclusions supported by data:** every conclusion in the abstract and discussion traces to a specific result in the paper; nothing is concluded that the data do not show.
- **No over-interpretation:** language does not exceed the evidence (causal claims from correlational data, generalization beyond the sample studied, absolute terms like "proves" or "first-ever"); claims are proportionate to what the results support.
- **Claims are supported:** assertions of fact or prior work carry a citation (links to Pass 1).

## Pass 9 - Research-integrity red flags

Three categories of finding are exactly the ones that, if they surface after publication instead of now, trigger a COPE-style investigation, correction, or retraction rather than a quiet fix. Missing or inadequate ethical approval is already covered in depth by Pass 4; the following do not have a dedicated home elsewhere in this checklist and need a genuine content check, not just a presence check.

- **Breach of confidentiality.**
  - Participant/patient identifiability beyond the consent-to-publish already checked in Pass 4: does the combination of demographic, geographic, clinical, or occupational detail make an individual identifiable even without a name or photo (a common risk in rare-disease case reports, small cohorts, or an unusual combination of age, location, and diagnosis)? Flag for further de-identification rather than assuming a general consent form covers it.
  - Third-party or collaborator confidential information: any unpublished data, personal communication, grant application, or another group's manuscript content used or referenced here — is there a stated permission (a signed release, or an explicit "personal communication, used with permission" attribution), not just an assumption that sharing was fine?
  - Peer-review confidentiality: if an author reviewed a related manuscript elsewhere, confirm no confidential content, data, or idea from that review appears in this one — a specifically named, recurring COPE issue.
  - Sensitive-location or sensitive-population data (e.g. endangered-species localities, indigenous community data) that needs redaction or a data-sharing agreement before disclosure.

- **Authorship disputes.** Resolving a dispute, or drafting the author list, order, and CRediT roles in the first place, is `authorship-credit`'s job, not this pass's — this pass only confirms the settlement is genuine, not assumed:
  - Every listed author has actually seen and approved the final author list, order, and role attribution — not just the corresponding author's assumption that everyone would agree.
  - No open disagreement has been communicated to the corresponding author about who is included, in what order, or as corresponding/co-first.
  - If the author list changed late (an addition, removal, or reorder close to submission) without a documented reason, flag it rather than letting it pass silently — a late, unexplained authorship change is itself a common red flag.
  - If a real, unresolved dispute surfaces, stop and hand off to `authorship-credit` rather than papering over it here.

- **Undeclared competing interests.** Goes beyond Pass 2's presence check of a competing-interests statement, into whether its content is actually complete:
  - Financial ties to anything related to the study's subject: consulting fees, honoraria, speaker fees, advisory-board or board membership, equity/stock ownership, or employment, with any company whose product, technology, or competitor is discussed or used in the study.
  - Intellectual property: a patent or patent application (filed, pending, or granted), covering a method, reagent, compound, or finding described in the manuscript, held by any author or their institution.
  - The funder's role: whether the funding source had any role in study design, data collection/analysis, or the decision to publish — commonly a separately required declaration, not covered by naming the funder alone.
  - Personal or professional relationships perceived as a conflict: a family relationship, a close collaborator tie, or a current/former mentor-mentee relationship with the handling editor or a likely reviewer.
  - Relevant relationships that have since ended (e.g. a consulting arrangement that concluded during the study period) — most journals expect these declared too, not only current ones.
  - Whether every co-author was actually asked individually, rather than the statement resting on the corresponding author's own assumption — a quiet, common cause of an undeclared competing interest surfacing after publication.

Treat any finding in this pass as **principal** by default: an undeclared competing interest, a confidentiality breach, or an authorship dispute discovered after publication is rarely a quiet fix — it is exactly the class of issue that becomes a public correction, an expression of concern, or worse.

If the user asks you to omit or soften a Pass 9 finding you already know about ("don't worry about it," "just leave that part out"), still record it as principal. A verbal reassurance is not a disclosure and does not change what was already learned; the "never invent" rule guards against fabricating a clean bill of health just as much as it guards against fabricating a problem.

## Before you submit

- Every principal finding resolved.
- Journal author-guideline requirements met (Pass 3), and any structured form/guideline handed off to `journal-submission-checklist`.
- Ethics, consent, and (if applicable) trial registration adequate, not just present (Pass 4).
- Statistical justification materials in order (Pass 5).
- Wet-lab source-data / unprocessed images prepared where the journal requires them (Pass 6).
- Every dataset and code artifact matched to a repository and deposition plan, and the DAS drafted (Pass 7).
- Scientific soundness checked (Pass 8): stats appropriate, conclusions supported, no over-interpretation, claims cited.
- Research-integrity red flags checked (Pass 9): no undeclared competing interest, no confidentiality breach, and the author list/order genuinely agreed by all authors, not assumed.
- Co-authors have reviewed and approved the version to be submitted.
