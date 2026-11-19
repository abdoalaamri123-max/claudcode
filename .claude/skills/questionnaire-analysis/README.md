# 问卷数据分析全流程助手 · Questionnaire / Survey Data Analysis Skill

> 一个面向 **Claude Code / Claude Agent** 的问卷·量表数据分析方法学技能包：从问卷设计、数据清洗、信效度，到差异检验、回归、结构方程与中介调节、APA 报告，覆盖整条分析链路。**中英文通用**，工具中立（实操以 SPSS/AMOS 为主，关键处附 R）。
>
> A bilingual (中文/English) methodology skill for survey & scale data analysis — from questionnaire design and data cleaning, through reliability/validity, difference tests, regression, SEM, mediation/moderation, to APA reporting. Tool-neutral (SPSS/AMOS-first, with R snippets).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Lang](https://img.shields.io/badge/lang-中文%2FEN-blue)
![Type](https://img.shields.io/badge/Claude-Skill-8A2BE2)
![Stage](https://img.shields.io/badge/coverage-设计→成文-success)
![Tools](https://img.shields.io/badge/SPSS%2FAMOS%2FR-supported-orange)

> 给读研做问卷、被审稿人追着要信效度/共同方法偏差/效应量的你。把"一份问卷数据该怎么规范分析"沉淀成 AI 能直接调用的技能包。

---

## 📑 目录 / Contents

- [解决什么痛点](#-解决什么痛点)
- [内容结构](#-内容结构)
- [八大阶段能力](#-八大阶段能力)
- [安装与使用](#-安装与使用)
- [使用场景示例](#-使用场景示例)
- [七条核心原则](#-七条核心原则)
- [常见问题 FAQ](#-常见问题-faq)
- [免责声明 / 贡献 / 许可](#-免责声明)
- [☕ 赞赏支持](#-赞赏支持)

---

## ✨ 解决什么痛点

做问卷研究，卡点几乎都在"规范"上：

- 这个变量是定序还是定距？该用 t 检验还是非参数？
- Cronbach's α 多少算合格？删题有什么依据？
- EFA 和 CFA 到底什么时候用哪个？KMO/AVE/CR 阈值多少？
- 审稿人说"共同方法偏差未处理"，Harman 单因素怎么做？
- SEM 拟合不好怎么救？χ²/df、CFI、RMSEA 标准是多少？
- 中介还在用 Baron-Kenny 逐步法？现在要 Bootstrap……
- 结果怎么写成 APA 表格？p=.000 为什么会被打回？

这个 Skill 把上述全部沉淀成**结构化方法文档 + APA 中英结果句模板 + 阈值速查工具**，让 AI 在你提问时按学界规范作答，并直接给出可粘进论文的句子。

**适合**：研究生/博士生、青年教师、做实证问卷研究的社科/管理/教育/心理/医护研究者。

## 📦 内容结构 / Structure

```
questionnaire-analysis/
├── SKILL.md                          # 技能主文件（触发与导航）
├── references/                       # 八份方法学详解（核心知识库）
│   ├── 01-questionnaire-design.md    # 量表设计·Likert·测量层次·样本量
│   ├── 02-data-cleaning.md           # 缺失值·异常值·反向计分·数据准备
│   ├── 03-descriptive-statistics.md  # 描述统计·正态性·共同方法偏差
│   ├── 04-reliability-validity.md    # α/CR/AVE·EFA·CFA·收敛/区分效度
│   ├── 05-difference-tests.md        # t检验·ANOVA·卡方·非参数·效应量
│   ├── 06-correlation-regression.md  # 相关·多元/层次/逻辑回归·共线性
│   ├── 07-sem-mediation.md           # SEM·CFA·中介/调节·Bootstrap·PROCESS
│   └── 08-reporting-apa.md           # APA表格·结果写作·p值/效应量
├── diagrams/                         # 流程图（Mermaid，GitHub 直接渲染）
│   ├── analysis-flow.md              # 总流程·方法决策树·EFA/CFA·中介调节
│   └── index.html                    # 离线渲染页，双击查看并截图
├── templates/                        # 即用模板
│   ├── apa-results-sentences.md      # APA 结果句（中英对照，替换数值即用）
│   └── analysis-checklist.md         # 全流程分析自检表
└── tools/
    └── stats-cheatsheet/             # 离线统计阈值&拟合指数速查表（双击即用）
        └── index.html
```

## 🧩 八大阶段能力 / What it covers

| 阶段 | 能让 AI 做的事 | 文档 |
| --- | --- | --- |
| 1 问卷设计 | 量表选型、Likert、测量层次判定、样本量(G*Power) | `01` |
| 2 数据清洗 | 缺失值(MI/FIML)、异常值、反向计分、维度合成 | `02` |
| 3 描述统计 | 描述、正态性、**共同方法偏差(Harman/CLF)** | `03` |
| 4 信度效度 | α/CR/AVE、EFA、CFA、收敛/区分效度 | `04` |
| 5 差异检验 | t、ANOVA、卡方、非参数 + 效应量 + 前提检验 | `05` |
| 6 相关回归 | 相关、多元/层次/逻辑回归、VIF 共线性 | `06` |
| 7 SEM/中介调节 | CFA→SEM 两步法、Bootstrap 中介、调节、有调节的中介 | `07` |
| 8 APA 报告 | APA7 表格、中英结果句、效应量与 CI 规范 | `08` |

## 🚀 安装与使用 / Install & Use

### 方式一：作为 Claude Code 个人技能（推荐）
```bash
git clone https://github.com/maydengximin-sketch/questionnaire-analysis-skill.git \
  ~/.claude/skills/questionnaire-analysis
```
Windows（PowerShell）：
```powershell
git clone https://github.com/maydengximin-sketch/questionnaire-analysis-skill.git "$env:USERPROFILE\.claude\skills\questionnaire-analysis"
```
之后用自然语言提问即可，中英文皆可。

### 方式二：只用速查工具
双击 `tools/stats-cheatsheet/index.html`，**离线**查阅信度/效度/EFA/SEM 拟合/效应量/前提假设/样本量的全部阈值标准，分四个标签页，适合截图。

### 方式三：直接取用 APA 模板
`templates/apa-results-sentences.md` 提供 t 检验、ANOVA、回归、CFA、SEM、中介、调节等的**中英对照结果句**，替换 `【】` 数值即可粘进论文。

## 💬 使用场景示例 / Example Prompts

```text
· 帮我判断这份问卷该用哪些分析（我有3个自变量、1个中介、1个因变量）
· 算一下这个量表的信度和效度，给我 APA 表格
· KMO 才 .62，我的 EFA 还能做吗？该怎么处理？
· 审稿人说要处理共同方法偏差，帮我做 Harman 检验并写一段
· 我的 SEM 拟合 RMSEA=.09 偏高，怎么修正？
· 用 PROCESS Model 4 做中介，帮我解读 Bootstrap 结果并写成 APA
· Help me report this regression in APA 7 style (English)
· 把这段中文结果翻译成英文期刊用的 APA 表述
```

## 🧭 七条核心原则 / Principles

1. **方法服从测量层次与设计**——先定变量类型，再选检验。
2. **先信效度，后假设检验**——量表不过关，后续结论不可信。
3. **报告效应量与置信区间**，不止 p 值。
4. **检查前提假设**——正态、方差齐性、共线性、拟合，违反要说明。
5. **中介调节用 Bootstrap**——弃用单纯 Sobel/逐步法。
6. **共同方法偏差要处理**——自评横断面必做并报告。
7. **如实报告**——前提违反、样本不足、拟合欠佳不藏不饰。

## ❓ 常见问题 FAQ

**Q：不会编程能用吗？** 能。以 SPSS/AMOS 菜单操作为主，R 代码是可选项；速查工具和模板双击/复制即用。

**Q：能投英文期刊吗？** 能。术语全程中英对照，结果句和表格都有英文版，符合 APA 7。

**Q：EFA 和 CFA 怎么选？** 不确定结构(自编/改编量表)用 EFA；验证已有结构(成熟量表)用 CFA。`04` 有详解。

**Q：它能替代统计老师/教材吗？** 不能。它帮你对齐规范、少走弯路，最终请以目标期刊与统计教材为准。

## ⚠️ 免责声明 / Disclaimer

本技能包提供方法学指引、阈值参考与模板，**不替代**专业统计咨询、目标期刊规范与统计教材。阈值（α/AVE/拟合指数等）采用通行标准，但不同领域/期刊存在差异，请以你的投稿要求为准。分析结论与学术责任由研究者承担。

## 🤝 贡献 / Contributing

欢迎 Issue / PR：补充方法、修订阈值、增加模板与工具、改进中英翻译。

## 📄 许可 / License

[MIT](./LICENSE)

---

## ☕ 赞赏支持

如果这个项目帮你少翻了几次统计书、少踩了几个审稿坑，欢迎请主包喝杯咖啡 ☕
**创作不易，你的一杯咖啡是我继续更新的动力～**（完全自愿，点个 ⭐ Star 就很开心啦）

| 支付宝 | 微信支付 |
| :---: | :---: |
| <img src="assets/alipay.jpg" width="240" alt="支付宝收款码"> | <img src="assets/wechat.jpg" width="240" alt="微信收款码"> |
| 秘境瑰宝 Mystery Realm | May |

> 也欢迎 Star ⭐ / Fork 🍴 / 分享给同样在做问卷研究的同学 🙏
