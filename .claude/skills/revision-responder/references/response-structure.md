# Response Letter Structure

Read this at Step 3. It defines the anatomy of the response-to-reviewers letter, the per-comment block, tone, and formatting.

## Overall structure

The cover letter (with the revisions overview) sits in front of this document. The response letter itself uses a three-level heading hierarchy, ordered editor first, then each reviewer in sequence.

- **Heading 1**: one per source, `Response to the Editor`, `Response to Reviewer #1`, `Response to Reviewer #2`, ... and a final `References cited in this response`.
- **Heading 2**: the groups within a source, `General comment`, `Major comments`, `Minor comments`. Use the reviewer's own section labels where they gave them; drop a group that does not apply.
- **Heading 3**: one per individual point, `Comment 1.`, `Comment 2.`, ... under each Major/Minor group.

```
[Header: manuscript ID, title, journal]
[Opening paragraph: thank the editor and reviewers; state that every point is addressed;
 explain the color convention (comments blue, replies black)]

# Response to the Editor                         (H1)
## General comment                               (H2)  overall editor remarks + Response
## Major comments                                (H2)
### Comment 1.                                    (H3)  verbatim comment -> Response -> Added manuscript text
### Comment 2.                                    (H3)
## Minor comments                                (H2)
### Comment 1.                                    (H3)

# Response to Reviewer #1                          (H1)   [new page]
## General comment                               (H2)  overall assessment + Response
## Major comments                                (H2)
### Comment 1.                                    (H3)
## Minor comments                                (H2)
### Comment 1.                                    (H3)

# Response to Reviewer #2                          (H1)   [new page]
...

# References cited in this response               (H1)
```

Handle the editor first because their instructions often carry the highest priority and set the frame for the reviewer points. Under `General comment`, quote the source's overall remarks verbatim and give a single warm `Response:`; specific points that need a per-comment block live under `Major comments` / `Minor comments` as `Comment N.` The `General comment` group has no `Comment N.` subheadings, since it holds one overall block. Start each Heading-1 section on a new page in any PDF or print version so the editor can route one reviewer's section cleanly.

## The per-comment block

Every `Comment N.` (Heading 3) gets exactly this block. This structure is what makes the letter a verification document.

**Preserve the comment verbatim.** Reproduce the editor's or reviewer's words exactly, in **blue font**, with no paraphrasing, correction, or trimming. They must recognize their own words.

**Split unnumbered comments.** If a reviewer wrote a block that bundles several distinct asks but did not number them, split it into separate `Comment N.` entries so each can be answered individually, while keeping each segment's exact wording. A single paragraph raising three issues becomes Comment 1, Comment 2, Comment 3, each quoting the relevant verbatim slice of the original. Never merge or reword; only divide.

**Then answer in black.** Use a bold `Response:` label, then show the change. Two accepted layouts, chosen by journal house style:

- **Quoted-text style (the templates' default; matches many Nature-family letters):** after the response, add a bold `Added manuscript text:` (or `Revised manuscript text:` for an edit rather than an addition) label, then the actual new/revised passage as a shaded block quote, so the reader sees exactly what changed.
- **Pointer style (for journals that ask you not to replicate text, e.g. Scientific Reports):** replace the block quote with a bold `Location in revised manuscript:` line pointing to the section, page, line, or figure/table number.

```
Response: [what you did, or why you disagree]
Added manuscript text:
> [the new or revised passage, exactly as it now reads]
```

- `Response:` is the reasoning and acknowledgment. Keep it concise and to the point; brevity is as valued as specificity. Match the length of the response to the depth of the comment: a brief point gets a brief answer, a substantial objection gets a fuller one. Show real effort where it counts, but do not go overboard on minor points.
- If the point needs no manuscript change (a pure clarification or a rebuttal), write a short italic note such as `(No manuscript change needed; addressed by the clarification above.)` rather than leaving it blank.

Confirm the house style with the user. The templates default to the quoted-text (block quote) style; switch to pointer style if the target journal asks you not to replicate text or figures.

### Worked example of a good block

> *1. The authors claim the method is faster but provide no timing comparison. This assertion is unsupported.* (blue)
>
> **Response:** We agree the speed advantage was asserted without quantification. We have added a direct timing benchmark against the two most common alternative workflows and now report wall-clock time per sample.
>
> **Added manuscript text:**
> > Across 24 samples, our workflow completed in 3.1 +/- 0.4 min per sample, compared with 11.8 +/- 1.2 min for [method A] and 9.4 +/- 0.9 min for [method B] on the same hardware (Table 2).

Under pointer style, the last part would instead read `Location in revised manuscript: Results, Sec 3.2, p. 8, ll. 214-219, and new Table 2.`

### The same block, done badly (avoid this)

> Response: We have revised the manuscript to address this comment. Thank you.

This is the single most common failure. It gives the editor nothing to verify, forces the reviewer to hunt through the manuscript, and reads as evasive even when the work was actually done. The second line (the location or quoted text) exists precisely to prevent it.

## Adding figures or tables

When a comment calls for a new or revised figure or table, make the change in the manuscript using the actual figure/table (referenced by its manuscript number, e.g. "new Figure 3", "revised Table 2"), never a fabricated one. Under the default pointer style, do not replicate the figure or reproduce large blocks of text in the response letter; point the reviewer to where the figure/table now appears in the revised manuscript. Only embed a figure in the letter if the target journal expects a self-contained response. If the figure does not yet exist, flag it with `[[NEEDS AUTHOR INPUT: ...]]`.

## Adding references

If answering a comment requires citing new literature, add the citation. References cited *in the response letter* are numbered independently from the manuscript's reference list, in their own sequence (e.g. [1], [2] local to the letter), and collected under a "References cited in this response" heading at the end of the letter. This keeps the letter self-contained and avoids clashing with the manuscript's numbering.

## When you lack the information

If the location/text line needs a number, location, or result the user has not given you, do not invent it. Write the response up to the point of the gap and insert the placeholder:

> Location in revised manuscript: Methods, Sec 2.3. We have added the requested reagent catalog numbers. [[NEEDS AUTHOR INPUT: catalog numbers and supplier for the anti-XYZ antibody]]

## Tone rules

- The register is soft, warm, and collaborative throughout; the goal is to pass review, not to win an argument. Peer review is a dialogue.
- Thank each reviewer, once, sincerely, briefly. Do not open every single response with "We thank the reviewer"; vary it and sometimes go straight to substance.
- Concede real points cleanly. "The reviewer is correct" costs nothing and builds credibility for the points where you do push back.
- When you disagree, do so respectfully and explain why: clarify your reasoning constructively and with evidence, never with attitude or bare assertion. See `difficult-cases.md`.
- Never write anything that blames the reviewer for not understanding, even implicitly. If they misread something, that usually means the manuscript was unclear, so fix the manuscript and say you have clarified it.
- Avoid hedging filler ("we believe we have adequately addressed"). State what you did.

## Formatting conventions to declare up front

In the opening paragraph, state the convention, then use it consistently:

- Editor and reviewer comments: **blue font**
- Author replies (including quoted revised manuscript text, which stays italic): **black font**
- In the manuscript itself: additions in colored text or tracked changes

Markdown cannot render font color, so when drafting in Markdown, label the parts explicitly (e.g. bold "Comment"/"Response" labels) and apply the actual blue/black colors when rendering to `.docx`, `.pdf`, or LaTeX. State whichever convention the final document uses so the editor is not guessing.
