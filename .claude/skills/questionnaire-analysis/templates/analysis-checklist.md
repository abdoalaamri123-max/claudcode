# 问卷数据分析全流程自检表 / Analysis Workflow Checklist

> 按顺序推进，每步打勾。这也是论文「数据分析」一节的写作骨架。

## 0. 准备 / Prep
- [ ] 明确研究假设 H1…Hn 与对应变量、测量层次
- [ ] 确认样本量满足所用方法（回归/SEM/中介的经验法则，见 references/01）

## 1. 数据清洗 / Cleaning（references/02）
- [ ] 剔除无效问卷（测谎题/规律作答/超快/大面积缺失），记录初始与有效 N
- [ ] 反向题已反向计分并验证
- [ ] 缺失值机制判断 + 处理（MI / FIML）
- [ ] 异常值诊断（z>3.29 / 马氏距离）与处理
- [ ] 维度分在信度达标后合成

## 2. 描述统计 / Descriptives（references/03）
- [ ] 样本人口学描述表
- [ ] 各变量 M、SD、偏度、峰度
- [ ] 正态性判断（偏度<2、峰度<7、Q-Q）
- [ ] 共同方法偏差检验（Harman/CLF）— 自评横断面必做

## 3. 信度与效度 / Reliability & Validity（references/04）
- [ ] Cronbach's α（必要时 CR）达标，删题有据
- [ ] 分清 EFA（探索）/ CFA（验证）
- [ ] EFA：KMO、Bartlett、因子数、累积方差、旋转载荷
- [ ] CFA：拟合指数、载荷、AVE、CR、收敛与区分效度
- [ ] 相关矩阵（含对角线 α）

## 4. 假设检验 / Hypothesis Testing
- [ ] 差异检验：选对方法 + 检验前提 + 效应量 + 事后比较（references/05）
- [ ] 相关/回归：前提全检查（线性/独立/正态/同方差/VIF/影响点）+ 效应量（references/06）
- [ ] SEM：两步法（先 CFA 后结构）+ 完整拟合指数（references/07）
- [ ] 中介：Bootstrap CI（不含 0）+ 间接效应大小（references/07）
- [ ] 调节：中心化 + 交互项 + 简单斜率图（references/07）

## 5. 报告 / Reporting（references/08）
- [ ] APA 7 数值规范（斜体符号、p 值、小数前导 0、效应量、CI）
- [ ] 标准表格（描述/相关、信效度、回归、中介）
- [ ] 每个假设明确支持/不支持
- [ ] 前提违反/局限如实说明
- [ ] 因果措辞与设计匹配（横断面慎用因果词）

## 工具速记 / Tools
| 任务 | SPSS | AMOS | R |
| --- | --- | --- | --- |
| 信度 | 分析→刻度→可靠性 | — | psych::alpha |
| EFA | 分析→降维→因子 | — | psych::fa |
| CFA/SEM | — | 画路径图 | lavaan::cfa/sem |
| 回归 | 分析→回归→线性 | — | lm + car::vif |
| 中介/调节 | PROCESS 宏 | Bootstrap | PROCESS / lavaan |
