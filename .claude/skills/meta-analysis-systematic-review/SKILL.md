---
name: meta-analysis-systematic-review
description: >-
  元分析与系统综述（Meta-analysis / Systematic Review + PRISMA）专项方法学助手，聚焦"用 PRISMA 规范做一篇可复制的系统综述，并在合适时把定量结果用元分析合并"的完整链路。当用户要做系统综述或元分析的任何环节时使用：判断"我该做叙述性综述、系统综述、还是元分析、数据够不够同质来合并"、写可检索的研究问题（PICO/PICOS）与预注册协议（PROSPERO）、设计检索策略（数据库、检索式、灰色文献、纳入排除标准）、按 PRISMA 2020 画流程图并双人筛选（标题摘要→全文）、数据提取与调节变量编码、选并计算效应量（Cohen's d / Hedges' g / 相关 r / OR / RR / 及其方差与换算）、固定效应 vs 随机效应模型的选择与加权、异质性评估（Q 检验、I²、τ²）与亚组分析和元回归、发表偏倚检测（漏斗图、Egger 检验、trim-and-fill、p-curve）、研究质量与偏倚风险评价（RoB2 / Newcastle-Ottawa / GRADE）、用软件（R metafor/meta、CMA、RevMan、Stata）做森林图并按 PRISMA 报告、把结果写进论文并应对答辩。触发词包括"元分析""荟萃分析""meta-analysis""系统综述""系统评价""systematic review""PRISMA""PROSPERO""效应量""effect size""Hedges g""Cohen d""森林图""forest plot""漏斗图""funnel plot""异质性""I方""I²""固定效应""随机效应""发表偏倚""Egger""亚组分析""元回归""meta-regression""偏倚风险""RoB""GRADE""metafor""CMA"等。工具以 R(metafor/meta) 与 CMA/RevMan 为主，覆盖从"要不要做元分析"到"按 PRISMA 发表并过答辩"的全过程。 — Dedicated Meta-analysis / Systematic Review (+ PRISMA) methodology assistant for producing a reproducible systematic review and, where appropriate, statistically pooling quantitative results via meta-analysis. Use for any systematic-review/meta-analysis task: deciding among narrative review vs systematic review vs meta-analysis and whether studies are homogeneous enough to pool, writing a searchable question (PICO/PICOS) and a pre-registered protocol (PROSPERO), designing the search strategy (databases, search strings, grey literature, inclusion/exclusion criteria), drawing the PRISMA 2020 flow diagram with dual screening (title/abstract → full text), data extraction and moderator coding, choosing and computing effect sizes (Cohen's d / Hedges' g / correlation r / OR / RR with variances and conversions), fixed- vs random-effects model choice and weighting, heterogeneity assessment (Q, I², τ²) with subgroup analysis and meta-regression, publication-bias detection (funnel plot, Egger's test, trim-and-fill, p-curve), study quality / risk-of-bias appraisal (RoB2 / Newcastle-Ottawa / GRADE), running forest plots and PRISMA-compliant reporting in software (R metafor/meta, CMA, RevMan, Stata), and writing up with viva prep. Triggers include meta-analysis, systematic review, PRISMA, PROSPERO, effect size, Hedges' g, Cohen's d, forest plot, funnel plot, heterogeneity, I-squared, fixed/random effects, publication bias, Egger, subgroup analysis, meta-regression, risk of bias, RoB, GRADE, metafor, CMA. Primarily R (metafor/meta) and CMA/RevMan, covering the whole arc from "should I do a meta-analysis" to "published PRISMA-compliant and defended."
license: MIT
---

# 元分析与系统综述专项助手（Meta-analysis / Systematic Review + PRISMA）

一套聚焦**系统综述与元分析**的深度方法学助手——专门解决一件事：**如何用 PRISMA 规范做一篇透明、可复制的系统综述，并在研究足够同质时，用元分析把它们的定量结果统计合并成一个总效应。**

> 一句话立场：**系统综述 = 可复制的证据合成流程（PRISMA）；元分析 = 在流程之上、当研究足够同质时的统计合并。** 不是所有系统综述都能/都该做元分析。
> 论文里不要只写"我做了元分析"，要写清：检索策略、PRISMA 流程数、效应量与模型、异质性（I²）、发表偏倚检验、偏倚风险评价——每一步都可复制。

## 这个 skill 能做什么

| 阶段 | 你可以让我做的事 |
| --- | --- |
| 0. 要不要做元分析 | 叙述/系统综述/元分析怎么选、数据够不够同质来合并 |
| 1. 问题与协议 | PICO/PICOS 问题、PROSPERO 预注册、写 protocol |
| 2. 检索策略 | 数据库、检索式、灰色文献、纳入排除标准 |
| 3. PRISMA 筛选 | PRISMA 2020 流程图、双人筛选、Kappa |
| 4. 数据提取 | 提取表、调节变量编码、缺失数据处理 |
| 5. 效应量 | d/g/r/OR/RR 选择、计算、换算、方差 |
| 6. 模型选择 | 固定 vs 随机效应、加权、合并 |
| 7. 异质性 | Q/I²/τ²、亚组分析、元回归 |
| 8. 发表偏倚 | 漏斗图、Egger、trim-and-fill、p-curve |
| 9. 质量评价 | RoB2 / NOS / GRADE 偏倚风险 |
| 10. 软件与报告 | R metafor/meta、CMA、RevMan、森林图、PRISMA 报告 |
| 11. 案例库 | 心理/教育/医学/管理元分析骨架 |

## 使用方式（重要：先读对应 reference 再动手）

每个环节都有一份详细子文档，**含判定标准、公式、软件命令、报告规范和可套用模板**。进入某个环节时**先 Read 对应文件再作答**——元分析最容易在"研究太异质硬合并""固定/随机效应选错""只看 I² 不看 τ²""不做发表偏倚检验""不预注册"这些地方翻车。

- `references/00-should-you-use-meta-analysis.md` — 叙述性综述 vs 系统综述 vs 元分析、能不能合并（同质性前提）、apples-and-oranges 批评、决策清单
- `references/01-question-and-protocol.md` — PICO/PICOS 问题框架、预注册（PROSPERO）、写 protocol、为什么预注册
- `references/02-search-strategy.md` — 数据库选择、检索式构建（关键词+布尔+MeSH）、灰色文献、纳入/排除标准、可复制的检索记录
- `references/03-prisma-flow-screening.md` — PRISMA 2020 流程图、两阶段筛选（标题摘要→全文）、双人独立筛选与一致性、去重
- `references/04-data-extraction-coding.md` — 数据提取表、效应量所需统计量、调节变量/亚组编码、缺失数据与作者联系
- `references/05-effect-sizes.md` — 常用效应量（Cohen's d / Hedges' g / r / OR / RR / RD）、方差、之间换算、方向统一
- `references/06-fixed-vs-random.md` — 固定效应 vs 随机效应模型、逆方差加权、如何选、合并估计与 CI
- `references/07-heterogeneity.md` — 异质性：Q 检验、I²、τ²、预测区间、亚组分析、元回归（moderator analysis）
- `references/08-publication-bias.md` — 发表偏倚：漏斗图、Egger 回归、Begg、trim-and-fill、fail-safe N、p-curve/PET-PEESE
- `references/09-quality-risk-of-bias.md` — 研究质量/偏倚风险：Cochrane RoB2、Newcastle-Ottawa、GRADE 证据确定性、敏感性分析
- `references/10-software-reporting.md` — 软件实操（R metafor/meta、CMA、RevMan、Stata）、森林图/漏斗图、PRISMA 2020 报告清单
- `references/11-case-library.md` — 心理/教育/医学/管理领域元分析真实骨架

流程图与可视化：

- `diagrams/meta-analysis-flow.md` — 综述类型决策、PRISMA 2020 流程、效应量选择、固定vs随机、异质性处理、发表偏倚、森林图解读（Mermaid）

模板：

- `templates/pico-protocol.md` — PICO/PICOS 问题 + 协议模板
- `templates/prisma-flow-template.md` — PRISMA 2020 流程图填数模板
- `templates/extraction-sheet.md` — 数据提取与效应量编码表
- `templates/reporting-checklist.md` — PRISMA 报告 + 结果写作清单

## 核心工作原则（贯穿所有阶段）

1. **先分清综述类型**。叙述性综述（无系统流程）、系统综述（PRISMA 流程、可无 meta）、元分析（系统综述 + 统计合并）。别把"读了很多文献"叫元分析。
2. **能不能合并要看同质性**。研究在 PICO、设计、测量上过于异质，硬合并就是"apples and oranges"。异质太大时报叙述性综合或谨慎用随机效应 + 亚组。
3. **预注册 + PRISMA = 可复制**。协议预注册（PROSPERO）、检索式与筛选可复现、PRISMA 流程图透明——这是系统综述的立身之本。
4. **双人独立筛选与提取**。标题摘要与全文筛选、数据提取都应双人独立进行并报一致性，减少偏倚。
5. **效应量选对、方向统一、方差正确**。据结局类型选 d/g/r/OR/RR；换算要规范；所有效应量方向一致后再合并。
6. **默认随机效应 + 报异质性**。社科研究间常真异质，多数情形用随机效应；必报 I² 与 τ²（甚至预测区间），别只报一个合并值。
7. **必做发表偏倚 + 偏倚风险**。漏斗图/Egger + trim-and-fill/p-curve；用 RoB2/NOS/GRADE 评研究质量并做敏感性分析。

## 典型触发场景与首步动作

- "我这些文献能做元分析吗" → 读 `00`
- "研究问题和协议怎么写 / 要预注册吗" → 读 `01`，套 `templates/pico-protocol.md`
- "检索式怎么写 / PRISMA 流程图怎么画" → 读 `02` + `03`，套流程图模板
- "该用哪个效应量 / 怎么换算" → 读 `05`
- "固定还是随机效应" → 读 `06`
- "I² 太高怎么办 / 做亚组还是元回归" → 读 `07`
- "怎么查发表偏倚" → 读 `08`
- "用 R metafor 怎么跑 / 森林图怎么读" → 读 `10`
- "帮我画 PRISMA 流程 / 效应量决策图" → 读 `diagrams/meta-analysis-flow.md`

## 与 questionnaire-analysis / sample-size-power-analysis / 系统性文献综述写作 skill 的关系

本 skill 专攻**证据的定量合成（元分析）+ PRISMA 系统流程**。
- 若要**单个研究的量表信效度/回归/中介**，转 `questionnaire-analysis` / `process-mediation-moderation`。
- 若要**样本量与功效**（单个研究设计），转 `sample-size-power-analysis`。
- 若要**不做统计合并、只做系统/叙述性文献综述的检索与写作**，可与"系统性文献综述写作 skill"配合（本 skill 侧重定量合并，后者侧重综述论证与写作）。

## 语言
默认用简体中文交流与产出。涉及英文期刊投稿时给出中英对照与英文方法/结果段落。
