# 问卷数据分析流程图 / Analysis Flowcharts

> Mermaid 图，GitHub 直接渲染。需要图片时打开同目录 `index.html` 截图，或贴到 https://mermaid.live 导出 SVG/PNG。

## 图 1 · 问卷数据分析总流程 / Overall Workflow

```mermaid
flowchart TD
    A[原始问卷数据] --> B[数据清洗<br/>剔无效·反向计分·缺失值·异常值]
    B --> C[描述统计<br/>M/SD·偏度峰度·正态性]
    C --> D[共同方法偏差检验<br/>Harman / CLF]
    D --> E{信度与效度}
    E --> E1[信度 α/CR]
    E --> E2[效度 EFA / CFA · AVE]
    E1 --> F{达标?}
    E2 --> F
    F -- 否 --> G[删题/修订量表<br/>回到测量模型]
    G --> E
    F -- 是 --> H[假设检验<br/>差异/相关/回归/SEM/中介调节]
    H --> I[APA 报告<br/>表格+效应量+CI]

    style D fill:#fff3cd,stroke:#b7791f
    style F fill:#fff3cd,stroke:#b7791f
    style I fill:#d1f0e0,stroke:#138a5b
    style E fill:#e7efff,stroke:#2563eb
```

## 图 2 · 分析方法决策树 / Which Test to Use

```mermaid
flowchart TD
    Q{研究问题类型?}
    Q -- 比较组间差异 --> D1{几组? 因变量类型?}
    D1 -- 2组·连续 --> t[t 检验<br/>不满足前提→Mann-Whitney]
    D1 -- ≥3组·连续 --> anova[ANOVA<br/>不满足→Kruskal-Wallis]
    D1 -- 分类×分类 --> chi[卡方检验]
    Q -- 变量间关系 --> D2{要不要控制/预测?}
    D2 -- 仅关联 --> corr[相关分析<br/>Pearson/Spearman]
    D2 -- 预测 --> reg[回归分析<br/>多元/层次/逻辑]
    Q -- 复杂因果结构 --> D3{含潜变量/多路径?}
    D3 -- 是 --> sem[结构方程 SEM]
    D3 -- 含中介/调节 --> med[中介/调节<br/>Bootstrap/PROCESS]

    style t fill:#e7f7ef,stroke:#138a5b
    style anova fill:#e7f7ef,stroke:#138a5b
    style reg fill:#e7efff,stroke:#2563eb
    style sem fill:#fff3cd,stroke:#b7791f
    style med fill:#fff3cd,stroke:#b7791f
```

## 图 3 · EFA / CFA 选择与信效度判定 / EFA vs CFA

```mermaid
flowchart TD
    S{量表结构已知吗?}
    S -- 未知·自编/改编 --> EFA[探索性因子分析 EFA]
    S -- 已知·成熟量表 --> CFA[验证性因子分析 CFA]
    EFA --> EFA1[KMO≥.70<br/>Bartlett p<.05]
    EFA1 --> EFA2[提取因子<br/>载荷≥.50·删双载荷]
    EFA2 --> EFA3[累积方差≥50-60%]
    EFA3 -. 另一样本交叉验证 .-> CFA
    CFA --> C1[拟合指数<br/>χ²/df<3·CFI/TLI≥.90·RMSEA≤.08]
    C1 --> C2[收敛效度<br/>载荷≥.5·AVE≥.5·CR≥.7]
    C2 --> C3[区分效度<br/>√AVE>相关·HTMT<.85]
    C3 --> OK[测量模型成立]

    style EFA fill:#e7efff,stroke:#2563eb
    style CFA fill:#fff3cd,stroke:#b7791f
    style OK fill:#d1f0e0,stroke:#138a5b
```

## 图 4 · 中介 / 调节分析流程 / Mediation & Moderation

```mermaid
flowchart TD
    M{效应类型?}
    M -- 中介 X→M→Y --> MED[PROCESS Model 4<br/>或 lavaan]
    MED --> MED1[Bootstrap 5000 次<br/>求间接效应 a×b 的 95%CI]
    MED1 --> MED2{CI 含 0?}
    MED2 -- 否 --> MEDok[中介显著<br/>报间接效应大小]
    MED2 -- 是 --> MEDno[中介不成立]
    M -- 调节 X×W→Y --> MOD[变量中心化<br/>建交互项 X×W]
    MOD --> MOD1{交互项显著?}
    MOD1 -- 是 --> MODok[调节存在<br/>画简单斜率图 ±1SD]
    MOD1 -- 否 --> MODno[无调节效应]
    M -- 有调节的中介 --> MM[PROCESS Model 7/8/14<br/>调节中介指数 + Bootstrap CI]

    style MEDok fill:#d1f0e0,stroke:#138a5b
    style MODok fill:#d1f0e0,stroke:#138a5b
    style MED1 fill:#fff3cd,stroke:#b7791f
    style MM fill:#e7efff,stroke:#2563eb
```

> 提醒：中介判定看 **Bootstrap 95%CI 是否含 0**（不含 0 才显著），不要再用过时的 Baron-Kenny 逐步法单独下结论。详见 [`../references/07-sem-mediation.md`](../references/07-sem-mediation.md)。
