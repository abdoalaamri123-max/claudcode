---
name: peer-review-check
description: Author self-check of a manuscript draft against Elsevier's official structured peer review prompts (April 2026), before submission. Fans out one sub-reviewer per manuscript section, then synthesises a severity-ranked gap list — for each prompt a reviewer will answer, what your draft has and the concrete fix — plus a submission-readiness verdict. Trigger on "/peer-review-check", "check my paper before submission", "is my manuscript submission-ready", "peer review self check", "structured peer review", "will this pass review", "run the Elsevier prompts on my draft", or when Angela hands over her own manuscript draft and asks whether it would survive peer review.
---

# Peer review check: author self-check against Elsevier prompts

Angela hands over **her own manuscript draft**. This skill checks it, section by section,
against Elsevier's official *Structured peer review prompts* (April 2026) and returns a
**gap list**: for each prompt a reviewer will be asked to answer, whether the draft satisfies
it, and if not, the exact fix. The point is to catch every reviewer objection before she
submits, not to referee someone else's paper.

Depth is **multi-agent deep**: one sub-reviewer per manuscript section runs in parallel, each
focused on its Elsevier prompt, then results are synthesised into one ranked report.

The full prompt tables (both article types) live in `references/elsevier-prompts.md`. Read that
file at the start of every run.

## Flow

### 1. Locate and read the manuscript

- If Angela gave a path, use it. Otherwise ask for the file (PDF, .docx, or .md/.tex).
- Read the whole thing:
  - `.md` / `.tex` / `.txt` → Read directly.
  - `.pdf` → Read via the `pages` parameter (whole document).
  - `.docx` → convert with the `markitdown` skill or `pandoc`, then read.
- Do not review from the abstract or memory alone. **Read the source first** (OPUS hard rule 3):
  every gap you report must cite something actually in the manuscript.

### 2. Detect the article type, confirm in one line

Decide **original research** vs **review article** (the two tables in the reference file).
Signals: a Methods/Results with new data and a study design → original research; a synthesis of
the field with search strategy / PRISMA / meta-analysis → review article. State the call in one
line and proceed; only pause if genuinely ambiguous.

### 3. Fan out one sub-reviewer per section (parallel)

For the detected article type, launch a general-purpose Agent per row in that table (Abstract,
Introduction, Methods, ... for original research; Overall relevance, Historical development, ...
for review). Launch them **in a single message** so they run concurrently. Give each agent:

- the manuscript file path (it reads the file itself),
- its section name and the **exact Elsevier prompt text** for that section,
- this instruction: *"You are pre-empting a peer reviewer who will answer this prompt about
  Angela's own draft. Judge whether the manuscript would satisfy that reviewer. Return, as a
  compact structured list: (a) verdict — PASS / MINOR GAP / MAJOR GAP; (b) evidence — quote or
  cite the specific place in the manuscript, with section/page; (c) what a reviewer would object
  to; (d) the concrete fix Angela should make before submitting. Only flag what is genuinely
  missing or weak. Do not invent problems, do not praise. If the prompt asks for something not
  applicable to this study (e.g. MCID for a non-clinical paper), say so and mark PASS."*

Always include the **Overall** (integrity/novelty) and **Title** prompts for original research;
always include **Language quality** and **Essential reporting** for review articles.

### 4. Synthesise the gap list

Collect all sub-reviewer returns into one report. Structure:

1. **Verdict line** — submission-ready / minor revisions needed / major gaps before submitting.
2. **Major gaps** first, then **minor gaps**, each as:
   - *Section* (Elsevier prompt it maps to)
   - *What the prompt asks*
   - *What your draft has* (the evidence the sub-reviewer found)
   - *Fix* (specific, actionable)
3. **Passed** — a short list of prompts the draft already satisfies, so she knows what not to touch.

Rank by how likely each gap is to draw a reviewer objection. Keep it scannable. Follow Angela's
style rules: sentence-case headings, no em dashes, no "not X but Y" construction.

### 5. Save and state the path

Save the report as Markdown **next to the manuscript** by default:
`<manuscript-dir>/<manuscript-name>_peer-review-check.md`. If the manuscript is inside the Research
vault or OneDrive, keep it there; do not move it. **Always state the absolute save path and whether
it is in the Obsidian vault or OneDrive** (OPUS hard rule 4). Then give a 3-5 line summary in chat:
verdict + the top gaps.

## Notes

- This is self-check, so frame everything as "before you submit, a reviewer will say X — here is
  how to close it." Not a referee report to send to a journal.
- If Angela instead wants to referee **someone else's** manuscript, or wants a full simulated
  multi-reviewer panel, route to the `academic-paper-reviewer` skill.
- The reference file is verbatim Elsevier text — do not paraphrase the prompts when handing them
  to sub-reviewers; a reviewer will answer the exact wording.
