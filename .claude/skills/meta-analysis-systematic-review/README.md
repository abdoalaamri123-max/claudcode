# 元分析与系统综述专项助手 · Meta-analysis & Systematic Review Skill

**🌐 [English](./README.en.md) | 简体中文**

> 一个面向 **Claude Code / Claude Agent** 的**元分析 / 系统综述（+ PRISMA）专项**方法学技能包。专门解决一件事：**如何用 PRISMA 规范做一篇透明、可复制的系统综述，并在研究足够同质时，用元分析把定量结果统计合并成一个总效应。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Lang](https://img.shields.io/badge/lang-中文%20|%20English-blue)
![Type](https://img.shields.io/badge/Claude-Skill-8A2BE2)
![Tool](https://img.shields.io/badge/R-metafor%20|%20CMA%20|%20RevMan-orange)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> 给正在做系统综述/元分析、却总在"我这些文献能不能合并""固定还是随机效应""I² 太高怎么办""要不要做发表偏倚""PRISMA 流程图怎么画"上卡壳的你。

> 核心立场：**系统综述 = 可复制的证据合成流程（PRISMA）；元分析 = 在流程之上、当研究足够同质时的统计合并。不是所有系统综述都能/都该做元分析。**

---

## 📑 目录
- [这是什么 / 解决什么痛点](#-这是什么--解决什么痛点)
- [它和其他量化 skill 有什么不同](#-它和其他量化-skill-有什么不同)
- [内容结构](#-内容结构)
- [十二个环节能帮你做什么](#-十二个环节能帮你做什么)
- [安装与使用](#-安装与使用)
- [七条核心原则](#-七条核心原则)
- [方法学渊源](#-方法学渊源)
- [免责声明 / 贡献 / 许可](#-免责声明)
- [☕ 赞赏支持](#-赞赏支持)

---

## ✨ 这是什么 / 解决什么痛点

元分析是近年最热、也最容易出错的方向。常见翻车：

- 把"读了很多文献"当**元分析**，其实连系统检索都没做；
- 研究**太异质硬合并**（apples and oranges），总效应无意义；
- **固定/随机效应选错**——机械按"I² 是否显著"决定，而非看研究是否概念同质；
- **只看 I²**，不看 τ² 与预测区间（I² 不是异质性的绝对度量）；
- **不做发表偏倚检验**，合并值虚高；
- 不**预注册**、不附**检索式与 PRISMA 流程图**，无法复制。

这个 skill 把"一篇经得起审稿的系统综述/元分析该怎么做"沉淀成 Claude 能直接调用的技能包——**每个环节都带判定标准、公式、软件命令、报告规范和可套用模板**。

## 🆚 它和其他量化 skill 有什么不同

| | 问卷分析 / PROCESS / AMOS-SEM | 样本量功效 | 本 · 元分析 |
| --- | --- | --- | --- |
| 分析对象 | **单个研究**的数据 | 单个研究的设计 | **多个研究**的证据合成 |
| 产物 | 信效度/中介/SEM | 所需样本量 | 合并效应 + 异质 + 偏倚 |
| 独有 | α、EFA/CFA、Bootstrap | 功效分析 | PRISMA、效应量合并、I²/τ²、森林图、发表偏倚 |

> 分工：单研究分析用前几个 skill；把一批研究**合成证据**用本 skill。若只做**不合并的系统/叙述性综述**，可配合"系统性文献综述写作 skill"。

## 📂 内容结构

```
meta-analysis-systematic-review/
├── SKILL.md                                   # 技能主入口（Claude 自动读取）
├── references/                                 # 12 份方法学子文档（用时先读）
│   ├── 00-should-you-use-meta-analysis.md      # 叙述/系统综述/元分析怎么选、能否合并
│   ├── 01-question-and-protocol.md             # PICO + PROSPERO 预注册
│   ├── 02-search-strategy.md                   # 检索式、数据库、灰色文献
│   ├── 03-prisma-flow-screening.md             # PRISMA 2020 流程 + 双人筛选
│   ├── 04-data-extraction-coding.md            # 提取表 + 调节变量编码
│   ├── 05-effect-sizes.md                      # d/g/r/OR/RR、换算、方向统一
│   ├── 06-fixed-vs-random.md                   # 固定 vs 随机效应
│   ├── 07-heterogeneity.md                     # Q/I²/τ²、亚组、元回归
│   ├── 08-publication-bias.md                  # 漏斗图/Egger/trim-and-fill/p-curve
│   ├── 09-quality-risk-of-bias.md              # RoB2/NOS/GRADE
│   ├── 10-software-reporting.md                # R metafor/meta、森林图、PRISMA 报告
│   └── 11-case-library.md                      # 心理/相关/医学/纯系统综述骨架
├── diagrams/
│   └── meta-analysis-flow.md                   # 综述类型/PRISMA/效应量/固定随机/异质/偏倚/森林图（Mermaid）
├── templates/
│   ├── pico-protocol.md                        # PICO + 协议模板
│   ├── prisma-flow-template.md                 # PRISMA 流程图填数模板
│   ├── extraction-sheet.md                     # 数据提取与效应量编码表
│   └── reporting-checklist.md                  # PRISMA 报告 + 结果写作清单
├── README.md / README.en.md / LICENSE
```

## 🧭 十二个环节能帮你做什么

| 环节 | 你可以让我做的事 | 文档 |
| --- | --- | --- |
| 0 要不要做 | 综述类型选择、能否合并 | `00` |
| 1 问题与协议 | PICO、预注册 | `01` |
| 2 检索策略 | 检索式、数据库 | `02` |
| 3 PRISMA 筛选 | 流程图、双人筛选 | `03` |
| 4 数据提取 | 提取表、调节编码 | `04` |
| 5 效应量 | d/g/r/OR、换算 | `05` |
| 6 模型选择 | 固定 vs 随机 | `06` |
| 7 异质性 | I²/τ²、亚组、元回归 | `07` |
| 8 发表偏倚 | 漏斗图、Egger、p-curve | `08` |
| 9 质量评价 | RoB2/NOS/GRADE | `09` |
| 10 软件报告 | metafor、森林图、PRISMA | `10` |
| 11 案例库 | 四类元分析骨架 | `11` |

## 🚀 安装与使用

**macOS / Linux**
```bash
git clone https://github.com/maydengximin-sketch/meta-analysis-systematic-review-skill.git \
  ~/.claude/skills/meta-analysis-systematic-review
```

**Windows（PowerShell）**
```powershell
git clone https://github.com/maydengximin-sketch/meta-analysis-systematic-review-skill.git "$env:USERPROFILE\.claude\skills\meta-analysis-systematic-review"
```

装好后直接对 Claude 说需求即可触发，例如：
- "我这些文献能做元分析吗？"
- "研究问题和协议怎么写？要预注册吗？"
- "该用哪个效应量？怎么换算？"
- "固定还是随机效应？"
- "I² 太高怎么办？做亚组还是元回归？"
- "怎么查发表偏倚？"
- "用 R metafor 怎么跑？森林图怎么读？"
- "帮我画 PRISMA 流程 / 效应量决策图"

> Claude 会按需读取对应 `references/` 文档，用判定标准、公式与模板作答。

## 🎯 七条核心原则
1. **先分清综述类型**——叙述/系统综述/元分析。
2. **能不能合并看同质性**——太异质别硬合。
3. **预注册 + PRISMA = 可复制**。
4. **双人独立筛选与提取**。
5. **效应量选对、方向统一、方差正确**。
6. **默认随机效应 + 报异质性**（I²/τ²/预测区间）。
7. **必做发表偏倚 + 偏倚风险**。

## 📚 方法学渊源
- Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2021). *Introduction to Meta-Analysis* (2nd ed.).
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71.
- Higgins, J. P. T., et al. (2023). *Cochrane Handbook for Systematic Reviews of Interventions*.
- Viechtbauer, W. (2010). Conducting meta-analyses in R with metafor. *JSS, 36*(3).
- Harrer, M., et al. (2021). *Doing Meta-Analysis with R*.
- Egger, M., et al. (1997). Bias in meta-analysis. *BMJ, 315*.
- Higgins & Thompson (2002). Quantifying heterogeneity. *Statistics in Medicine, 21*.

## ⚠️ 免责声明

本 skill 是**方法学辅助工具**，不替代你的统计判断、导师指导与目标期刊/报告规范（PRISMA、Cochrane）。所有结果必须**来自你自己的系统检索与数据**，案例中的数字均为体例示范的虚构值，切勿套用。合并与偏倚校正的结论高度依赖纳入研究质量，请谨慎解读。

## 🤝 贡献
欢迎 Issue / PR：补充方法细节、修订判定标准、增加模板与流程图、改进翻译、报告错误。

## 📄 许可
[MIT](./LICENSE) — 自由使用、修改、分发，保留版权声明即可。

---

## ☕ 赞赏支持

如果这个项目帮你把元分析的坑绕过去了，欢迎请主包喝杯咖啡 ☕
**创作不易，你的一杯咖啡是我继续更新的动力～**（完全自愿，点个 ⭐ Star 就更开心啦）

| 支付宝 | 微信支付 |
| :---: | :---: |
| <img src="assets/alipay.jpg" width="240" alt="支付宝收款码"> | <img src="assets/wechat.jpg" width="240" alt="微信收款码"> |
| 秘境瑰宝 Mystery Realm | May |

> 也欢迎 Star ⭐ / Fork 🍴 / 分享给同样在做元分析的同学 🙏
