# 04 · 信度与效度 / Reliability & Validity

> 量表分析的核心关卡。**先信效度达标，假设检验才有意义**。先分清你要做的是 EFA（探索结构）还是 CFA（验证已有结构）。

## 一、信度 / Reliability

| 指标 | 含义 | 阈值 | 工具 |
| --- | --- | --- | --- |
| **Cronbach's α** | 内部一致性 | ≥ .70 可接受；≥ .80 良好；探索性≥.60 | SPSS `分析→刻度→可靠性分析` |
| **组合信度 CR** (Composite Reliability) | CFA 框架下的构念信度 | ≥ .70 | AMOS/lavaan 由载荷计算 |
| 重测信度 Test-retest | 跨时间稳定性 | r ≥ .70 | 两次施测相关 |
| McDonald's ω | α 的更稳健替代 | ≥ .70 | R `psych::omega` |

要点：
- α 受题项数影响，题少时偏低；看**校正后项总相关(CITC)** ≥ .30–.40，删低 CITC 题可提升 α。
- 看"项已删除的 α"：删某题若 α 明显上升，考虑删该题（结合理论）。
- CR 优于 α（不假设各题载荷相等）。SEM 论文常同时报 α 与 CR。
- **R 计算 CR/AVE**：`semTools::reliability(fit)`。

## 二、效度 / Validity 总览
| 类型 | 回答 | 如何获得 |
| --- | --- | --- |
| 内容效度 Content | 题项是否覆盖构念 | 专家评定、CVI、文献支撑 |
| 结构效度 Construct | 是否测到潜在构念 | EFA / CFA |
| 收敛效度 Convergent | 同构念题项是否聚合 | 标准化载荷≥.5(.7佳)、AVE≥.5、CR≥.7 |
| 区分效度 Discriminant | 不同构念是否可分 | √AVE > 因子间相关 (Fornell-Larcker)；HTMT<.85/.90 |
| 效标/预测效度 Criterion | 与外部标准的关联 | 与效标变量相关 |

## 三、探索性因子分析 EFA / Exploratory Factor Analysis

用途：**不确定结构**时探索维度（自编量表、量表改编）。

### 前提检验
- **KMO** ≥ .70 适合（≥.80 良好，<.60 不宜）。
- **Bartlett 球形检验** p < .05（拒绝相关阵为单位阵）。

### 步骤与标准
1. 提取方法：主成分 PCA（常用于降维）或主轴因子 PAF/最大似然 ML（用于潜在构念）。
2. 因子数确定：特征值 > 1（Kaiser）、碎石图(scree plot)拐点、平行分析(parallel analysis，最准)、累积解释方差 ≥ 50%(社科常≥60%)。
3. 旋转：构念相关用斜交 Promax/Oblimin；假定独立用正交 Varimax。
4. 题项筛选标准：
   - 因子载荷 **≥ .50**（≥.40 勉强）；
   - **删除双重载荷题**（在两因子载荷均 >.40 且差 <.20）；
   - 删除共同度(communality) < .40 的题；
   - 删除独立成因子的单题。
5. SPSS：`分析→降维→因子`。R：`psych::fa()` + `fa.parallel()`。

## 四、验证性因子分析 CFA / Confirmatory Factor Analysis

用途：**已有理论结构**时验证测量模型（成熟量表、EFA 后交叉验证）。需在 AMOS / lavaan / Mplus 做。

### 测量模型评估
1. **拟合指数**（见 `07` 与速查工具）：χ²/df < 3、CFI/TLI ≥ .90(.95佳)、RMSEA ≤ .08(.06佳)、SRMR ≤ .08。
2. **收敛效度**：标准化载荷 ≥ .50(.70 佳且显著)、**AVE ≥ .50**、**CR ≥ .70**。
3. **区分效度**：
   - Fornell-Larcker：每个构念 **√AVE > 它与其他构念的相关系数**。
   - **HTMT** < .85（严格）/ .90（宽松）。
4. AVE 计算：AVE = Σ(标准化载荷²)/题项数；CR = (Σ载荷)² / [(Σ载荷)² + Σ(1−载荷²)]。

> EFA vs CFA 别混用同一批数据"先探索再验证"而不分样本——理想做法是**折半**或另取样本交叉验证。

## 五、报告示例（中/英）
> 中：各分量表 Cronbach's α 介于 .82–.91，组合信度 CR 均大于 .70，平均方差抽取量 AVE 介于 .53–.68，均大于 .50，标准化因子载荷介于 .61–.88（p<.001），表明量表具有良好的信度与收敛效度。各构念 AVE 的平方根均大于其与其他构念的相关系数，区分效度良好。
> EN: Cronbach's α ranged from .82 to .91 and CR exceeded .70 for all subscales. AVE ranged from .53 to .68 (all > .50), with standardized loadings between .61 and .88 (p < .001), supporting good reliability and convergent validity. The square root of each AVE exceeded the inter-construct correlations, indicating adequate discriminant validity.

## 信效度自检
- [ ] 反向题已计分（见 `02`）
- [ ] 报告了 α（必要时 CR）且达标，删题有理由
- [ ] 分清并正确做了 EFA 或 CFA
- [ ] EFA 报告 KMO/Bartlett/解释方差/旋转后载荷
- [ ] CFA 报告拟合指数 + 载荷 + AVE + CR + 区分效度
- [ ] 收敛与区分效度均有证据

## 关键参考
- Hair et al. (2019). *Multivariate Data Analysis* (8th ed).
- Fornell & Larcker (1981). Evaluating SEM with unobservable variables.
- Henseler, Ringle & Sarstedt (2015). HTMT criterion.
- 吴明隆 (2009).《结构方程模型——AMOS 的操作与应用》.
