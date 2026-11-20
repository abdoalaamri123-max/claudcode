---
name: journal-selector
description: Help researchers choose where to submit a manuscript, evaluate journal fit, and maintain a categorized journal database. Use this skill whenever the user asks where to submit a paper, asks to rank journals for a manuscript, wants a submission tier/ladder (target plus fallbacks), asks whether a specific journal fits their work, asks whether a manuscript is Nature/Science/Cell-worthy or has broad enough interest for a flagship journal, mentions impact factor / acceptance rate / review speed / open-access fees in a submission context, or wants to build or update a list of journals by field. Trigger this even when the user only describes a paper's findings and asks "where should this go" without naming the word "journal", and for proteomics, mass spectrometry, spatial omics, oncology, and translational/clinical work specifically, though the framework is field-general.
---

# Journal Selector

**Always respond in English** (tables, headers, and prose), regardless of the language the user writes in.

Help researchers decide where to submit. This skill supports three scenarios. Identify which one the user wants, then follow that path. When in doubt, ask one short clarifying question.

1. **Rank a tier/ladder for a specific manuscript** — produce a scored, ordered list of target and fallback journals.
2. **Evaluate one journal against a manuscript** — decide fit and explain why.
3. **Build or update a categorized journal list** — maintain a reference of journals by field.

## Data sources

> **Where the numbers come from.** This skill does not bundle a numeric journal database (bibliometric datasets are license-restricted). Get the hard numbers live by **web search** and use the bundled qualitative knowledge for fit and logistics.

This skill draws on two complementary sources:

1. **Live web search — the hard bibliometric numbers (Dimension 2 and the soft inputs to Dimension 3).** For any journal the recommendation depends on, web-search the current **JCR Journal Impact Factor** (Clarivate, released each June) and its recent trend, **CiteScore** and **quartile** (Scopus/Scimago), and the **SJR H-index**. For Dimension 3, look up the journal's own author guidelines / editorial pages (and third-party trackers) for acceptance difficulty, typical time-to-first-decision, and open-access status/APC. Treat any third-party "predicted IF" as an estimate, not the real value, and prefer the journal's own pages and the authoritative index (JCR/Scopus) over aggregators.
2. **`references/journals.md`** — curated *qualitative* knowledge search alone will not give you quickly: each venue's editorial taste / what angle it rewards (for Dimension 1), a publisher / sponsoring-society / country table, submission entry points, and the institutional-blacklist caution list. Read it for fit judgment, publishing-org metadata, and submission logistics.

Use web search for "what are the current numbers"; use `references/journals.md` for "would this paper actually fit here and how do I submit". When a venue is not in `references/journals.md`, web-search both its numbers and its editorial scope.

## Required input (Scenarios 1 and 2)

The input must let **all three scoring dimensions** be evaluated, not just selling-point match. Organize the needed information by the dimension it feeds. If the elements feeding a dimension are absent, that dimension can only be scored from the journal side, which is incomplete — ask for what is missing.

**For selling-point match (D1) — the manuscript's content:**
1. **Core discovery** — the central finding, with brief background and the bottleneck/gap it resolves (what was the open problem, what does this close).
2. **Innovation category** — which of method / biology / clinical implication is the *strongest* novelty (one may dominate, or it may be a combination), stated explicitly.
3. **Advance over prior / competing work** — how this differs from and exceeds the current state of the art. Novelty is relative; editors and reviewers weigh the delta, not the result in isolation.
4. **Significance statement** — why the work matters and to whom; the "so what".

**For tier calibration (D2) — the work's reach:**
5. **Magnitude / ambition** — incremental, substantial, or field-defining, judged against the flagship-tier substantive bar in Dimension 1 (breadth of interest beyond the subfield, a genuine conceptual advance, mechanistic vs. correlational evidence, and, for the matching article type, resource value / technical breakthrough / public-health urgency). This sets a realistic ceiling tier and prevents both over-reaching (Nature for an incremental result) and under-shooting (a mid journal for a landmark study).
6. **Field / target audience** — for field-relative prestige and venue-scope fit.
7. **Data scale** — cohort/sample/feature size and breadth; a proxy for both rigor and ambition.
8. **Manuscript type** — research article / brief communication / resource / protocol / review, since this gates eligible journals and article formats.

**For practicality (D3) — the author's constraints:**
9. **Timeline / urgency** — deadlines (grant, thesis, tenure) and scooping/priority risk. This is what justifies up-weighting speed.
10. **Budget / OA mandate** — APC the author can pay, and whether a funder requires gold open access. This gates expensive or OA-only venues.
11. **Journals to avoid / prior history** — venues already tried (rejection or transfer offers), conflicts of interest, or any the author rules out.

**Optional:** an **aim journal** already in mind, to evaluate or benchmark against.

**Recommended input:** a **cover letter or the manuscript Introduction** supplies elements 1-8 (content and reach) in the author's own framing; a title + abstract is a lighter substitute. Elements 9-11 (constraints) are usually *not* in the manuscript and should be asked for if not volunteered, because they drive the weight adjustments in the scoring framework (e.g. tight timeline → up-weight practicality; OA mandate → filter venues). 

**How much to ask:** elements 1, 2, and 4 are essential — if missing, ask before scoring rather than guessing. Elements 3 and 5-8 sharpen accuracy; infer from the input where reasonable, ask only if a gap materially changes the recommendation. Elements 9-11 default to "none stated" if the user does not raise them; surface them as a brief one-line prompt rather than blocking. Do not over-interrogate.

## Scoring framework

Every journal recommendation gets scored on three dimensions, each 1-10, plus a weighted total. Always show the per-dimension scores and the ranking, not just a final verdict.

**Dimension 1 — Selling-point match (1-10).** How well the manuscript's core contribution matches what the journal publishes. Decompose the manuscript into three angles and judge which the journal rewards:
- *Method/technical* novelty (new assay, instrument, pipeline, model)
- *Biological* discovery (new mechanism, biology, unexpected finding)
- *Clinical/translational* value (cohort, biomarker, diagnostic, therapeutic relevance)

A journal scores high only if its editorial taste matches the manuscript's *strongest* angle. A biology-driven story sent to a methods journal scores low on this dimension even if the journal is prestigious. This dimension is computed fresh per manuscript and is the most important one.

Score D1 against this rubric so it is reproducible, not a gut number:
- **9-10:** the manuscript's strongest angle is exactly what this journal is known for, AND the work clears the journal's usual evidence bar (e.g. in vivo validation, external cohort, or mechanism depth that the journal expects).
- **7-8:** strong topical match, but one expected element is thinner than the journal typically wants (e.g. internal-only validation, in vitro only where in vivo is customary).
- **5-6:** plausible scope fit but the angle is not the journal's focus, or a key expected element is missing — real major-revision or borderline-desk-reject risk.
- **3-4:** scope overlaps but the journal rewards a different angle than the manuscript leads with.
- **1-2:** wrong venue type for this angle (e.g. a chemistry-novelty journal for a clinical cohort).

**Evidence-bar cap (hard rule, prevents prestige from masking a misfit):** if the manuscript lacks an element a journal effectively requires for that article type — most commonly *in vivo validation* or an *external/independent cohort* for high-tier biology/clinical venues — cap D1 at 5 for that journal regardless of topical match, and label it a near-certain desk-reject or major-revision risk. The four-test history showed why: a purely in vitro mechanism story scores high on topic at Cell Host & Microbe but is realistically a desk reject there; the cap encodes that so the weighted total cannot float it into the ladder.

**Flagship-tier substantive bar (apply only when scoring a Nature/Science/Cell-tier or top Nature-family/Cell-family venue — Dimension 2 anchor 8-10).** At this tier, editors weigh the manuscript's own substance more than topical fit. Roughly in weight order:

- *Primary — the two that decide most flagship-tier calls:*
  - **Breadth of interest** — would scientists in *other* fields find the conclusion novel or directly relevant, not just specialists in this subfield?
  - **A striking conceptual advance** — do the conclusions change how the field thinks about the problem, rather than extend or confirm what was already believed?

**Operational test for "credibly present" (prevents the bar from being a rubber stamp):** for breadth of interest, name one specific field or subfield *outside* the manuscript's own subfield whose researchers would plausibly read or cite this; if none can be named concretely, treat breadth of interest as not credibly present. For conceptual advance, name the specific prior belief, model, or assumption the conclusion overturns or revises; if no such prior belief can be stated concretely, treat it as not credibly present. A criterion is credibly present only when this naming exercise produces something concrete — not when it merely feels plausible.

- *Also weighed — each strengthens or weakens the case, none alone is decisive:*
  - **Strong logical support** — do the methods and evidence actually bear the full weight of the claim, without over-reaching beyond what was shown?
  - **Mechanistic insight, not just correlation** — does the paper explain *why*, not only show *that*?
  - **Likely to inspire further research** — would this open a new line of work for others, not just close one question?
- *Article-type-specific alternate paths — any one can itself justify flagship-tier candidacy for the matching format, even without a classic conceptual advance:*
  - **Significant resource value** (e.g. a genome, a screen, a reference dataset others will reuse) — for Resource-type submissions.
  - **Significant technical breakthrough** (e.g. a new structural or single-molecule method) — for Methods/Technical-type submissions.
  - **Significant public interest** (e.g. an outbreak pathogen, a phase-I trial) — for urgent-relevance submissions.

**Scoring rule:** for a flagship-tier venue, cap D1 at 4-5 if *neither* primary criterion is credibly present and *none* of the article-type alternate paths apply — label it "solid work, but not flagship-tier material; aim one tier down." If exactly one primary criterion is present, cap D1 at 6-7 — "plausible but a real stretch, hinges on how the editor reads it." Only let D1 reach 8-10 for a flagship venue when *both* primary criteria are credibly present (or one article-type alternate path clearly applies), and even then flag explicitly if the secondary criteria are weak (e.g. correlational-only evidence, claims that outrun the data) as a risk to the editor's send-out decision. This cap composes with the evidence-bar cap above — apply whichever is lower, and say which one bound the score.

**Dimension 2 — Impact & prestige (1-10).** Built from the two *hard* bibliometric signals plus field reputation:
- **Impact factor — level AND trend.** Web-search the journal's current JCR Impact Factor, CiteScore, and quartile. Read the IF over the last few years as a **trend**: a rising trajectory (e.g. 6.9 → 7.3 → 7.8) is a positive signal, a falling one (e.g. 8.8 → 8.0 → 6.9) is a caution flag even if the current level looks fine. JCR (Clarivate, released each June) is the authoritative IF source; treat any third-party "predicted IF" as an estimate, not fact.
- **Journal H-index (CiteScore / Scimago).** A measure of sustained citation impact, more stable than IF year-to-year. Look it up on Scimago (SJR); note that journal H-index is source-dependent, so record which source an external figure came from.
- **Field reputation.** IF is field-relative; weight reputation within the manuscript's field (use the journal's quartile within the relevant subject category), not the raw number.

Anchor the score using the journal's IF and quartile within the manuscript's field:
- **10:** flagship multidisciplinary / top-of-field (Nature, Science, Cell) and the top general-medicine journals for clinical work (NEJM, The Lancet, JAMA).
- **8-9:** top Nature-family and elite society journals (Nat Methods, Nat Biotech, Nat Med, Nat Cancer, Cancer Cell, Molecular Cell), the BMJ, and high-impact specialty clinical journals (Lancet Oncology, JAMA Oncology); typically very high IF, Q1.
- **6-7:** strong Q1 specialist / broad high-impact (Nature Communications, Science Advances, MCP, EMBO Mol Med, Cell Reports Medicine).
- **4-5:** solid Q1/Q2 field journals (JPR, Clinical Proteomics, Analytical Chemistry, Cell Reports).
- **2-3:** mid Q2/Q3 society journals (Proteomics, Journal of Proteomics, JASMS).
- **1:** low-tier Q4 / quality-risk venues (flag and discourage).

This table anchors the *journal's* prestige tier; it says nothing about whether *this manuscript* actually clears the bar for an 8-10 venue. That substantive judgment is Dimension 1's flagship-tier substantive bar, above — a journal scoring 9 here can still be capped low on D1 if the manuscript itself doesn't clear that bar.

**Dimension 3 — Practicality (1-10).** Combine review time, acceptance difficulty, and open-access status/cost into one accessibility/cost-efficiency score, from the journal's own author guidelines/editorial pages plus third-party trackers (e.g. journal-reported time-to-first-decision, community acceptance-rate estimates, the OA/APC page). Higher = faster, more likely to accept, and/or cheaper to publish. A slow, highly selective, expensive venue scores low even if prestigious. D2 and D3 usually pull in opposite directions.

Map what you find onto ordered buckets for D3:
- **Acceptance difficulty:** `Very Easy (≥80%)` > `Easy (60–80%)` > `Moderate (40–60%)` > `Difficult (20–40%)` > `Very Difficult (<20%)`. Unknown = don't penalize; note it.
- **Time to first decision:** `Very Fast (<1 month)` > `Fast (1–2 months)` > `Moderate (2–4 months)` > `Slow (4–6 months)` > `Very Slow (>6 months)`. Unknown = note it.
- **Open access:** fully OA (APC likely applies) / Hybrid / Transformative (OA optional) / subscription. Cross-check the APC against the journal's own page when cost matters.

Anchor D3 roughly:
- **8-10:** fast first decision (`Very Fast`/`Fast`) and/or easy acceptance (`Easy`/`Very Easy`) and/or low or no APC.
- **5-7:** `Moderate` turnaround and/or `Moderate` acceptance and/or moderate APC.
- **2-4:** `Slow`/`Very Slow` review, `Difficult`/`Very Difficult` acceptance, or high APC (pick the worst-binding factor).
- **1:** very slow, very selective, and expensive together.
Note which factor dominated, and that acceptance/review-time figures from third-party trackers are estimates (verify against the journal's author guidelines for a firm decision).

### Weighted total

Default weights, tuned so that fit dominates and prestige outranks practicality:
- Selling-point match: **×0.5**
- Impact & prestige: **×0.3**
- Practicality: **×0.2**

Total = round(0.5·D1 + 0.3·D2 + 0.2·D3, 1), on a 1-10 scale. State the weights you used. If the user signals different priorities (e.g. "I need this out fast" or "prestige is all that matters"), adjust weights and say so.

## Reliability and verification

Separate hard data from soft estimates and treat them differently.

- **Hard (drives D2):** IF, CiteScore, quartile, H-index — web-searched from JCR (Clarivate, June release) and Scopus/Scimago. These are the numbers a decision hinges on, so pull them live rather than from memory.
- **Soft (informs D3 only, never present as fact):** acceptance difficulty and time-to-first-decision from third-party trackers or community estimates. Useful for direction; confirm against the journal's author guidelines before relying on them. Treat any third-party "predicted IF" as a forecast, not the real IF.

**Verification discipline (required on every final ranking or single-journal verdict):** for the top ~5-8 shortlisted journals, web-search the current JCR IF, recent trend, quartile, and SJR H-index before presenting. Do not present precise numbers from memory. Submission URLs change too — give the journal's homepage as the entry point but tell the user to confirm the live "Submit" link from the journal's own page. If web search is genuinely unavailable, say plainly that specific figures could not be verified and give only qualitative tier judgments.

## Scenario 1 — Rank a submission ladder

1. Extract the manuscript from the input (see **Required input** above): content elements (1-4) for selling-point match, reach elements (5-8) for tier calibration, and constraint elements (9-11) for practicality. A cover letter or Introduction covers 1-8; pull constraints from the user if not volunteered. Apply constraints to the weights before scoring — e.g. a tight timeline or scooping risk up-weights practicality (D3); an OA mandate filters or down-weights expensive/non-OA venues; a stated ambition ceiling caps the tier. State any weight change. Ask briefly only for missing essentials (core discovery, innovation category, significance); infer the rest where reasonable.
2. **Check coverage first.** Decide whether the manuscript's field is well covered by the bundled editorial-taste knowledge in `references/journals.md`, which is deepest for proteomics, MS, spatial omics, oncology, and clinical translation, and also spans the major Nature/Science/Cell family sub-journals and field flagships in neuroscience, immunology, microbiology/microbiome, hepatology & gastroenterology, cardiology, urology, hematology, extracellular vesicles, materials/nanomedicine, and the high-impact China-based venues. For fields outside that coverage, say explicitly that fit judgment is weaker and web-search the venues' editorial scope and numbers.
3. Build a candidate set of 6-12 venues spanning tiers: start from the in-scope venues in `references/journals.md`, and web-search for additional field-appropriate journals by topic and IF/quartile to round out the tiers, then bring in editorial-taste judgment for each.
4. Score each on the three dimensions, applying the D1 rubric, the evidence-bar cap, and — for any flagship/top Nature-family/Cell-family candidate — the flagship-tier substantive bar. Compute the weighted total.
5. **Verify the shortlist live before presenting (required, not optional).** For the top ~5-8 candidates, web-search current JCR IF, recent IF trend, quartile, and SJR H-index. This is the verification discipline above; it must actually run on every final ranking. If a search is genuinely unavailable, state plainly that specific figures could not be verified and present only qualitative tier judgments.
6. Present as a ranked table from highest total to lowest, grouping into "reach", "match", "safe". For any journal hit by the evidence-bar cap, mark it and name the missing element. For any journal on the institutional-blacklist list, add the caution.
7. Add a short paragraph naming the top recommendation and the most sensible fallback, one sentence on the prestige-vs-practicality trade-off, and — following the skill's discipline — the single question whose answer would most change the ceiling (e.g. external vs internal validation, in vitro vs in vivo; for a flagship-tier reach, "would this surprise someone outside the subfield" or "is this mechanism or correlation").
8. For the top recommendation and main fallback, append the submission entry point (homepage + platform), the **publisher / sponsoring society / country** (from the metadata table in `references/journals.md`), and remind the user to confirm the live "Submit" link before submitting.

Use this output structure (English):

```
## Submission ladder: [manuscript short name]

Weights: Selling-point match ×0.5 | Impact ×0.3 | Practicality ×0.2

| Journal | Selling-point | Impact | Practicality | Weighted | Tier | Rationale |
|------|:---:|:---:|:---:|:---:|------|------|
| ...  |  9  |  8  |  4  | 7.4 | reach | ... |

**Top pick:** ... | **Safe fallback:** ...
**Publisher / society / country (top pick & fallback):** ...
**Trade-off:** ...
**The one question that most changes the ceiling:** ...
```

## Scenario 2 — Evaluate one journal

1. Web-search the journal's current numbers (JCR IF and trend, CiteScore, quartile, H-index) and check its editorial taste in `references/journals.md`; web-search its editorial scope too if it is not in that file. The live search is required for any real decision.
2. Score the three dimensions for *this manuscript at this journal*, applying the D1 rubric and the evidence-bar cap (if the paper lacks an element this journal effectively requires, cap D1 at 5 and say so), and, if this is a flagship/top Nature-family/Cell-family venue, the flagship-tier substantive bar (cap D1 at 4-5 if neither breadth-of-interest nor a conceptual advance is credible and no article-type alternate path applies).
3. Give a clear verdict: good fit / marginal / poor fit, with the deciding reason. Selling-point match almost always decides it. State what would have to be true about the paper for the journal to become a good fit. If the journal is on the institutional-blacklist list, add that caution. If the verdict is good or marginal, append the submission entry point, the publisher / sponsoring society / country, and the reminder to confirm the live link.

## Scenario 3 — Build or update a journal list

1. The curated qualitative layer is `references/journals.md` (editorial taste, submission portals, publisher/society/country metadata, blacklist cautions). There is no bundled numeric database; numbers come from live web search.
2. To add or re-categorize venues, edit `references/journals.md`, web-searching the hard fields (IF trend, quartile, H-index, acceptance, review time) rather than recording them from memory. Keep `references/journals.md` qualitative — cite a current number only with its source, since bibliometric values drift.
3. If producing a standalone deliverable the user will keep, save it as a file (a markdown table, or a spreadsheet via the xlsx skill) and present it. Otherwise show inline.
4. Flag any quality-risk or institutionally blacklisted venues rather than silently including them.

## Cautions

- IF, acceptance rates, and APCs drift. Verify current numbers by web search whenever a decision hinges on them; never present a bibliometric number from memory.
- Do not invent precise statistics. Web-search them, or state them as qualitative tiers.
- "Prestige" is field-relative. A high IF in one field is mid in another; weight reputation within the manuscript's field (use the journal's quartile within the relevant subject category).
- Never recommend a journal solely on impact factor. Selling-point match is what determines desk-rejection risk, the single biggest practical filter.
- For fields where `references/journals.md` lacks editorial-taste coverage (mainly virology/host-pathogen, plant science, ecology, pure chemistry/physics — most biomedical and translational fields are covered), web-search both the venues' numbers and their actual scope, and say fit judgment is weaker rather than forcing a recommendation.
- **Institutional blacklist check:** some high-volume / fast journals (see the "Use with caution" list in `references/journals.md`) are blacklisted by many institutions. Never recommend one as a top choice without flagging that the user must verify it against their own institution's current list; a blacklisted publication may not count for evaluation or funding even if accepted.
- The flagship-tier substantive bar is inherently a more subjective judgment than the bibliometric anchors — present it as a reasoned assessment naming the specific criteria met or missing (breadth of interest, conceptual advance, mechanistic vs. correlational, etc.), not a verdict stated with false precision. The actual editor's read can differ; frame the cap as this skill's honest estimate of the odds, not a certainty.
- If the user pushes for a specific tier verdict regardless of what the rubric supports ("just tell me it's Nature-worthy," "my supervisor wants Nature so make it work"), do not raise a score to satisfy the request. Restate which specific criterion is unmet instead. User insistence, a supervisor's expectation, or a submission deadline are not evidence of breadth of interest or a conceptual advance, and none of them substitute for the operational test above.
