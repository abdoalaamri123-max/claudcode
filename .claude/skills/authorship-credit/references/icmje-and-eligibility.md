# ICMJE authorship criteria & the eligibility engine

ICMJE decides *who counts as an author*. CRediT does not. A person can hold CRediT roles and still fail ICMJE. This file is the gatekeeper.

## The four criteria (all four required)

An author must meet **every** one of these (ICMJE Recommendations, updated Jan 2024):

1. **Substantial contributions** to the conception or design of the work; **or** the acquisition, analysis, or interpretation of data for the work; **AND**
2. **Drafting the work or reviewing it critically** for important intellectual content; **AND**
3. **Final approval** of the version to be published; **AND**
4. **Agreement to be accountable** for all aspects of the work, ensuring that questions about the accuracy or integrity of any part are appropriately investigated and resolved.

Meeting only some of the four is not enough. The four are cumulative, not a menu.

The user's pasted journal text (frequently Elsevier's wording) is a restatement of these four; if it differs in emphasis, the canonical four above govern.

## The rule that catches most mistakes

Certain contributions **do not, on their own, qualify a person for authorship**. Per ICMJE, these activities alone are insufficient:

- **Acquisition of funding** (CRediT: Funding acquisition)
- **General supervision of a research group** (CRediT: Supervision, when it is general oversight only)
- **General administrative support** (CRediT: Project administration)
- **Provision of materials, reagents, samples, patients, or instrumentation** without intellectual contribution (CRediT: Resources)
- **Writing assistance, technical editing, language editing, proofreading** (a professional medical writer, a translator, an English editor)

Any of these belongs in **Acknowledgments** unless the person *also* has a qualifying contribution under criterion 1 (real conceptual input, real data analysis/interpretation) *and* meets criteria 2–4.

Note the nuance for real PIs: a genuine senior author usually did far more than "general supervision" — they shaped the concept, interpreted the data, and critically revised the manuscript. Those are qualifying contributions. Do not mechanically demote a PI to Acknowledgments; check whether their real role includes Conceptualization / interpretation / critical revision. The flag is against *supervision-only* bylines, not against PIs.

**The reverse nuance for hands-on roles:** Investigation, Formal analysis, and Software are not in the non-qualifying list above, but that does not make every instance of them automatically substantial. Someone who mechanically executed a pre-built script or a fixed protocol with no design or interpretive input of their own has not clearly met criterion 1 just because the activity nominally maps to "Formal analysis" or "Investigation" — see the parallel caution in `credit-taxonomy.md`. Ask what judgment or design choice, if any, the person actually contributed; if the honest answer is none, criterion 1 is not clearly met and Acknowledgment is the more defensible default, subject to the same "ask, don't assume" discipline as any other classification here.

## The linkage clause (why "did the work but didn't write" is not an exclusion)

ICMJE is explicit that criterion 1 and criteria 2–3 are linked: **anyone who qualifies under criterion 1 should have the opportunity to participate in the review, drafting, and final approval** (criteria 2 and 3). So when someone clearly did substantial work but the input does not show they drafted/reviewed or approved, the correct response is **not** to exclude them. It is to flag that they must be given the chance to review and approve, after which they qualify. Frame it that way.

Conversely, someone who only reviewed/approved (criteria 2–4) but made **no** substantial contribution under criterion 1 does not qualify. Criterion 1 is the substantive gate.

## Per-person classification

For each person, evaluate all four criteria and assign one status:

- **AUTHOR** — meets 1, 2, 3, and 4. Include on the byline.
- **INCOMPLETE (author-eligible)** — meets 1 and 4, but the input does not establish 2 and/or 3. Do not exclude. Output: "Meets the substantive contribution; must be given the opportunity to review and approve the manuscript to complete authorship (ICMJE criteria 2 and 3)." Then treat as an author for ordering purposes, with the flag attached.
- **ACKNOWLEDGE** — does not meet criterion 1 on its own; contributions fall entirely within the non-qualifying set above. Route to Acknowledgments with wording. Explain *why* (which criterion fails).
- **NEEDS INPUT** — the description is too thin to judge criterion 1. Ask what specifically they did before classifying. Use the `[[NEEDS INPUT: ...]]` flag.

Always show, per person, which of the four criteria are met (e.g. "1 ✓ · 2 ✓ · 3 ? · 4 ✓") so the judgment is auditable.

## Accountability and disclosures (criterion 4, often forgotten)

Criterion 4 means every author takes responsibility for the integrity of the whole work, not just their slice, and should be able to identify which co-authors are responsible for other parts. It also implies each author confirms no undisclosed conflicts. You cannot verify agreement from a job description, so criterion 4 is normally satisfied by the authors' explicit sign-off at submission; note this as a step rather than asserting it is already met.

## Corresponding author

The corresponding author is an administrative role, not a separate tier of authorship. They submit the manuscript, handle correspondence and the editorial/peer-review process, are the contact for questions after publication, and typically manage the ICMJE disclosure and approval paperwork. There can be more than one (co-corresponding). Only the corresponding author's affiliation is used to determine any open-access / publishing-agreement eligibility; co-authors' affiliations do not affect that. Being corresponding does not require being first or last, though it is usually one of them.

## Groups / consortium authorship

If the work has a large team or a named consortium, ICMJE allows group authorship (byline lists the group, with individual members' contributions recorded elsewhere), or a mix of named individual authors plus "on behalf of [Group]". If the user's list implies this scale, offer it as an option rather than forcing a flat byline.
