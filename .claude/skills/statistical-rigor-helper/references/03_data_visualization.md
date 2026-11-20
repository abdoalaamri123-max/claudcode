# Chapter 3: Data Visualization
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/03-chap.html*

## Core concepts
- Two distinct goals: **exploration** (discover structure, generate hypotheses for yourself) vs. **presentation** (communicate one finding clearly to others). Decide which one a plot is for — the right chart type differs.
- **Grammar of graphics**: any plot = (1) data, (2) geometric object/mark (`geom`: point, bar, line, box, violin, hex...), (3) aesthetic mappings of variables to visual properties + a scale for each (linear/log/rank), (4) coordinate system, (5) a statistical transform (`stat`) applied before drawing, (6) optional faceting into small multiples, (7) layout/theme. Python: plotnine implements this literally; matplotlib/seaborn implement the same ideas less explicitly (seaborn `estimator=`/`kind=` ~ stat/geom choice).
- **Layers**: one plot can overlay multiple geoms/stats on the same data (e.g., raw points + smoothed trend + confidence band). Each layer is a separate analytical claim — justify each independently, don't add a trend line just because the API makes it a one-liner.
- Every geom has an implicit default **stat** computed before rendering: bar→count, histogram→bin+count, smooth→loess/lm fit, density→KDE, ecdf→empirical CDF. Know what statistic is being computed under the hood before trusting the shown shape.
- Fidelity ladder for comparing univariate distributions across groups, worst to best: bar-of-means (worst) → boxplot → violin/density → dot/beeswarm/raw points (best if N is modest) → ECDF (most rigorous, lossless). Prefer showing individual points or the full distribution over any single summary statistic whenever N is small/moderate.
- Extra dimensions beyond x/y: encode via color, shape, size, alpha, or faceting (small multiples by a categorical or binned-continuous variable). `geom_point`-type marks technically support x, y, fill, color, shape, size, alpha simultaneously (~7 dims) — but stacking more than 1-2 of these on one geom becomes indecipherable. Facet instead of overloading aesthetics.
- Plot **shape (aspect ratio)** is an analytic parameter, not cosmetic. Two rules of thumb: (1) if both axes are in the same units, force equal/fixed aspect ratio (`coord_fixed()`; Python: `ax.set_aspect('equal')`) — e.g. PCA component 1 vs. 2, or log-ratio vs. log-ratio; (2) if axes are in different units, consider **banking to 45°**: choose the aspect ratio so the median absolute slope of the line ≈ 1, which reveals rate-of-change features (e.g. sunspot-cycle example: banking exposed a saw-tooth shape invisible at the default square aspect ratio, even though the plot took less space).
- Color perception is 3-dimensional (e.g. HCL: hue/chroma/luminance). Palette *type* must match data *type*: **qualitative** (unordered categories), **sequential** (low→high continuum), **diverging** (continuum with a meaningful zero/reference midpoint). ColorBrewer defines all three (Python: `seaborn.color_palette`, matplotlib named colormaps like `viridis`/sequential, `RdBu_r`/diverging).

## Common mistakes / pitfalls
- **Barplot of group means**: collapses an entire distribution into one number, hiding skew, multimodality, outliers, *and* sample size. The book states this plainly: "given the amount of space they take, barplots are a poor way to visualize data" — and calls it "outright misleading" when the mean isn't representative (skewed/multimodal/outlier-laden data). Watch for this in any biology figure showing bars + error bars with no visible points.
- **Overplotting**: raw scatter of many points collapses to a "featureless black mass" in dense regions, hiding internal structure. Naive fixes have their own blind spots: alpha/transparency alone still saturates where points are dense; 2D density contours or KDE smoothing can make small, real, isolated point clusters (rare subpopulations, outlier regions) disappear entirely from the plot.
- **Density/violin plots hide sample size**: two groups with very different N can be drawn with identical visual weight (same peak height, same area). Always check or require n to be shown alongside any density/violin comparison.
- **Smoothing bandwidth is a hidden researcher degree of freedom**: too narrow → spurious "wiggly" peaks; too wide → real peaks/modes get smoothed away. A "peak," "shoulder," or claim of bimodality that only appears at one bandwidth choice is suspect.
- **Modality claims are scale-dependent**: "the number of modes of a density depends on scale transformations of the data, via the chain rule" — the same data can look unimodal on log scale and bimodal on the raw (linear) scale, or vice versa. Never assert "this distribution is bimodal" as a biological fact without stating the scale, and check both.
- **Apparent trends from uneven point density**: plotting y against a raw x can produce a fake-looking trend or heteroscedasticity purely because points are denser in one region of x. Classic example in the chapter (MA-plot-style): variance of M looked like it depended on A in the raw scatter, but re-plotting M against `rank(A)` showed the dependency was a density artifact, not real.
- **Heatmap/dendrogram ordering looks like data structure but is largely an aesthetic choice**: hierarchical-clustering leaf order is arbitrary at every internal node (each branch can flip without changing the tree's topology or fit), so a visually striking "block" in a heatmap may not reflect any statistically meaningful grouping. Don't over-interpret adjacency/block patterns without checking whether they're robust to the ordering/linkage method (Python: `seaborn.clustermap`, `scipy.cluster.hierarchy`).
- **Equal-width binning for faceting a continuous variable** (`cut`) gives panels with very unequal n; comparing panels then implicitly compares apples with wildly different sample sizes. Use quantile-based cuts if panels need comparable n.
- **Adding a regression/smoothing line just because it's easy** is not always meaningful — the chapter explicitly poses this as a check: is it appropriate to summarize this scatter with a trend line at all (right functional form, no confound, no Simpson's-paradox-style subgroup structure)?
- **Color scale misuse**: (a) using a sequential/rainbow-style palette for inherently diverging data (e.g. log-fold-change, z-scores) obscures which values are above vs. below the reference/zero — must use a diverging palette with the midpoint fixed at the meaningful value (Python: `matplotlib.colors.TwoSlopeNorm(vcenter=0)` with `RdBu_r`/`coolwarm`); (b) letting hue, chroma, and luminance all vary freely in a categorical palette makes some categories perceptually "louder" than others (irradiation illusion: light regions look bigger than dark ones of equal area) — fix chroma/luminance and vary only hue; (c) light pastel colors work for area fills but are too low-contrast for lines/points on a white background, which need dark, low-luminance marks.
- **"Laziness" and "getting carried away"** are both named as failure modes: laziness = accepting default plot settings without thinking about whether they fit the data; getting carried away = adding visual decoration/complexity with no added informational payoff, cluttering the message.

## Assumptions to verify
- Is the mean actually a representative summary of this distribution (not skewed / multimodal / dominated by outliers)? If unsure, do not reduce it to a bar-of-means.
- When comparing distributions across groups (density/violin/ECDF), are sample sizes comparable — or does n need to be shown/annotated so the reader isn't misled?
- Does a claimed density feature (mode, shoulder, bimodality) survive changing the bandwidth/bin-width, and changing the scale (raw vs. log)?
- Does an apparent scatterplot trend or heteroscedasticity survive re-plotting against `rank(x)` instead of raw `x`?
- Are the two plotted axes in genuinely the same units (requiring fixed/equal aspect ratio — e.g. PCA components, log-ratio vs. log-ratio) or different units (aspect ratio is a free display choice, candidate for banking)?
- Is the color-scale type (qualitative/sequential/diverging) actually matched to the data's structure (unordered categories vs. ordered continuum vs. signed continuum around a real reference point)?
- If a heatmap/clustering-based row-column order is shown, would the qualitative conclusion survive a different, equally valid ordering or linkage method?
- If a continuous variable was binned for faceting or coloring, were the bins chosen for equal width or equal count — and does that choice affect the comparison being drawn?
- Is a fitted trend/smoothing line on a scatterplot actually warranted, or was it added by default?

## Diagnostic checks
- Redraw any bar-of-means figure as a boxplot + jittered/beeswarm points (or violin) and check whether the message changes. (Python: `seaborn.boxplot`/`violinplot`/`swarmplot`/`stripplot`.)
- For scatterplots with many points (roughly >1000), check for overplotting; if present, compare a raw alpha-blended scatter against a hexbin or 2D-density version, and confirm outlier/sparse regions aren't silently dropped (re-overlay raw points in sparse regions if they matter). (Python: `plt.hexbin`, `seaborn.kdeplot(x,y,fill=True)`.)
- Refit the KDE/histogram at 2-3 different bandwidths or bin widths; only trust features that are stable across them.
- Re-plot the same variable on both log and linear scale before asserting anything about the number of modes/peaks.
- Re-plot y vs. `rank(x)` alongside y vs. `x` to check whether an apparent variance-vs-x or trend pattern is a point-density artifact rather than real.
- For heatmaps, try an alternate ordering (e.g., order by first principal component, or a different linkage method) and see whether the same visual blocks persist.
- Check whether n per group is visible somewhere in or near any density, violin, or bar plot.
- For color-encoded continuous data, confirm whether the variable has a meaningful zero/reference point; if yes, verify the palette is diverging and centered there, not sequential.
- If faceting on a discretized continuous variable, check panel sample sizes are roughly balanced (or note the imbalance).

## Quick checklist
- [ ] No bars-of-means without also showing distribution/points (box, violin, beeswarm, or ECDF).
- [ ] Sample size n shown or stated wherever distributions are compared visually.
- [ ] Overplotting checked in any dense scatterplot; alpha/hexbin/density used appropriately, without silently dropping outliers.
- [ ] KDE bandwidth / histogram bin-width treated as a parameter to stress-test, not a default to trust.
- [ ] No "bimodal"/"multimodal" claims without stating scale (raw vs. log) and checking both.
- [ ] Any scatterplot "trend" cross-checked against a rank-transformed axis to rule out a density artifact.
- [ ] Color-scale type matches data type: qualitative / sequential / diverging (diverging scale's midpoint fixed at the real reference value, e.g. 0 for log-fold-change).
- [ ] Fixed/equal aspect ratio used when both axes share units (PCA, log-ratios); banking considered for line/rate plots in different units.
- [ ] Heatmap block structure not over-interpreted as "real" without checking robustness to ordering/linkage choice.
- [ ] Every added visual element (extra layer, line, color, decoration) earns its place — no default-laziness, no unneeded visual candy.

## Key terms
- **Grammar of graphics** — data + geom + aesthetic mapping/scale + coordinate system + stat + facet + layout; the compositional model underlying ggplot2/plotnine.
- **Geom** — the geometric mark representing data (point, bar, line, box, violin, hex, ...).
- **Aesthetic (aes)** — mapping from a data variable to a visual property (x, y, color, fill, shape, size, alpha).
- **Stat** — the statistical transform computed before drawing (count, bin, density/KDE, ECDF, smooth/loess).
- **Faceting** (small multiples / trellis / lattice) — splitting one plot into subplots by one or more categorical (or binned continuous) variables; shows up to ~4-5 dimensions.
- **ECDF** (empirical cumulative distribution function) — lossless, assumption-free representation of a 1D sample's distribution; preferred over density/histogram when smoothing artifacts are a concern (Python: `seaborn.ecdfplot`, `statsmodels.distributions.ECDF`).
- **Banking (to 45°)** — choosing a plot's aspect ratio so the median absolute slope of a line ≈ 1, to make rate-of-change features (e.g. cyclic asymmetry) visible.
- **Hexagonal binning (hexbin)** — 2D-histogram-like binning for scatterplots; avoids both overplotting and the over-smoothing of density contours.
- **HCL color space** (hue/chroma/luminance) — perceptually-motivated color coordinates; fix chroma & luminance and vary only hue for a balanced categorical palette.
- **Qualitative / sequential / diverging palette** — the three palette classes (ColorBrewer convention) matched respectively to unordered categories, an ordered continuum, and a signed continuum around a meaningful midpoint.
- **Dendrogram/leaf ordering** — the row/column order imposed by hierarchical clustering in a heatmap; arbitrary at every internal branch, so not itself evidence of structure.
- **Chain rule effect on modes** — nonlinear rescaling of a variable (e.g. log vs. linear) changes the apparent number of modes of its density; modality is not scale-invariant.
