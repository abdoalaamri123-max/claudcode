# Submission Readiness Report

**Manuscript:** [Title]  |  **Target journal:** [Journal]
**Date:** [date]  |  **Checked by:** [name]
**Study type detected:** [e.g. human-tissue proteomics, retrospective cohort; note if a structured guideline/form also applies (NP / MCP / CP / CONSORT / STROBE / ARRIVE / PRISMA) and hand off to `journal-submission-checklist` for that depth]

## Verdict

- **Principal findings cleared:** [YES / NO]  ([n] found, [n] resolved)
- **Ready to submit:** [YES / NOT YET]  [one line on what remains]

---

## 1. Principal findings (must all be resolved before submitting)

| # | Pass | Location | Issue | Fix |
|---|------|----------|-------|-----|
| P1 | [e.g. Ethics] | [section] | [what is wrong or missing] | [what to do] |
| P2 |  |  |  |  |

## 2. Minor findings (fix where reasonable)

| # | Pass | Location | Issue | Fix |
|---|------|----------|-------|-----|
| M1 |  |  |  |  |
| M2 |  |  |  |  |

## 3. Ethics and consent

- **Approval type required:** [human / animal / human tissue-biobank / exempt]
- **Approval present and specific:** [status] — [approving body + protocol/approval number, or gap]
- **Informed consent:** [status] — [general consent / consent-to-publish for identifiable images, or gap]
- **Trial registration (if applicable):** [status] — [registry + number, or gap]

## 4. Statistical justification materials

- **Sample-size justification:** [status] — [note]
- **Test named and appropriate (Methods):** [status] — [note]
- **Figure legends state their own test and an exact replicate n:** [status] — [list any figure/panel with a missing test, a vague replicate count ("repeated multiple times"), or a legend/Methods mismatch]
- **Multiple-comparison correction:** [status] — [note]
- **Supporting statistical materials needed for submission:** [yes/no] — [what, if so]

## 5. Wet-lab raw-data / source-data requirements

- **Unprocessed blots/gels available:** [status]
- **Raw microscopy/imaging available:** [status]
- **Source Data file needed and prepared:** [status]

## 6. Data and code deposition status

| Artifact | Type | Repository | Status | Accession |
|---|---|---|---|---|
| [e.g. raw MS files] | [proteomics / sequencing / structure / code / generic] | [PRIDE / GEO / PDB / Zenodo] | [deposited / pending / exempt] | [accession, or "pending"] |

## 7. Draft declarations ready to paste

- **Ethics/consent statement:** {{draft}}
- **Data availability statement:** {{draft, per `references/data-deposition-guide.md` templates}}
- **Code availability statement:** {{draft, if applicable}}
- **Funding / competing-interests statement:** {{draft}}

## 8. Scientific soundness (light catch-net)

- **Statistical method appropriate:** [status] — [note]
- **Conclusions supported by data:** [status] — [note]
- **No over-interpretation:** [status] — [note]
- **Claims cited:** [status] — [note]

## 9. Research-integrity red flags

- **Breach of confidentiality:** [status] — [participant identifiability beyond consent-to-publish / third-party data permission / peer-review confidentiality / sensitive-location data, or "none found"]
- **Authorship dispute:** [status] — [all authors confirmed to have seen and approved the final list/order, or a flagged late change / open disagreement — hand off to `authorship-credit` if real]
- **Undeclared competing interest:** [status] — [financial ties / IP / funder role / personal relationship not yet disclosed, or "none found"]

*(Missing or inadequate ethical approval is covered in Section 3 above, not repeated here.)*

## 10. Hand-off to sister skills

- [ ] `journal-submission-checklist` — if the target journal or study design requires a structured form (NP / MCP / CP / CONSORT / STROBE / ARRIVE / PRISMA).
- [ ] `review-simulator` — for a full pre-submission stress test (simulated editor desk assessment + 2-3 reviewer reports), beyond this report's light soundness catch-net.
- [ ] `statistical-rigor-helper` — for the real statistics rigor check (confounding, pseudoreplication, distributional assumptions, CV/data leakage), beyond this report's presence/naming check in Section 4. `figure-checker`'s `legend_check.py` covers the mechanical part of Section 4's figure-legend check (undefined error bars, missing *n*, unnamed test) — run it alongside.
- [ ] `figure-checker` — for figure-specific numeric consistency, image-file hygiene, and the visual-design/journal-format checklist, beyond this report's raw-data presence check in Section 5.
- [ ] `table-checker` — for a table's own internal formatting (decimal uniformity, units in header vs. cells, footnote-defined abbreviations, main-text vs. supplement placement), beyond this report's cross-manuscript consistency check.
- [ ] `cover-letter-writer` — to draft the short confirmatory declarations for the cover letter, using the same facts established here.
- [ ] `authorship-credit` — if authorship/CRediT roles are not yet settled, or a real authorship dispute surfaced in Section 9.
- [ ] `citation-auditor` — for citation accuracy, genuine support, and missing-citation checks, beyond this report's citation-*mapping* check in Section 1.

---

*Reminder. Everything flagged here should be fixed before submitting, not deferred. Once submitted, further changes require editor approval; once accepted, `proof-checker` is the right skill for the typeset proof, not this one.*
