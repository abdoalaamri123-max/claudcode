---
name: citation-auditor
description: Two modes for citation work, both grounded only in real database lookups and never invented. FIND mode takes a claim and finds real supporting references in PubMed, bioRxiv, medRxiv, and arXiv; if no claim is given and the user asks to find every unsupported claim, it splits the manuscript into claims and finds references for each, giving the supporting location, evidence strength, and an insertion suggestion per candidate. VERIFY mode audits existing citations for metadata accuracy, duplicate entries, retracted-paper citations, genuine support (misrepresentation), omission of relevant or contradicting work, and selective citation patterns, outputting a field-level correction report with severity grading. Use whenever the user wants to find a citation for a claim, check whether citations are correct, complete, unbiased, or cite a retracted paper, verify reference metadata, or clean a Zotero or BibTeX library (for your own published paper's errors, see post-publication-corrector instead).
---

# Citation Auditor

Two citation jobs: **Find** the right references for a claim, and **Verify** that existing citations are correct, correctly used, and correctly formatted. Both are grounded only in real database lookups.

## The one rule that cannot be broken

**Never invent a citation.** Every reference this skill proposes or confirms must come from a real database lookup and carry a real identifier (PMID, DOI, or arXiv ID). Never fabricate a reference, a DOI, metadata, or a claim that a paper "supports" something you did not actually read. If a lookup returns nothing, say so; do not fill the gap from memory. This is the entire reason to route through databases rather than recall.

## Two modes

- **Find (default when a claim is given):** find supporting references for that one claim. If no claim is given and the user asks to "find every unsupported claim and suggest citations", first split the manuscript into individual evidence-needing claims, then find references for each. Read `references/finding-references.md`.
- **Verify:** audit existing citations for metadata accuracy (including duplicate entries), retraction/validity status, genuine support, format, and (on request or for a thorough pass) citation-integrity issues — omission and selective citation. Read `references/verifying-citations.md`.

If it is unclear which mode applies, ask one short question.

## Sources

Search and retrieve only from real sources, by identifier where possible (DOI, PMID, arXiv ID) for structured metadata:

- **PubMed** (published biomedical literature) via the PubMed connector.
- **bioRxiv and medRxiv** (preprints) via the bioRxiv connector, which covers both.
- **arXiv** (physics, CS, quantitative biology preprints) via its public API/site.
- **Zotero** (the user's own library) via the Zotero connector: check it first, since a wanted paper may already be there.

Load these connectors with tool_search before use. Where a connector is not available, fall back to the database's website or public API via web search and fetch, still recording the real identifier.

## Dependencies and secrets

- PubMed retrieval needs an email configured (`PUBMED_EMAIL`, or `mcp-server/config.toml`).
- Never write an Elsevier (or any) API key into a repository file. Keep secrets only in local secure configuration, never committed.

## Find workflow

Read `references/finding-references.md` for the selection rules and how to present candidates.

1. **Get the claim(s).** One claim is the default. In sweep mode, first split the manuscript into individual statements that need evidence, and number them.
2. **Classify each claim** to know what kind of source it needs: a specific experimental fact wants an original research article; whole-field background wants one high-quality review; a direct comparison with the user's results wants the few most representative studies.
3. **Search the right sources** (Zotero first, then PubMed/bioRxiv/medRxiv/arXiv). Read the abstract, and the relevant section where needed, of each candidate.
4. **Keep only papers that actually support the claim**, not keyword matches. Prefer primary literature over secondary; include a seminal work and recent (roughly 3 to 5 years) work where the claim is introductory.
5. **Present 2 to 4 candidates per claim**, each with: the **supporting location** (which clause of the sentence, or where in the manuscript, it backs), the **evidence strength** (strong / moderate / weak, with why), and an **insertion suggestion** (exact spot and citation placement, so each marker sits next to the specific assertion it supports).
6. **Export on request** in the target citation and export format (BibTeX, RIS, or CSL-JSON), or add the entry to the user's Zotero library via the connector.

## Verify workflow

Read `references/verifying-citations.md`.

1. Extract each citation and the claim it is attached to.
2. Cross-validate its metadata against multiple sources by DOI/PMID/arXiv ID, and check whether two or more reference-list entries resolve to the *same* underlying work (a duplicate entry — common after merging co-authors' reference lists, or citing a preprint and its later published version separately).
3. Check retraction and validity status against more than one source (PubMed, the publisher/DOI page, and the Retraction Watch Database) *before* the support check below — a retracted source cited as if still valid is a "must fix" regardless of whether it happens to support the claim's wording.
4. Check completeness, whether the cited work genuinely supports the claim (reading the actual relevant section, not just the abstract — this is where misrepresentation gets caught), and the reference-list *metadata* format (a malformed DOI, a wrong journal-name abbreviation). In-text citation *prose* punctuation (`et al.` comma/period placement, over-citation trimming) is `manuscript-copyeditor`'s job, not this one's.
5. On request, or for a thorough pass, also check citation integrity: **omission** (a well-known, seminal, or contradicting paper that appears to be missing for a given claim) and **selective citation** (whether the set of citations for one point represents the literature fairly, or leans one-sided). Both require an independent literature search, so this is an opt-in deeper pass, not run by default — see `references/verifying-citations.md` Step 5. Report these as an observation with a real citation behind it, never as an accusation of deliberate bias or misconduct.
6. Output a field-level correction report with severity grading, explaining conflicts rather than merging them.
7. Where asked, clean the wrong metadata in the Zotero or BibTeX library.

## Output

- **Find:** a per-claim table of candidates with supporting location, evidence strength, and insertion suggestion; optional export file or Zotero entries.
- **Verify:** a field-level table (field, original value, trusted-source value, difference, evidence link) with severity for each finding — including duplicate entries and retraction/validity status — plus a citation-integrity table (omission / selective citation) when that pass is run.

Template in `assets/citation-report.md`.

## Cautions

Reading candidates for every claim in a whole-manuscript sweep is token-intensive, so the default is one claim at a time; run the sweep only when the user asks. The same applies to Verify mode's omission and selective-citation checks (Step 5 of `references/verifying-citations.md`): both require an independent literature search per claim, so run them on request or for a genuinely thorough pass, not by default alongside routine metadata verification. Retraction status (Step 3) is cheap by comparison — check it by default for every reference, not just on request, since a single database's status field is not always reliable and the cost of missing a retraction is high. Prefer original literature over secondary, cite only what genuinely supports the point, do not over-cite, and do not omit a field's classic work. Above all, never surface a reference that did not come from a real lookup, and never present an apparent omission or selective-citation pattern as an accusation of deliberate bias or misconduct — describe the gap, back it with a real citation, and leave intent to the author.
