---
name: reviewer-recommender
description: Recommends a ranked shortlist of peer reviewers for any manuscript by mining the manuscript's own reference list for independent domain experts and supplementing with general subject knowledge, then verifying every candidate live and applying hard conflict-of-interest exclusions. Trigger whenever the user asks who should review their paper, needs a reviewer list for journal submission, pastes a reference list and wants expert matches, or asks who is active in a subfield, even without the word "reviewer". Also trigger on "who should I suggest?", "find me experts in X", or "I need to submit my paper to [journal], who would be good?". When a reference list is provided, use it as the primary evidence source.
---

# Reviewer Recommender

A skill for recommending peer reviewers for any manuscript. It works by mining
the manuscript's **reference list** for independent domain experts and
supplementing with **general subject knowledge**, then **verifying every
candidate live** (affiliation, current activity) and applying conflict-of-interest
exclusions.

**The governing idea: the best reviewer is someone who has already published on
your topic independently of you.** The reference list reveals exactly who that
is, regardless of field. When references are available, mine them first; general
knowledge fills gaps and adds breadth, less reliably.

> **How candidates are sourced.** This skill has no bundled database of named
> researchers (a curated list of individuals would be third-party personal data).
> Candidates come from the reference list and general knowledge and are always
> verified live, so affiliation/activity flags matter throughout. Full method:
> `references/reviewer-selection-method.md`.

## The one rule that cannot be broken

**Never invent.** Do not fabricate affiliations, infer institutional
relationships you cannot verify, or present a name as a strong match without a
clear basis. When a candidate's current affiliation or activity status is
uncertain, flag it explicitly rather than asserting confidence. A wrong
recommendation wastes the editor's time and reflects on the submitting author.

Placeholder for uncertain information, used verbatim in output:
`[[VERIFY: <what is uncertain, e.g. "current affiliation — may have moved from ETH">]]`

---

## Accepted inputs

More detail gives better results:

| Input | Signal quality |
|-------|---------------|
| Title or topic description only | Baseline |
| Title + target journal | Good |
| Title + journal + author affiliations | Better |
| Any of the above + reference list | Best |

If the user gives only a vague topic with no journal, ask one focused question
before proceeding: "Which journal are you targeting, and is the primary novelty
methodological or biological?" Both answers change the ranking.

---

## Workflow

Read `references/reviewer-selection-method.md` for the full method; the steps below
are the summary.

### Step 1: Parse all inputs
Collect: manuscript info (title, abstract, keywords, or free description); target
journal (ask if not provided); author affiliations (for conflict detection); the
reference list (if provided); and any exclusions the user has already flagged.

### Step 2: Mine the reference list (run first when references are provided)
This is the strongest signal. Identify high-citation anchors, recent key-paper
authors (last 3–5 years), the closest non-collaborator corresponding authors, and
any authors who published in the *same* target journal. Build the conflict
exclusion list at the same time: any author sharing a paper with a submitting
author is a hard exclusion. Produce a ranked reference-derived candidate list.

### Step 3: Supplement with general subject knowledge
Add researchers publicly prominent in the manuscript's specific subfield
(senior/corresponding authors of major reviews or foundational papers, names
recurring across recent key literature). This is a **weaker** signal than
reference-derived candidates. For proteomics/MS and their subfields, general
knowledge is usually good; for an unfamiliar or narrow subfield it is weakest —
say so plainly, and treat the output as a starting point for the author's own
judgement, not a final answer.

### Step 4: Verify every candidate live (required)
For each candidate, confirm they are real and currently active, and web-search
their current affiliation. Flag anything you cannot confirm with
`[[VERIFY: ...]]`. Never present an unverified affiliation as fact.

### Step 5: Score, filter, and apply COI exclusions

| Criterion | Signal | Weight |
|-----------|--------|--------|
| **Reference signal** | Corresponding author on cited papers, especially recent or same-journal | Highest |
| **Topic relevance** | Main area directly overlaps manuscript core topics | High |
| **Journal fit** | Profile matches target journal's editorial expectations | High |
| **Independence** | Not same institution, not in co-author network, not advisor/trainee | Required — disqualifies if absent |
| **Activity** | Published in last 5 years; not so senior that response rate drops | Medium |
| **Balance** | Geographic and gender diversity across the shortlist | Medium |

**Hard exclusions — never recommend:**
- Co-authors on any paper shared with the submitting authors
- Same-lab or same-institution members
- PhD/postdoc advisors or current trainees
- Recent grant co-investigators or other close collaborators without shared authorship, and immediate family or other close personal relationships, when disclosed
- Anyone the user explicitly excludes *for a stated conflict of interest*

If the user's stated reason for excluding someone is that they expect that person
to be critical of the methods or results, rather than a genuine conflict of
interest, decline to add them to the hard-exclusion list on that basis alone —
say plainly that anticipated scientific disagreement is not a conflict of
interest, and that excluding likely-critical reviewers defeats the purpose of
peer review. That concern belongs in the soft-caution list below.

**Soft cautions — flag, do not auto-exclude:**
- Very senior or eminent figures (may decline or be slow to respond)
- Authors of directly competing preprints (note bias risk)
- Authors very heavily cited in the manuscript (may feel pressure to be positive)

**Journal fit in practice.** Reason from the target journal's known editorial
preferences: for methods journals (e.g. Nature Methods), promote method
developers and benchmarking experts even with partial topical overlap; for
clinical journals, promote researchers with cohort/biomarker experience over pure
method specialists; for broad-interest journals (Nature/Science), weight
broad-impact researchers over narrow specialists.

### Step 6: Output
Produce the structure below.

---

## Output structure

```
## Reviewer recommendations for: [manuscript title]
## Target journal: [journal]
## Authors / affiliations: [if provided]

### Core topics identified
[topic 1], [topic 2], [topic 3]

### Journal fit profile applied
[one sentence: what this journal weights most]

### Reference-derived candidates
(only present if a reference list was provided)
- **Name** (Affiliation) — [signal: "corresponding author on 3 cited papers 2022-2024, two in target journal"]  [[VERIFY: affiliation]]

### Primary recommendations (5-8 names)
1. **Name** (Affiliation — [[VERIFY: ...]] if uncertain)
   Source: reference-derived / general knowledge / both
   Match: [specific rationale tied to this manuscript and journal]
   Note: [conflict flag, caution, or VERIFY tag]

### Extended list (4-6 names)
- **Name** (Affiliation) — [brief rationale]

### Exclusion list
- **Name** — [reason: co-author / same institution / advisor / user request]

### Caveats
[standard caveats below]
```

---

## Quality checks before finalizing

- If references were provided, do the primary picks include at least one reference-derived name?
- Does ranking reflect the journal's stated priorities?
- Are all hard exclusions removed (co-authors, same lab, advisors)?
- Is there geographic and gender diversity across the shortlist?
- Have very senior or potentially slow-responding reviewers been deprioritized in favor of active mid-career experts?
- Is **every** name verified live, with `[[VERIFY: ...]]` on any affiliation/activity that could not be confirmed?

---

## Caveats (include in output)

- No curated database backs these suggestions; **every name needs independent verification** of current affiliation and activity before submission. Say this explicitly rather than presenting the output with unwarranted confidence.
- Cross-check all names against the authors' full co-author list and recent shared grants, not just the reference list provided here.
- Tailor the output to the journal's submission form: "suggest reviewers" and "exclude reviewers" are separate fields serving different purposes.
- For an unfamiliar or narrow subfield, general-knowledge-only suggestions are the weakest-confidence output this skill can produce — treat them as a starting point, not a final answer.
