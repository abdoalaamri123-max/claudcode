---
name: journal-reformatter
description: Reformats a manuscript into a target journal's format without changing the wording, either converting it from another journal's style (e.g. Cell to Nature) or applying a target's format to a plain, unstyled draft. Fetches the target's current author guidelines, or uses a bundled official template when available (e.g. Science's manuscript and supplementary-materials templates), then converts citation and reference style, section structure and headings, abstract, figure/table callouts, title-page and author formatting, and layout, reporting every change and listing what still needs manual supplementation. Use whenever the user wants to adapt, reformat, convert, or restyle a paper for a journal, move a manuscript from one journal format to another after a rejection or a change of target, or format a fresh draft for a target journal for the first time. Trigger even if the user just says "change this paper from Cell format to Nature format" or "put this in the Science template."
---

# Journal Reformatter

Adapt a written manuscript into a target journal's format. The job is **format, structure, and style only, never the wording.** You relabel, reorder, renumber, and restyle; you do not rewrite the author's sentences.

## Two starting points

- **Restyling (source is another journal's format).** The manuscript is already styled for a named journal (e.g. Cell) and needs to move to a different one (e.g. Nature) — typically after a rejection or a change of target. The "current style" is that source journal's convention.
- **First formatting (source is a plain, unstyled draft).** The manuscript has no journal styling yet — a working draft with ad hoc or inconsistent headings, citation markers, and layout. There is no named source journal to map from; instead, read whatever structure and citation convention the draft already uses (however inconsistent) as the starting point, and convert directly into the target's format. The same dimension-by-dimension conversion in `references/reformatting-map.md` applies to both cases — the only difference is whether the "from" side is a known journal's convention or the draft's own ad hoc state.

Ask which situation applies if it is not clear from the request or the files; if a source journal is not named and the manuscript reads as an unstyled draft, default to first formatting.

## The one rule that cannot be broken

**Do not change the text content.** The author's prose stays exactly as written. The only permitted text changes are mechanical and structural: section heading labels, citation markers, reference-list formatting, figure/table callout style, and moving existing blocks into the target's order. Never paraphrase, condense, or "improve" a sentence — that's `manuscript-copyeditor`'s job, a separate skill for language, grammar, and style — and never invent bibliographic data (a missing volume, DOI, or page range is flagged for the author, not guessed). If a reformatting step would require rewording (e.g. an abstract over the target's length limit), do not do it silently; put it in the manual-supplement list.

## Inputs

- **The manuscript.** An editable source is strongly preferred: DOCX (use the `docx` skill) or LaTeX (edit the `.tex`/`.bib`). A PDF can be read but not cleanly reflowed, so if only a PDF is given, extract its content, do what you can, and note that applying the changes needs the editable source.
- **Source format** (optional) — the journal it is currently styled for, e.g. Cell, if the manuscript is already formatted for one. If it is a plain, unstyled draft with no prior journal formatting, there is no source format to name; say so instead of guessing one, and treat the draft's own ad hoc structure and citation markers as the starting point.
- **Target format** (e.g. Nature) — required in both cases.
- **The target journal's author guidelines.** The skill fetches these automatically from the journal or publisher website (see step 1). The user may also provide guidelines directly (a file or URL), or the official journal template they have downloaded, which is faster and avoids any doubt about which journal or version. Requirements change, so the current official guide is the authority.

## Journal template notes

This skill does **not** bundle publishers' copyrighted Word templates. For some journals it does ship a **notes file** that distills the template's structural requirements, so you can build to the correct structure and then populate the journal's own template (the user downloads it from the publisher, or you fetch the current author guidelines):

- **Science** — `references/science-template-notes.md` distills the AAAS Science manuscript and supplementary-materials templates (exact section labels, title/abstract limits, heading levels, citation and reference style, the CRediT-style author-contributions block, and the rule that supplementary materials is always a separate file). Download the current official templates from the Science author resources (https://www.science.org/content/page/science-information-authors).

When a notes file covers the target, use it as the structural spec, build the output to that structure, and — if the user supplies the journal's own downloaded template — populate that template's docx (via the `docx` skill) so the native styles come from the journal's file. Still spot-check the live site if the submission is time-sensitive or the notes file's stated date is more than 3 months old, since journals revise these periodically. Everything else is unchanged: format and structure only, never the wording, and never invent a field the source manuscript does not supply.

## What gets reformatted

See `references/reformatting-map.md` for how each dimension maps and which parts are automatic versus manual. The dimensions:

- **Citations and references:** the biggest change (e.g. author-year in-text with an alphabetical list, to numbered superscript with a numbered list, or vice versa). Convert in-text markers and rebuild the reference list in the target's format.
- **Section structure and headings:** section names and order (e.g. Summary vs Abstract; STAR Methods vs Methods; Methods position).
- **Abstract/summary:** name, structured vs unstructured, and a length-limit flag.
- **Figure and table callouts and legends:** "Figure 1" vs "Fig. 1" style, legend placement, and numbering.
- **Title page and authors:** affiliation markers, corresponding-author notation, ORCID placement.
- **Required sections and statements:** data availability, author contributions, ethics, funding, conflict of interest (presence and labeling are checked; missing ones are flagged for the author to write). This is a presence check only: whether the declaration's actual content is correct and complete before first submission is `submission-screener`'s job, and the shorter confirmatory version of these same declarations that goes in the cover letter is `cover-letter-writer`'s job, not this skill's.
- **Layout:** line numbering, spacing, headings case, and other formatting the target specifies.

## Workflow

**1. Get the target journal's current guidelines and read them.** First check whether the target has a template notes file ("Journal template notes" above); if so, read it (e.g. `references/science-template-notes.md`) and use it as the structural spec, only checking the live site if the submission is time-sensitive. Otherwise, unless the user supplied the guidelines, fetch them from the web: search for the journal's author instructions (for example the journal name plus "guide for authors" or "information for authors"), then fetch the official journal or publisher page (Elsevier/ScienceDirect, Nature, Springer, Wiley, the society site, etc.), preferring the current official page over mirrors, aggregators, or caches. Extract the formatting requirements that drive the reformat:
- citation and reference style (author-year vs numbered; exact reference-list format, "et al." threshold, journal-name abbreviation, DOI requirement);
- required sections and their order, and section naming;
- abstract type and word limit;
- figure/table callout style, legend placement, and figure file/resolution specs;
- title-page and author/affiliation format;
- required statements (data availability, contributions, ethics, funding, competing interests);
- limits (word, figure, table, reference, title) and layout rules (line numbering, spacing).

Treat the fetched official guide as the authoritative spec. If the page cannot be fetched (paywall, script-only content, or an unclear match), do not guess from memory: tell the user, ask for the URL or the guidelines file, and apply known conventions only as a clearly labeled interim, flagged for verification.

Also identify the manuscript's current style. If a source journal was named, use its known convention. If the manuscript is an unstyled draft, there is no named convention to look up — instead read the draft directly to establish its current ad hoc state: what citation marker style it already uses (if any, and whether consistent), what section headings and order it already has, and how figures/tables are currently called out. This ad hoc state is the "from" side of the conversion, exactly as a named source journal's convention would be.

**2. Convert each dimension, preserving wording.** Work through the dimensions above using `references/reformatting-map.md`. Reference/citation conversion is the error-prone part: parse the in-text citations and the reference list, rebuild both in the target style, and mark anything ambiguous (e.g. a citation that cannot be matched to a list entry) for checking. Move existing text blocks into the target's section order without editing their content.

If the draft has no citations or reference list at all yet, there is nothing to restyle for that dimension — say so and move on; do not invent references to fill the gap (that is `citation-auditor`'s job, not this skill's). Reformat only what the draft already has.

**3. Build the change log.** Record every change: dimension, from, to, and where. This is how the author sees what happened and can verify it. Template in `assets/change-log.md`.

**4. Build the manual-supplement list.** Everything the reformat cannot do automatically: required sections the author must write, content exceeding a word/figure/reference limit that needs an author trimming decision, missing bibliographic fields, ambiguous citations, and figure-file/resolution requirements that need new files. Each item is specific and located.

**5. Output.** Deliver the reformatted manuscript, the change log, and the manual-supplement list.

## Output

- **Reformatted manuscript** in the same editable format as the input (DOCX or LaTeX), with wording untouched. For a target with a notes file, build to that structure; if the user supplies the journal's own downloaded template, populate that docx rather than a separately re-created file.
- **Reformatted supplementary materials**, as its own separate file, when the manuscript has supplementary content and the target requires SM as a separate file (Science does; see `references/science-template-notes.md`).
- **Change log** (`assets/change-log.md`): a table of every change (dimension, from, to, location) so the author can review and confirm.
- **Manual-supplement list:** the specific, located items that still need the author, because they require new content, a trimming decision, or information only the author has.

## Cautions

Base the reformat on the target's current official author guidelines, fetched fresh from the journal or publisher site (or supplied by the user); requirements change, so do not rely on remembered conventions, and confirm you have the right journal's current page. A template notes file is not exempt from this: it carries a date (Science's is December 2025), so for a submission where accuracy really matters, still confirm nothing has changed since. Citation-style conversion is the most error-prone step; present it as done-but-verify. Above all, the wording does not change: if a step seems to need rewording, it belongs in the manual-supplement list, not in an edit. For an unstyled draft, do not assume it silently follows some named journal's convention; read it as-is and convert directly from whatever ad hoc state it is actually in.
