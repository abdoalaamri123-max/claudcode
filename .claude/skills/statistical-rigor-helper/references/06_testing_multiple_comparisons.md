# Chapter 6: Testing (Hypothesis Testing & Multiple Comparisons)
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/06-chap.html*

## Core concepts

- **Five steps of a valid hypothesis test** (in this order, decided *before* seeing the data):
  1. Pick the effect of interest and a **test statistic**.
  2. Set up a **null hypothesis** → derive/simulate the **null distribution** of the test statistic under it.
  3. Choose the **rejection region**: the subset of outcomes whose total null probability is small (≤ α).
  4. Collect data, compute the test statistic.
  5. Reject the null if the statistic falls in the rejection region.
  Violating this order (choosing the hypothesis, statistic, or region *after* looking at the data) is the root cause of p-hacking/HARKing (see below).

- **p-value** = probability, under the null, of seeing a test statistic at least as extreme as observed. Equivalent framing: transform the test statistic to `[0,1]` via its null CDF; by construction the p-value is **Uniform(0,1) under a true, continuous null**. This uniformity is the basis of the p-value-histogram diagnostic, the BH procedure, and the two-groups model.

- **Type I/II error table** (single test):
  | | H0 true | H0 false |
  |---|---|---|
  | Reject | Type I error (false positive), rate = α = FPR | True positive |
  | Don't reject | True negative | Type II error (false negative), rate = β = FNR |
  - `1 − α` = specificity. `1 − β` = **power** = sensitivity = true positive rate.
  - Reducing one error type increases the other; α = 0.05 is a historical convention, not a law of nature — the right threshold is context-dependent.

- **t-test statistic**: `t = c · (m1 − m2) / s`, `c = sqrt(n1·n2/(n1+n2))`, `s` = pooled SD, under normality/equal-variance/independence gives the t-distribution with `n1+n2−2` df. Variants: one- vs two-sample, paired vs unpaired, equal-variance vs Welch (unequal variance).

- **Permutation tests**: only assume **exchangeability** of observations under the null (strictly weaker than the t-test's iid-normal assumption). Use the same test statistic but derive its null distribution empirically by shuffling group labels. Agreement between permutation and parametric p-values is expected but not guaranteed (Central Limit Theorem territory) — don't assume it.

- **Multiple testing framework** (m tests): `m0` true nulls, `m − m0` true alternatives, `R` rejections, `V` = false positives among rejections (Type I), `T` = false negatives (Type II).

- **FWER** (family-wise error rate) = `P(V > 0)`. Under independence: `P(V>0) = 1 − (1−α)^m0 → 1` as `m0` grows. Controlling FWER means guaranteeing near-zero probability of *any* false positive across the whole family.

- **Bonferroni method**: to get FWER ≤ α_FWER over m tests, use per-test threshold `α = α_FWER / m`. Simple, conservative, valid under any dependence structure — but the threshold becomes vanishingly small as m grows, killing power.

- **FDR** (false discovery rate) = `E[ V / max(R,1) ]` — the *expected proportion of false positives among rejections*, not a per-test guarantee. FDR = FWER when all nulls are true (`V = R`). Because it's an expectation, the realized false discovery *proportion* in any one experiment can be higher or lower than the nominal FDR.

- **Benjamini–Hochberg (BH) procedure** (controls FDR at level `φ`):
  1. Sort p-values ascending: `p(1) ≤ p(2) ≤ … ≤ p(m)`.
  2. Find the **largest** `k` such that `p(k) ≤ φ · k / m`.
  3. Reject hypotheses `1, …, k`.
  Equivalent graphical view: plot sorted p-values vs. rank, draw a line through the origin with slope `φ/m`; reject everything at or left of the **rightmost** crossing point. Python: `statsmodels.stats.multitest.multipletests(pvals, alpha=φ, method='fdr_bh')`.

- **Two-groups model** (mixture view of the p-value distribution): `f(p) = π0 + (1−π0)·f_alt(p)`, where `π0` = fraction of true nulls, `f_alt` = density of p-values under the alternative.
  - **Local fdr**: `fdr(p) = π0 / f(p)` — probability that a hypothesis with p-value exactly `p` is a false positive; monotonically increasing in `p`.
  - **Tail-area Fdr**: `Fdr(p) = π0·p / F(p)`, `F(p) = ∫₀ᵖ f(t)dt` — average FDR among all hypotheses rejected at threshold `p`. This is what BH approximately targets.
  - fdr/Fdr are local vs. total (marginal vs. average cost analogy) — Fdr/FDR is a **set property** of the whole rejected batch; fdr is a property of one hypothesis. Neither is a p-value, and **the terms "corrected p-value"/"adjusted p-value" are misleading** for exactly this reason (they suggest a per-hypothesis quantity where none may exist) — despite this, "adjusted p-value"/"q-value" remains standard practical shorthand for the BH-derived per-feature value; treat it as an FDR-scale threshold, not a probability attached to that one gene/protein.

- **Independent hypothesis weighting (IHW)**: use an auxiliary **covariate** to give hypotheses unequal weight in the testing procedure, increasing power over plain BH. A valid covariate must be:
  1. **statistically independent of the p-value under the null**, but
  2. **informative about power and/or π0** (i.e., correlated with whether H0 is true / how strong the alternative signal is).
  Example: `baseMean` (mean normalized read count) in RNA-seq — low-count genes have underpowered tests (p-values concentrate near uniform/null-like regardless of truth), high-count genes have well-powered tests. IHW puts more of the α "budget" into strata where rejections are likely, less into strata with essentially no power. Python: no widely-adopted native port; practical approximation = stratify hypotheses into covariate bins and apply BH within each stratum (manual "independent filtering"), or call Bioconductor's `IHW` via `rpy2`.

- **Testing vs. classification**: hypothesis testing is for the **asymmetric** case — a default/uninteresting state (null) vs. a rare/interesting one (alternative) that you'd only act on given strong evidence. Symmetric two-way decisions with no default belong to classification (different objectives/assumptions) — don't force a classification problem into a testing framework or vice versa.

## Common mistakes / pitfalls

1. **No multiple-testing correction at all.** Reporting per-test p < 0.05 as "significant" across many genes/variants/pixels/clusters without any FWER or FDR correction. This is the textbook jellybean/xkcd-882 mistake scaled to genomics (thousands to billions of tests). Flag any multi-hypothesis analysis whose "significant" list came straight from raw p-values.

2. **Wrong correction family for the goal.** FWER/Bonferroni is appropriate only when a *single* false positive across the whole family is unacceptable (e.g., one definitive confirmatory claim, forensic/legal matching). For exploratory screens with downstream follow-up (the overwhelming majority of biology: differential expression, GWAS, marker screens), **FDR/BH is the right tool and has far more power** — Bonferroni's per-test threshold `α/m` becomes unusable for large m. Using Bonferroni "to be safe" in a discovery/screening context is a real and common power-destroying error; using BH where a single false claim would be catastrophic is the opposite error.

3. **p-value hacking.** Trying multiple test statistics, normalizations, outlier-removal rules, or subgroups until some p < α appears "by chance" (with m analysis choices, ~1 in 20 will cross α=0.05 purely by chance for each choice tried). Violates the "decide before seeing data" rule.

4. **HARKing** (Hypothesizing After Results are Known). Presenting a hypothesis discovered by exploring the data as if it had been the pre-specified one. Related and needs the same scrutiny as p-hacking.

5. **Non-independence inflating significance (pseudo-replication).** Treating technical replicates, duplicated samples, or correlated measurements as independent observations shrinks p-values dramatically with **zero new biological information**. Concrete demonstration from the book: duplicating the exact same `PlantGrowth` dataset (n doubled, means/effect size unchanged) took the t-test from p = 0.047 to p = 0.0036. Any pipeline that inflates apparent n by mixing levels of replication (e.g., pretending 8 plants × 2 technical replicates = 16 independent samples) is invalid.

6. **Double-dipping / selecting hypotheses on the same data used to test them.** E.g., picking "high-variance" genes, or an eyeballed cluster split, from the dataset and then testing for differences using that same data — the selection is not independent of the test statistic under the null, so resulting p-values are anti-conservative and multiple-testing correction on them is invalid. Requires either a held-out/independent dataset, sample splitting, or a selection procedure provably independent of the test under the null (see independent filtering, next).

7. **Invalid covariate for filtering or weighting ("independent filtering" done wrong).** Filtering hypotheses (e.g., dropping low-count genes before testing) or weighting them (IHW) is a *valid, power-increasing* technique **only if** the filter/weight covariate is independent of the p-value under the null. Common failure: filtering or weighting by a quantity that is itself derived from the test statistic or the same contrast (e.g., filtering by observed effect size, or by a covariate correlated with the test statistic even when H0 is true). This breaks the null-uniformity of the surviving p-values and invalidates FDR control on the filtered set — it is functionally a subtler form of double-dipping. Always check with a stratified p-value histogram/ECDF that null p-values look uniform *within* each stratum of the covariate.

8. **One-sided test misuse.** Switching to a one-sided test after seeing which direction the effect went (to roughly halve the p-value) is invalid — the direction of a one-sided alternative must be fixed by prior knowledge, before the data are seen. Default to two-sided unless there is a genuine, pre-specified reason to only care about one direction.

9. **Optional stopping / repeated peeking.** Re-running an experiment, or checking significance partway through data collection and stopping as soon as p < α, inflates the false-positive rate exactly like running multiple uncorrected tests (the book's own coin-flip Q: "if we repeated the whole procedure, might we then reject the null?" — yes, with elevated probability). Requires a pre-specified sample size/stopping rule, or a proper sequential-testing design with alpha-spending, not ad hoc peeking.

10. **Confusing statistical significance with effect size / biological significance.** A p-value is a *necessary but not sufficient* condition for "interesting" — it conflates true effect size with sample size (the same real effect gives a smaller p-value with more data; see the duplication example above, which shows this mechanically). Never report or act on significance alone; always pair it with an effect-size estimate (fold-change, mean difference, confidence/credible interval) and ask whether that magnitude is biologically meaningful.

11. **Skipping the p-value histogram.** Not plotting the p-value histogram before trusting a multiple-testing result is itself a methodological gap — it is described as "an important sanity check for **any** analysis that involves multiple tests." Absence of this plot in a writeup/notebook is a reviewable omission.

12. **Assuming BH validity without checking dependence.** Plain BH's FDR-control guarantee formally requires the p-values to be independent, or positively dependent in a specific technical sense (PRDS). Under arbitrary/negative dependence (e.g., strongly correlated features from shared batch/technical structure), plain BH can under-control FDR. Fallback: Benjamini–Yekutieli (BY, more conservative, valid under arbitrary dependence — `statsmodels` `method='fdr_by'`), or explicitly model/remove the dependence structure first.

## Assumptions to verify

- **Test statistic matches the alternative you actually care about.** Different statistics have power against different alternatives (e.g., total-heads-count vs. a runs/streak statistic detect different kinds of coin unfairness) — a non-significant result only rules out the alternatives your chosen statistic is sensitive to.
- **Independence of observations** within a test — iid assumption behind both the binomial/t-test null distribution and the exchangeability assumption behind permutation tests. Check for hidden replication structure (technical vs. biological replicates, batches, paired samples) before trusting either.
- **Parametric assumptions of the null distribution** (e.g., normality and equal variance for the classic t-test) — data that are always positive, skewed, or count-based violate this; cross-check with a permutation test or the appropriate discrete/count-based test.
- **Paired vs. unpaired structure** must match the experimental design (measurements before/after on the same unit → paired test).
- **Exchangeability/independence of hypotheses** behind plain BH — see mistake #12 above.
- **Covariate independence under the null** for any filtering/weighting scheme (independent filtering, IHW) — see mistake #7. Verify empirically with stratified histograms/ECDFs rather than assuming it.
- **Direction of one-sided tests fixed a priori** — see mistake #8.
- **Order of the five steps was respected** — hypothesis, test statistic, and rejection region fixed before the data were examined. If this order was violated, treat resulting p-values as descriptive/hypothesis-generating only, and require replication on independent data or an explicit accounting of the effective search space (garden of forking paths).

## Diagnostic checks

- **Plot the p-value histogram first, always**, for any analysis with more than a handful of tests. Reading the shape:
  - **Flat/uniform everywhere** → consistent with all/mostly-null, i.e., little or no detected signal (could mean no real effect, or insufficient power — check power separately).
  - **Uniform "floor" + peak near 0** → the expected, healthy mixture: flat part = null component (`π0`), peak = true alternative signal.
  - **Peak near 0 with a shoulder trailing rightward** (not a clean spike) → mix of well-powered and under-powered alternatives; a classic sign that an informative covariate (e.g., read depth, abundance, effect size class) exists and stratifying/weighting (independent filtering, IHW) could recover power.
  - **Spikes concentrated at the right edge (near 1)** → often a **discreteness artifact** — e.g., low-count/low-n tests where the test statistic can only take a few discrete values, so p-values pile up near 1. Not necessarily a red flag, but re-examine whether the null approximation (asymptotic normal/t) is appropriate for those low-n tests, or filter them out.
  - **Hump/bulge in the middle, or any non-uniform shape when the tests are known/assumed to be (nearly) all null** → red flag for a broken independence assumption, unmodeled batch effect, or null-model misspecification. Diagnose by simulating data under a true null with the same dependence structure as the real data (e.g., morph from independent to correlated replicates) and confirming whether the histogram flattens or reproduces the same distortion.
  - **Anti-conservative excess mass near 0 with no plausible biological signal** → suspect pseudo-replication/non-independence or an unaccounted confounder/batch effect inflating apparent significance; cross-check against a permutation-based or batch-corrected null.
- **Visual/quick FDR estimate**: rough `π0 ≈ 2 · mean(p > 0.5)` (assumes the null p-values are uniform, so half of them exceed 0.5); then `estimated FDR at threshold α ≈ π0 · α / (fraction of p ≤ α)`.
- **BH graphical check**: sort p ascending, plot vs. rank `k`, overlay the line `y = φ·k/m` through the origin; the rejection set is everything at/left of the **rightmost intersection**.
- **Schweder–Spjøtvoll plot**: plot `(1 − p_i, N(p_i))` where `N(p)` = count of p-values `> p`. Under the null, this traces close to a straight line through the origin; fit a line to the left-hand portion (large `1−p`, i.e., large `p`) — its slope/intercept estimates `m0` (or `π0`), independent of the BH machinery. Useful cross-check against `π0` estimates from other methods.
- **Fit the two-groups mixture model** (e.g., via an fdrtool/qvalue-style approach; Python: the `qvalue` package implements Storey's q-value method, or fit `π0`/`f_alt` manually) to get `π0` and local fdr estimates, and sanity-check against the visual/BH-derived estimates above — large disagreement signals a modeling problem.
- **Stratify the p-value histogram / ECDF by a candidate covariate** (e.g., expression level, coverage, effect size bucket) before adopting it for independent filtering or IHW — confirm that (a) within-stratum null p-values still look uniform (independence under the null) and (b) `π0`/power visibly differs across strata (informativeness) — both conditions must hold.
- **Compare theoretical vs. simulated/permutation null distributions** for any parametric test whose assumptions are in doubt (normality, equal variance, independence) — large disagreement between the two invalidates the parametric p-value.
- **Simulate an all-null dataset with the real data's dependence structure** to directly check whether your actual type-I error is controlled at the nominal α (the book's own suggested exercise: morph simulated replicates from independent to highly correlated and watch the p-value histogram distort away from uniform).

## Quick checklist

- [ ] Is this a single confirmatory test, or one of many (m > 1) — if m > 1, is a multiple-testing correction applied at all?
- [ ] Is the correction method matched to the goal: FDR/BH for exploratory screening with follow-up, FWER/Bonferroni only when a single false positive is unacceptable?
- [ ] Was the hypothesis, test statistic, and rejection region fixed *before* looking at the data — any sign of p-hacking or HARKing (many statistics/pipelines tried, best one reported)?
- [ ] Are the tested units truly independent observations, or is there hidden pseudo-replication (technical replicates, duplicated rows, batch structure) inflating apparent n?
- [ ] Was any gene/feature/cluster selected using the same data it is then tested on (double-dipping)?
- [ ] If hypotheses were filtered or weighted by a covariate (independent filtering, IHW), is that covariate independent of the p-value under the null, and is this verified with a stratified histogram — not just assumed?
- [ ] Is a one-sided test used, and if so, was the direction fixed a priori (not chosen after seeing which way the data went)?
- [ ] Was there any optional stopping / repeated peeking at significance during data collection?
- [ ] Is statistical significance being reported/interpreted alongside an effect size, or on its own as if it implied biological importance?
- [ ] Has the p-value histogram been plotted and inspected for uniformity of the null component (flat baseline, no unexplained hump/bulge/edge spikes)?
- [ ] If BH/FDR was used, is there a reason to suspect strong negative or otherwise non-PRDS dependence among tests that would call for BY instead?
- [ ] Are "adjusted p-values"/q-values being correctly understood as FDR-scale thresholds on a set, not as per-hypothesis error probabilities?

## Key terms

- **Null hypothesis (H0)** — the default, tractable model of "nothing interesting happening," assumed true for computing the null distribution.
- **Alternative hypothesis** — the "interesting"/rare state one seeks evidence for.
- **Test statistic** — numerical summary of data used to distinguish H0 from the alternative.
- **Null distribution** — distribution of the test statistic under H0.
- **Rejection region** — subset of test-statistic outcomes, of small total null probability (α), that triggers rejecting H0.
- **Significance level (α)** — chosen false-positive rate / size of the rejection region; conventional but arbitrary default 0.05.
- **p-value** — probability under H0 of a result at least as extreme as observed; Uniform(0,1) under a true continuous null.
- **Type I error** — false positive (reject a true H0). **Type II error** — false negative (fail to reject a false H0).
- **FPR/specificity, FNR/power(sensitivity)** — false positive rate (=α) and its complement; false negative rate (β) and its complement (power).
- **FWER** — family-wise error rate, `P(V>0)`, probability of ≥1 false positive across all tests.
- **Bonferroni correction** — per-test threshold `α/m` to control FWER at α.
- **FDR** — false discovery rate, `E[V/max(R,1)]`, expected proportion of false positives among rejections.
- **Benjamini–Hochberg (BH)** — step-up procedure controlling FDR at a target level `φ` using ordered p-values.
- **Benjamini–Yekutieli (BY)** — FDR-controlling variant valid under arbitrary dependence (more conservative than BH).
- **Adjusted p-value / q-value** — BH-derived per-feature value; interpret as an FDR-scale threshold, not a per-hypothesis probability.
- **Two-groups model** — mixture `f(p) = π0 + (1−π0) f_alt(p)` describing the p-value distribution across many tests.
- **π0** — fraction of true null hypotheses among all tests.
- **Local fdr** — `π0/f(p)`, probability a specific p-value is a false positive (per-hypothesis quantity).
- **Tail-area Fdr** — `π0·p/F(p)`, average FDR among hypotheses rejected at threshold p (set property).
- **Exchangeability** — the (weaker than iid-normal) assumption underlying permutation tests: swapping labels doesn't change the joint distribution under H0.
- **Independent filtering** — dropping/down-weighting hypotheses using a covariate independent of the p-value under the null, to increase power without inflating FDR.
- **Independent hypothesis weighting (IHW)** — data-driven generalization of independent filtering that assigns hypothesis-specific weights from a covariate.
- **p-value hacking** — trying many analytic choices until a significant result appears.
- **HARKing** — hypothesizing after results are known; presenting post-hoc discoveries as pre-specified.
- **Double-dipping / data snooping** — selecting hypotheses/features using the same data subsequently used to test them.
- **Optional stopping** — inflating false-positive rate by repeatedly checking significance and stopping once a threshold is crossed.
- **Pseudo-replication** — treating non-independent measurements (technical replicates, duplicated data) as independent samples.
