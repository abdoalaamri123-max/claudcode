# 03 · 描述统计、正态性与共同方法偏差 / Descriptives, Normality & CMB

## 一、描述性统计 / Descriptive Statistics
- 连续变量：均值 M、标准差 SD、最小/最大、偏度 Skewness、峰度 Kurtosis。
- 分类变量：频数 n、百分比 %。
- 人口学特征：用表呈现样本构成（性别、年龄、学历等）。
- SPSS：`分析 → 描述统计 → 描述`（连续）/`频率`（分类）。
- R：`psych::describe(df)`、`summary()`、`table()`。

## 二、正态性检验 / Normality
参数检验(t/ANOVA/Pearson/回归)假定（近似）正态。检查：
| 方法 | 标准 |
| --- | --- |
| 偏度 Skewness | 绝对值 < 2（宽松）/ < 1（严格） |
| 峰度 Kurtosis | 绝对值 < 7（宽松）/ < 3 |
| Shapiro-Wilk | p > .05 为正态（小样本敏感） |
| K-S 检验 | p > .05 为正态（大样本过于敏感，慎用） |
| 图示 | 直方图、Q-Q 图、P-P 图 |

> 实务：大样本下 S-W/K-S 极易显著，**优先看偏度峰度与 Q-Q 图**。|偏度|<2 且 |峰度|<7（West et al. 1995）通常可用参数法。严重偏态考虑变换(对数/平方根)或非参数法(见 `05`)。

## 三、共同方法偏差 / Common Method Bias (CMB)

自评、单一来源、横断面问卷**必须**做并报告 CMB 检验。

### 1. Harman 单因素检验（最常用，但较弱）
- 把所有题项一起做 EFA(不旋转)，看**第一个因子**解释的方差。
- 标准：第一因子方差 **< 40%**（部分用 50%）则 CMB 不严重。
- 局限：只是必要非充分，审稿人常嫌弱，建议加做下面方法。

### 2. 控制未测潜因子法 / Unmeasured Latent Method Factor (CLF)
- 在 CFA/SEM 中加一个**共同方法潜因子**，让所有题项同时载荷于其构念与该方法因子。
- 比较加入前后路径系数变化、或方法因子解释方差。AMOS 中加 CLF 共变。

### 3. 其他
- 单因子 CFA vs 多因子 CFA 对比（单因子拟合差则支持区分）。
- 标记变量法(marker variable)。
- 程序层面预防见 `01`。

### 报告示例（中/英）
> 中：采用 Harman 单因素检验，未旋转的探索性因子分析析出特征值大于 1 的因子若干，第一个因子解释方差为 32.6%，小于 40%，表明本研究共同方法偏差不严重。
> EN: Harman's single-factor test showed the first factor accounted for 32.6% of the variance (< 40%), indicating common method bias was not a serious concern.

## 四、相关矩阵（描述阶段常一并报告）
- 报告各变量均值、标准差与两两相关(Pearson)，作为后续回归/SEM 的基础表（APA 表见 `08`）。
- 区分效度初步证据：变量间相关不应过高(如 > .85 提示共线/构念重叠)。

## 关键参考
- Podsakoff et al. (2003, 2012). Common method biases. *J Appl Psychol*.
- West, Finch & Curran (1995). SEM with nonnormal variables.
- 周浩、龙立荣 (2004). 共同方法偏差的统计检验与控制方法.《心理科学进展》.
