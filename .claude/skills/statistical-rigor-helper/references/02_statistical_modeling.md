# Chapter 2: Statistical Modeling
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/02-chap.html*

## Core concepts
- Probability vs statistics: probability reasons deductively (known model + known params → P(data)); statistics reasons upward (observed data → estimated model + params). Don't treat an assumed distribution as a verified one.
- Maximum likelihood estimation (MLE): pick θ̂ maximizing L(θ|x) = ∏ f(xᵢ|θ). Always work with log-likelihood (sum of logs) — multiplying many small probabilities underflows to exactly 0 and silently breaks optimization/comparison.
- Closed-form MLEs: Poisson λ̂ = sample mean; Binomial(n,p) p̂ = successes/n. Not all MLEs are this clean — some require numerical optimization (scipy.optimize.minimize, or a grid search as a sanity check) and can be unintuitive.
- Constrained multinomial MLE: if categories are linked by a biological model rather than free (e.g. Hardy-Weinberg: p_MM=p², p_MN=2pq, p_NN=q²), fit the constrained model (1 free parameter: allele frequency), not raw per-category proportions — and adjust df accordingly (see below).
- Bayesian inference: treat θ itself as a random variable. Posterior(θ|data) ∝ Likelihood(data|θ) × Prior(θ). Can iterate — posterior of round 1 becomes the prior for round 2 — but only valid if the same θ truly underlies both datasets.
- Conjugate prior example: Beta(α,β) prior + Binomial(n,y) likelihood → Beta(α+y, β+n−y) posterior — closed-form update, no numerical integration required (scipy.stats.beta).
- Posterior point estimates differ: posterior mean, posterior median, and MAP (mode) are generally different values, especially for skewed/bimodal posteriors — state which one is reported and why.
- Bayesian credible interval ≠ frequentist confidence interval: a credible interval (e.g. 2.5th/97.5th posterior percentiles) is a direct probability statement about θ given the data; a CI is not.
- The χ² statistic Σ(observed−expected)²/expected is only *approximately* χ²-distributed; the approximation improves as cell counts grow. "Chi-squared" names both this statistic and the theoretical χ²_ν distribution — don't conflate the two.
- Markov chain / sequential dependence: model P(next symbol | previous k symbols) instead of assuming independence whenever adjacent categorical outcomes are correlated (e.g. dinucleotide bias, CpG islands).
- Log-likelihood-ratio score: log[P(x|model A)/P(x|model B)], built by summing per-position/per-transition log-odds — standard way to discriminate between two candidate generative (often Markov-chain) models.
- Rare, independent events along a sequence/genome ⇒ per-window counts are Poisson-distributed, and gaps/waiting-times between events are Exponential-distributed. Know which representation (count vs. gap) implies which distribution.
- Count outcomes (reads, spectral counts, motif counts) need a GLM with a count-appropriate error distribution (Poisson/negative binomial via statsmodels GLM), not ordinary linear regression with Gaussian residuals.

## Common mistakes / pitfalls
- Fitting a distribution without checking goodness of fit first — trusting a single summary statistic instead of visualizing (rootogram, "Poissonness" plot, QQ-plot).
- Silently keeping (or dropping) outliers when computing an MLE: a single extreme value pulls a mean-based estimate (e.g. Poisson λ̂) up or down, changing downstream p-values — decide explicitly and state the direction of bias (it is not automatically "conservative").
- Reporting only the MLE point estimate without checking the shape of the (log-)likelihood near its maximum — a flat likelihood means many parameter values are nearly as consistent with the data; report a CI/likelihood plot, not just θ̂.
- Trusting the χ² approximation with small expected cell counts — use exact/simulation alternatives instead (Fisher's exact / hypergeometric test for contingency tables; permutation or Monte Carlo p-values for custom statistics).
- Computing df for a goodness-of-fit χ² test as simply (#categories − 1) when the null model's parameters were estimated from the same data — each estimated parameter removes one further df (HWE example: 3 categories, 1 estimated allele frequency ⇒ df = 3−1−1 = 1, not 2).
- Treating a significant contingency-table independence test as evidence of a specific mechanism — it only says "not independent," not why.
- Picking a one-sided test after seeing the data, to shrink the p-value — one-sidedness must follow from a pre-specified directional hypothesis (e.g. Chargaff's rule predicts smaller-than-random deviation), not be chosen post hoc.
- Reporting Monte Carlo/permutation p = 0 — with B replicates you cannot resolve probabilities below ~1/B; report "< 1/B", and prefer a theoretical null distribution once validated (via QQ-plot) since it has no such floor.
- Assuming adjacent categorical data (sequence positions, spatial bins, repeated time points) are i.i.d. multinomial draws without checking — dinucleotide/spatial correlation is common and breaks the independence assumption behind simple multinomial/binomial tests.
- Using a strongly peaked prior without justification, especially with little data — it will dominate the posterior; if switching to a flatter prior changes the conclusion, that must be disclosed.
- Chaining Bayesian updates (posterior → next prior) across datasets that may not share the same true parameter (batch effects, different conditions/populations) — this silently assumes exchangeability; use a hierarchical model (parameter varies by group) if that assumption is doubtful.
- Applying ordinary Gaussian linear regression to count data instead of a GLM with a count-appropriate distribution.
- Fitting a single unimodal distribution to a histogram that is visibly bimodal — bimodality signals a mixture of two populations that one distribution cannot represent.

## Assumptions to verify
- Does the chosen parametric family (Poisson/binomial/multinomial/normal/exponential) actually match the data's support and shape? Check visually before using it for p-values or CIs.
- Are cell/category counts large enough for the χ² asymptotic approximation to be trustworthy? If not, use an exact test or simulate the null directly.
- Are the categorical outcomes truly independent draws, or is there known sequential/spatial structure requiring a Markov/hierarchical model instead?
- If the null model's parameters were estimated from the same data being tested, has df/p-value been adjusted for that?
- Is the prior's influence on the posterior appropriate given how much data there is (peaked prior + little data ⇒ prior dominates)? Was this checked with a prior-sensitivity analysis?
- For a one-sided test, was the direction specified by the scientific hypothesis before looking at the data?
- For regression on count/rate outcomes, is the residual/error distribution appropriate (not assumed Gaussian by default)?

## Diagnostic checks
- Rootogram: bars of observed √counts hung from theoretical √counts; good fit ⇒ bars' bottoms align with the axis. Reveals over/under-dispersion invisible in a plain histogram.
- "Poissonness"/probability-transform plots (e.g. vcd::distplot equivalent): transform counts so a good fit appears as points on a straight line; deviations at the tails flag misfit (e.g. extra-large gaps beyond an exponential fit near a sequence boundary).
- QQ-plot: plot sample quantiles of an empirical/simulated statistic against theoretical (or a second sample's) quantiles (scipy.stats.probplot, or manual quantile comparison); points on y=x ⇒ good agreement. Use to confirm a simulated null statistic really matches a claimed theoretical distribution (e.g. χ²) before relying on the theoretical p-value shortcut.
- Inspect the log-likelihood curve's curvature at its maximum — sharper curvature ⇒ tighter CI around the MLE/MAP; flatter curvature ⇒ report uncertainty, not just the point estimate.
- Histogram of a derived score across the full dataset — look for multimodality (a sign of a mixture of subpopulations rather than one homogeneous group).
- Compare per-category observed frequencies to the frequencies expected from a fitted structured model side by side (e.g. HWE-expected genotype counts vs. observed), not just via one omnibus p-value.

## Quick checklist
- [ ] Visualized the raw distribution before choosing a parametric family?
- [ ] Confirmed goodness-of-fit with a rootogram/probability-plot/QQ-plot, not eyeballed alone?
- [ ] Checked for outliers and decided explicitly whether/how they affect the MLE?
- [ ] Verified expected cell counts are large enough before trusting a χ² p-value (else used Fisher's exact / permutation test)?
- [ ] Counted degrees of freedom correctly, subtracting one per parameter estimated from the data?
- [ ] Checked whether "independent" categorical observations actually have sequential/spatial dependence?
- [ ] If Bayesian: reported which posterior summary (mean/median/MAP) was used and checked prior sensitivity?
- [ ] If simulating a null distribution: used enough replicates B to resolve the reported p-value, or switched to a validated theoretical distribution?
- [ ] If regressing on counts: used a GLM with an appropriate error distribution, not plain Gaussian linear regression?
- [ ] Looked at the shape (curvature/flatness, unimodal/bimodal) of the likelihood or score distribution, not just its maximum?

## Key terms
- **Likelihood function** L(θ|x): probability of the observed data as a function of the parameter (same formula as the probability, different variable of interest).
- **MLE**: θ̂ maximizing L; use scipy.stats `.fit()` or scipy.optimize when no closed form exists.
- **MAP (maximum a posteriori)**: mode of the posterior — a Bayesian point estimate.
- **Prior / Posterior**: belief about θ before / after observing data; posterior ∝ likelihood × prior.
- **Conjugate prior**: prior family whose posterior stays in the same family (e.g. Beta–Binomial; scipy.stats.beta).
- **Credible interval**: Bayesian interval with a direct posterior-probability interpretation.
- **Marginal distribution**: distribution of an observable after integrating out uncertainty in a parameter.
- **Monte Carlo integration**: approximate an integral (e.g. posterior mean) by averaging simulated draws; useful with no closed form or high dimensionality.
- **Contingency table**: cross-tab of ≥2 categorical variables; test independence via χ² (scipy.stats.chi2_contingency) or Fisher's exact test (scipy.stats.fisher_exact) for small counts.
- **Yates' continuity correction**: default adjustment for 2×2 χ² tests to reduce small-sample bias.
- **Degrees of freedom (df)**: χ² distribution parameter = (#free categories) − (#parameters estimated from data).
- **Hardy-Weinberg equilibrium (HWE)**: constrained multinomial (p², 2pq, q²) null model for genotype frequencies — 1 free parameter, not 2.
- **Markov chain / transition matrix**: sequential-dependence model where the next state's probability depends only on a finite window of previous states.
- **Position weight matrix (PWM/PSSM) / sequence logo**: per-position multinomial probabilities along a sequence motif.
- **Log-likelihood-ratio score**: sum of log-odds between two candidate models, used for classification/discrimination.
- **Rootogram**: goodness-of-fit plot hanging observed √frequencies from theoretical ones.
- **Permutation test**: null distribution built by reshuffling data under the null hypothesis; resolution limited to 1/(number of permutations).
