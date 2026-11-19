# 05 · 差异检验 / Difference Tests

> 用于比较组间差异（如不同性别/学历在某变量上的差异）。**先看测量层次与前提假设，再选检验**。务必报告效应量。

## 一、选择决策 / Which Test

| 自变量(分组) | 因变量 | 前提满足 | 用 | 前提不满足 |
| --- | --- | --- | --- | --- |
| 2 组(独立) | 连续 | 正态+方差齐 | 独立样本 t 检验 | Mann-Whitney U |
| 2 组(配对) | 连续 | 差值正态 | 配对样本 t 检验 | Wilcoxon 符号秩 |
| ≥3 组(独立) | 连续 | 正态+方差齐 | 单因素 ANOVA | Kruskal-Wallis H |
| ≥3 组(重复测量) | 连续 | 球形性 | 重复测量 ANOVA | Friedman |
| 2 个分组因素 | 连续 | 正态+方差齐 | 双因素 ANOVA（含交互） | — |
| 分类 | 分类 | 期望频数≥5 | 卡方检验 χ² | Fisher 精确检验 |

## 二、前提假设 / Assumptions
- **正态性**：见 `03`（偏度峰度、Q-Q）。
- **方差齐性 Homogeneity**：Levene 检验 p > .05 为齐性。t 检验不齐时用校正（Welch's t / 不假设等方差行）；ANOVA 不齐用 Welch ANOVA + Games-Howell 事后。
- **独立性**：观测相互独立（抽样设计保证）。

## 三、t 检验 / t-test
- SPSS：`分析→比较平均值→独立样本 T 检验`。
- 报告：t(df) = 值, p, **Cohen's d**（效应量）+ 两组 M±SD。
- Cohen's d：0.2 小、0.5 中、0.8 大。

## 四、方差分析 ANOVA
- 单因素：SPSS `分析→比较平均值→单因素 ANOVA`，事后比较选 Tukey/Bonferroni（齐性）或 Games-Howell（不齐）。
- 报告：F(df组间, df组内) = 值, p, **η² 或 partial η²**（偏 η²：.01 小、.06 中、.14 大）。
- 双因素：关注主效应 + **交互效应**；交互显著要做简单效应分析(simple effects)。
- 重复测量：检查球形性(Mauchly)，违反用 Greenhouse-Geisser 校正。
- 协方差分析 ANCOVA：控制协变量后比较，需满足回归斜率同质。

## 五、卡方检验 / Chi-square
- 适用：两个分类变量的关联(独立性检验)或拟合优度。
- 前提：**期望频数 ≥ 5 的格子占比 ≥ 80%**，否则用 Fisher 精确检验或合并类别。
- 报告：χ²(df, N=) = 值, p, 效应量 **Cramér's V / φ**。

## 六、效应量速记 / Effect Sizes
| 检验 | 效应量 | 小/中/大 |
| --- | --- | --- |
| t 检验 | Cohen's d | .20 / .50 / .80 |
| ANOVA | η² / partial η² | .01 / .06 / .14 |
| 卡方 | Cramér's V | 依 df，约 .10 / .30 / .50 |
| 相关 | r | .10 / .30 / .50 |

## 七、报告示例（中/英）
> 中：独立样本 t 检验表明，男生的满意度（M=3.82, SD=0.61）显著高于女生（M=3.55, SD=0.67），t(298)=3.45, p=.001, Cohen's d=0.42，为中等偏小效应。
> EN: An independent-samples t-test showed males reported significantly higher satisfaction (M=3.82, SD=0.61) than females (M=3.55, SD=0.67), t(298)=3.45, p=.001, d=0.42.

## 自检
- [ ] 选对了检验（匹配测量层次与组数）
- [ ] 检验并报告了前提假设（正态、方差齐性）
- [ ] 前提违反时改用校正/非参数法
- [ ] 报告了 p 值 + 效应量 + 描述统计
- [ ] 多组比较做了事后检验

## 关键参考
- Field (2018). *Discovering Statistics Using IBM SPSS Statistics*.
- Cohen (1988). *Statistical Power Analysis for the Behavioral Sciences*.
