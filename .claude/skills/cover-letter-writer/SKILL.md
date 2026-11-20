---
name: cover-letter-writer
description: Drafts the cover letter for the first (initial) submission of a manuscript to a journal. It produces a professional, appropriately structured letter that states the manuscript's basic information, conveys the significance and broad interest of the work, argues journal fit, and includes the required declarations (conflict of interest, ethics and consent, originality and exclusivity, prior dissemination such as preprints or conferences, data availability, and all-author approval), plus suggested and opposed reviewers where the journal asks for them. It never fabricates a declaration, a registration number, a data link, or a reviewer, and it leaves out material that belongs in the paper. Use whenever the user is preparing a first journal submission and wants a cover letter, submission letter, or letter to the editor written, or asks how to write one. This is the first-submission cover letter, distinct from the response cover letter used at revision and from an appeal letter.
---

# Cover Letter Writer

**Scope: this skill is for the first (initial) submission of a manuscript to a journal.** It writes the cover letter that accompanies a new submission, not the response/revision cover letter used when returning a revised manuscript (that one is handled by `revision-responder`), and not an appeal letter.

Draft the cover letter for a first submission to a journal. The letter's job is to introduce the manuscript to the editor, make the case for its significance and fit, and carry the required declarations. It is a short, professional letter, not a summary of the paper.

**Why this matters:** the cover letter is the one place in the whole submission package to address the editor directly. Use it to explain specifically why this research suits *this* journal, not just why it is good research — showing that care was taken to understand the journal's scope reads as respect for the editor's time, while a generic, could-be-sent-anywhere letter reads as the opposite.

## The one rule that cannot be broken

**Do not fabricate any factual or legal statement.** Conflict-of-interest status, ethics approvals and patient consent, a clinical-trial registration number, a data-repository link or password, confirmation that all authors approved, prior-publication or preprint history, and suggested/opposed reviewer names are all statements only the authors can make. Draft the sentence structure, but insert the actual value only if the user supplied it; otherwise use `[[NEEDS AUTHOR INPUT: ...]]`. Never invent a registration number, a link, or a reviewer. If the user asks you to invent one anyway ("just make up a plausible reviewer, I don't have time"), decline and offer the real fallback instead — for a reviewer, mining the manuscript's own reference list for authors of cited related work (see the reviewers section below); for a registration number, link, or approval, the `[[NEEDS AUTHOR INPUT: ...]]` flag. Repeated pressure to comply is not new information that makes fabrication acceptable.

## Inputs

- **The manuscript** (to draw the title, submission type, word/figure/table counts, and the aim, significance, and highlights). An editable file or the text.
- **The target journal** (full name, and its aims and scope; note any similar articles it has published that support fit).
- **Author-supplied specifics**, which cannot be inferred: corresponding-author contact and institutional email, whether an editor has been contacted (and the editor's name), COI status, ethics/consent/trial-registration details, preprint or conference history, data-availability link (and password if any), confirmation all authors approved, and any suggested or opposed reviewers. Ask for or flag whatever is missing.

## Guide the user: information to collect

Do not silently guess the author-supplied specifics. First draft what can be drawn from the manuscript (title, type, counts, significance), then present the user a short, grouped checklist of what is still needed and ask for the missing required items before finalizing. Reinforce the required ones: a cover letter that ships with a required declaration blank or invented is worse than one that waits for the value.

**Required (the letter is not complete without these):**
- Target journal full name and submission type (original article, review, case report, short communication, etc.).
- Manuscript title, and word / figure / table counts.
- Corresponding author name and institutional email (not a private address).
- Conflict-of-interest status (specific conflicts, or an explicit "none").
- Ethics and informed-consent status where human/animal work is involved.
- Confirmation the work is original and not under consideration elsewhere.
- Confirmation all authors have approved the submission.
- Full author list and their institutional affiliations.

**Provide if applicable (ask, and include only when relevant):**
- Handling editor's name, if known or previously contacted.
- Clinical-trial registration number, for a trial.
- Prior dissemination: preprint link, or conference/proceedings details.
- Data-availability link, and password if the repository uses one.

**Optional (strengthens the letter):**
- Suggested reviewers (name, institution, email, and a relevant reference each) and any opposed reviewers.
- The journal's aims/scope and any of its prior articles similar to the submission, to argue fit.
- Any highlight the authors want emphasized beyond what the manuscript makes obvious.

Present this as a checklist the user can fill in one pass (interactive options are fine on a client that supports them). For every required item still missing at drafting time, insert a `[[NEEDS AUTHOR INPUT: ...]]` flag and list it prominently, rather than proceeding as if it were handled.

## What to include

Detail and standard phrasings are in `references/cover-letter-elements.md`. In order:

1. **Professional presentation:** institutional (not private) email; institutional letterhead where available.
2. **Polite salutation:** "Dear Editor," or, if the handling editor is known, "Dear Dr. [Name],".
3. **Submission statement with basics:** title, submission type (original article, review, case report, short communication, etc.), the full journal name in italics, word count, figure and table counts, and corresponding-author contact.
4. **Significance and broad interest:** a few distilled sentences on the aim, key findings, innovation, and impact, not copied from the abstract, and explicitly why readers beyond the immediate subfield should care.
5. **Journal fit:** why the work suits this journal's aims and scope, citing the journal's own prior related articles where possible.
6. **Continuity:** brief reference to the authors' own related published work, a few citations, not many.
7. **Declarations:** conflict of interest; ethics, consent, and trial registration; originality and exclusivity; prior dissemination (preprint link, conference details); data availability (link and password); all-author approval.
8. **Reviewers:** suggested reviewers (and opposed reviewers) where the journal invites them.
9. **Courteous close** and a signature that may state the author's titles and positions.

## What to leave out

- Detailed materials, methods, results, discussion, or conclusions; these are in the paper.
- The authors' CVs or publication lists.
- Boasting about the authors' honors or standing (the signature may carry titles and positions, but the body should not self-promote).

## Workflow

1. Gather the inputs. Draft what the manuscript provides, then guide the user through the information-to-collect checklist above, asking for the missing required items and reinforcing that the letter cannot be finalized until each required item is supplied or explicitly confirmed.
2. Draft the letter in the order above, distilling significance in the authors' own framing rather than copying the abstract, and foregrounding broad interest.
3. For each declaration, write the sentence and insert the real value or a `[[NEEDS AUTHOR INPUT: ...]]` flag.
4. For suggested reviewers, follow the principle in the reference: propose genuine experts (often authors of relevant work cited in the manuscript), with a line of justification each, not just personal acquaintances.
5. Keep it concise, professional, and free of the excluded material. Collect all flagged gaps into a short list at the end.

## Output

A ready-to-send cover letter (Markdown by default, or Word via the `docx` skill on request), plus a short list of any `[[NEEDS AUTHOR INPUT]]` items the author must supply before sending, with the required items called out separately from the optional ones so the author sees what actually blocks submission.

## Cautions

This is the first-submission cover letter; the response/revision cover letter is handled by `revision-responder`. Keep declarations truthful and author-confirmed, never invented. Argue significance and broad interest without overstating, and keep the letter short.

The declarations drafted here (COI, ethics/consent, data availability) are a short confirmatory version for the editor, not a substitute for the full declarations that belong in the manuscript itself. Whether the manuscript has those required declaration sections present is `journal-reformatter`'s job, and whether their content is correct and complete (before first submission) is `submission-screener`'s job; neither is done by this skill. The underlying fact must be the same in both places, so if the user has already stated it to one of those skills in this session, reuse it here rather than asking again or letting it drift.

## The unhelpful-cover-letter failure mode

The most common way a cover letter fails is restating the abstract without ever answering "why this journal, specifically" — that question is the entire point of writing a cover letter instead of just resubmitting the abstract. If a draft could be sent unchanged to five different journals, it has not yet done this letter's actual job; tie the significance and journal-fit sentences to something concrete about *this* journal (its scope, its readership, its own prior related articles), not generic praise.
