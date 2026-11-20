# Science: Template Notes

Distilled from Science's own official Word templates (December 2025). The templates themselves are not bundled (they are AAAS's copyrighted files); download the current versions from the Science author resources (https://www.science.org/content/page/science-information-authors):
- Science manuscript Word template
- Science supplementary-materials Word template

Dated December 2025. Templates get revised, so for a live submission still spot-check `https://www.science.org/content/page/science-information-authors` (or search "Science instructions for preparing initial manuscript") that nothing has changed since. This file exists so the exact requirements below do not need re-deriving from the docx every time.

## Why this matters for the reformat

Science auto-extracts the title, authors, abstract, and other fields from the manuscript for its system, keyed on exact section-label wording. Getting these labels and the section order right is not cosmetic here: it drives correct parsing on submission, not just visual style.

## Section labels and order (exact wording, each followed by a colon in the template)

`Title:` -> `Authors:` -> `Affiliations:` -> `Abstract:` -> `Main Text:` -> `References and Notes` -> `Acknowledgments:` -> `Supplementary Materials`

Do not paraphrase these labels (e.g. not "Introduction" in place of "Main Text:").

## Limits and format specifics

- **Title:** 96 characters and spaces or fewer; avoid jargon and abbreviations where possible.
- **Abstract:** 100-125 words, one paragraph: opening question/framing (comprehensible to a general reader), background specific to the study, results, one concluding sentence.
- **Authors:** one single paragraph, no line breaks. Given name or initial + family name, separated by commas. Superscript numbers link to affiliations; non-superscript symbols (`*†‡§¶#**††‡‡...`) mark author notes (equal contribution, present address, etc.), in that fixed symbol order.
- **Affiliations:** each a separate paragraph, preceded by the matching superscript number, ending in a period; city and country only (no full mailing address); use a semicolon to separate institution from address.
- **Corresponding author:** marked with `*` in the author list, email given as "*Corresponding author. Email: ...".
- **Headings (Main Text):** up to three levels: level 1 bold, level 2 bold+italic, level 3 italic. Each heading is its own paragraph break. No heading may precede the first paragraph of the main text. Subheadings are required in Research Articles and Reviews.
- **Figure/table callouts:** main text uses "Fig. 1", "Table 1"; supplementary items are cited as "fig. S1", "table S1" (lowercase "fig"/"table" for SM items). Figures/tables cited in first-mention order throughout, including SM items.
- **Citations:** parenthetical italic number, e.g. "(1)"; multiple as "(2, 3)"; a run as an en dash "(4-6)". Citation order follows first appearance across text, text boxes, captions, notes, acknowledgments, then supplementary materials.
- **References and Notes:** a single numbered list covering both main text and supplementary materials citations; no second reference list in the SM. Each reference is its own number, ending in a period; do not combine a reference with an explanatory note under one number. Style: `A. Person, B. Person, Article title. Credible Journal #Volume, #pg-#pg (#Year). doi:#`. References cited only in the SM still belong in this one list and are not counted toward main-text length limits.

## Acknowledgments (fixed subsection order, each its own paragraph)

1. Free-text acknowledgment of non-author contributions, including any AI-assisted-writing or editing-service disclosure.
2. **Funding:** each source its own paragraph, full agency name, grant number, and recipient initials.
3. **Author contributions:** CRediT taxonomy encouraged; each CRediT role its own line, initials only, no punctuation between initials (e.g. "Conceptualization: SBB, DLA, MPW").
4. **Diversity, equity, ethics, and inclusion** (optional).
5. **Competing interests:** required for every author, including an explicit "no competing interests" statement when true.
6. **Data, code, and materials availability:** required in every paper, even when there is nothing newly created; any restriction (e.g. an MTA) stated explicitly. A repository DOI, if any, is numbered as the last main-reference-list item before the supplementary references and cited here. If everything is in the paper/SM, use the fixed sentence "All data are available in the main text or the supplementary materials."

## Supplementary Materials block (end of main manuscript, a list only)

Lists what the SM contains (Materials and Methods, Supplementary Text, Figs. S1 to S#, Tables S1 to S#, References, Movies/Audio/Data S# as applicable) and flags which references are SM-only. The actual supplementary content is a **separate file**, built from the bundled SM template, never appended to the main manuscript file.

## Supplementary materials template specifics

- Cover page: title, full author list, corresponding-author email (pasted verbatim from the main manuscript, no line breaks), then a description of what the file includes (drawn from the same list format as the main manuscript's Supplementary Materials block).
- No second reference list: SM citations are already covered by the single main-text reference list.
- Not a venue for extra discussion, analysis, interpretation, or critique of other work; text content is Materials and Methods and Supplementary Text only.
- Each figure or table on its own page, placed above its caption; large tables wider than the page go in a separate spreadsheet file (.xlsx or similar) instead of the SM document.

## What this changes about the reformat workflow for Science

When the target is Science, treat these notes as the primary structural authority, per the "Journal template notes" section of `SKILL.md`. Build the manuscript to this structure and, if the user supplies Science's own downloaded manuscript template, populate it; put supplementary materials into the separate Science supplementary-materials template, exactly as Science requires. Everything else in this skill's rules still applies unchanged: format and structure only, never the author's wording; never invent a missing reference field, funding detail, or contribution; flag anything the template requires that the source manuscript does not supply.
