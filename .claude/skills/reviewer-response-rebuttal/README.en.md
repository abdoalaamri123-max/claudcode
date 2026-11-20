# Response to Reviewers / Rebuttal Skill

**🌐 English | [简体中文](./README.md)**

> A **Response to Reviewers / Rebuttal** skill for **Claude Code / Claude Agent**. It solves the most anxiety-inducing step for authors: **after a major/minor revision decision, how to write a point-by-point response letter that satisfies editors and reviewers and turns an R&R into an acceptance.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Lang](https://img.shields.io/badge/lang-中文%20|%20English-blue)
![Type](https://img.shields.io/badge/Claude-Skill-8A2BE2)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> Core stance: **a revision is not "just fix it" — it's re-persuasion. Every reply must let the reviewer see, without opening the manuscript: comment → what you did → the revised text (page/line).**

---

## ✨ What it is / the pain it solves

After a major/minor revision, authors get stuck on:
- Not reading the decision letter well — **can't tell hard requirements from suggestions**, miss the deal-breakers;
- Point-by-point replies with no structure — "revised" and nothing else, reviewers can't find the change;
- One comment they **disagree** with — either combatively pushing back or caving entirely;
- **Conflicting reviewers** — only daring to follow one;
- Tone either **too meek or too aggressive**;
- Reply says "revised" but the manuscript **doesn't match** — bounced on resubmission.

Every stage ships decision criteria, good/bad examples, bilingual phrases, and reusable templates.

## 🆚 vs the ssci-writing skill

| | ssci-writing skill | This · Response skill |
| --- | --- | --- |
| Stage | **before** submission (journal choice, gap, IMRaD, writing) | **after** submission (decision letter → resubmit) |
| Product | a submittable manuscript | a response letter that turns R&R into acceptance |
| Unique | desk-reject avoidance, hypotheses, structure | decision-letter parsing, three-part replies, push-back/conflict handling, cover letter, phrase bank |

> Chain them: **ssci-writing to write and submit; this skill to catch the reviews and revise back.**

## 📂 Structure

```
reviewer-response-rebuttal/
├── SKILL.md
├── references/ 00–11 (mindset & triage, decision-letter anatomy, response structure,
│                point-by-point, tone & diplomacy, agreeing & revising, disagreeing respectfully,
│                conflicting reviewers, request types, cover letter, resubmission checklist, phrase bank & cases)
├── diagrams/rebuttal-flow.md   # Mermaid
├── templates/ (response letter, point-by-point table, cover letter, phrase bank)
└── README.md / README.en.md / LICENSE
```

## 🚀 Install

**macOS / Linux**
```bash
git clone https://github.com/maydengximin-sketch/reviewer-response-rebuttal-skill.git \
  ~/.claude/skills/reviewer-response-rebuttal
```

**Windows (PowerShell)**
```powershell
git clone https://github.com/maydengximin-sketch/reviewer-response-rebuttal-skill.git "$env:USERPROFILE\.claude\skills\reviewer-response-rebuttal"
```

Then paste your decision letter / reviewer comments and ask Claude (e.g. "triage these comments into a checklist", "draft point-by-point replies", "help me push back politely on one comment", "the two reviewers conflict — what now?", "write the cover letter", "check my replies match the revised manuscript").

## 🎯 Seven core principles
1. **Never skip a comment** — each gets its own numbered reply.
2. **Zero-cost verification** — quote revised text + page/line.
3. **Thank, respond, locate** — the three-part reply.
4. **Revise when you can; justify with evidence when you can't.**
5. **Confident but respectful** — grateful not fawning, firm not combative.
6. **Surface conflicts** — defer to the editor, don't secretly follow one.
7. **Verifiable and traceable** — replies map exactly to the revised manuscript.

## 📚 Key sources

Noble (2017), *PLoS Comput Biol*; Annesley (2011), *Clinical Chemistry*; Williams (2004), *JAAD*.

## ⚠️ Disclaimer

A writing/workflow aid — it does not replace your academic judgment, supervisor, or the journal's policies. All content must be grounded in **your own manuscript and real revisions**; templates and phrases are scaffolding only. Never claim analyses or results you did not actually perform.

## 📄 License

[MIT](./LICENSE).

---

> ⭐ Star / 🍴 Fork / share it with anyone waiting on reviews — it all helps.
