# Finding References

Read this for Find mode. The task: for a given claim, surface real references that genuinely support it, chosen well. Everything here is subordinate to the one rule: only real, looked-up references with real identifiers; never invented.

## Splitting claims (sweep mode)

When the user asks to find citations for a whole manuscript, first break the text into individual statements that need evidence, and number them. A sentence often carries more than one claim; separate them, because each may need a different reference. Statements of the author's own new results do not need external citations; background, prior findings, methods, and comparisons do.

## Match the source type to the claim

- **Specific experimental fact or finding** -> the original research article that first reported it. Do not cite a review for a specific result.
- **Whole-field background or a general statement** -> one high-quality, recent review is enough.
- **Direct comparison with the user's own results** -> the few most representative studies, chosen for relevance, not quantity.

## Which database

- Check **Zotero** (the user's library) first; the paper may already be there with a clean entry.
- **PubMed** for published biomedical work.
- **bioRxiv / medRxiv** for preprints (biology, health sciences).
- **arXiv** for physics, computer science, and quantitative-biology preprints.

Retrieve by DOI / PMID / arXiv ID whenever you have one, for exact structured metadata. Read the abstract (and the relevant section, if needed) before proposing a paper.

## Selection rules (in priority order)

1. **Primary over secondary (most important).** If you can cite the original work, do not cite a paper that merely cites it. Reviews are for background, not for specific facts.
2. **Genuine support, not keyword match.** A paper qualifies only if it actually substantiates the claim. Matching terminology is not support; confirm from the abstract or text.
3. **Every evidence-needing sentence gets a citation**, and no more citations than the point requires. Do not over-cite.
4. **Do not omit a field's classic work.** For an introductory or background claim, combine a seminal paper with recent (roughly 3 to 5 years) work.
5. **Placement matters.** A citation marker should sit next to the specific assertion it supports, not dumped at the end of a multi-part sentence. If one reference supports the first clause and another the second, place each marker at its clause, so the reader can tell which source backs which claim.
6. **Weak support does not resolve a claim.** If every real candidate found is only weak or tangential (per the evidence-strength grading below), say so explicitly rather than presenting the weak matches as if they satisfy the claim as worded — a table of genuinely weak citations can still function as citation cover for an overreaching claim. Recommend narrowing or hedging the claim to match what the found evidence actually supports, instead of stretching the citation.

## Presenting candidates

For each claim, give 2 to 4 candidates. For each candidate:

- **Reference:** full metadata with its real identifier (PMID / DOI / arXiv ID).
- **Supporting location:** the exact clause or sentence it backs (and, in sweep mode, the manuscript location).
- **Evidence strength:** strong / moderate / weak, with a one-line reason (e.g. "direct experimental demonstration in the same system" vs "related but in a different model").
- **Insertion suggestion:** where to place the marker and, if the sentence has multiple claims, which clause it attaches to.

Note the type (original article vs review vs preprint) so the user can honor the primary-over-secondary rule. Flag a preprint as not yet peer reviewed.

## Export and library

On request, output the chosen references in the target citation and export format (BibTeX, RIS, or CSL-JSON), matching the user's reference manager (Zotero, EndNote, etc.), or add them to Zotero via the connector. Never export an entry whose metadata you could not confirm from a real lookup.
