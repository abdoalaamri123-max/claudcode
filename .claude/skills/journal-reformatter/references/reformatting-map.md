# Reformatting Map

Read this when converting a manuscript into a target journal's format. For each dimension it says what to change and which parts are automatic versus flagged for the author. The overriding rule holds throughout: change format and structure, never the author's wording, and never invent missing data.

Where the target journal's author guidelines are available (fetched from the journal or publisher website, or supplied by the user), they win over any convention here; journal requirements change, so use the current official guide. For a target with a template notes file (see "Journal template notes" in `SKILL.md`), that notes file is the authoritative structural source; for Science, that is `references/science-template-notes.md`, which encodes the journal's extracted requirements (exact section labels, title/abstract limits, three-level heading style, citation style, CRediT-style contributions, and the separate-file rule for supplementary materials) more precisely than the generic conventions below.

This map applies equally to both starting points a manuscript can be in: already styled for a named source journal, or a plain, unstyled draft with no journal formatting yet. When there is no named source, treat the draft's own ad hoc citation markers, headings, and layout — whatever they happen to be, even inconsistent — as the "from" side of each dimension below.

## 1. Citations and references (the largest change)

The main axis is author-year versus numbered.

- **Author-year (e.g. Cell-style): (Smith et al., 2020)** in text, with an alphabetical reference list.
- **Numbered (e.g. Nature-style): superscript or bracketed numerals** in text, with a reference list numbered in order of first appearance.

To convert:
- Parse every in-text citation and map it to its reference-list entry.
- Rebuild the in-text markers in the target style (renumber in citation order for numbered styles; format names/year for author-year).
- Rebuild the reference list in the target's format (author initials vs full names, journal-name abbreviation vs full, element order, punctuation, DOI presence, "et al." threshold).
- **Automatic:** reordering, renumbering, and reformatting of entries that are complete.
- **Flag for the author:** any in-text citation that cannot be matched to a list entry (or vice versa), *or that matches more than one reference-list entry ambiguously* (e.g. two "Smith et al., 2020" entries with no disambiguator such as an initial or a letter suffix) — not only citations with zero matches, since silently picking one during renumbering is a reference-integrity error, not a cosmetic one; any reference missing fields the target format requires (volume, pages, DOI); anything where the source data is ambiguous. Never fabricate a missing field.
- **Unstyled draft with an inconsistent or absent citation style:** parse whatever markers are actually present, even if mixed or informal (e.g. some citations bracketed, some not); if there are no citations or reference list at all, there is nothing to convert for this dimension — note that and move on rather than inventing one.

## 2. Section structure and headings

Journals differ in section names, order, and where Methods sit.

- Map source section names to the target's (e.g. Summary to Abstract; STAR Methods to Methods; Results and Discussion combined vs separate).
- Reorder existing sections into the target's sequence (e.g. Methods at the end vs after the introduction) by moving blocks, not rewriting them.
- Apply the target's heading case, numbering, and levels.
- **Flag for the author:** a target-required section that has no source equivalent (it needs to be written); a source section the target does not allow (the author must decide where its content goes).

## 3. Abstract / summary

- Rename to the target's term (Summary vs Abstract).
- Apply structured vs unstructured format.
- Check the length against the target limit. **Do not trim by rewording;** if it is over length, flag it for the author with the current and allowed counts.

## 4. Figures, tables, and legends

- Convert callout style ("Figure 1" vs "Fig. 1"; "Table 1"; panel reference style).
- Apply the target's legend placement (in text vs end of manuscript) and numbering.
- Renumber if section reordering changed first-mention order, keeping callouts and legends consistent.
- **Flag for the author:** figure file format, resolution, or size requirements that need new files; any figure permission the target requires.

## 5. Title page and authors

- Apply the target's affiliation markers (superscript numerals vs symbols), corresponding-author notation, and ORCID placement.
- Apply title case/length rules; if the title exceeds a length limit, flag rather than reword.
- **Flag for the author:** any required author-level detail not present (e.g. contribution codes).

## 6. Required sections and statements

Check presence of each statement the target requires and flag any that are missing for the author to write:

- Data (and code) availability.
- Author contributions.
- Ethics approvals / consent.
- Funding.
- Conflict of interest / competing interests.
- Any journal-specific declaration (e.g. AI-use disclosure).

Presence and relabeling are automatic; writing a missing statement is manual.

## 7. Layout and general formatting

- Line numbering, line spacing, margins where specified.
- Heading capitalization and font conventions the target defines.
- Units, number, and date style if the target specifies a house style (formatting only, not values).
- Consistent application throughout.

## Limits summary (always flag, never auto-resolve by rewording)

Word count, abstract length, figure/table count, reference count, and title length. Report current vs allowed and leave the trimming decision to the author.
