# 审稿意见回应 / Rebuttal 专项助手 · Response to Reviewers Skill

**🌐 [English](./README.en.md) | 简体中文**

> 一个面向 **Claude Code / Claude Agent** 的**审稿意见回应 / 修回信（Response to Reviewers / Rebuttal）专项**技能包。专门解决投稿人最焦虑的一步：**收到 major/minor revision 后，如何把一封逐条回应信写得让编辑和审稿人满意，把 R&R 转化为录用。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Lang](https://img.shields.io/badge/lang-中文%20|%20English-blue)
![Type](https://img.shields.io/badge/Claude-Skill-8A2BE2)
![Scope](https://img.shields.io/badge/覆盖-读懂决定信→重投-success)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> 给刚收到审稿意见、心里发慌、不知道"这条同不同意""该不该反驳""两个审稿人打架怎么办""语气要多客气"的你。

> 核心立场：**修回不是"改完就行"，而是一次"再说服"。每条回应都要让审稿人不必翻原稿，就看到"意见→你的处理→改后的原文（页码/行号）"。**

---

## 📑 目录
- [这是什么 / 解决什么痛点](#-这是什么--解决什么痛点)
- [它和 ssci-writing skill 有什么不同](#-它和-ssci-writing-skill-有什么不同)
- [内容结构](#-内容结构)
- [十二个环节能帮你做什么](#-十二个环节能帮你做什么)
- [安装与使用](#-安装与使用)
- [七条核心原则](#-七条核心原则)
- [参考](#-参考)
- [免责声明 / 贡献 / 许可](#-免责声明)
- [☕ 赞赏支持](#-赞赏支持)

---

## ✨ 这是什么 / 解决什么痛点

拿到 major/minor revision，很多人卡在：

- 读不懂编辑决定信——**分不清硬要求和建议**、抓不住"决定性意见"；
- 逐条回应**没有章法**，写成"已修改"三个字，审稿人找不到改在哪；
- 有一条**不认同**，要么硬刚得罪审稿人，要么憋屈全改；
- 两个审稿人**要求相反**，只敢听一个、装看不见另一个；
- 语气**不是太卑就是太刚**；
- 回应信说改了，改稿里**却对不上号**，重投被退。

这个 skill 把"一封能把 R&R 变录用的回应信该怎么写"沉淀成 Claude 能直接调用的技能包——**每个环节都带判定标准、正反例、中英句式和可套用模板**。

## 🆚 它和 ssci-writing skill 有什么不同

| | ssci-writing skill | 本 · 审稿回应 skill |
| --- | --- | --- |
| 阶段 | 投稿**前**：选刊、gap、IMRaD、摘要/引言/方法/结果写作 | 投稿**后**：从决定信到重投 |
| 产物 | 一篇能投出去的稿子 | 一封能把 R&R 变录用的回应信 |
| 独有 | desk reject 规避、假设写法、方法结构 | 决定信拆解、逐条三段式、反驳/冲突处理、cover letter、句式库 |

> 两者衔接：**用 ssci-writing 把稿子写好投出去，用本 skill 把审稿意见接住、改回去。**

## 📂 内容结构

```
reviewer-response-rebuttal/
├── SKILL.md                                  # 技能主入口（Claude 自动读取）
├── references/                                # 12 份子文档（用时先读）
│   ├── 00-mindset-and-triage.md               # 心态与分诊
│   ├── 01-decision-letter-anatomy.md          # 读懂编辑决定信
│   ├── 02-response-letter-structure.md        # 回应信整体结构与格式约定
│   ├── 03-point-by-point.md                   # 逐条回应黄金三段式
│   ├── 04-tone-and-diplomacy.md               # 语气与外交辞令
│   ├── 05-agreeing-revising.md                # 同意并修改
│   ├── 06-disagreeing-respectfully.md         # 礼貌反驳 push back
│   ├── 07-conflicting-reviewers.md            # 审稿人意见冲突
│   ├── 08-request-types.md                    # 常见要求类型逐类应对
│   ├── 09-cover-letter.md                     # 给编辑的 cover letter
│   ├── 10-resubmission-checklist.md           # 重投核对与时间管理
│   └── 11-phrase-bank-cases.md                # 高频英文句式 + 真实骨架
├── diagrams/
│   └── rebuttal-flow.md                       # 全流程/三段式/决策分支/语气光谱/冲突处理（Mermaid）
├── templates/
│   ├── response-letter-template.md            # 完整回应信模板
│   ├── point-by-point-table.md                # 逐条回应工作表
│   ├── cover-letter-template.md               # cover letter 模板
│   └── phrase-bank.md                         # 中英对照句式速查
├── README.md / README.en.md / LICENSE
```

## 🧭 十二个环节能帮你做什么

| 环节 | 你可以让我做的事 | 文档 |
| --- | --- | --- |
| 0 心态分诊 | 定策略、拆清单、标决定性意见 | `00` |
| 1 拆解决定信 | 分清硬要求/建议/必答 | `01` |
| 2 回应信结构 | 搭骨架 + 格式约定 | `02` |
| 3 逐条三段式 | 复述→修改→引原文+页行号 | `03` |
| 4 语气外交 | 不卑不亢的措辞 | `04` |
| 5 同意并修改 | 写得具体可核查、防假改 | `05` |
| 6 礼貌反驳 | 有据 push back + 交编辑裁量 | `06` |
| 7 冲突审稿人 | 摊开+权衡+请编辑定夺 | `07` |
| 8 要求类型 | 补分析/文献/理论/方法/因果/语言 | `08` |
| 9 cover letter | 给编辑的附信 | `09` |
| 10 重投核对 | 一致性、tracked changes、时间 | `10` |
| 11 句式库 | 中英句式 + 案例 | `11` |

## 🚀 安装与使用

**macOS / Linux**
```bash
git clone https://github.com/maydengximin-sketch/reviewer-response-rebuttal-skill.git \
  ~/.claude/skills/reviewer-response-rebuttal
```

**Windows（PowerShell）**
```powershell
git clone https://github.com/maydengximin-sketch/reviewer-response-rebuttal-skill.git "$env:USERPROFILE\.claude\skills\reviewer-response-rebuttal"
```

装好后把决定信/审稿意见贴给 Claude，说你的需求即可触发，例如：
- "我收到 major revision，帮我把意见拆成清单、定策略"
- "帮我逐条起草回应（三段式）"
- "有一条我不同意，怎么礼貌反驳？"
- "两个审稿人要求相反，怎么办？"
- "帮我写 cover letter"
- "重投前帮我核对回应和改稿一致"

> Claude 会按需读取对应 `references/` 文档，用判定标准、句式与模板作答。

## 🎯 七条核心原则
1. **一条都不能漏**——每点都有独立编号回应。
2. **让审稿人零成本核实**——引改后原文 + 页行号。
3. **先感谢、再回应、后定位**——三段式。
4. **能改就改，不能改就有据说清**——证据而非情绪。
5. **语气不卑不亢**——感谢但不谄媚，坚定但不对抗。
6. **冲突意见要摊开**——请编辑裁断，别偷偷只听一个。
7. **可核查、可追溯**——回应与改稿严格对应。

## 📚 参考
- Noble, W. S. (2017). Ten simple rules for writing a response to reviewers. *PLoS Computational Biology, 13*(10).
- Annesley, T. M. (2011). Top 10 tips for responding to reviewer and editor comments. *Clinical Chemistry, 57*(4).
- Williams, H. C. (2004). How to reply to referees' comments when submitting manuscripts. *JAAD, 51*(1).

## ⚠️ 免责声明

本 skill 是**写作与流程辅助工具**，不替代你的学术判断、导师指导与目标期刊的具体政策。所有回应内容必须**基于你自己的稿件与真实修改**——模板与句式仅为脚手架，切勿套用空话或做出与改稿不符的承诺。请勿在回应中编造未实际执行的分析或结果。

## 🤝 贡献
欢迎 Issue / PR：补充要求类型、修订句式、增加模板、改进翻译、报告错误。

## 📄 许可
[MIT](./LICENSE) — 自由使用、修改、分发，保留版权声明即可。

---

## ☕ 赞赏支持

如果这个项目帮你把审稿意见稳稳接住了，欢迎请主包喝杯咖啡 ☕
**创作不易，你的一杯咖啡是我继续更新的动力～**（完全自愿，点个 ⭐ Star 就更开心啦）

| 支付宝 | 微信支付 |
| :---: | :---: |
| <img src="assets/alipay.jpg" width="240" alt="支付宝收款码"> | <img src="assets/wechat.jpg" width="240" alt="微信收款码"> |
| 秘境瑰宝 Mystery Realm | May |

> 也欢迎 Star ⭐ / Fork 🍴 / 分享给同样在等审稿意见的同学 🙏
