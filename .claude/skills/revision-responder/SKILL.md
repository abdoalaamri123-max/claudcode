---
name: revision-responder
description: Three modes for peer-review outcomes. DRAFT mode produces the full response package (point-by-point response-to-reviewers letter, cover letter, tracked-changes manuscript, summary of revisions, evaluation checklist) from a manuscript plus the editor/reviewer comments letter. REVIEW mode audits an existing response letter against the revised manuscript, outputting a summary plus a point-by-point evaluation checklist. APPEAL mode drafts a formal appeal (rebuttal) letter to the handling editor when a paper was rejected and the author has genuine, evidence-based grounds to contest the decision, not mere disagreement. Use for a revision decision, decision letter, reviewer comments, a "revise and resubmit", a "major/minor revision", an appeal, a rebuttal letter, appealing a rejection, or checking, auditing, or improving a response letter. Trigger even from a pasted decision email, rejection letter, or draft response or appeal letter, even without the words "response letter" or "appeal".
---

# Revision Responder

Write and audit the correspondence a corresponding author sends back to a journal at revision: the point-by-point **response to reviewers**, the **cover letter**, and the supporting deliverables (a **tracked-changes manuscript**, a **summary of revisions**, and an **evaluation checklist**).

The governing idea: **a response letter is a verification document, not a piece of polite prose.** Write it so the editor and reviewers can be convinced the manuscript is now acceptable without reopening the clean manuscript: state exactly what changed and where, quote the revised text, and append any references you cite. Politeness matters, but it is secondary to traceability.

## Three modes

Decide which the user needs from their request and the files they gave:

- **Draft mode** (default): the user is writing a response and gives the manuscript plus the editor/reviewer comments letter. Produce the full package (Draft workflow below).
- **Review mode**: the user has a response letter and wants it checked before submitting. They give the revised manuscript plus the response letter. Follow `references/review-mode.md`.
- **Appeal mode**: the paper was rejected and the author has genuine, evidence-based grounds to contest the decision. Produce a formal appeal (rebuttal) letter to the handling editor. Follow `references/appeal-mode.md`.

If it is ambiguous which applies, ask one short question first.

## The one rule that cannot be broken

**Never fabricate.** Do not invent results, data, statistics, p-values, line/page numbers, figure panels, citations, or manuscript edits the user has not supplied or confirmed. When a response needs something you do not have, insert a placeholder and stop: `[[NEEDS AUTHOR INPUT: <what is missing>]]`. A flagged gap is always better than a confident invention a reviewer can catch.

## Key principles

- **Respect the reviewers' role.** They are experts improving the work. Unless the editor says otherwise, respond to every point, including ones recommending rejection. A skipped comment reads as evasion.
- **Engage, do not rebut.** Reviews improve the paper; reviewers want to see real effort. Do what you reasonably can to convince, but do not go overboard, and match the depth of each response to the depth of the comment. A strong revision means engaging thoughtfully and transparently, not agreeing with everything.
- **Be easy to review.** A structured point-by-point letter and a clearly marked-up manuscript make the reviewer's job easier and improve acceptance odds.
- **Move promptly.** Start when the decision arrives, not at the deadline; high-impact journals have long timelines, so speed helps.
- **Make it self-contained.** The reader should be able to assess the revision from the package with minimal back-and-forth.

## What a good response letter looks like

- Starts with a brief thank you to the editor and reviewers.
- Repeats each comment exactly (no paraphrasing), followed immediately by the response.
- Makes each change traceable: quote the revised text (shaded block), or, under pointer-style journals, point precisely to where it now sits.
- Separates responses by editor and reviewer.
- Formatted for readability. Long is fine; hard to follow is not.

In Draft mode, meet this standard; in Review mode, grade against it.

## Inputs

**Draft mode:** (1) the manuscript, to locate and quote changes; (2) the editor/reviewer comments letter. If only the letter is given, you can still draft, but flag every location `[[NEEDS AUTHOR INPUT]]` and ask for the manuscript.

**Review mode:** (1) the revised manuscript, to verify claimed changes exist; (2) the response letter. Without the manuscript you can assess structure, tone, and coverage but not verify claims; say so.

## Draft workflow

Read `references/response-structure.md` at step 4 for the full format spec; read `references/difficult-cases.md` at step 6 only for hard comments.

**1. Catalogue and number.** From the comments letter, extract manuscript ID, title, journal, decision type, deadline, and the files the journal requires. Decision types set the stance: *minor* (mostly comply, crisp replies), *major* (substantive work, some reasoned pushback), *reject-and-resubmit* (treat as major, watch framing), *transfer* (confirm which comments still apply), *unclear* (ask). Copy every comment in verbatim, grouped editor first then Reviewer 1, 2, ... and by the reviewer's own General / Major / Minor structure. Keep a stable internal ID per point (E.1, R1.1, R2.1) for the tracking and evaluation tables; these map to the `Comment N.` headings in the letter. If a reviewer bundled several asks into one unnumbered block, split it, keeping each segment's exact wording.

**2. Classify each comment.** Tag each by type (experiment / analysis / clarification / writing / framing / factual / compliance), required action (comply / add-analysis / add-experiment / rebut / clarify-only), severity (central / supporting / minor), and whether it needs author input. This sets how much each reply must say and surfaces central + needs-input points early so the author can plan real work.

**3. Mark up the manuscript.** Work on a copy, never the clean file. Use tracked changes to mark where each revision occurs.

**4. Draft the point-by-point, major changes first.** Read `references/response-structure.md`. The letter uses a three-level hierarchy: Heading 1 `Response to the Editor` / `Response to Reviewer #1` / ...; Heading 2 `General comment` / `Major comments` / `Minor comments`; Heading 3 `Comment 1.`, `Comment 2.`. Under each `Comment N.`: the verbatim comment (blue), a bold `Response:` (black), then the change. Respond to every point; where you cannot act, give a brief rationale. Match reply length to comment depth.

House style for showing the change (confirm with the user): default **quoted-text style**, where `Added manuscript text:` (or `Revised manuscript text:` for an edit) is followed by the passage as a shaded block quote. For journals that ask you not to replicate text (e.g. Scientific Reports), use a `Location in revised manuscript:` pointer instead.

**5. Update data, tables, figures, references.** Make changes in the manuscript using the actual manuscript figure/table by number, never fabricated. New citations get their own independent numbering in the letter, collected at the end.

**6. Handle clarifications and hard comments.** A misunderstanding means the text was unclear: clarify the manuscript, then say so. For infeasible requests, reviewer factual errors, conflicting reviewers, statistics, framing, compliance, appeals, or a reviewer conflict of interest, read `references/difficult-cases.md` and respond evidence-first and non-defensively.

**7. Draft the cover letter (front of package).** Three movements: (a) a thank you grounded in the actual comments, not a generic phrase; (b) one or two sentences summarizing the main revisions, covering any editor-flagged point; (c) this transition (adjust for pointer style): "Below we respond to each comment individually, describe the change made, and, where relevant, reproduce the new or revised manuscript text in shaded boxes for ease of reference. All changes are marked in the manuscript using tracked changes. Newly cited references have been verified and added to the reference list." It summarizes; it never replaces the point-by-point. Template: `assets/cover-letter-template.md`.

**8. Build the manuscript-side deliverables.**
- **Tracked-changes manuscript (.docx):** genuine Word track changes on a copy of the manuscript, via the `docx` skill (`<w:ins>`/`<w:del>` runs; validate with its `validate.py`). Every change a `Response:` refers to should appear here at the cited location. If no manuscript was supplied, flag it.
- **Summary of revisions (standalone):** a scannable table, one row per change, columns `# | Prompted by | Change | Location`, for the author to self-check.

**9. Self-audit.** Run the checklist below and fix every miss, then output it plus a per-comment table (columns `Comment | Status | Note`; status = addressed / partially addressed / rebutted / could-not-address) as a standalone file.

Checklist:
- Every editor and reviewer comment has a response; comments-in count equals responses-out. Editor-flagged points also appear in the cover-letter summary.
- Every comment is verbatim; unnumbered blocks were split.
- Every "we revised..." has a location (and quoted text under quoted-text style); no fabricated specifics (flag with `[[NEEDS AUTHOR INPUT]]`).
- Added figures/tables are actual manuscript items; letter-cited references are numbered independently and listed at the end.
- Order is editor first then reviewers; comments blue, replies black; each Heading-1 section starts a new page in print/PDF.
- Tone is soft and collaborative; disagreements are respectful and explained.
- All five deliverables are present (or the missing one is flagged).
- Every `[[NEEDS AUTHOR INPUT]]` is collected into one visible list.

## Output package

Five artifacts, unless the user asks for a subset:

1. **Cover letter (front):** thank you grounded in the comments, one or two sentences of revision summary, the standard transition.
2. **Response to Reviewers:** the point-by-point (main artifact). Editor first, then each reviewer; comments blue, replies black; cited references at the end with independent numbering.
3. **Tracked-changes manuscript (.docx).**
4. **Summary of revisions (standalone working file).**
5. **Evaluation checklist + per-comment table (standalone).**

Two ready-to-fill templates ship in `assets/`: `response_letter.md` and `response_letter.docx` (Word, with the blue/black convention and H1/H2/H3 hierarchy applied). Start from `response_letter.docx` for a Word submission, or render `response_letter.md` via the `docx`/`pdf` skills; Markdown cannot show font color, so label comments and replies when drafting there.

## Review workflow

For auditing an existing letter, read `references/review-mode.md`: take the revised manuscript plus the letter, grade against the good-letter standard, verify each claimed change against the manuscript, and deliver a summary plus a point-by-point evaluation table (with a verified / mismatch / not-found column). Never report a verification you did not perform.

## Appeal workflow

For a rejection appeal, read `references/appeal-mode.md` for the grounds that justify an appeal, the letter structure, and the tone cautions, and start from the template in `assets/appeal-letter.md`. Appeals are for genuine, evidence-based grounds only (a factual error, a missed or misread piece of key content, procedural unfairness, or a demonstrable reviewer error), never for mere disagreement with the outcome. Lay out the case for and against appealing rather than pushing the author toward one; whether to appeal is the author's decision. If the author decides not to appeal, or the appeal is denied, hand off to `journal-selector` (a new target journal) and `cover-letter-writer` (a fresh first-submission letter) rather than dead-ending the conversation.

## Tone

The purpose is to get the manuscript through, so the register is soft, warm, and collaborative, never combative. Peer review is a dialogue. Rewrite defensive notes ("the reviewer clearly did not read the paper") into courteous language. Disagreement is allowed but must be respectful and explained, grounded in scientific reasoning. Do not concede a point that is not wrong just to be agreeable, and do not dismiss a point without a reason.

## Rebuttal strategy and phrase bank

For the persuasion mindset behind each point-by-point response (Draft workflow Steps 4 and 6), a playbook of response strategies keyed by comment type (novelty attack, factual error, insufficient gain, insufficient experiments), and a bank of reusable opening/conceding/pushing-back/clarifying phrases, read `references/rebuttal-strategy.md`. Read it alongside `references/difficult-cases.md`: difficult-cases.md covers how to handle specific hard-comment categories, and rebuttal-strategy.md covers the underlying strategy and phrasing that applies across all comment types, including straightforward ones.
