# 06 · 相关与回归 / Correlation & Regression

## 一、相关分析 / Correlation
| 类型 | 适用 |
| --- | --- |
| Pearson r | 两连续变量、线性、近正态 |
| Spearman ρ | 定序或非正态 |
| Kendall τ | 小样本定序、并列多 |
| 点二列 | 一连续一二分 |

- 报告：r 值、p、N；做成相关矩阵表（APA，见 `08`）。
- 解读：方向(±)、强度(.10/.30/.50)、显著性；相关 ≠ 因果。
- 警惕：相关 > .85 提示多重共线/构念重叠。

## 二、多元线性回归 / Multiple Regression

### 前提假设（务必检查）
1. 线性 Linearity（散点/残差图）
2. 残差独立 Independence（Durbin-Watson 约 1.5–2.5）
3. 残差正态 Normality（残差 P-P/直方图）
4. 同方差 Homoscedasticity（残差 vs 预测值无喇叭形）
5. **无多重共线性**：**VIF < 10**（严格 <5）、容忍度 Tolerance > .10、条件指数 < 30
6. 无强影响点（Cook's distance < 1）

### 操作与报告
- SPSS：`分析→回归→线性`，勾选共线性诊断、DW、残差图。
- 分类自变量需设**虚拟变量(dummy)**。
- 报告：
  - 整体：R²、调整 R²、F(df1, df2)、p；
  - 每个预测变量：非标准化 B、标准误 SE、**标准化 β**、t、p、95%CI；
  - 效应量 f²（.02/.15/.35 小中大）。
- R：`lm()` + `summary()` + `car::vif()`。

## 三、层次回归 / Hierarchical Regression
- 分步纳入变量块（如先控制变量，再自变量，再交互项）。
- 关注 **ΔR²** 及其显著性(F change)，判断新变量块的增量解释力。
- 常用于检验**调节效应**（自变量×调节变量，见 `07`）。

## 四、逻辑回归 / Logistic Regression
- 适用：**二分类因变量**（是/否、流失/留存）。
- 报告：回归系数 B、Wald χ²、p、**OR(Exp(B)) 及 95%CI**、模型 −2LL、Nagelkerke R²、Hosmer-Lemeshow 拟合(p>.05 好)、分类正确率。
- 多分类用多项逻辑回归；有序因变量用有序逻辑回归。

## 五、调节效应初步（详见 `07`）
- 连续变量交互前做**中心化(mean-centering)**或标准化以减共线、便于解释。
- 交互项 = 中心化自变量 × 中心化调节变量。
- 交互项显著即存在调节；用简单斜率(simple slope)图解释。

## 六、报告示例（中/英）
> 中：多元回归分析表明，模型整体显著，F(3, 296)=28.74, p<.001，解释了因变量 22.6% 的方差(调整 R²=.226)。其中工作满意度(β=.34, p<.001)和组织支持(β=.21, p=.002)显著正向预测离职意向，所有 VIF < 2，不存在多重共线性问题。
> EN: Multiple regression showed a significant model, F(3, 296)=28.74, p<.001, explaining 22.6% of the variance (adjusted R²=.226). Job satisfaction (β=.34, p<.001) and organizational support (β=.21, p=.002) were significant predictors; all VIFs < 2, indicating no multicollinearity.

## 自检
- [ ] 选对相关系数类型
- [ ] 回归前提全部检查（线性/独立/正态/同方差/共线性/影响点）
- [ ] 分类自变量已设虚拟变量
- [ ] 报告 R²/调整R²/F + 各变量 B/β/t/p/CI + 效应量
- [ ] 交互前做了中心化并用简单斜率解释

## 关键参考
- Cohen, Cohen, West & Aiken (2003). *Applied Multiple Regression/Correlation*.
- Field (2018). *Discovering Statistics Using IBM SPSS*.
- Aiken & West (1991). *Multiple Regression: Testing and Interpreting Interactions*.
