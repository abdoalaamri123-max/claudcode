# Chapter 0-1: Introduction & Generative Models for Discrete Data
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/00-chap.html and 01-chap.html*

## Core concepts

- **Two directions of reasoning.** *Top-down / generative*: assume a probability model with known parameters, deduce the distribution of any event by math or simulation. *Bottom-up / statistical modeling*: start from data, infer/fit the model that could have produced it (Ch. 2). Know which direction an analysis is actually doing — deduction from assumed-known parameters is a much stronger (and more fragile) claim than inference from data.
- **Generative models are building blocks, not the finish line.** Simple models (Bernoulli, binomial, Poisson, multinomial) let you compute a reference/null distribution against which real data can be compared. Always ask: what is the null/reference model here, and is it the "interesting" one to reject?
- **Exchangeability → sufficiency.** If order/position doesn't matter (the random variable is exchangeable), the vector of level counts captures all relevant information — a legitimate data compression. One common way trials become exchangeable is if they are independent. Don't rely on this compression if order/position actually carries information (e.g., spatial or temporal structure).
- **Bernoulli → binomial → Poisson → multinomial**, in order of generality:
  - Bernoulli: single binary trial, parameter `p` = P(success).
  - Binomial `B(n,p)`: count of successes in `n` iid Bernoulli trials. `P(X=k) = C(n,k) p^k (1-p)^(n-k)`. Python: `scipy.stats.binom(n, p)`.
  - Poisson(λ): approximates `B(n,p)` when `p` is small and `n` is large, with `λ = np`. Good model specifically for **rare events**. Depends only on the product `np`, not on `n` and `p` individually — useful for combining variable "opportunity" (e.g., different sequence lengths) into one rate. `P(X=k) = λ^k e^{-λ}/k!`. Python: `scipy.stats.poisson(lam)`.
  - Multinomial: generalizes binomial to >2 categorical outcomes/levels (e.g., A/C/G/T counts); probabilities across levels must sum to 1. Python: `scipy.stats.multinomial(n, p)`.
- **Poisson mean = variance = λ**, so SE = `sqrt(λ)`. This is a load-bearing identity: it is the reference against which real count data should be checked (see Diagnostic checks).
- **Monte Carlo / simulation** is a first-class alternative to closed-form probability calculations, especially once a problem isn't analytically tractable. Precision of a Monte Carlo estimate is limited by its "granularity": with `B` simulations, estimated probabilities cannot be resolved finer than roughly `1/B`. To credibly claim a probability is below some small threshold (e.g. `<1e-6`), you need many more than `1/threshold` simulated trials, not just `1/threshold`.
- **p-value ≠ probability the hypothesis is true.** A p-value is `P(data | H0)`, not `P(H0 | data)`. Keep this distinction explicit in any write-up.
- **Power** = P(reject H0 | HA true) = true positive rate. Conventional target: **power ≥ 0.80** when planning experiments/sample size. A test with 80% power still misses the true effect 20% of the time if repeated.
- **Choice of null hypothesis requires scientific judgment, not just mathematical convenience.** The null should be a "straw man" whose rejection is actually interesting — a null that's already known to be biologically implausible (e.g., "all 4 nucleotides equally likely" for real genomic DNA) may be easy to reject but scientifically uninteresting.
- **Large p, small n problem**: with many more features/parameters (e.g., p=20,000 genes) than samples (e.g., n=200), ordinary multivariate models become non-identifiable / overfit. Remedies: regularization/sparsity (assume most parameters are zero or near-zero), or empirical Bayes (borrow strength by assuming groups of parameters are similar rather than estimating each independently from scratch).
- **Multiple testing arithmetic**: with per-test false-positive rate α and p independent null tests, expected false positives ≈ `p × α`. Example from the book: α=0.05, p=20,000 → ~1000 expected false positives if nothing is real. This is the reason for multiple-testing correction (Ch. 6) whenever many features/hypotheses are tested at once.
- **EDA before/with CDA.** Exploratory data analysis (visualize first, let the data suggest structure) should precede or accompany confirmatory/hypothesis-driven analysis; iterate at different resolutions/perspectives rather than committing to one pass of Fisher-style "hypothesize → design → collect → test."
- **Reproducibility as infrastructure**: treat the analysis script/notebook as a lab notebook — one coherent, re-runnable record (equivalent practice in Python: a versioned Jupyter/quarto notebook or script under git), not a one-off interactive session whose steps aren't preserved.

## Common mistakes / pitfalls

- **Selection / "look-elsewhere" effect on extreme values.** Worked example: scanning 100 independent positions and reporting the probability of the *single* largest observed count (7) as if only one position had been examined. Naive calc: `P(X≥7)` for one Poisson(0.5) ≈ `1e-6`. Correct calc accounts for having taken a max over 100 positions: `P(max over 100 ≥ 7) = 1 − (1−ε)^100 ≈ 1 − e^{-100ε} ≈ 100ε ≈ 1e-4` — about **100× larger**. Whenever a reported extreme value/p-value was the max (or min) selected out of many candidates (positions, genes, clusters, thresholds), the per-candidate tail probability must be corrected for the number of candidates scanned — do not report the single-comparison p-value for a value you found by scanning many.
- **Treating "independent" as literally exactly true.** In practice complete independence rarely holds; the assumption is really that any real correlations/dependencies are weak/rare enough that ignoring them is a good approximation. Silent violation of this (e.g., spatially or temporally correlated measurements, batch effects, shared upstream noise) breaks the variance formulas of binomial/Poisson/multinomial and invalidates downstream p-values and power calculations.
- **Dropping unobserved categories from a count table.** A naive tally over observed values only will silently omit a category that had zero occurrences; a properly defined categorical/factor variable with pre-declared levels will still report it with count zero. Missing-zero categories can distort goodness-of-fit statistics and expected counts.
- **Confusing p-value direction**: reporting/interpreting `P(data|H0)` as if it were `P(H0|data)`.
- **Using the theoretical chi-square approximation when it doesn't apply.** The weighted sum-of-squares goodness-of-fit statistic `Σ (E_i − x_i)² / E_i` is only well-approximated by a χ² distribution under adequate conditions; it breaks down when some categories/boxes have very low expected probabilities and mostly-zero counts. In that regime, use a simulation/Monte-Carlo-derived null distribution instead of the χ² table value.
- **Assuming a model's parameters are "known" when they are actually estimated.** The clean deductive (top-down) probability calculations in this chapter only work because the false-positive rate, number of trials, and independence were all *stipulated* as known. Real analyses almost always have to estimate these from data first (Ch. 2) — that estimation step adds uncertainty that a purely deductive calculation ignores.
- **Reporting a p-value to many significant digits as if the underlying model were exact.** Both the naive (`1e-6`) and corrected (`1e-4`) probabilities in the epitope example were below standard significance thresholds (0.05, 0.01, 0.001), so the reject/accept decision didn't change — but the two numbers differ 100-fold, which would matter if the exact magnitude of the p-value itself is the deliverable (e.g., forensic/legal contexts, or when the same discrepancy would flip a decision at a stricter threshold).

## Assumptions to verify

- Are trials/observations actually **independent**, or only approximately so? What correlated structure (batch, spatial, temporal, shared library prep, phylogeny) could break it?
- Is the process actually **exchangeable** (order/position truly irrelevant), justifying compressing data down to counts?
- Is `p` (per-trial probability) actually **small** and `n` actually **large** enough that a Poisson approximation to a binomial is reasonable — or are you in a regime where the full binomial (or something else) is needed?
- Are all "known" parameters (false-positive rate, rate λ, per-category probabilities) truly known, or were they estimated from the same or related data (in which case extra uncertainty must be propagated)?
- If reporting an extreme/max/min statistic, did you select it from a larger set of candidates (positions, genes, tests)? If so, is the reported probability corrected for that selection?
- Is the chosen null hypothesis actually a scientifically interesting straw man, or a convenient-but-implausible baseline whose rejection tells you nothing new?
- If testing many features/hypotheses at once, is a multiple-testing correction applied, or is a single-test threshold (e.g., α=0.05) being used naively p times?

## Diagnostic checks

- **Mean vs. variance check for count data.** For a true Poisson(λ), mean ≈ variance ≈ λ (SE = √λ). Compute both from your data: if observed variance is much larger than the mean, the data are **overdispersed** relative to Poisson — a plain Poisson model is the wrong choice and a model that allows extra variance (e.g., a mixture/negative-binomial-type model, covered in later chapters) is needed instead.
- **Expected-count check for chi-square goodness-of-fit.** Before trusting a χ² p-value from a sum-of-squares statistic, check whether any category has very low expected count / mostly-zero observed count; if so, don't trust the χ² approximation — use a simulated null distribution instead.
- **Compare a histogram of a simulated null statistic to the theoretical distribution** before relying on the theoretical one, especially in non-standard cases (sparse categories, small samples, non-independence).
- **Power check via simulation**: simulate under a plausible alternative and compute the fraction of simulated datasets for which your test/threshold rejects H0 — this is your empirical power; compare against the 0.80 convention before trusting a planned sample size.
- **Selection-adjusted tail probability**: if reporting `P(observed extreme ≥ x)`, recompute it as `1 − (1 − ε)^N` (or via simulation of the max/min over N draws) where `ε` is the single-draw tail probability and N is the number of candidates scanned — not just `ε` itself.

## Quick checklist

- [ ] Identify whether the analysis step is top-down (deduce from assumed model) or bottom-up (infer model from data) — don't blur the two.
- [ ] State the null model explicitly and justify why rejecting it would be scientifically interesting.
- [ ] Check independence/exchangeability assumptions against the actual experimental design (batches, spatial/temporal structure, shared processing).
- [ ] For count data modeled as Poisson: verify variance ≈ mean; flag overdispersion.
- [ ] For binomial→Poisson approximations: confirm `p` small, `n` large.
- [ ] If an extreme/max/min value was selected from many candidates, correct the reported probability for the number of candidates (don't report the single-comparison tail probability).
- [ ] For χ²-type goodness-of-fit statistics: check for categories with low expected/zero counts; fall back to simulation if present.
- [ ] If testing many features, apply multiple-testing correction rather than a flat per-test α.
- [ ] If claiming a probability is very small via simulation, confirm the number of Monte Carlo trials is well in excess of `1/probability` (simulation granularity ≈ `1/B`).
- [ ] Distinguish "known" parameters from estimated ones; don't treat estimated parameters as if their uncertainty is zero.
- [ ] Confirm p-values are reported/interpreted as `P(data|H0)`, never as `P(H0|data)`.
- [ ] Verify categorical/count tallies preserve zero-count categories rather than silently dropping unobserved levels.

## Key terms

- **Generative model**: a probability model from which data could plausibly have been produced; enables computing probabilities of any event by deduction or simulation given known parameters.
- **Bernoulli trial**: single binary (success/failure) event with probability `p` of success.
- **Binomial `B(n,p)`**: number of successes in `n` independent, identically-distributed Bernoulli trials.
- **Poisson(λ)**: distribution for counts of rare events; limiting case of binomial as `n→∞`, `p→0`, `np=λ` fixed; mean = variance = λ.
- **Multinomial**: generalization of binomial to more than two outcome levels (e.g., 4 nucleotides), with `Σp_i = 1`.
- **Exchangeable**: random variable/sequence whose joint distribution doesn't depend on the order of observations.
- **Sufficient statistic**: a summary (e.g., counts) that captures all information in the data relevant to the model's parameters.
- **Rank statistic / extreme value analysis**: ordering observations to study the distribution of the maximum/minimum; needed whenever "the biggest value we saw" is the quantity of interest.
- **Monte Carlo method**: using computer-generated random draws from a model to approximate probabilities that are hard or impossible to get analytically.
- **Power**: P(reject H0 | HA true); conventional target ≥ 0.80.
- **Null distribution**: the distribution of a test statistic under H0, obtained either analytically (e.g., χ²) or by simulation.
- **Empirical Bayes**: estimating many related parameters jointly by borrowing strength across them, rather than independently from scratch.
- **Overdispersion**: observed variance exceeding what the assumed model (e.g., Poisson) predicts from the mean — a signal that the model is misspecified.
