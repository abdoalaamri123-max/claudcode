# Meta-analysis & Systematic Review Skill

**🌐 English | [简体中文](./README.md)**

> A **Meta-analysis / Systematic Review (+ PRISMA)** methodology skill for **Claude Code / Claude Agent**. It solves one thing: **how to produce a transparent, reproducible systematic review with PRISMA and, when studies are homogeneous enough, statistically pool their quantitative results into an overall effect via meta-analysis.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Lang](https://img.shields.io/badge/lang-中文%20|%20English-blue)
![Type](https://img.shields.io/badge/Claude-Skill-8A2BE2)
![Tool](https://img.shields.io/badge/R-metafor%20|%20CMA%20|%20RevMan-orange)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> Core stance: **a systematic review is a reproducible evidence-synthesis process (PRISMA); a meta-analysis is the statistical pooling on top of it, only when studies are homogeneous enough. Not every systematic review can or should be a meta-analysis.**

---

## ✨ What it is / the pain it solves

Meta-analysis is a hot but error-prone area. Common failures:

- Calling "I read a lot of papers" a **meta-analysis** without a systematic search;
- **Pooling overly heterogeneous studies** (apples and oranges) into a meaningless overall effect;
- **Wrong fixed/random-effects choice** — mechanically by "is I² significant" instead of conceptual homogeneity;
- **Reading only I²**, ignoring τ² and the prediction interval (I² is not an absolute measure of heterogeneity);
- **Skipping publication-bias tests**, inflating the pooled effect;
- Not **pre-registering**, not attaching the **search string and PRISMA flow diagram** — irreproducible.

Every stage ships decision criteria, formulas, software commands, reporting standards, and reusable templates.

## 🆚 vs other quantitative skills

| | Questionnaire / PROCESS / AMOS-SEM | Sample size & power | This · Meta-analysis |
| --- | --- | --- | --- |
| Analyzes | a **single study's** data | a single study's design | **many studies'** evidence synthesis |
| Product | reliability/mediation/SEM | required sample size | pooled effect + heterogeneity + bias |
| Unique | α, EFA/CFA, bootstrap | power analysis | PRISMA, effect-size pooling, I²/τ², forest plot, publication bias |

## 📂 Structure

```
meta-analysis-systematic-review/
├── SKILL.md
├── references/ 00–11 (should-you-use, question & protocol, search strategy, PRISMA & screening,
│                data extraction, effect sizes, fixed vs random, heterogeneity, publication bias,
│                quality & risk of bias, software & reporting, case library)
├── diagrams/meta-analysis-flow.md   # Mermaid
├── templates/ (PICO protocol, PRISMA flow, extraction sheet, reporting checklist)
└── README.md / README.en.md / LICENSE
```

## 🚀 Install

**macOS / Linux**
```bash
git clone https://github.com/maydengximin-sketch/meta-analysis-systematic-review-skill.git \
  ~/.claude/skills/meta-analysis-systematic-review
```

**Windows (PowerShell)**
```powershell
git clone https://github.com/maydengximin-sketch/meta-analysis-systematic-review-skill.git "$env:USERPROFILE\.claude\skills\meta-analysis-systematic-review"
```

Then ask Claude (e.g. "can these studies be meta-analyzed?", "which effect size?", "fixed or random effects?", "I² is high — subgroup or meta-regression?", "how do I check publication bias?", "how do I run metafor / read a forest plot?").

## 🎯 Seven core principles
1. **Distinguish review types** — narrative / systematic / meta-analysis.
2. **Poolability depends on homogeneity** — don't force apples and oranges.
3. **Pre-registration + PRISMA = reproducibility.**
4. **Dual independent screening and extraction.**
5. **Right effect size, unified direction, correct variance.**
6. **Default random effects + report heterogeneity** (I²/τ²/prediction interval).
7. **Always test publication bias + risk of bias.**

## 📚 Key sources

Borenstein et al. (2021); Page et al. (2021, PRISMA 2020); Cochrane Handbook (2023); Viechtbauer (2010, metafor); Harrer et al. (2021); Egger et al. (1997); Higgins & Thompson (2002).

## ⚠️ Disclaimer

A methodological aid — it does not replace your statistical judgment, supervisor, or reporting standards (PRISMA, Cochrane). All results must come from **your own systematic search and data**; numbers in the cases are illustrative fictional values. Pooled and bias-corrected conclusions depend heavily on the quality of included studies.

## 📄 License

[MIT](./LICENSE).

---

> ⭐ Star / 🍴 Fork / share it with fellow evidence synthesizers — it all helps.
