---
name: review-simulator
description: Simulates the journal review of a submission and produces one report containing an editor desk assessment and 2 to 3 independent reviewer reports. Given the submission materials and the target journal, it first runs a desk review (aims and scope fit, novelty and importance against the journal's bar, plausibility of methods and conclusions, compliance and completeness) with a send-out or desk-reject call, then writes distinct reviewer reports (overall assessment, numbered major and minor comments, and a recommendation), and an editor synthesis weighing them by argument quality. It is a pre-submission dry run grounded in the manuscript, clearly labeled as a simulation, and it never fabricates data or external facts. Use whenever the user wants to simulate or mock peer review, see what an editor or reviewers would say, get a desk-review or reviewer-style critique, or stress-test a paper before submitting.
---

# Review Simulator

Simulate the review a submission would receive and return a single report with two voices: an **editor's desk assessment** and **2 to 3 reviewer reports**, plus a short editor synthesis. It is a **pre-submission stress test, run before the first submission**, on the manuscript, its figures and tables, or the overall results storyline, to help the author find weaknesses before real reviewers do.

## Framing and the one rule

This is a **simulation to help the author**, not a real editorial decision, and the report says so. Ground every judgment in the actual manuscript. **Never fabricate**: do not invent data, results, or specific external facts (for example that a particular paper contradicts the work). Internal soundness, clarity, method completeness, over-claiming, and consistency are all judgeable from the manuscript; for novelty and field-context claims that need external evidence, flag them for the author to verify (or point to `citation-auditor`) rather than asserting invented prior work. If the target subfield is outside grounded knowledge, say so explicitly rather than presenting novelty or competitive-landscape judgments with unwarranted confidence. Keep the tone constructive, specific, and evidence-based.

## Inputs

- **The submission materials.** Required: the manuscript; plus any supplementary files (figures, tables, supplementary methods/data), and the cover letter if available. Read PDFs with the `pdf-reading` skill and Word files with the `docx` skill.
- **The target journal. Required.** Ask the user for it before proceeding if it is not given, because scope fit, the novelty and importance bar, and the interdisciplinary-readership expectation all depend on the specific journal. Use its aims and scope to calibrate the review.

## Two roles

- **Editor (desk review):** the triage decision, whether the paper should be sent out or desk-rejected. Read `references/editor-deskreview.md`.
- **Reviewers (peer review):** deep assessment of the science, 2 to 3 independent reports with differing emphases. Read `references/reviewer-review.md`.

## Workflow

1. **Ingest** the materials and identify the target journal and its bar.
2. **Editor desk review:** assess aims and scope fit, novelty and importance against the journal's threshold (the decisive gate for high-impact journals), first-pass plausibility of methods and conclusions, and compliance and completeness (ethics, data availability, competing interests, format, and image integrity where visible). Reach a desk decision: desk-reject (with clear reasons) or send for review. Note that a fast, honest desk-reject respects the author's time.
3. **Reviewer reports (2 to 3):** for each simulated reviewer, first read for the whole (is the question important, the claim novel, the conclusions supported, the work credible and a fit), then assess against the five evaluation criteria (originality, scientific importance, interdisciplinary readership, technical soundness, readability) using the eight dimensions in `references/reviewer-review.md`. Central to technical soundness is whether the scientific argument holds up: is anything overclaimed, are the statistical methods appropriate, and is every conclusion supported by the data. Write an overall assessment, numbered Major and Minor comments, and a recommendation. Give the reviewers slightly different emphases so the panel reads realistically, not three copies of one review.
4. **Editor synthesis:** weigh the reviews by the quality of their reasoning, not by vote count; reconcile conflicts; list the prioritized must-fix issues; and give an overall simulated decision (accept / minor revision / major revision / reject).
5. **Assemble** the report from `assets/review-report.md`.

## Output

One report (template in `assets/review-report.md`) with: a simulation disclaimer; the editor desk assessment and send-out/desk-reject call; 2 to 3 reviewer reports (overall, Major, Minor, recommendation); and the editor synthesis and overall decision. Each comment is specific, located, and marked must-fix versus suggestion. Tag each issue by type where it applies: **unsupported claim**, **technical flaw**, **evidence-chain gap** (a break between data, result, and conclusion), or a **readability barrier for non-specialist readers**. Flag anything needing external verification with `[[VERIFY: ...]]`.

## Relationship to sister skills

- `journal-submission-checklist` — for an authoritative, evidence-quoted compliance verdict against a specific publisher-family form or reporting guideline (NP/MCP/CP, CONSORT/STROBE/ARRIVE/PRISMA). This skill's desk-review compliance-and-completeness read (step 2) is a first-pass impression from a simulated editor's perspective, not a substitute for that depth — where the two disagree on a compliance item, `journal-submission-checklist`'s evidence-quoted verdict governs.
- `submission-screener` — the general pre-submission QC pass; this skill is the deep version of its Pass 8 light scientific-soundness catch-net.
- `statistical-rigor-helper` — for the specific statistical mechanism behind a "the statistics don't support this claim" finding.
- `citation-auditor` — for verifying whether a specific external fact or competing claim raised in a reviewer comment is real.

## Principles (applied throughout)

Disagree with evidence, not attitude; note strengths as well as problems; match the depth of a comment to the severity of the issue; do not rewrite the paper into how you would have written it; say when you are unsure; keep each reviewer's comments consistent with its recommendation; judge major comments by accuracy, reproducibility, and scientificity, and calibrate novelty to the target journal's bar. Be professionally courteous. Avoid empty verdicts like "not novel enough" or "poorly written" without specific, actionable reasons, which help neither the editor nor the author. Confidentiality and conflict-of-interest norms are part of the framing the report models. If asked to soften a verdict, guarantee acceptance, or make the report more reassuring than the manuscript warrants, decline: the simulation's whole value is surfacing exactly what a real reviewer would catch, so keep every recommendation and severity label evidence-based regardless of the request.
