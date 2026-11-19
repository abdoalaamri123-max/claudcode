# 02 · 数据清洗与准备 / Data Cleaning & Preparation

> 顺序：剔除无效问卷 → 反向计分 → 缺失值 → 异常值 → 维度合成 → 准备分析。清洗过程要可追溯（记录每步剔除多少、为什么）。

## 一、剔除无效问卷 / Screening
剔除标准（在文中报告剔除数与标准）：
- 测谎/注意力题答错
- 规律作答（如全选同一项）、答案方差为 0
- 填答时长异常过短
- 关键变量大面积缺失
- 不符合纳入标准（如非目标人群）

## 二、反向题计分 / Reverse Coding
- 5 点量表：新值 = 6 − 原值；7 点：新值 = 8 − 原值（即"最大+1−原值"）。
- **务必在信度/因子分析前完成**，否则 α 被严重低估、因子结构错乱。
- SPSS：`转换 → 重新编码为不同变量` 或 `Compute: new = 6 - old`。
- R：`6 - x` 或 `psych::reverse.code()`。
- 自检：反向计分后，该题与同维度其他题应正相关。

## 三、缺失值 / Missing Data

### 诊断
- 计算每个变量与每个个案的缺失比例。
- 判断缺失机制：完全随机 MCAR / 随机 MAR / 非随机 MNAR（Little's MCAR 检验，p>.05 支持 MCAR）。

### 处理策略
| 方法 | 适用 | 备注 |
| --- | --- | --- |
| 成列删除 Listwise | 缺失少(<5%)且 MCAR | 简单但损失样本 |
| 均值/中位数替换 | 不推荐用于主分析 | 低估方差 |
| **多重插补 Multiple Imputation** | MAR、缺失较多 | 推荐，SPSS `多重插补`/R `mice` |
| **FIML（极大似然）** | SEM 分析 | AMOS/Mplus/lavaan 内置，首选 |
| EM 算法 | 连续变量 | SPSS `缺失值分析` |

- 经验：单变量缺失 <5% 且 MCAR，listwise 可接受；否则用 MI 或 FIML。
- SEM 中**优先 FIML**（lavaan: `missing = "fiml"`；AMOS 勾选 Estimate means and intercepts）。

## 四、异常值 / Outliers
- **单变量**：标准化分数 |z| > 3.29（p<.001）视为极端；或箱线图 IQR 法。
- **多变量**：马氏距离(Mahalanobis distance) 对照 χ² 临界值(df=变量数, p<.001)。
- 处理：核实录入错误→改正；真实极端值→可保留并做敏感性分析，或 winsorize；剔除需说明。
- 不要无理由删点来"美化"结果。

## 五、维度/总分合成 / Composite Scores
- 维度分 = 该维度题项**均值**（推荐，量纲一致）或加总。
- 合成前确认该维度信度达标（见 `04`）。
- 也可用因子得分(factor scores)，但均值法更透明常用。

## 六、其他准备
- 检查变量编码、值标签、变量类型设置正确（SPSS 变量视图）。
- 连续变量分组前慎重（中位数分组损失信息，回归优先保留连续）。
- 为后续分析建立清晰的变量命名（如 `SAT_mean`, `EE1..EE5`）。

## 清洗自检 / Checklist
- [ ] 记录了初始 N、剔除数与剔除标准、最终有效 N
- [ ] 反向题已正确反向计分并验证
- [ ] 缺失机制已判断、处理方法已选定并将报告
- [ ] 异常值已诊断与处理（说明）
- [ ] 维度分在信度达标后再合成
- [ ] 变量类型/标签/缺失码设置正确

## 关键参考
- Tabachnick & Fidell (2019). *Using Multivariate Statistics* (ch. 4).
- Enders (2010). *Applied Missing Data Analysis*.
- Little (1988). A test of MCAR for multivariate data.
