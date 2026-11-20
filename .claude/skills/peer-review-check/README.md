# peer-review-check

A [Claude Code / Agent SDK skill](https://docs.claude.com/en/docs/claude-code/skills) that
does an **author self-check** of a manuscript draft against Elsevier's official
[*Structured peer review prompts*](https://www.elsevier.com/) (April 2026), before you submit.

Instead of waiting for reviewers to tell you what's missing, it pre-empts them: it reads your
draft, detects the article type, and runs one focused sub-reviewer per manuscript section, each
answering the exact Elsevier prompt a real reviewer will be asked. It then synthesises a
**severity-ranked gap list** and a submission-readiness verdict.

## What you get

For every Elsevier prompt, the report tells you:

- **Verdict** — pass / minor gap / major gap
- **What your draft has** — the specific evidence, cited from your manuscript
- **What a reviewer would object to**
- **The concrete fix** to make before submitting

Ranked most-likely-objection first, with a short "already passes" list so you know what not to touch.

## Coverage

Follows Elsevier's two prompt sets verbatim:

- **Original research articles** — Abstract, Introduction, Methods, Results, Discussion, References, Overall (novelty + ethics/integrity), and Title.
- **Review articles** — Overall relevance, Historical development, References, Methods & reproducibility, Statistical analyses, Essential reporting (PRISMA), Language quality.

Non-applicable prompts (e.g. MCID for a non-clinical paper) are marked pass rather than invented as problems.

## Install

Clone into your skills directory:

```bash
git clone https://github.com/narcoco/peer-review-check.git ~/.claude/skills/peer-review-check
```

## Use

Point the assistant at a draft (PDF, `.docx`, or `.md`/`.tex`) and ask any of:

- `/peer-review-check`
- "check my paper before submission"
- "is my manuscript submission-ready"
- "will this pass review"

## How it works

- **Multi-agent deep review**: one sub-reviewer per section runs in parallel, each scoped to its
  Elsevier prompt, then results are synthesised into one report.
- Reads the actual manuscript before flagging anything — every gap cites real text.
- Frames output as self-check ("a reviewer will object to X, here's how to close it"), not a
  referee report to send to a journal.

## Files

- `SKILL.md` — the skill definition and flow.
- `references/elsevier-prompts.md` — the Elsevier prompt tables, verbatim, for both article types.

## Attribution

The peer review prompts are Elsevier's *Structured peer review prompts* (April 2026), reproduced
for author self-checking. This skill is an independent tool and is not affiliated with or endorsed
by Elsevier.

## License

MIT
