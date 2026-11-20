---
name: post-publication-corrector
description: Handles the post-publication error-correction workflow, strictly for a paper that is already published and has a confirmed error. Classifies the case as a Corrigendum (author's own error), an Erratum (publisher/production error), an Expression of Concern (credible doubt, not yet resolved), or a Retraction (COPE-grounded misconduct or invalidating error), then drafts the co-author notification, the formal correction request to the handling editor, and the published notice wording. Trigger is narrow, only when the user reports a confirmed post-publication error and asks about a corrigendum, erratum, retraction, expression of concern, or how to correct or retract a published paper. Not for pre-submission or proof-stage issues (submission-screener, review-simulator, proof-checker instead); not for a paper you merely cite as a reference (citation-auditor checks whether a cited source was retracted) — only for a paper the user themselves authored. Never asserts misconduct occurred on its own.
---

# Post-Publication Corrector

The last link in the suite's error-catching chain: what happens when an error survives `submission-screener`, `review-simulator`, and `proof-checker`, and is only discovered after the paper is actually published.

**Scope: narrow, and strictly post-publication.** Trigger only when both are true:

1. **The paper is already published** (online or in print) — not a preprint, and not "accepted but not yet online" (that's `proof-checker`'s stage).
2. **A specific, real error or integrity concern has actually been identified** — not a hypothetical or a general "how do journal corrections work" question. It's fine to explain the classification framework for a hypothetical, but only draft the actual notification, letter, or notice against a real, confirmed case.

If either condition doesn't hold, this is the wrong skill: redirect to `proof-checker` (proof not yet approved), or `submission-screener` / `review-simulator` (pre-submission).

## The one rule that cannot be broken

**Never determine that misconduct occurred, and never draft a retraction notice with vague wording when the true reason is known.** This skill classifies against COPE's published criteria and drafts the resulting documents; it does not adjudicate a misconduct allegation itself — that is an institutional or journal investigation's job. Where the classification is genuinely ambiguous, or where anything resembling fabrication, falsification, plagiarism, or duplicate publication is even plausibly in play, flag it and recommend the corresponding author route the case through the institution's research-integrity office and/or a COPE-guided process, rather than deciding unilaterally. Never invent what went wrong, never assume co-author agreement without it being explicitly confirmed or the disagreement explicitly documented, and never soften a known, specific cause into vague language ("administrative reasons") — COPE requires retraction notices to be specific and informative.

## Relationship to sister skills

- `proof-checker` — the adjacent, earlier-stage skill: catches production and content errors *before* publication, at the final proof, precisely so they never reach this skill. This one only starts once a paper is already published and an error slipped through anyway.
- `submission-screener` / `review-simulator` — pre-submission checks; not this skill's stage under any circumstance.
- `authorship-credit` — if the "error" is actually a needed authorship change (an author omitted, wrongly included, or misordered, discovered post-publication), that skill decides who should be an author; this skill drafts how to formally correct the published record once that's settled (typically also via a Corrigendum — see `references/correction-classification.md`).

## Workflow

**1. Confirm scope.** Check both trigger conditions above. Gather: the published paper's full citation (title, authors, journal, DOI, volume/issue/pages), what was found, and how it was discovered.

**2. Classify.** Read `references/correction-classification.md` for the full COPE-grounded decision framework, and work through it in order: the authors' own honest error that leaves the conclusions intact → Corrigendum; the publisher's own production error that leaves the conclusions intact → Erratum; credible but unresolved doubt (an ongoing investigation, disputed data, an unconfirmed allegation) → Expression of Concern; confirmed major error, misconduct, unethical research, or compromised peer review → Retraction. Present the classification as a recommendation with the specific criterion it meets, not an unappealable verdict — the corresponding author (and, for anything retraction-adjacent, the institution) confirms it.

**3. Draft the co-author notification.** A short, factual message to every co-author: what was found, how, the proposed classification and why, and what's being asked of them — review and written agreement, or a documented objection. Don't proceed to the editor letter without this step at least being attempted; journals expect either all-author agreement or an explicit, documented account of disagreement.

**4. Draft the formal request to the editor.** States the finding, the requested correction type and why, confirms co-author agreement status (all agreed / specific dissent noted), and describes what's enclosed (proposed replacement text, figure, or data).

**5. Draft the published notice wording.** The text that will actually appear as the correction/retraction notice, linked to the original paper: cites the original publication in full, states plainly what was wrong, states the correction (or, for a retraction, the reason, specifically and without euphemism), and states whether the paper's conclusions are affected.

## Inputs

- **The published paper's full citation** (title, authors, journal, DOI, volume/issue/pages). Required.
- **What was found, and how** — required, in the author's own account; this skill does not investigate or independently verify the underlying science.
- **Co-author list and contact context**, if drafting the notification.
- **Any existing institutional or journal investigation status**, if the case is already in that process.

## Output

A single report (template in `assets/correction-report.md`): the classification and its rationale, the co-author notification draft, the editor request letter, and the published notice wording — each flagged `[[NEEDS AUTHOR INPUT: <what is missing>]]` wherever a fact, a co-author's agreement, or an institutional determination is still outstanding.

## Cautions

Correction and retraction norms are set by COPE and enforced per journal; this skill's classification framework reflects COPE's published guidelines, but the applicable journal or institution may layer its own procedural requirements on top (a specific submission channel, a required institutional sign-off) — confirm these rather than assuming this skill's generic workflow is the complete procedure. This is a drafting and classification aid, not a substitute for legal or research-integrity-office advice once an allegation of misconduct is actually in play.
