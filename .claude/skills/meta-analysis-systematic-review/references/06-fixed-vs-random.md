# 06 · 固定效应 vs 随机效应模型

> 合并效应量前要选模型。选错会误导合并值与置信区间。社科多数情形用**随机效应**。

## 一、两种模型的假设

| | 固定效应 fixed-effect | 随机效应 random-effects |
| --- | --- | --- |
| 假设 | 所有研究估计**同一个真效应**，差异仅来自抽样误差 | 各研究的真效应**不同**，来自一个效应分布 |
| 加权 | 逆方差（大样本权重大） | 逆方差 + 研究间方差 τ²（权重更均衡） |
| 推断范围 | 仅这些研究 | 可推及更广的研究总体 |
| 何时用 | 研究高度同质、功能上相同 | 研究间存在真实异质（社科常态） |

## 二、怎么选

- **默认随机效应**：社科/教育/心理研究在人群、干预、测量上几乎总有真异质，随机效应更现实、更保守。
- 固定效应仅当你有充分理由相信所有研究估计同一效应（罕见）。
- **别用"I² 不显著就固定效应"**这种机械规则——模型选择应基于**研究是否概念上同质**，而非异质性检验是否显著（检验力受研究数影响）。

## 三、加权与合并

- 逆方差加权：权重 = 1/方差（随机效应再加 τ²）。
- 合并效应 = 加权平均；给出合并估计 + 95%CI + z/p。
- **随机效应还应报预测区间（prediction interval）**：描述未来单个研究真效应的可能范围，比 CI 更能体现异质性的实际含义。

## 四、τ² 的估计方法

- 随机效应的研究间方差 τ² 有多种估计器：DerSimonian-Laird（经典但可能低估）、**REML（推荐）**、Paule-Mandel 等。
- metafor 默认 REML；报告时说明用了哪种。

## 五、少量研究时的注意

- 研究很少（如 <5）时 τ² 估计不稳，随机效应 CI 可能过窄 → 用 **Hartung-Knapp-Sidik-Jonkman（HKSJ）调整**得到更稳健的 CI（metafor 支持）。

## 六、常见误区
- ❌ 机械按"I² 是否显著"选模型。
- ❌ 明明异质却用固定效应（CI 过窄，假显著）。
- ❌ 随机效应不报预测区间。
- ❌ 少量研究用 DL 不做 HKSJ 调整。

## 关键参考
- Borenstein, M., et al. (2021). *Introduction to Meta-Analysis*（fixed vs random 章）.
- Borenstein, M., et al. (2017). Basics of meta-analysis: I² is not an absolute measure of heterogeneity. *Research Synthesis Methods, 8*.
- IntHout, J., et al. (2016). Plea for prediction intervals. *BMJ Open, 6*.
