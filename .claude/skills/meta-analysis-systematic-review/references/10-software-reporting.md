# 10 · 软件实操与 PRISMA 报告

> 元分析的计算与作图交给软件，重点是选对工具、跑对模型、报全。以 R 的 metafor/meta 为主线，兼顾 CMA/RevMan。

## 一、常用软件

| 软件 | 特点 |
| --- | --- |
| **R：metafor** | 最强大、灵活、免费；escalc 算效应量，rma 拟合模型，forest/funnel 作图，支持元回归、RVE、多层 |
| **R：meta / dmetar** | 语法友好，dmetar 配套教材《Doing Meta-Analysis in R》 |
| **CMA（Comprehensive Meta-Analysis）** | 商业、界面友好，入门快 |
| **RevMan** | Cochrane 官方，医学系统综述标准 |
| **Stata（metan/meta）** | 流行病学常用 |

## 二、R metafor 最小流程

```r
library(metafor)
# 1. 算效应量（如标准化均值差 SMD=Hedges' g）
dat <- escalc(measure="SMD", m1i=m1, sd1i=sd1, n1i=n1,
              m2i=m2, sd2i=sd2, n2i=n2, data=raw)
# 2. 随机效应模型（REML）
res <- rma(yi, vi, data=dat, method="REML")
summary(res)                 # 合并效应、CI、I²、τ²、Q
predict(res)                 # 预测区间
# 3. 森林图 / 漏斗图
forest(res); funnel(res); regtest(res)   # Egger
# 4. 元回归
rma(yi, vi, mods=~moderator, data=dat)
```

## 三、森林图（forest plot）怎么读

- 每行=一个研究：**方块=效应量点估计**（大小∝权重），**横线=95%CI**。
- 底部**菱形=合并效应**（宽度=合并 CI）。
- 竖线=无效应线（d=0 或 OR=1）：菱形是否跨过它=合并是否显著。
- 看研究间点估计分散程度直观感受异质性。

## 四、PRISMA 2020 报告清单

按 PRISMA 2020 的 **27 条清单**报告，关键：
- 结构化摘要、目的、纳排标准、信息源与**完整检索式**、筛选流程、数据提取、效应量、模型、异质性、偏倚风险、发表偏倚、结果（含森林图）、GRADE、局限、注册号。
- 附 **PRISMA 流程图**（见 `03`）。
- 用 `templates/reporting-checklist.md` 自查。

## 五、结果写作要点

- 报告：纳入研究数与总样本、合并效应量 + 95%CI + p、I²/τ²/预测区间、亚组/元回归、发表偏倚、偏倚风险/GRADE。
- 森林图 + 漏斗图入正文或附录。
- 讨论异质来源、局限、对实践/理论的含义。

## 六、常见误区
- ❌ 只报合并值，不报 I²/CI/偏倚检验。
- ❌ 不附检索式与 PRISMA 流程图（不可复制）。
- ❌ 软件默认设置照单全收却不理解（如默认 DL 而非 REML）。
- ❌ 森林图菱形跨 0 仍说"有显著效应"。

## 关键参考
- Viechtbauer, W. (2010). Conducting meta-analyses in R with metafor. *JSS, 36*(3).
- Harrer, M., et al. (2021). *Doing Meta-Analysis with R: A Hands-On Guide*.
- Page, M. J., et al. (2021). PRISMA 2020. *BMJ, 372*, n71.
