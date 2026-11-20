# Reviewer-selection method (no named-person database)

Read this for the full method behind `SKILL.md`. This skill does **not** ship a
curated list of named individuals; it derives reviewer candidates from the
manuscript's own reference list plus general subject knowledge, and verifies
everything live. The governing idea: **the best reviewer is someone who has
already published on your topic, independently of you — and the reference list is
the most reliable place to find that person.**

## Why reference-list mining is the primary signal

A manuscript's reference list is a pre-filtered set of researchers who work on
the exact problem, chosen by the authors themselves. Mining it is more reliable
than recalling names from memory, works in every field equally, and yields
candidates whose relevance is demonstrable (you can point to the cited paper).
Always mine the reference list first when one is available.

## Step-by-step

### 1. Extract candidate authors from the reference list

- **High-citation anchors.** Corresponding/senior authors of the foundational or
  most-cited references are domain authorities and strong candidates *if
  independent* of the submitting team.
- **Recent key papers (last 3–5 years).** Authors publishing recently on adjacent
  problems give timely, informed reviews and accept more often.
- **Closest non-collaborator authors.** Among corresponding authors in the list,
  find those whose work most resembles the manuscript's core contribution but who
  share no co-authorship with the submitting team — the highest-priority picks:
  expertise demonstrated, conflict absent.
- **Target-journal correspondents.** Reference-list authors who published in the
  *same* target journal know its standards and have cleared its bar.

### 2. Supplement with general subject knowledge

Where the reference list is thin, or to add breadth, add researchers publicly
prominent in the manuscript's specific subfield (senior/corresponding authors of
major reviews or foundational papers, names recurring across recent key
literature). Treat this as a **weaker** signal than reference-derived candidates,
because it is not anchored to a specific cited paper. For proteomics, mass
spectrometry, and their subfields (DIA, single-cell, spatial, clinical/
translational, PTMs, plasma, computational, top-down, glycoproteomics,
structural, cross-linked MS), general knowledge of the field is usually good; for
an unfamiliar or very narrow subfield it is weakest — say so.

### 3. Verify every candidate live (required)

Because no curated database backs these names, **every** suggested candidate must
be verified before it reaches the user:

- Confirm the person is real and currently active (recent publications).
- Confirm their current affiliation by web search; if uncertain, flag it with the
  placeholder rather than asserting it:
  `[[VERIFY: current affiliation — could not confirm; last seen at <X>]]`.
- Never present a name as a strong match without a concrete basis (a specific
  cited paper, or a clearly relevant recent body of work).

### 4. Apply conflict-of-interest exclusions (both directions)

**Hard exclusions — never recommend:**
- Co-authors on any paper shared with the submitting authors.
- Same-lab or same-institution members.
- PhD/postdoc advisors or current trainees of the authors.
- Recent grant co-investigators / other close collaborators without shared
  authorship, and immediate family or other close personal relationships, when
  disclosed.
- Anyone the user explicitly excludes **for a stated conflict of interest**.

If the user's stated reason for excluding someone is that they expect that person
to be *critical* of the methods or results, rather than a genuine conflict of
interest, do **not** add them to the hard-exclusion list on that basis alone —
say plainly that anticipated scientific disagreement is not a conflict of
interest, and that excluding likely-critical reviewers defeats the purpose of
peer review. That concern belongs in the soft-caution list below.

**Soft cautions — flag, do not auto-exclude:**
- Very senior/eminent figures (may decline or respond slowly).
- Authors of directly competing preprints (note bias risk).
- Authors very heavily cited in the manuscript (may feel pressure to be positive).

### 5. Score and rank

| Criterion | Signal | Weight |
|-----------|--------|--------|
| **Reference signal** | Corresponding author on cited papers, especially recent or same-journal | Highest |
| **Topic relevance** | Main area directly overlaps the manuscript's core topics | High |
| **Journal fit** | Profile matches the target journal's editorial expectations (methods-heavy vs. broad-impact vs. clinical/translational) | High |
| **Independence** | Not same institution, not in co-author network, not advisor/trainee | Required — disqualifies if absent |
| **Activity** | Published in the last ~5 years; not so senior that response rate drops | Medium |
| **Balance** | Geographic and gender diversity across the shortlist | Medium |

Reason about the target journal's known editorial preferences from general
knowledge (methods journals reward method developers and benchmarking experts;
clinical journals reward cohort/biomarker experience; broad-interest journals
reward broad-impact researchers) rather than a per-journal weighting table.

## The one rule

Never invent a person, affiliation, or institutional relationship. When a
candidate's current affiliation or activity status is uncertain, flag it with
`[[VERIFY: ...]]` rather than asserting confidence. A wrong recommendation wastes
the editor's time and reflects on the submitting author.
