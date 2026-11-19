# 07 · 结构方程模型与中介调节 / SEM, Mediation & Moderation

> 进阶分析。SEM 前提：样本足够(≥200)、测量模型(CFA)先达标，再估结构模型。中介调节优先 Bootstrap。

## 一、结构方程模型 SEM / Structural Equation Modeling

### 两步法 / Two-step Approach (Anderson & Gerbing 1988)
1. **测量模型 CFA**：先验证各潜变量的信效度与拟合（见 `04`）。
2. **结构模型**：测量模型达标后，再估计潜变量间的路径关系。
- 不要跳过 CFA 直接跑全模型。

### 拟合指数标准 / Fit Indices（核心，记牢）
| 指数 | 可接受 | 良好 | 说明 |
| --- | --- | --- | --- |
| χ²/df (CMIN/DF) | < 3 | < 2 | 卡方受样本量影响大 |
| **CFI** | ≥ .90 | ≥ .95 | 比较拟合 |
| **TLI** (NNFI) | ≥ .90 | ≥ .95 | |
| **RMSEA** | ≤ .08 | ≤ .06 | 近似误差，报 90%CI |
| **SRMR** | ≤ .08 | ≤ .05 | 标准化残差 |
| GFI/AGFI | ≥ .90 | — | 受样本量影响，渐少用 |
| IFI/NFI | ≥ .90 | — | |

> 报告时选一组即可：常报 **χ²/df、CFI、TLI、RMSEA(含CI)、SRMR**。不要只挑好看的报。

### 模型修正 / Modification
- 看**修正指数 MI(Modification Indices)**，但**只在理论可解释时**释放参数（如允许同构念两题误差共变）。
- **禁止**纯为提升拟合而跨构念乱连——会被审稿质疑。
- 报告修正了什么、为什么。

### 工具
- AMOS：画路径图、直接出拟合与标准化系数。
- R `lavaan`：
  ```r
  library(lavaan)
  model <- '
    # 测量模型
    F1 =~ x1 + x2 + x3
    F2 =~ y1 + y2 + y3
    # 结构路径
    F2 ~ F1
  '
  fit <- sem(model, data=df, estimator="ML", missing="fiml")
  summary(fit, fit.measures=TRUE, standardized=TRUE)
  ```
- Mplus：复杂模型（非正态、类别指标、多层）更强。

## 二、中介效应 / Mediation

模型：自变量 X → 中介 M → 因变量 Y。

### 现代标准（弃用单纯逐步法）
- **优先 Bootstrap**（偏差校正，5000 次）求**间接效应 a×b 的 95%CI**：**CI 不含 0 即中介显著**。
- 报告：间接效应值、Boot SE、Boot 95%CI；直接效应；总效应。
- 完全中介 vs 部分中介的提法已弱化，**重点报间接效应是否显著及其大小**。
- Sobel 检验假定正态、偏保守，可作辅助但不单独依赖；逐步法(Baron & Kenny)已过时。

### 工具
- **PROCESS 宏**（Hayes，SPSS/R/SAS）：Model 4 = 简单中介。
- AMOS：用 Bootstrap 估计 user-defined estimand 的间接效应。
- lavaan：定义 `:=` 间接效应 + `se="bootstrap"`：
  ```r
  model <- ' M ~ a*X
             Y ~ b*M + c*X
             indirect := a*b
             total := c + a*b '
  fit <- sem(model, data=df, se="bootstrap", bootstrap=5000)
  parameterEstimates(fit, boot.ci.type="bca.simple")
  ```

## 三、调节效应 / Moderation
- X → Y 的关系随调节变量 W 变化。核心是 **X×W 交互项**显著。
- 连续变量先**中心化/标准化**再做乘积项。
- 显著后画**简单斜率图**（W 取 ±1SD），并做简单斜率检验。
- PROCESS Model 1 = 简单调节。
- 报告：交互项系数、ΔR²、不同 W 水平下的简单斜率。

## 四、有调节的中介 / Moderated Mediation
- 间接效应 a×b 随调节变量变化。
- 报告**调节中介指数(Index of Moderated Mediation)** + Bootstrap CI（不含 0 显著）。
- PROCESS Model 7/8/14 等（按调节位置选模型号）。

## 五、报告示例（中/英）
> 中：结构方程模型拟合良好，χ²/df=2.13, CFI=.96, TLI=.95, RMSEA=.052(90%CI[.041,.063]), SRMR=.043。工作压力通过情绪耗竭对离职意向的间接效应显著，间接效应=.18, Boot SE=.04, 95%CI[.11, .27]，不包含 0，表明情绪耗竭起中介作用。
> EN: The structural model fit the data well, χ²/df=2.13, CFI=.96, TLI=.95, RMSEA=.052 (90%CI[.041,.063]), SRMR=.043. The indirect effect of job stress on turnover intention via emotional exhaustion was significant (indirect=.18, Boot SE=.04, 95%CI[.11,.27], excluding zero), supporting mediation.

## 自检
- [ ] 样本量满足 SEM 要求
- [ ] 先 CFA（测量模型）达标，再结构模型
- [ ] 报告了完整一组拟合指数（不是只挑好的）
- [ ] 模型修正有理论依据并说明
- [ ] 中介用 Bootstrap CI（不含 0 判显著），报间接效应大小
- [ ] 调节做了中心化 + 简单斜率图
- [ ] 有调节的中介报告了调节中介指数

## 关键参考
- Kline (2016). *Principles and Practice of SEM* (4th ed).
- Hayes (2022). *Introduction to Mediation, Moderation, and Conditional Process Analysis* (3rd ed) — PROCESS.
- Anderson & Gerbing (1988). Two-step approach.
- Hu & Bentler (1999). Cutoff criteria for fit indices.
- 温忠麟、叶宝娟 (2014). 中介效应分析：方法和模型发展.《心理科学进展》.
