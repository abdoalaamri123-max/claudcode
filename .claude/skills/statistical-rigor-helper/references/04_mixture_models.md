# Chapter 4: Mixture Models
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/04-chap.html*

## Core concepts
- **Finite mixture**: density is a weighted sum of component densities, `f(x) = Σ_k λ_k φ_k(x)`, `Σλ_k=1`. Two-component case: `f(x)=λφ1(x)+(1−λ)φ2(x)`.
- **Infinite mixture**: number of components as large as (or larger than) the number of observations (e.g. the empirical distribution itself, or a hierarchical model with a continuous latent parameter per observation).
- Mixtures are built by **augmenting data with a latent/hidden label U**: `p(x,u|θ) = p(x|u,θ) p(u|θ)`. If U were observed, estimation splits into independent per-group MLEs (Eq 4.4) — this is what makes mixture fitting hard: U is *not* observed.
- **EM algorithm** alternates two steps until convergence:
  - **E-step**: given current parameters θ, compute each observation's **membership weight** (soft posterior probability of belonging to component k), e.g. `w(x,1) = λφ1(x) / [λφ1(x)+(1−λ)φ2(x)]`.
  - **M-step**: given membership weights, re-estimate θ via weighted MLE (weighted mean/SD per component; λ = mean of weights).
  - This is **soft assignment**: observations partially belong to multiple components, not hard 0/1 labels.
  - Directly maximizing the true marginal likelihood `L_marg(θ;x) = ∫_U p(x,u|θ) dU` is intractable; EM instead maximizes a tractable surrogate `Q(θ,θ_t) = ∫_U log p(x,u|θ) p(u|x,θ_t) dU` at each step (Eqs 4.6–4.9).
  - Always work with **log-likelihood**, not raw likelihood: (1) turns products into sums, so derivatives of a sum of per-observation terms are needed for MLE, not a product rule; (2) avoids floating-point underflow/overflow — even a few hundred multiplied probabilities can exceed the exponent range of double precision. See "log-sum-exp trick."
- **Component labels are arbitrary**: e.g. swapping component index 1↔2 together with λ↔(1−λ) in `f(x)=λφ1(x)+(1−λ)φ2(x)` gives the identical density. This exchangeability is the root cause of the "label switching" problem: different EM runs, bootstrap replicates, or software can report the "same" fit with components in a different order.
- **Zero-inflated mixture**: `f_zi(x) = λ·δ(x) + (1−λ)·f_count(x)`, where `δ` is a point mass at 0. Distinguishes **structural zeros** (true absence, e.g. species truly not in a habitat) from **sampling zeros** (present but not detected, drawn from `f_count`, which may itself yield zeros).
- **ECDF as an n-component mixture**: `f̂_n(x) = (1/n)Σ δ_{x_i}(x)` — the observed sample is a mixture of n point masses. This is the basis of the **nonparametric bootstrap**: resample from the empirical distribution (not the true, unknown F) to approximate the sampling distribution of any statistic `τ̂`.
- Nonparametric = number of parameters is as large as (or larger than) the sample size; the bootstrap (n components) qualifies.
- **Infinite mixtures as building blocks**: e.g. Laplace distribution = scale mixture of normals, `X = √W · Z`, `W ~ Exp(1)`, `Z ~ N(0,1)`. Asymmetric Laplace `AL(θ,μ,σ)`: `E(X)=θ+μ`, `Var(X)=σ²+μ²` — mean and variance are linked through the *same* latent variable, producing realistic mean-variance dependence seen in microarray/MS intensities and promoter lengths.
- **Gamma-Poisson mixture (= negative binomial distribution)**: generate rate `λ_i ~ Gamma(a,b)`, then `X_i ~ Poisson(λ_i)`. Two equivalent parameterizations: `(a,p)` or `(mean μ, dispersion α=1/a)`, with `Var = μ + αμ²`. Standard model for RNA-seq/count data overdispersion.
- **Variance-stabilizing transformation (delta method)**: if `Var(X_i)=v(μ_i)`, the transform `g` solving `g'(x) = 1/√v(x)` makes `Var(g(X_i))` ≈ constant. Concrete solved cases:
  - `v(μ)=μ` (Poisson) → `g(x)=√x`.
  - `v(μ)=αμ²` (constant coefficient of variation) → `g(x)=log(x)` — this is why log-transforms are so common for intensity/count data with CV roughly constant across the dynamic range.
  - `v(μ)=μ+αμ²` (gamma-Poisson/negative binomial) → `g_α(x) = (1/2√α)·arcosh(2αx+1)`, which behaves like `√x` for small x and like `log(x)` for large x.

## Common mistakes / pitfalls
- **Assuming the number of components K is known/fixed and never validated.** The EM machinery in this chapter *requires* K and the parametric family to be specified in advance; it does not choose them for you. Treat K as a modeling assumption to be justified, not a free parameter to scan and pick by best log-likelihood alone — log-likelihood is monotonically non-decreasing as K grows, so raw-likelihood-based selection systematically overfits K. (Formal model-selection tools such as BIC/AIC and cluster-validation methods are outside this chapter's scope — see the clustering chapter.)
- **Trusting a single EM run.** EM is only guaranteed to reach a local optimum of the likelihood; the trajectory (and the point it converges to) depends on the starting values — "analogous to a hike to the top of a mountain, which can start at different places and may take different routes, but always leads to the top of *a* hill — as long as there is only one hilltop and not several." Always **refit from multiple different starting points** and check that the parameter estimates and log-likelihood agree before trusting the result.
- **Label switching**: because component labels are exchangeable, comparing/averaging parameter estimates across multiple EM runs, bootstrap replicates, or against ground truth by *component index* is invalid — a "component 1" in one run may correspond to "component 2" in another. Match components by parameter value (e.g., sort by mean) before comparing.
- **Ignoring non-identifiability / overlapping components.** When components genuinely overlap (e.g. two regression lines/curves crossing), individual observations near the overlap cannot be reliably assigned to either component — the posterior weight is near 0.5 regardless of how much data you have. This is a property of the data-generating process, not a fitting failure; report assignment uncertainty rather than forcing a hard label.
- **Reporting only hard cluster labels and discarding the membership weights.** The soft weights *are* the uncertainty in the assignment; collapsing to argmax throws that away and can misrepresent confidence, especially near component boundaries.
- **Conflating structural and sampling zeros** in count data (e.g. ChIP-seq, microbiome, presence/absence data) — fitting a single Poisson/negative binomial to data that actually has an excess of "true absence" zeros will bias the fitted count-generating parameters. Check for zero-inflation before fitting a plain count model.
- **Bootstrap misuse**: increasing the number of bootstrap resamples (`nboot`/`B`) only reduces *Monte Carlo* error (approximation of the exhaustive bootstrap); it does **not** fix the deeper approximation of using the empirical distribution in place of the true one. With a small or biased original sample, the bootstrap sampling distribution can be poor no matter how large `nboot` is.
- **Sloppy convergence criteria**: no tolerance, or no `maxiter` safety cap, risks non-terminating loops or premature stopping on noise; also enforce a `miniter` so the algorithm doesn't quit after an accidental small first-step delta.
- **Fitting tests/regressions on raw heteroscedastic data** (counts, intensities) generated by a hierarchical/mixture process without first checking/applying a variance-stabilizing transform — violates the constant-variance assumption of many downstream methods.

## Assumptions to verify
- Is the parametric family for each component (e.g. normal, Poisson) actually plausible for the underlying biological measurement?
- Is K (number of components) justified by the science/design, not just assumed for convenience?
- Are components separated enough for the estimated parameters — and any derived cluster assignments — to be meaningful? (Near-total overlap ⇒ near non-identifiable mixture.)
- Does the "independent observations" assumption underlying the factorized likelihood (Eq 4.4) hold (no replicate/batch correlation structure being ignored)?
- For zero-heavy count data: is a plain (non-inflated) count distribution actually adequate, or is there evidence of structural zeros?
- For any variance-stabilizing transform in use: does the assumed mean-variance relationship `v(μ)` actually match what's observed in the data (plot SD vs mean per group/replicate to check)?

## Diagnostic checks
- Refit EM/GMM from several different random initializations (and/or cross-check against an established library implementation); compare final log-likelihoods and parameter estimates — disagreement flags a local-optimum problem.
- Plot log-likelihood vs. EM iteration to confirm monotonic increase to convergence (not oscillation, not an early false stop).
- Inspect the distribution of posterior membership weights, not just argmax labels — look at how many observations have confident (near 0 or 1) weights vs. ambiguous (~0.5) weights. A high ratio of "confidently assigned" observations (e.g., flexmix's summary uses a default threshold `δ=1e-4` on posterior probability) indicates well-separated components; a low ratio indicates overlap/non-identifiability.
- If ground-truth or independently known labels exist, cross-tabulate them against estimated component membership (a truth table / confusion matrix) — off-diagonal mass reveals identifiability problems, not necessarily a modeling bug.
- Overlay the fitted mixture density (and each weighted component density) on the data histogram — visually confirm fit rather than trusting parameter values alone.
- For count data, plot the histogram with a log10 y-axis to check whether the zero bin is elevated relative to the trend implied by counts 1, 2, 3, … (sign of zero-inflation).
- For hierarchical count models (gamma-Poisson/negative binomial), check goodness of fit with a rootogram (√observed frequency vs. theoretical probability) — bars should end close to the axis across the whole range, not just at the mode.
- Before/after applying a variance-stabilizing transform, plot SD (or variance) vs. mean across strata/replicates/bins — should flatten out after the correct transform.
- Sanity-check a from-scratch EM implementation against a trusted library's output on the same data (same tolerance) — mismatched estimates indicate an implementation bug before anything else.

## Quick checklist
- [ ] Is the number of mixture components K assumed rather than validated, and could raw log-likelihood alone have driven that choice?
- [ ] Was EM/GMM fitting repeated from multiple starting points to rule out local optima?
- [ ] When comparing components across runs/replicates/software, were they matched by parameter value (not index), to avoid label-switching errors?
- [ ] Are posterior membership weights (soft assignments) inspected and reported, not just hard argmax labels?
- [ ] Could components be genuinely non-identifiable or overlapping (e.g. crossing regression curves, near-equal means)? Is assignment uncertainty near such regions acknowledged?
- [ ] For count data: are structural zeros distinguished from sampling zeros (zero-inflation), if relevant?
- [ ] Is the log-likelihood (not raw likelihood) used for optimization/reporting, for numerical stability?
- [ ] If bootstrapping, is `nboot`/`B` large enough for Monte Carlo error, while recognizing this can't fix a small or biased original sample?
- [ ] Has a variance-stabilizing transform been checked/applied when the data are known/suspected to have mean-dependent variance, before downstream tests or regressions?
- [ ] Are EM convergence criteria (tolerance, min/max iterations) explicit and sane, not left to silent defaults?

## Key terms
- Finite mixture / infinite mixture
- Latent (hidden) variable, label U
- EM algorithm: E-step, M-step
- Membership weight / posterior responsibility (soft assignment)
- Marginal likelihood; Q-function (expected complete-data log-likelihood)
- Label switching (component-index exchangeability)
- Identifiability (of mixture components)
- Zero-inflation: structural zero vs. sampling zero
- ECDF, nonparametric bootstrap, sampling distribution, Monte Carlo error
- Laplace / asymmetric Laplace distribution; scale mixture
- Gamma-Poisson mixture ≡ negative binomial distribution; dispersion parameter α
- Heteroscedasticity, variance-stabilizing transformation, delta method

## Python equivalents (use with care — not from the source text)
- `sklearn.mixture.GaussianMixture(n_components=k, n_init=...)` — set `n_init` > 1 to guard against local optima; `.bic()`/`.aic()` available for comparing K (formal criteria not covered in this chapter; still monotonicity-of-likelihood caveat applies).
- `scipy.stats.nbinom` for the gamma-Poisson/negative-binomial distribution; `statsmodels.discrete.count_model.ZeroInflatedPoisson` / `ZeroInflatedNegativeBinomialP` for zero-inflated count models.
- `scipy.stats.bootstrap` or manual resampling with `numpy.random.choice(..., replace=True)` for the nonparametric bootstrap.
