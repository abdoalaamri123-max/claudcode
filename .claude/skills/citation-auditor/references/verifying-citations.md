# Verifying Citations

Read this for Verify mode. The task: check that existing citations are real, correct, genuinely supportive, and properly formatted, and produce a correctable structured report. Everything is grounded in real lookups; never assert a correction you cannot evidence.

## Step 1 - Extract each citation and its claim

Pair every in-text citation with the specific statement it is attached to, so you can judge both the metadata and whether the source actually supports that statement.

## Step 2 - Multi-source cross-validation

For each reference, look it up by DOI / PMID / arXiv ID and compare its fields across more than one authoritative source (e.g. PubMed metadata, the DOI/Crossref record, the publisher page). Compare:

- authors (and author order),
- title,
- year,
- volume and issue,
- pages,
- DOI,
- publication status (published, in press, preprint, retracted).

**Duplicate detection.** Once every reference resolves to a real identifier, check whether two or more reference-list entries resolve to the *same* underlying work — common after merging reference lists from multiple co-authors' managers, or citing a preprint and its later published version as if they were two different sources. Flag duplicates for merging into one entry, and flag a preprint/published-version pair for consolidating to the published version once it exists.

## Step 3 - Retraction and validity status

Check this before Step 4's support check — a retracted source dominates the finding regardless of whether it happens to support the claim's wording.

- **Check more than one source.** A single database's "publication status" field (Step 2) is not always enough: cross-check retraction status against PubMed's own retraction linkage, the publisher/DOI landing page, and the **Retraction Watch Database** (the most comprehensive independent tracker) — not every retraction is promptly or correctly flagged everywhere.
- **A retracted source cited as if still valid is a "must fix," not a style note.** If a retracted paper is cited to support a substantive claim (a finding, a method, a conclusion) without the retraction being acknowledged, the claim's own reliability may now rest on retracted evidence — this is a serious, submission-blocking error, not a metadata nicety.
- **Distinguish citing a retraction from relying on the retracted claim uncritically.** A manuscript that discusses a retraction directly, or cites a retracted paper specifically to note it did not replicate, is not the same error; the concern is treating the retracted finding as reliable support without flagging that it was retracted.
- **An Expression of Concern is a softer but real flag too** — note it distinctly from a full retraction, since it signals unresolved doubt rather than confirmed invalidity. (See `post-publication-corrector`'s classification framework if the user needs the full COPE-grounded distinction between the two.)

## Step 4 - Content and support checks

- **Completeness:** required fields present for the target format.
- **Genuine support:** the cited work actually substantiates the claim, not a keyword coincidence. Confirm this from the full relevant section of the actual paper (methods, results, or discussion, not just the title or abstract) — misrepresentation, the most common way this check fails, comes from stopping at the abstract. If the source does not actually support the claim, flag a mismatch.
- **Primary vs secondary:** a specific fact cited to a review rather than the original is flagged as a weakness.

## Step 5 - Citation integrity checks (omission and selective citation)

Distinct from Step 3: these judge what the manuscript does *not* cite, or a pattern across several citations for the same point, not whether one existing reference supports its own claim. Both require an independent literature search (same sources as Find mode), so treat this as an opt-in deeper pass, not something run by default on every citation check — see Cautions in `SKILL.md`.

- **Omission.** For a major claim, especially in the Introduction or Discussion, independently search the literature for landmark, highly cited, or directly competing work in the same specific area — not just whatever the manuscript already cites. Flag a well-known or seminal paper that appears to be missing, and flag especially any contradicting or complicating finding that a fair-minded reader would expect the manuscript to acknowledge or address, even briefly.
- **Selective citation (a pattern, not a single reference).** Across a topic or claim, does the *set* of citations chosen represent the literature fairly, or does it lean toward supportive work while omitting comparably relevant contradicting or competing findings (a competing group's directly on-point paper, a meta-analysis or replication that complicates the claim)? Judge the pattern across the citations for one point, not a single reference in isolation.

**Report these as an observation, not an accusation.** State what appears to be missing and why it looks relevant, backed by a real citation from an actual lookup, never invented — and let the author decide whether to address it. Never assert that an author deliberately suppressed a finding or acted in bad faith; describe the gap and its likely relevance, and leave intent to the author. This holds even under direct questioning ("is this bias?", "did they do this on purpose?") — answer with the observable pattern and its evidence only, and decline to render a verdict on intent regardless of how the question is phrased. These two checks are inherently more judgment-heavy than metadata verification, and a false positive is more costly here (accusing an author of a selective-citation pattern when the omission was an honest oversight) than a metadata typo — hold the bar higher before calling out an apparent pattern, and flag genuine uncertainty ("possible gap, unconfirmed") rather than asserting deliberate omission or bias with false confidence.

## Step 6 - Conflict flags

Call out, with the evidence, each of:

- **Volume/year vs DOI/online-year conflict** (the registered year disagrees with the issue year).
- **Author-order anomaly** (order differs from the source of record).
- **Page deviation** (page range does not match).
- **Title inconsistency** (wording differs from the record).
- **DOI misdirection** (the DOI resolves to a different work than cited).

When the DOI, the volume/issue, and the online-publication year disagree, **explain the conflict; do not force the values into one merged entry.** Some of these are legitimate (advance online vs issue assignment), so describe what each source says and let the author resolve it.

## Step 7 - Field-level report with severity

Output one row per checked field that has an issue:

| Reference | Field | Original value | Trusted-source value | Difference | Evidence (link/ID) | Severity |
|-----------|-------|----------------|----------------------|-----------|--------------------|----------|

Severity levels:

- **Must fix:** wrong DOI, wrong paper, a retracted or formally corrected source cited as if still valid (verified against more than one source), a citation that does not support its claim (misrepresentation).
- **Recommend check:** author-order or page discrepancy, title wording differences, a specific fact cited to a review, a well-known or seminal paper that appears to be missing (omission), a citation set that appears to lean one-sided on a given point (selective citation), or a duplicate reference-list entry for the same underlying work.
- **For reference only:** minor style/formatting differences within an otherwise-correct entry.
- **Cannot verify:** no authoritative record found, or a suspected omission/selective-citation pattern that isn't confirmable with confidence; state this rather than guessing.

## Step 8 - Clean the library

Where asked, correct the wrong metadata in the Zotero or BibTeX library, using the trusted-source values from the table, and only for entries where a real lookup established the correct value. Leave "cannot verify" and unresolved-conflict entries for the author to decide, with the conflict explained.
