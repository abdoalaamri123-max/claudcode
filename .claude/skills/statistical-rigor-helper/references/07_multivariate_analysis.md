# Chapter 7: Multivariate Analysis
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/07-chap.html*

## Core concepts

- A data matrix has observations (samples) in rows and variables (features) in columns. **Watch orientation**: RNA-seq/genomics data are conventionally stored *transposed* (features as rows, samples as columns) — always confirm which axis is which before feeding a matrix to a PCA function.
- **Centering**: subtract the column mean (mean of centered data = 0). **Scaling/standardizing**: divide by the column SD (new SD = 1). The correlation coefficient itself is just the dot product of two centered-and-scaled variables:
  ρ̂ = Σ(xᵢ-x̄)(yᵢ-ȳ) / [√Σ(xᵢ-x̄)² · √Σ(yⱼ-ȳ)²]
- PCA is an **unsupervised**, purely **linear** technique: it treats all variables symmetrically (no response/predictor distinction), using only linear combinations, f(ax+by) = a·f(x) + b·f(y). It is *not* regression — regressing x-on-y vs y-on-x gives two different asymmetric lines (minimizing vertical or horizontal residuals respectively); the PCA/first-principal-component line minimizes *orthogonal* distances instead, and is the same line regardless of which variable you'd call "response."
- Total variance ("inertia") of a centered point cloud decomposes as: (variance of points projected onto a candidate line) + (sum of squared orthogonal distances to that line) = constant. So the line that **minimizes** orthogonal residuals is exactly the line that **maximizes** variance of the projected points — this is why "maximize variance" and "best line fit" define the same first PC.
- Singular Value Decomposition (SVD) is the engine under PCA: X = U S Vᵀ, with UᵀU = I, VᵀV = I, and S diagonal with entries s₁ ≥ s₂ ≥ … ≥ 0 (singular values, decreasing). Rank of X = number of non-zero singular values.
- Principal components ("scores") = US (equivalently XV). **Loadings** = columns of V: the coefficients of the linear combination of original variables that defines each new PC axis.
- Eigen-decomposition link: XᵀX = V S² Vᵀ = V Λ Vᵀ. Eigenvalues λₖ = sₖ² = variance of the k-th principal component. PCs are always ordered by decreasing eigenvalue/variance.
- Number of usable components k ≤ min(n, p), n = #observations, p = #variables.
- If X is centered and scaled to unit variance per column, the eigenvalues of the covariance matrix sum to p (the number of variables) — a useful sanity check (book's turtles example: Σsₖ²/(n−1) = 3 = number of variables).
- **Biplot** = scores + loadings plotted together: points (observations) plus arrows (variables) in the same PC plane. The angle between two variable-arrows approximates their correlation; arrow length approximates how well that variable is captured ("quality of representation") in that specific 2D plane — a short arrow means the variable is poorly represented by these two PCs, not that it's unimportant overall.
- **Correlation circle**: variables plotted as arrows inside/on a unit circle; only variables whose arrows approach the circle's radius (length ≈ 1) are well summarized by the plotted plane.
- **Weighted PCA**: if experimental groups are unequally represented (e.g. very unbalanced sample-group sizes), unweighted PCA lets the larger group's variance dominate the leading PCs. Reweight rows (e.g. weight = 1/group size) before decomposition to give each group equal influence.

## Common mistakes / pitfalls

- **Skipping centering/scaling when variables have different units or wildly different scales.** PCA on the raw covariance matrix is scale-sensitive: a variable with 10x the SD of another dominates PC1 even if it isn't more biologically important. Book's example: decathlon 110m-hurdles SD ≈ 0.51 vs 1500m SD ≈ 13.66 — over an order of magnitude apart; standardize first, or deliberately choose covariance vs correlation matrix and justify the choice.
- **Python-specific trap**: `sklearn.decomposition.PCA` only *centers* by default — it does **not** standardize. Skipping an explicit `StandardScaler` step before PCA silently means "PCA on the covariance matrix," which is scale-dominated whenever input units/ranges differ.
- **Over-interpreting loadings/correlation-circle directions causally, or literally.** Sign of a loading/PC is arbitrary (flipping it changes nothing about eigenvalues), and the *encoding direction* of a variable matters: e.g. race times (lower = better) vs. throw/jump distances (higher = better) point in "opposite" raw directions even though both reflect athletic ability. Flip signs of oppositely-coded variables before reading correlations off a loading plot, and never claim PCA "explains" or "causes" anything — it is exploratory/descriptive only, not inferential.
- **Choosing the number of retained PCs (k) via a fixed variance-explained cutoff (e.g. "80%") without looking at the scree plot's shape.** When several consecutive eigenvalues are close in magnitude, the *subspace* they span is well defined but the individual axes/loadings within it are not: a small perturbation of the data can rotate them arbitrarily while spanning the same subspace ("unstable" PCs). A hard percentage cutoff can slice straight through such a tied group. Always look for a clear elbow/drop in the screeplot before fixing k.
- **A top PC reflecting a technical artifact rather than biology.** The book's T-cell expression PCA plot flags a mislabeled sample as an outlier along a PC axis; unbalanced experimental groups (e.g. far more E3.25 than E4.5 samples in the Hiiragi mouse data) let the largest group dominate the leading PC unless samples are reweighted. Always project known technical/experimental covariates (batch, processing date, group size, sample order, genotype/litter pairing) onto the PC scatter before concluding a PC axis reflects the biology of interest.
- **Reading Euclidean distances/angles off a PCA plot without checking how much variance the plotted axes actually capture.** A plot built on a low-variance PC2, or on only 2 of many needed PCs, can visually suggest tight clustering or separation that isn't real — always report/annotate % variance explained by each plotted axis.
- **Not fixing the aspect ratio of PCA plots** (`coord_fixed()` / `ax.set_aspect('equal')`). Because eigenvalues are sorted decreasing, var(PC1) ≥ var(PC2) always — a correctly scaled PCA plot is always at least as wide as tall. An unequal-aspect or square plot visually inflates later PCs and distorts the geometry (distances/angles) shown in a biplot or correlation circle.
- **Running PCA on non-linear structure.** PCA only finds linear combinations / flat-subspace structure. If the true structure is curved or manifold-like, PCA still "succeeds" numerically but its axes won't track the real structure — a non-linear method is the correct tool instead (out of this chapter's scope, but flag the mismatch when the data look non-linear in pairwise scatterplots).
- **Outliers dominating the top PCs.** Because PCA maximizes variance (a squared-distance criterion), a handful of extreme or mislabeled points can single-handedly define the direction of PC1 or PC2. Screen for outlier influence before trusting the leading components.
- **Using PCA when you actually have a specific outcome/response variable to predict or explain.** PCA is unsupervised and symmetric across variables; use regression or another supervised method instead when there is a designated response.

## Assumptions to verify

- Data are continuous/numeric (or at least ordinal/roughly interval); raw counts or sparse zero-inflated data (OTU tables, unfiltered mass spec, scRNA-seq counts) may need transformation (log, variance-stabilizing) before PCA — check the frequency of zero/near-zero values first.
- Variables are on comparable scales, OR the choice to use the covariance matrix (unscaled) vs. correlation matrix (scaled) has been made deliberately and is justified by whether original units/relative variances are meaningful.
- The relationships you care about are (approximately) linear combinations of the measured variables — check pairwise scatterplots/correlation heatmap for obviously non-linear or non-monotonic bivariate relationships *before* running PCA.
- Sample groups are balanced, or unequal group sizes have been accounted for (weighted PCA), so no single group's within-group variance swamps the between-group signal of interest.
- No single extreme outlier/mislabeled sample is dictating PC1/PC2 — screen with a first-pass PCA or simple univariate outlier check.

## Diagnostic checks

- Look at pairwise scatterplots and the correlation matrix/heatmap *before* PCA to build intuition about the data's "true" dimensionality and which variables cluster together.
- Always produce and inspect the **screeplot** (eigenvalues / variance explained, decreasing order) before deciding k. Look for a clear elbow/drop; be suspicious of near-equal consecutive eigenvalues (unstable subspace).
- Report/annotate the % variance explained by each PC axis actually shown in any 2D/3D score plot.
- Use fixed/equal-aspect axes for any PCA scatterplot or biplot; a region wider than tall is expected and correct (var(PC1) ≥ var(PC2)).
- Build a correlation circle / loadings plot alongside the scores plot; trust only loadings whose arrow length is close to the unit-circle radius (well represented in that plane).
- Color/facet the PC score plot by every available metadata covariate (batch, processing date, sex, genotype, litter/pairing, sample order, library size/cell count) to check whether a leading PC tracks a technical confound rather than biology.
- Cross-check implementation-specific output: different PCA functions/packages differ in naming and sometimes in scaling convention for "loadings" vs "scores" (R's `prcomp`, `princomp`, `dudi.pca`, raw `svd` all format output differently) — verify exactly which matrix you're looking at. In Python, distinguish `sklearn.decomposition.PCA.components_` (loadings, unit-norm rows) from `.transform(X)` (scores), and confirm `explained_variance_ratio_` is being read/plotted correctly.
- As a hand-rolled-PCA sanity check: verify UᵀU ≈ I, VᵀV ≈ I, and (for standardized data) Σλₖ ≈ p.

## Quick checklist

- [ ] Confirm matrix orientation (samples in rows, features in columns) before running PCA.
- [ ] Decide, explicitly, whether to center-only or center-and-scale (correlation vs covariance matrix) — check variable units/SDs first; in Python, remember `sklearn.decomposition.PCA` does NOT scale by default.
- [ ] Inspect pairwise scatterplots/correlation heatmap before PCA.
- [ ] Always view the screeplot before choosing k; watch for near-tied eigenvalues (unstable axes) and avoid rigid variance-% cutoffs.
- [ ] Annotate every PC scatter/biplot with % variance explained per axis, and use equal-aspect axes.
- [ ] Color the score plot by all known technical covariates (batch, date, group size, litter/pairing) to rule out a confound driving PC1/PC2.
- [ ] Check for and assess the influence of outliers/mislabeled samples before trusting the leading PCs.
- [ ] Reweight observations if experimental groups are strongly unbalanced.
- [ ] Don't over-interpret loading sign/direction without checking the natural encoding direction of each variable.
- [ ] Remember PCA is unsupervised, linear, and exploratory — not causal, not a substitute for regression/supervised analysis, and not appropriate for strongly non-linear structure.

## Key terms

- **PCA (Principal Component Analysis)**: unsupervised linear dimension-reduction method finding orthogonal directions of maximal variance.
- **SVD (Singular Value Decomposition)**: X = U S Vᵀ; the linear-algebra machinery underlying PCA. Python: `numpy.linalg.svd` (returns `Vt`, the transpose of R's `V`).
- **Singular value / eigenvalue**: sₖ / sₖ² = λₖ; λₖ is the variance captured by the k-th PC.
- **Loadings**: coefficients (columns of V) defining each PC as a linear combination of original variables. Python: `PCA.components_` (rows).
- **Scores**: coordinates of observations in the new PC space (= US = XV). Python: `PCA.transform(X)`.
- **Scree plot**: bar/line plot of eigenvalues (or % variance explained) in decreasing order; primary tool for choosing k.
- **Biplot**: combined plot of scores (points) and loadings (arrows) in the same PC plane.
- **Correlation circle**: unit-circle plot of variable loadings/correlations with the PC axes.
- **Rank (of a matrix)**: number of non-zero singular values; minimal number of rank-1 pieces needed to reconstruct X exactly.
- **Inertia**: total variance of the (centered) point cloud; decomposes across PCs.
- **Orthonormal**: unit-norm and mutually perpendicular (UᵀU = I); unrelated to the normal distribution.
- **Weighted PCA**: PCA where observations are given unequal weights (e.g. inverse group size) before decomposition.
