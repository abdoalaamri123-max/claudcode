# Chapter 5: Clustering
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/05-chap.html*

## Core concepts

- Clustering assigns a categorical group label to objects based on (dis)similarity. It is **descriptive/exploratory**, not inferential — there is generally no ground truth and no p-value for "this clustering is real."
- Two families of methods:
  - **Partitioning** (k-means, k-medoids/PAM): fix k up front, alternate center-estimation and point-assignment.
  - **Hierarchical (agglomerative)**: bottom-up merging into a tree; k is chosen later by cutting the tree.
  - **Density-based** (DBSCAN): finds regions of high density separated by sparse regions; no k needed, handles non-convex shapes.
- Distance/metric choice is the foundational, and most subjective, decision — different metrics on the same data legitimately answer different scientific questions.
  - Euclidean: `d(A,B) = sqrt(sum((a_i-b_i)^2))`. Assumes features are commensurable and uncorrelated.
  - Minkowski (L_m): generalizes Euclidean (m=2), Manhattan/L1 (m=1, sum of abs differences), Chebyshev/L∞ (m→∞, max abs difference).
  - Mahalanobis / weighted Euclidean: rescales by the (co)variance structure of the features — accounts for differing dynamic range and correlation between features. Needed whenever features are correlated or on different scales but you don't want to lose that structure by pre-scaling.
  - Jaccard distance (`1 - f11/(f01+f10+f11)`): for presence/absence data where co-occurrence is more informative than co-absence (mutations, OTUs, ecological data). Ignores double-absence (f00).
  - Correlation-based distance: `d(A,B) = sqrt(2*(1-cor(A,B)))` — 0 for perfectly correlated, sqrt(2) for uncorrelated, 2 for perfectly anti-correlated.
  - Hamming/edit distance: for character/sequence data (mutations, genotypes); may need substitution-cost weighting for biological sequences.
  - Gower's distance: mixed categorical + continuous features.
  - Python: `scipy.spatial.distance.pdist/cdist` (metrics: `'euclidean'`, `'cityblock'`, `'chebyshev'`, `'minkowski'`, `'hamming'`, `'jaccard'`, `'mahalanobis'`, `'correlation'`).
- Hierarchical linkage choices and their behavior:
  | Linkage | Definition | Pros | Cons |
  |---|---|---|---|
  | Single (min jump / nearest neighbor) | `d12 = min_{i∈C1,j∈C2} d_ij` | good at finding elongated/chain clusters | comb-like trees, chaining artifact |
  | Complete (max jump) | `d12 = max_{i∈C1,j∈C2} d_ij` | compact, tight classes | one outlier point can distort groups |
  | Average | mean pairwise distance between clusters | similar-size, similar-variance clusters | not robust to outliers |
  | Ward | minimizes within-cluster variance (ANOVA-style) | very efficient, statistically motivated | forces small clusters if true variability is high |
  - Python: `scipy.cluster.hierarchy.linkage(method='single'/'complete'/'average'/'ward')`, `fcluster` to cut the tree, `dendrogram` to plot; `sklearn.cluster.AgglomerativeClustering`.
- k-medoids/PAM algorithm: pick k observations as seeds → assign each point to nearest center → recompute each center as the **medoid** (actual observation minimizing total in-cluster distance) → repeat until stable. k-means is the same but replaces the medoid with the arithmetic mean (centroid), so centers need not be actual data points.
  - Python: `sklearn.cluster.KMeans`; k-medoids via `sklearn_extra.cluster.KMedoids` or `scipy.cluster.vq` adaptation.
- DBSCAN: builds clusters from **density-reachability** — point q is directly density-reachable from p if within radius `eps` and p has ≥ `minPts` neighbors within `eps`; a cluster is a maximal set of mutually density-connected points with at least `minPts` members. Handles arbitrary cluster shapes and does not require specifying k, but is sensitive to `eps`/`minPts` and degrades sharply with added dimensions (curse of dimensionality — `eps` had to be raised from ~0.65 to ~0.95 going from 5 to 7 marker dimensions in the flow-cytometry example to keep finding groups of reasonable size).
  - Python: `sklearn.cluster.DBSCAN`, `sklearn.cluster.OPTICS`.
- Within-cluster sum of squares (WSS), the basic building block for validation:
  `WSS_k = Σ_ℓ Σ_{x_i∈C_ℓ} d²(x_i, x̄_ℓ)` — equivalently, `(1/2n_ℓ) Σ_i Σ_j d²(x_i,x_j)` summed over clusters (avg. pairwise in-cluster distance). WSS_k is monotonically decreasing in k and hits 0 when every point is its own cluster — **it is not by itself a criterion for choosing k**.
- Calinski-Harabasz index (variance-ratio criterion, ANOVA-F-like):
  `CH(k) = (BSS_k/WSS_k) × (N-k)/(N-1)`, where `BSS_k = Σ_ℓ n_ℓ (x̄_ℓ - x̄)²`. Pick k maximizing CH(k).
  - Python: `sklearn.metrics.calinski_harabasz_score`.
- Gap statistic (Tibshirani, Walther & Hastie 2001) — compares observed log(WSS) to log(WSS) on reference ("no cluster structure") data:
  1. Compute `log(WSS_k)` on the real data for a range of k.
  2. Generate B reference datasets from a homogeneous/uniform (no-cluster) distribution with the same dimensions/range; compute `log(W*_kb)` for each, b=1..B.
  3. `gap(k) = mean_b(log W*_kb) - log(WSS_k)`.
  4. `sd_k` = std dev of `log(W*_kb)` across b; pick the smallest k such that `gap(k) ≥ gap(k+1) - s'_{k+1}`, where `s'_{k+1} = sd_{k+1} * sqrt(1+1/B)` (the "1-SE rule"). An alternative simpler rule is just the first local maximum of gap(k).
  - No single canonical Python package; reimplement the algorithm or use a third-party `gap-stat` package — verify it matches this definition before trusting output.
- Silhouette index, per point i: `S(i) = (B(i) - A(i)) / max(A(i), B(i))`, where A(i) = mean distance to other points in i's own cluster, B(i) = mean distance to points in the nearest other ("neighboring") cluster.
  - Interpretation: S(i) near +1 → well-clustered; near 0 → point sits on/near a cluster boundary; negative → likely assigned to the wrong cluster. Average silhouette across points/clusters is a standard way to compare candidate k values.
  - Python: `sklearn.metrics.silhouette_score` (mean) and `silhouette_samples` (per point).
- Cluster stability / resampling ("tight clusters", "strong forms"): repeat clustering on bootstrap subsamples (e.g. 67% of samples without replacement), predict held-out points' membership from each run's centers, build a consensus clustering, and measure each run's agreement with the consensus (agreement ≈ 1 = stable/reproducible partition; low/diffuse agreement = no stable structure at that k). This is the most direct way to avoid over-trusting a single clustering run.
- Computational complexity: all-pairs distance computation is O(n²) in time and memory; classic hierarchical clustering (e.g. naive `hclust`) is O(n³) in time — becomes impractical for very large n (n=10^6 → ~4 TB distance matrix). k-means/PAM-style methods are O(n) per iteration since they only track distances to the (fixed, small) number of centers, not all pairs. Fast hierarchical implementations exist (`fastcluster`); scale method choice to n.

## Common mistakes / pitfalls

- **Treating cluster output as biologically "real" without validation.** Clustering algorithms are designed to always produce clusters, even on pure noise or randomly scattered points (cf. WWII London bombing map: clusters appeared visually in data later revealed to be spatially random). Absence of validation is itself a red flag.
- **Choosing k by eyeballing a plot or picking a "nice-looking" number** instead of using WSS/elbow, Calinski-Harabasz, gap statistic, silhouette, or resampling stability — and especially never reporting *which* criterion was used or whether several disagree.
- **Not scaling/standardizing features before Euclidean-distance clustering.** Any feature on a larger numeric scale (or measured in different units) will dominate the distance and thus the clustering, regardless of its actual biological importance. Decide explicitly whether "equal importance per feature" is the intended assumption.
- **Using plain Euclidean distance for the wrong data type**: presence/absence or mutation data (should use Jaccard/binary distance), highly correlated or differently-scaled features (should use Mahalanobis), sequence data (should use Hamming/edit distance), compositional/count data (consider correlation-based or transformed distances). Mismatched metric silently produces a wrong-shaped answer.
- **Ignoring cluster instability under resampling or reinitialization.** k-means/PAM results depend on random seed choice; rerunning with a different seed or subsample can change cluster assignments substantially. A clustering that is not reported alongside a stability/agreement check should be treated as provisional.
- **Clustering on features contaminated by a confound** (batch, sequencing depth, total count, library size) rather than biological signal. E.g., restricting to top-variable genes is partly a defense against many weakly informative genes' small individual batch effects accumulating and swamping true signal — clustering on raw high-dimensional data without any feature selection/confound control risks recovering the confound structure, not biology.
- **Treating clustering output as if it carried a p-value or hypothesis-test-style significance.** There is no general null-hypothesis test for "this clustering is correct" — the closest available tools are comparisons against reference/null distributions (gap statistic) and stability under resampling, and even these are diagnostics, not p-values.
- **Using WSS alone to pick k.** WSS_k decreases monotonically and trivially reaches 0 when k = n (every point its own cluster) — it must be compared across k via an elbow, or benchmarked against a null/reference distribution (gap statistic), never minimized outright.
- **Over-reading dendrogram leaf order/adjacency.** In a dendrogram, sibling subtree order is arbitrary (the tree can be "rotated" at any internal node, like a mobile) and horizontal spacing carries no meaning — only vertical (linkage height) does. Two leaves adjacent in the plot need not be evolutionarily/biologically close (non-monophyletic neighbors). Do not narrate a story from left-right leaf position.
- **Forcing k-means/PAM onto non-convex, very unequal-sized, or unequal-density clusters.** These methods implicitly assume clusters are blob-shaped and comparably sized; a genuinely larger or odd-shaped true cluster will get split up, or points misassigned. Diagnostic: plot the data (or a 2D projection) and check whether clusters look convex/blob-like before trusting k-means/PAM output; consider DBSCAN or hierarchical clustering with single/complete linkage for irregular shapes.
- **Ignoring differing group frequencies/densities when doing distance-threshold ("nearest center") assignment** (e.g., OTU-style taxonomic assignment). Groups with very different abundances/sizes will show different apparent "radii" purely from sampling more instances of the same per-observation error — equal-radius assignment is a manifestation of the representativeness heuristic (Tversky & Kahneman) and is a known bias, not a neutral default.
- **Not transforming skewed/heavy-tailed intensity data before clustering** (e.g., raw flow/mass cytometry counts) — bimodal structure that clearly separates two populations may be invisible until a variance-stabilizing transform (e.g., asinh) is applied.
- **Reporting one clustering method/parameterization as "the" answer.** The chapter's own methodology is to compare multiple gene-set sizes × multiple k × multiple methods and look for a subpopulation structure that recurs across all of them — a robust finding should not depend on one arbitrary choice.
- **DBSCAN `eps`/`minPts` tuned once and reused blindly across differing dimensionality or feature subsets.** As more markers/features are added, distances concentrate (curse of dimensionality) and `eps` typically must increase just to keep finding non-trivial clusters — this is a symptom to check for, not a parameter to "set and forget."

## Assumptions to verify

- Are the chosen features on comparable scales, or does scaling/standardization need to happen before computing distances? (Confirm explicitly, don't assume.)
- Does the distance metric match the data type and the scientific question (continuous vs. correlated vs. binary/presence-absence vs. compositional vs. sequence)?
- Are the features free of confounds (batch, depth, total count) that could dominate the distance structure, or has some correction/feature-selection step addressed this?
- Is it plausible that clusters are roughly convex and comparable in size (justifying k-means/PAM), or should shape/density-based or hierarchical methods with non-Ward linkage be preferred?
- Has k been chosen by an explicit, stated criterion (elbow/WSS, CH index, gap statistic, silhouette), rather than by inspection alone?
- Has the stability of the clustering been checked under resampling/reinitialization, or is a single run being reported as final?
- Is there independent biological information (markers, known cell types, survival outcome, treatment response) available to help validate that the discovered groups are meaningful, rather than relying on the clustering algorithm's internal criteria alone?
- Is n large enough, and the algorithm's complexity (O(n²) distance matrix, O(n³) naive hierarchical clustering) small enough, to be computationally tractable — or is an approximate/scalable method needed?

## Diagnostic checks

- Plot WSS_k (or log WSS_k) vs. k and look for an elbow — but corroborate with at least one other criterion below; a decreasing curve alone is not sufficient.
- Compute the Calinski-Harabasz index across a range of k and pick the maximizer.
- Run the gap statistic: compare log(WSS_k) on the real data to log(WSS) on B reference datasets simulated with no cluster structure (uniform, or same covariance but homogeneous); use the 1-SE rule or first local maximum to pick k.
- Compute silhouette scores (mean and per-point) for candidate k; near-zero or negative points indicate ambiguous/misassigned observations and a possibly poor choice of k.
- Bootstrap/resample the data (e.g., cluster 67% subsamples repeatedly), build a consensus clustering, and measure per-run agreement with the consensus — low or diffuse agreement means the "cluster" is not stable/reproducible at that k.
- Rerun k-means/PAM with several different random seeds/initializations and check whether assignments (not just WSS) are consistent.
- Visualize the actual data (scatterplots, 2D projections across different feature pairs, density contours) before trusting any distance-based clustering — check that clusters actually look separated and roughly convex if using k-means/PAM.
- If using a dendrogram/heatmap, check the length of inner branches near the cut point — short inner branches mean weak evidence for that split; don't over-trust visually "clean-looking" heatmap blocks produced purely by reordering rows/columns.
- Cross-check clustering results across multiple reasonable choices (different distance metrics, different feature subsets/gene-set sizes, different k) — a finding that only appears under one specific configuration is fragile.
- If clusters are being interpreted biologically, cross-tabulate against known labels/annotations/outcomes (e.g., contingency table of cluster assignment vs. known sample group) as external validation, keeping in mind this is confirmatory, not a formal significance test.

## Quick checklist

- [ ] Distance metric matches data type (continuous/correlated → Euclidean or Mahalanobis; binary/presence-absence → Jaccard; sequences → Hamming/edit; mixed types → Gower).
- [ ] Features scaled/standardized before distance computation, or a deliberate reason given not to.
- [ ] Confounds (batch, depth, total count) checked for and addressed (e.g., feature selection, covariate adjustment) before clustering.
- [ ] k chosen via an explicit criterion (WSS elbow, Calinski-Harabasz, gap statistic, silhouette) — not by eye.
- [ ] Cluster stability checked via resampling/bootstrap or multiple random seeds/initializations.
- [ ] Cluster shape assumption checked — non-convex/unequal-size data routed to DBSCAN or non-Ward hierarchical linkage rather than forced into k-means/PAM.
- [ ] No p-value or significance claim attached to "this clustering is correct" — only stability/validation diagnostics.
- [ ] Dendrogram interpretation limited to vertical branch structure/heights; no meaning read into leaf left-right order or non-monophyletic adjacency.
- [ ] Biological/external validation attempted (known markers, labels, outcomes) rather than relying solely on internal clustering criteria.
- [ ] For DBSCAN specifically: `eps`/`minPts` re-tuned when dimensionality or feature set changes, and behavior checked for curse-of-dimensionality symptoms.
- [ ] Computational method (naive hierarchical vs. k-means vs. optimized libraries) appropriate for the sample size n.

## Key terms

- **Medoid**: an actual observation chosen as a cluster center (used in PAM/k-medoids), vs. **centroid**: the arithmetic mean of cluster members (used in k-means), which need not be an observed data point.
- **Linkage**: the rule for computing distance between two already-formed clusters during agglomerative clustering (single, complete, average, Ward).
- **WSS / BSS**: within-cluster / between-cluster sum of squared distances; used to build validation criteria like Calinski-Harabasz.
- **Gap statistic**: comparison of observed within-cluster dispersion to that expected under a reference "no cluster structure" distribution, used to choose k.
- **Silhouette index**: per-point measure of how well-matched a point is to its own cluster vs. the next-best (neighboring) cluster.
- **Tight clusters / strong forms**: clusters that recur reliably across repeated/resampled clustering runs, used as evidence of genuine structure.
- **Density-reachability**: DBSCAN's core notion — points connected through a chain of sufficiently dense, mutually nearby neighborhoods (radius `eps`, minimum neighbor count `minPts`).
- **Curse of dimensionality**: as the number of features grows, pairwise distances tend to concentrate/become less discriminative, degrading density- and distance-based clustering unless parameters (e.g., DBSCAN's `eps`) are adjusted.
- **Representativeness heuristic**: cognitive bias (Tversky & Kahneman) of assigning objects to the nearest group "center" without accounting for differing group frequencies/densities — a caution against naive equal-radius distance-based classification.
- **Cophenetic distance**: the height in a dendrogram at which two objects are first joined into the same cluster; used to compare/evaluate hierarchical trees.
