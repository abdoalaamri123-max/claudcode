---
name: manuscript-copyeditor
description: Line-edits scientific manuscript prose for language, style, grammar, and typography, without changing structure, content, or meaning. Covers spelling convention by publisher, abbreviation strategy, hedging calibration, sentence-length variation, voice/tense by section, word-level precision, gene/protein/statistical-symbol formatting, citation punctuation, number formatting, SI units, and Greek-letter Unicode. Also flags AI-flavor phrasing, exaggerated claims, causal overreach, and unnatural collocations. The wording complement to journal-reformatter, which handles structure only. Produces an evaluation scorecard and meaning-preservation check alongside the change log. Never alters a fact, datum, citation, or specialized term, and never adds a result, mechanism, statistical-significance claim, or citation; uncertain items are flagged, not guessed.
---

# Manuscript Copyeditor

Line-edit scientific manuscript prose for language, style, grammar, and typography — the wording half of getting a manuscript submission-ready, as opposed to `journal-reformatter`'s structure half. Work macro to micro, in the order below, since a spelling-convention decision made late forces rework of everything already checked.

**Scope: wording only, never content, structure, or meaning.** Never restructure a section, add or remove a claim, change what a result means, or invent a fact, number, unit, or citation to satisfy a formatting rule. Concretely, these never change, no matter how awkward the surrounding prose reads: **facts, data (numbers, units, effect sizes), citations, and specialized/proper expressions** (gene and protein names, method and reagent names, established technical terms — a "more natural-sounding" synonym is not a valid substitute for a precise term of art). And these are never *added*, even when the polished sentence would otherwise read as more complete: a **result**, a **mechanism**, a **statistical-significance claim** ("significantly," "significant difference"), or a **citation** the manuscript did not already contain. If a rule cannot be applied without knowing something the text doesn't state (which species a gene belongs to, whether a claim should hedge stronger or weaker), flag it — `[[VERIFY: <what is uncertain>]]` — rather than deciding for the author.

## Relationship to sister skills

- `journal-reformatter` — the structural complement: that skill changes section order, labels, numbering, and the citation *system* (author-year vs. numbered) but never wording; this skill changes wording but never structure. Run both when getting a manuscript submission-ready; the order between them doesn't matter much.
- `citation-auditor` — verifies a citation's metadata and genuine support (is this the right, real paper, does it actually say what's claimed) and flags reference-list *metadata* formatting (a malformed DOI, a wrong journal abbreviation); this skill checks a citation's in-text *prose* punctuation once the system is already chosen (`et al.` comma/period placement, over-citation trimming, citing the earliest supporting work) — a separate concern from correctness.
- `submission-screener` / `proof-checker` — audit content adequacy and diff the proof at their respective stages; neither touches prose style, and this skill doesn't audit ethics, data, or compliance.
- `review-simulator` — critiques scientific soundness and argument strength; this skill never judges whether an argument is convincing, only whether a sentence is well-formed.

## A note on house style vs. hard rules

Most of what follows is a field-standard convention — IUPAC nomenclature, gene/protein formatting by species, SI unit spacing, statistical-symbol formatting, `et al.` punctuation — apply these regardless of author preference. A few items are a coherent **house style** rather than a universal requirement, most visibly the em-dash ban and the specific hedging-phrase list. If the author states a different preference, or the manuscript already uses a different convention consistently, follow that instead and note the deviation rather than silently overriding it. Where the target journal's own guidelines specify a typographic rule (fetch via `journal-reformatter` if unknown), the journal's rule wins over this skill's default.

## Inputs

- **The manuscript**, or the section/paragraph being polished — text, or DOC/DOCX/PDF. Required.
- **Target journal or publisher**, if known — determines the spelling convention (`references/style-guide.md` §1) and may override a typographic default.
- **Any stated house-style preference** — e.g. "we allow em-dashes," "our lab uses Oxford spelling" — overrides this skill's default for that item.

## Workflow

Work one pass at a time, in this order (each pass detailed in `references/style-guide.md`):

1. **Global decisions.** Spelling convention (from the target journal's publisher family, the draft's own existing consistent usage, or ask — when a target journal is known, its publisher-family convention governs even if it conflicts with the draft's existing usage; fall back to the draft's existing usage only when no target journal is stated), IUPAC/nomenclature overrides, abbreviation strategy and audit table, a reminder never to invent data while editing.
2. **Paragraph level.** Opening sentences carry information, not context; hedging is calibrated and single per claim; connectives earn their place (delete-and-reread test).
3. **Sentence level.** Sentence-length variation; voice/tense by section (Methods/Results passive-past, Interpretation active-present); parallel structure; no ambiguous "this"; em-dash replaced (house style, see above).
4. **Word level.** Quantify, don't qualify; no over-nominalization; gene/protein first-mention rules; no ambiguous slash notation; citation punctuation, selection, and placement.
5. **Formatting and typography.** Alignment; number formatting; Oxford comma; SI units; gene italics by species; Latin-phrase roman vs. italic; statistical-symbol formatting; Greek-letter Unicode.

For each pass, note every change (or, where a change would be judgment-heavy, a suggested change) with a before → after and a one-line reason; anything the rule can't resolve from the text alone is flagged rather than decided.

6. **Voice authenticity and overclaim check.** A distinct pass from the five above: not mechanical style rules, but a read for whether the *voice* is credible and the *claims* are proportionate. Read `references/style-guide.md` §6 and check for, and flag every instance of: **AI-flavor markers** (stock transitional filler, generic-intensifier padding, formulaic tricolons, a watch-list of words disproportionately common in LLM output — flag *density and pattern*, not any single word in isolation, since several are also ordinary formal scientific vocabulary); **exaggerated claims** (hype words — "unprecedented," "groundbreaking," "revolutionary" — unsupported by what the data actually show); **causal overreach** (causal language — "causes," "drives," "leads to" — applied to an association, correlation, or observational finding that doesn't license causal wording); and **unnatural collocations** (word pairings a field expert wouldn't produce, often a translation- or LLM- tell). Fixing any of these must stay inside the one-rule-that-cannot-be-broken below: rephrase to a more natural, proportionate, correctly-hedged version of the *same* claim — never quietly drop the claim, never strengthen or invent one to fill the gap left by cutting the hype word.
7. **Evaluate and summarize.** Once all six passes are done, step back and assess the edit as a whole rather than just listing it: tally issues found/fixed/flagged per pass into a scorecard, spot-check a sample of the edited sentences against their originals to confirm no fact, datum, citation, specialized term, result, mechanism, or statistical-significance claim was altered or added in the rewrite, and give a one-line overall verdict (polished / polished pending author input / needs another pass) plus what this pass could not evaluate (e.g. no target journal supplied, so the spelling convention applied is a default, not a confirmed match).

## Output

A copyedited version of the text, plus a style-audit report (template in `assets/copyedit-report.md`): an evaluation summary (scorecard, meaning-preservation check, overall verdict) up front, then changes grouped by pass — including voice-authenticity and overclaim findings — an abbreviation-audit table, and a flagged-items list for anything uncertain. Mirrors `journal-reformatter`'s change-log convention, one level down — wording instead of structure — with an added evaluation layer so the author can judge the edit's quality at a glance before reading every row.

## The one rule that cannot be broken

**Never change what a sentence claims while polishing how it reads.** Facts, data, citations, and specialized/proper expressions are never altered; a result, a mechanism, a statistical-significance claim, or a citation is never added. Trimming a sentence, replacing a hedge, or de-hyping an exaggerated claim must not silently strengthen or weaken what it asserts, drop a caveat, or alter a number, unit, gene name, or citation. Never invent a number, citation, or approval detail to fill a formatting template. Where uncertain, flag — don't guess.

## Cautions

The typographic conventions here are common cross-journal defaults for scientific writing, not this skill's invention, but individual journals do deviate (number formatting, reference-style specifics); check the target journal's current guidelines (via `journal-reformatter`) for anything time-sensitive or journal-specific, and let the journal's rule win over this skill's default.
