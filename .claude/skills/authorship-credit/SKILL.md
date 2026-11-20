---
name: authorship-credit
description: Decide and document authorship for a scientific manuscript. From a list of people and what each of them did, map every contribution to the 14 CRediT roles, judge each person against the four ICMJE authorship criteria (flagging who qualifies as an author versus who belongs in Acknowledgments), and recommend an author order with rationale. Produces a CRediT author statement, an Author Contributions paragraph, an eligibility table, and acknowledgment wording. Use whenever the user is settling who goes on a paper, in what order, who is corresponding, who gets co-first / equal-contribution, how to write the CRediT / author-contributions section, whether a funder or supervisor or reagent-provider should be an author, or asks anything about ICMJE authorship criteria or CRediT taxonomy. Trigger even when the user just pastes a list of names and jobs and says "sort out authorship" without naming ICMJE or CRediT.
---

# Authorship & CRediT

Turn "here are the people and what they did" into a defensible authorship decision: who is an author, in what order, who is corresponding, what each person's CRediT roles are, and who should instead be acknowledged.

The governing idea: **authorship is a judgment, not a formatting task.** The user is not asking to have a paragraph typed up; they are asking whether each person has earned a byline and where they sit on it. So the primary output is the reasoning and the flags, and the formatted CRediT statement / contributions paragraph are downstream of that. Never silently promote someone into the author list or drop someone out of it. Surface the call and let the user decide.

## The two frameworks this skill runs on

1. **CRediT** (Contributor Roles Taxonomy) is a *descriptive* vocabulary of 14 roles. It records what each person did. It does **not** decide who is an author. A person can hold CRediT roles and still not qualify for authorship. Full role list and how to map fuzzy job descriptions onto it: `references/credit-taxonomy.md`.

2. **ICMJE** is the *gatekeeping* standard. It decides who counts as an author at all, via four criteria that must **all** be met. The crucial, most-often-missed part is that several common contributions (funding, general supervision, admin, providing reagents, language editing) do **not by themselves** confer authorship. The eligibility logic, the four criteria, and the "acknowledge instead" fallback: `references/icmje-and-eligibility.md`.

Keep them separate in your head: CRediT answers *what did they do*, ICMJE answers *does that make them an author*. Read both reference files before doing the assessment. The user's pasted journal wording (often Elsevier's phrasing) is a restatement of ICMJE; treat the canonical four criteria as authoritative.

## Intake

You need, per person: a **name** and a **description of what they did**. Everything else you can flag or ask for. Before assessing, make sure you also know (ask briefly only for what is missing and actually matters):

- **Target journal / field**, if known. This sets the house style for the CRediT statement and the ordering convention (life-sciences default: first author = lead, last author = senior/PI). If unknown, use the life-sciences default and say so.
- **Who, if anyone, is the intended corresponding author** and who is the senior/PI. Often the user already knows.
- **Any intended equal-contribution (co-first / co-senior) groupings**, or a note that this is open.
- **Whether the list is exhaustive** — ask whether everyone who contributed is on the list, not only whether anyone on the list should come off it. Silent omission of a real contributor (a departed student, a collaborator dropped without discussion) is the more common real-world path to ghost authorship than an explicit request to exclude someone whose contribution was just described.

Do not force a long questionnaire. If the user pasted names and jobs and said "sort this out," proceed with sensible defaults and state each assumption inline. Prefer the tappable-options tool over prose questions if you do need to ask.

Handle input in whatever language the user uses (Chinese and English are both common here) and produce the deliverables in that language, keeping the canonical CRediT role labels in English as journals require them.

## Workflow

Work through these in order. The first three are the substance; the last is formatting.

**1. Map each person to CRediT roles.** Using `references/credit-taxonomy.md`, translate each free-text job description into specific CRediT roles. Where the description supports it, mark degree of contribution as **lead / equal / supporting** (CRediT permits this). If a description is too vague to map confidently (e.g. "helped with the project"), do not invent roles; flag it and ask what specifically they did. Never assign a role the description does not support.

**2. Assess ICMJE eligibility per person.** Using `references/icmje-and-eligibility.md`, evaluate all four criteria for each person and classify them into one of:
   - **Author (meets all four)** — proceed.
   - **Author-eligible but incomplete** — did substantial work (criterion 1) but the input does not show drafting/revising (criterion 2) or final approval (criterion 3). The correct fix is almost never exclusion; it is to *give them the opportunity* to review and approve. Say this explicitly rather than dropping them.
   - **Acknowledge, not author** — their only contributions are ones that do not qualify on their own (funding, general supervision, general admin, reagent/sample provision, language/technical editing). Flag clearly, explain why, and route them to Acknowledgments with suggested wording.
   - **Needs input** — description too thin to judge.

   State, per person, which of the four criteria are met and which are not. This table is the heart of the output.

**3. Recommend author order.** Using `references/author-ordering.md`, propose an order with a one-line rationale per position. Identify: first author (and any co-first / equal-contribution group), the middle-author sequence (descending contribution), the senior/last author, and the corresponding author(s). Ordering is partly a social and negotiated decision, so present it as a recommendation, note where reasonable people could order differently, and flag genuine contests (e.g. two plausible co-first authors) for the authors to settle. Do not present a contested order as if it were determined by rule.

**4. Produce the deliverables.** Read `assets/output-template.md` for exact formats, and generate the set below.

## Output package

Deliver these, adapting to what the user asked for:

1. **Eligibility table** — one row per person: proposed position, CRediT roles (with lead/equal/supporting), which ICMJE criteria are met (1/2/3/4), and a status (author / incomplete / acknowledge / needs-input) with a short note. This is the primary artifact; lead with it.
2. **Recommended author order** — the ordered byline with a one-line rationale per position, corresponding author(s) marked, equal-contribution groups marked, and any contested calls flagged for the authors.
3. **CRediT author statement** — the journal-ready statement, one entry per author: `Name: Role, Role, Role.` using exact CRediT labels. Format per `assets/output-template.md`.
4. **Author Contributions paragraph** — the same information in prose, the form many journals print. Keep it faithful to the CRediT mapping; do not embellish.
5. **Acknowledgments wording** — for everyone routed out of the author list, suggested acknowledgment sentences (funding, supervision, materials, editing), so no real contribution silently disappears.

If the user only wants one of these (e.g. "just give me the CRediT statement"), give that, but still surface any eligibility red flag you found rather than formatting a list you believe is wrong.

## Rules that do not bend

- **Never fabricate a contribution, role, affiliation, or that someone approved the manuscript.** If the input does not establish something an author byline requires, flag it with an explicit placeholder rather than assuming it. Use: `[[NEEDS INPUT: <what is missing, e.g. "did X draft or review the manuscript?">]]`.
- **Never silently change who is on the paper.** Adding an author, dropping an author, or reordering are decisions you *recommend and justify*, never ones you make quietly inside a formatted paragraph.
- **CRediT roles do not equal authorship.** Holding a role, even several, does not by itself satisfy ICMJE. Keep the two judgments distinct.
- **Funding, general supervision, general administration, reagent/sample provision, and language/technical editing do not on their own justify authorship.** This is the single most common error; apply it every time, and route such contributors to Acknowledgments unless they also have a qualifying intellectual contribution.
- **Order is a recommendation.** Especially for co-first, co-corresponding, and last-author calls, present the reasoning and let the authors decide; do not manufacture false certainty.

## Ethics note to carry into the conversation

Gift authorship (adding someone who did not qualify, e.g. a department head) and ghost authorship (omitting someone who did qualify, e.g. a departed student or a medical writer) are both research-integrity violations, not stylistic choices. If the user's framing points toward either, say so plainly and kindly, and hold the ICMJE line while explaining the reasoning. The goal is a byline the authors could defend to an editor or an integrity committee.
