---
name: presubmission-inquiry
description: Drafts a pre-submission inquiry (enquiry) letter to a journal editor, sent before full submission to gauge whether the journal would welcome the manuscript. Given the target journal and the manuscript's topic and key finding, it fetches the journal or publisher website to confirm whether the journal accepts pre-submission enquiries and by what channel, and to identify the handling editor whose subject scope best matches the paper, then drafts a short, targeted inquiry to that editor. It never invents an editor, email, or policy; anything it cannot confirm on the site is flagged for the author. Use when the user has chosen a target journal and wants to send a pre-submission enquiry, ask an editor whether a paper is of potential interest, find the right editor to handle a manuscript, or write a pre-submission letter. This is distinct from the first-submission cover letter.
---

# Presubmission Inquiry

Draft a pre-submission inquiry: a short letter to a journal editor, sent before a full submission, asking whether the journal would be interested in considering the manuscript. Its purpose is to gauge interest and reach the right editor before the author invests in a full, formatted submission. It is brief and targeted, not a full cover letter.

## The one rule that cannot be broken

**Do not invent an editor, an email, or a journal policy.** The handling editor's name and contact, and the journal's pre-submission process, must come from the journal or publisher website. If the site does not show a subject-matched editor, an email, or a clear pre-submission policy, say so and flag it (`[[NEEDS AUTHOR INPUT: ...]]` or "not found on the site") rather than guessing. A confidently wrong editor name or address is worse than an honest gap.

## Inputs

- **The target journal.** Required.
- **The manuscript topic and key finding**, ideally with the title, abstract, and the field/subfield, so an editor can be matched and the significance summarized. If the manuscript is provided, draw these from it.
- **Corresponding-author details** for the signature (institutional email preferred).

## Workflow

Read `references/presubmission-inquiry-guide.md` for how to find the editor, find the process, and structure the letter.

**1. Check the journal's pre-submission process.** Search for and fetch the journal's author guide and pre-submission information (for example the journal name with "presubmission enquiry" or "presubmission inquiry", or the guide-to-authors page). Determine whether the journal accepts pre-submission enquiries at all, and if so the channel (an option in the online submission system, an email to the editorial office, or a form) and any expected format. If the journal states it does not offer pre-submission enquiries, report that and advise proceeding to full submission instead of drafting one.

**2. Identify the handling editor.** Fetch the journal's editorial board or editors page and find the editor whose stated subject scope best matches the paper's topic. Prefer a subject-matched editor; if the board lists no clear match, or enquiries are routed centrally, fall back to the editorial office or the editor-in-chief, and say which. Record the editor's name, role, why they match, and the source page. Confirm any email from the site; do not construct one.

**3. Draft the inquiry.** Address the identified editor (or office) and write a short letter: the manuscript title and type, two to four sentences distilling the key finding, its significance, and its broad interest (not a full abstract dump unless the process expects the abstract), and the explicit ask, whether the editor would welcome a full submission. Keep it concise and professional.

**4. Report.** Return the drafted letter, the identified editor (name, role, match reason, source, and the channel to send it), the journal's pre-submission policy as found, and a short list of anything that could not be confirmed on the site.

## What to keep out

- A full methods/results walkthrough; this is an enquiry, not the paper.
- The full set of submission declarations and reviewer lists; those belong in the first-submission cover letter (`cover-letter-writer`), not here.
- Any invented editor, address, or policy.

## Output

A short pre-submission inquiry letter (Markdown by default), plus a brief findings note: the matched editor and why, the pre-submission channel, and flags for anything unverified. If the journal does not accept pre-submission enquiries, no letter is drafted and the author is told so.

## Cautions

Journal editorial boards and policies change and vary, so rely on the current site, cite where each fact came from, and flag what you could not confirm. This skill covers the pre-submission enquiry only; the full first-submission cover letter is handled by `cover-letter-writer`, and choosing a journal is handled by `journal-selector`.
