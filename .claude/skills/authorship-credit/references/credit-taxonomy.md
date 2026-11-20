# CRediT taxonomy: the 14 roles and how to map onto them

CRediT (Contributor Roles Taxonomy) is the standard, journal-recognized vocabulary for *what each contributor did*. It is descriptive only. Use the exact labels below in the output; journals validate against them.

## The 14 roles (use these exact labels)

1. **Conceptualization** — Ideas; formulation of the overarching research goals and aims, the core hypothesis, the study concept.
2. **Data curation** — Management of data: annotation, scrubbing, metadata, maintaining and archiving the data for use and reuse (including deposition to repositories).
3. **Formal analysis** — Application of statistical, mathematical, computational, or other formal techniques to analyze the study data.
4. **Funding acquisition** — Securing the financial support for the project. *(Does not alone confer authorship — see ICMJE reference.)*
5. **Investigation** — Conducting the research and experiments; the hands-on doing of the work; data/evidence collection.
6. **Methodology** — Development or design of methodology; creation of models; establishing the protocol or assay.
7. **Project administration** — Management and coordination of the research activity planning and execution. *(Does not alone confer authorship.)*
8. **Resources** — Provision of study materials, reagents, patient samples, animals, instrumentation, computing resources, or other analysis tools. *(Provision alone is usually an acknowledgment, not authorship.)*
9. **Software** — Programming and software development; designing programs; implementing code; testing components.
10. **Supervision** — Oversight and leadership responsibility for the research activity planning and execution, including mentorship external to the core team. *(General supervision alone does not confer authorship.)*
11. **Validation** — Verification, whether as part of the activity or separate, of the overall replication/reproducibility of results and other outputs.
12. **Visualization** — Preparation, creation, and presentation of the published work; specifically figures, data presentation, visualization.
13. **Writing – original draft** — Preparation, creation, and presentation of the published work; specifically writing the initial draft (including substantive translation).
14. **Writing – review & editing** — Preparation of the published work by those in the original research group; critical review, commentary, revision, including pre- or post-publication stages.

## Degree of contribution

CRediT allows marking a role as **lead**, **equal**, or **supporting**. Use it when the descriptions support a distinction (e.g. two people both analyzed data, but one led). Do not assign degree you cannot justify from the input.

## Mapping fuzzy free-text descriptions onto roles

People rarely describe their work in CRediT terms. Translate. Some common phrasings and their usual mapping (confirm, do not assume, when a phrase is ambiguous):

| What the person says | Likely CRediT role(s) |
|---|---|
| "came up with the idea / designed the study" | Conceptualization; often Methodology |
| "ran the experiments / did the lab work / collected samples in clinic" | Investigation |
| "developed the assay / built the LMD-MS workflow / set up the protocol" | Methodology; possibly Software if it involved code |
| "did the stats / ran DEqMS / analysed the proteomics data" | Formal analysis |
| "wrote the pipeline / built the tool / coded the analysis" | Software; often Formal analysis |
| "organized and cleaned the data / deposited to PRIDE/ProteomeXchange" | Data curation |
| "made the figures" | Visualization |
| "wrote the first draft" | Writing – original draft |
| "gave feedback on the manuscript / edited it / commented on drafts" | Writing – review & editing |
| "checked the results reproduced / re-ran to confirm" | Validation |
| "provided the patient samples / gave us the cell line / shared the antibody" | Resources (flag: provision alone → likely Acknowledgment) |
| "supervised / is my PI / oversaw the project" | Supervision (flag: general supervision alone → not author) |
| "got the grant / funded it" | Funding acquisition (flag: not author on its own) |
| "coordinated the collaboration / managed logistics / kept the project on track" | Project administration (flag: admin alone → not author) |
| "provided the mass spec / gave instrument time" | Resources (flag) |
| "did the English editing / proofread" | not a CRediT authorship role → Acknowledgment (language editing) |

A single person usually holds several roles. A first author on an experimental paper commonly holds Conceptualization (equal/supporting), Investigation (lead), Formal analysis (lead), Visualization (lead), and Writing – original draft (lead). A senior/PI commonly holds Conceptualization, Supervision, Funding acquisition, and Writing – review & editing — and those last two do not by themselves make them an author, but the first two typically do.

## The four "flagged" roles

Four roles carry a flag because holding *only* them does not satisfy ICMJE criterion 1: **Funding acquisition, Supervision, Project administration, Resources.** When a person's mapped roles are drawn *entirely* from this set (plus, at most, Writing – review & editing that amounts to light comments), stop and route them through the ICMJE eligibility logic before treating them as an author. See `icmje-and-eligibility.md`.

## A fifth caution: mechanical execution is not automatically "substantial"

Investigation, Formal analysis, and Software look unambiguous — unlike the four flagged roles above, they map straight to ICMJE criterion 1 in the table above. But the mapping assumes genuine analytical or interpretive input, not mechanical execution of someone else's design. "Ran the pre-built pipeline someone else wrote, with the parameters someone else chose" and "designed the analysis approach and interpreted what it showed" both map to the same CRediT label (Formal analysis or Investigation) on a first pass, yet only the second is unambiguously substantial for criterion 1. When a description reads as purely mechanical (running a script, following a fixed protocol step-by-step with no design or interpretive input), probe for the actual level of judgment involved before confirming the role satisfies criterion 1 on its own — see `icmje-and-eligibility.md`.
