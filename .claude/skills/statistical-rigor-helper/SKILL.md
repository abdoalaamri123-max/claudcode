---
name: statistical-rigor-helper
description: Advises on which statistical method to use before an analysis is run, and checks an existing analysis or manuscript statistics section for rigor, using rules distilled from Modern Statistics for Modern Biology (Holmes & Huber). Two modes. Method selection, before running an analysis, e.g. t-test vs Wilcoxon, Poisson vs negative binomial for count data, how to pick k for clustering. Rigor check, on an existing analysis, notebook, or manuscript statistics section, for differential expression/count data, clustering, PCA/ordination, mixture models, multiple-testing correction, cross-validation, image quantification, or experimental design, catching confounding/batch effects, pseudoreplication, data/CV leakage, p-hacking, or wrong distributional assumptions. Companion to submission-screener for the statistical-justification review step. Trigger even without the word statistics, e.g. am I leaking information in my cross-validation, is my pseudobulk confounded by cell count.
---

# Statistical Rigor Helper

A working reference for choosing and checking statistical methods in
biological data analysis (Python-oriented), distilled from Susan Holmes &
Wolfgang Huber's *Modern Statistics for Modern Biology* (MSMB), freely
available at https://www.huber.embl.de/msmb/. Treat the book itself as the
canonical, citable source for anything in this skill — the files here are a
compressed, checklist-oriented distillation of it, not a replacement. The book
is written around R/Bioconductor; everything here has been translated to the
underlying statistical concept, with Python equivalents (scipy, statsmodels,
scikit-learn, pydeseq2, scanpy, ...) noted where confident. When no Python
mapping is given for something, the concept still applies — find the
matching tool yourself rather than assuming it's R-only.

## The one rule that cannot be broken

**Never fabricate a statistical result, a diagnostic outcome, or an assessment of soundness.** A verdict ("this p-value histogram looks healthy," "this design is confounded," "this clustering is stable") must come from actually reading the analysis or running the relevant check — never from assuming what a typical analysis of this kind would look like. If the data needed to run a diagnostic isn't available, say so and describe what running it would show, rather than asserting a result. A clean analysis deserves a short, honest "looks sound" — not a fabricated list of issues to seem thorough, and not a confident pass on something that was never actually checked.

## Two modes of use

This skill does two different jobs. Identify which one the user needs before
diving into the reference files — they call for different workflows. If
results already exist for the analysis in question, treat it as Mode 2
regardless of how prospectively the question is phrased (e.g. "what test
should I use for X" about an analysis already run and seen) — ask directly if
it's unclear whether results exist yet. Mode-1-style advice given after the
result is already known risks rationalizing a result in hindsight rather than
genuinely guiding the choice.

### Mode 1 — Advise on method selection (before the analysis is run)

Trigger when the user is deciding *how* to analyze data they haven't tested
yet, or is unsure which of several plausible methods fits. Don't just hand
back a menu of options — make a concrete recommendation:

1. **Pin down the data type and the actual question.** Counts, intensities,
   or continuous measurements? Paired or unpaired? How many groups, and is
   the outcome categorical or continuous? How many features/hypotheses are
   being tested at once? Is there a natural blocking/grouping structure
   (same patient at two timepoints, same TMA core, same batch)?
2. **Consult the matching reference file(s)** (map below) for the relevant
   menu of methods and the assumptions each one depends on.
3. **Recommend a specific method, and say why.** State which assumption(s)
   it relies on, why it fits this data/question better than the default the
   user was about to reach for, and what would go wrong with that default
   (e.g., "don't default to Pearson correlation on compositional/count data —
   use chi-square distance / correspondence analysis instead, because Pearson
   lets the highest-count features dominate and misrepresents co-occurrence
   structure").
4. **Name the diagnostic check(s) the user should run once results exist**
   (e.g., "after fitting this, plot the p-value histogram" or "check the
   mean-variance relationship before trusting the Poisson assumption") —
   method selection and rigor-checking are two ends of one pipeline, not
   separate concerns, and Mode 2 picks up exactly there.
5. **If more than one method is genuinely defensible** (parametric vs.
   nonparametric, paired vs. unpaired, FDR vs. FWER), say so explicitly and
   give the deciding factor, rather than picking one arbitrarily or listing
   every option with no recommendation.

### Mode 2 — Check the rigor of an existing analysis

Trigger when reviewing an analysis, notebook, or manuscript statistics
section that already exists.

1. **Identify the analysis type(s) involved.** Most real analyses touch more
   than one: e.g. a pseudobulk differential-expression workflow involves
   count-data GLMs (ch08) *and* multiple testing (ch06) *and* possibly
   clustering (ch05) or PCA (ch07) upstream, plus experimental-design
   questions (ch13) about what counts as a replicate.
2. **Read the matching reference file(s)** from `references/` (map below).
3. **Always run the Universal Checklist below regardless of analysis type**
   — these are the mistakes that recur across nearly every chapter and are
   the highest-value things to catch.
4. **If the data is accessible, run the relevant helper script(s)** from
   `scripts/` rather than eyeballing p-value histograms or confound
   correlations by hand.
5. **Report findings the way a good reviewer would**: for each issue, state
   (a) the pitfall, (b) the concrete mechanism by which it would bias this
   specific result (not just "this is generally bad practice"), and (c) a
   specific fix. Order by how much the issue would actually change the
   conclusion, not by how many checklist items it touches. A clean analysis
   deserves a short, honest "looks sound" response, not manufactured padding.
6. **Hold the checklist's objective definitions even against pushback.** If the user disputes a correct finding ("Reviewer 2 flagged this but I think they're wrong, back me up"), apply the same definition (independent unit vs. technical replicate, correction family, distributional match) regardless — a correct diagnosis doesn't become wrong because the author disagrees with it. State the objective basis again rather than softening the verdict to match what the user wants to hear.

Neither mode replaces picking a specific library API or teaching the
underlying math from scratch — if the user needs the latter, this skill's
job is to flag what to be careful about while they (or another skill) handle
implementation.

## Relationship to sister skills

- `submission-screener` — its pre-submission QC pass includes checking a manuscript's *statistical justification materials* (Pass 5), alongside internal consistency, ethics/consent adequacy, research-integrity red flags, and data/code deposition. That single checklist item is exactly Mode 2 of this skill, applied to whatever statistics/methods section the manuscript contains: `submission-screener` handles everything else in the submission-readiness pass, this skill owns statistical correctness specifically. When screening a manuscript's statistics, run both.
- `review-simulator` — critiques scientific soundness and argument strength at the level a peer reviewer would (does the evidence support the claim); this skill goes one level deeper into the statistics themselves (is the method, the assumption, the correction appropriate). A review-simulator finding of "the statistics don't support this claim" is exactly the kind of thing this skill's Mode 2 can substantiate with the specific mechanism.

## Universal checklist

These same failure modes show up across nearly every chapter of the book.
Check them on *every* rigor-check (Mode 2), before diving into anything
topic-specific — and keep them in mind during method selection (Mode 1) too,
since the right method is often the one least likely to trip one of these:

- [ ] **Confounding / leakage check.** Is there a covariate (batch, processing
      day, operator, reagent lot, library size, total counts, cell number per
      pseudobulk sample, detection rate, TMA core/section ID) that correlates
      with **both** the group of interest and the outcome? If so, the
      biological and nuisance effects are not separable from this data alone
      — no downstream model fixes it after the fact. Use
      `scripts/confound_correlation_check.py`, or cross-tabulate/correlate
      manually. This is the single most common real mistake this skill exists
      to catch.
- [ ] **Pseudoreplication.** Does `n` count independent biological units
      (patients, animals, independent cultures), or does it silently include
      technical replicates (repeated sections/cores/scans/library preps from
      the same biological unit)? Treating the latter as independent inflates
      apparent significance with zero new biological information.
- [ ] **Multiple testing.** If more than one hypothesis/feature is being
      tested, is a correction applied at all, and is it the right family for
      the goal (FDR/BH for exploratory screening with follow-up — the
      overwhelming majority of biology — vs. FWER/Bonferroni only when a
      single false positive would be unacceptable)?
- [ ] **p-value histogram.** For any multi-test analysis, has the p-value
      histogram actually been plotted and inspected (uniform baseline + peak
      near 0 = healthy; a hump, edge spike, or non-uniform shape under a
      known-null setting = broken independence, batch effect, or null
      misspecification)? Use `scripts/pvalue_histogram_check.py`.
- [ ] **Distributional assumption match.** For count/intensity data: is
      variance roughly equal to the mean (Poisson-adequate) or does it exceed
      it (overdispersion, needing negative-binomial/GLM)? Check with
      `scripts/mean_variance_check.py` rather than assuming.
- [ ] **Double-dipping.** Was any feature, hypothesis, or cluster selected
      using the same data it is then tested on (e.g., filtering to
      "high-variance genes" before testing them, or forming a cluster split
      and then testing for group differences using that split)?
- [ ] **Data leakage in cross-validation / ML.** Was any preprocessing
      (scaling, imputation, feature selection, batch correction, PCA) fit on
      the full dataset (including test folds) before splitting? Are related
      samples (same patient/TMA core/batch) kept together across folds
      rather than split (grouped CV)? Was hyperparameter tuning nested inside
      an outer evaluation loop?
- [ ] **Unvalidated exploratory claims presented as confirmed.** Clustering,
      PCA/ordination axes, network layouts, and dendrogram leaf order are all
      descriptive/exploratory — none of them carry a p-value by default. Has
      clustering been validated (stability under resampling, an explicit
      k-selection criterion) rather than eyeballed? Has a PCA/ordination axis
      been checked against known technical covariates before being called
      "biological"?
- [ ] **Design balance.** Are the factor of interest and any nuisance/batch
      factors balanced/orthogonal (cross-tab factor levels), or is there
      partial/total confounding baked into the design itself?
- [ ] **Effect size vs. significance.** Is a p-value or "significant" call
      accompanied by an effect-size estimate (fold-change, mean difference,
      CI), or is significance alone being treated as if it meant
      "biologically important"?
- [ ] **Visualization honesty.** No bar-of-means without the underlying
      distribution/points shown; sample size visible wherever distributions
      are compared; no over-interpreted heatmap/dendrogram block structure
      without a robustness check.
- [ ] **Order of operations.** Was the hypothesis, test statistic, and
      rejection region fixed *before* looking at the data (no p-hacking /
      HARKing / one-sided-test-after-seeing-direction / optional stopping)?

## Reference map

Read the file(s) matching the current analysis or method-selection question.
All files live in `references/` and cite specific book sections (URL in each
file's header).

| File | Covers | Consult when... |
|---|---|---|
| `01_generative_models.md` | Bernoulli/binomial/Poisson/multinomial, exchangeability, selection effects, power, EDA-before-CDA | Choosing a base distribution for discrete/count data; reasoning about an extreme value selected from many candidates; basic power intuition |
| `02_statistical_modeling.md` | MLE, Bayesian inference, chi-square goodness-of-fit, Markov chains, degrees of freedom | Fitting any parametric model; contingency tables; sequence/Markov-chain data; Bayesian updating across datasets |
| `03_data_visualization.md` | Grammar of graphics, distribution-comparison plots, color scales, aspect ratio, overplotting | Any plot design decision; reviewing a figure before it goes in a paper/report |
| `04_mixture_models.md` | EM algorithm, label switching, zero-inflation, gamma-Poisson, variance-stabilizing transforms | Fitting Gaussian/other mixtures; zero-inflated count data; deciding on a VST |
| `05_clustering.md` | Distance metrics, linkage, k-means/PAM/DBSCAN, k-selection (gap statistic, silhouette, CH index), stability | Any clustering analysis; choosing k; validating whether clusters are "real" |
| `06_testing_multiple_comparisons.md` | Hypothesis testing framework, FWER/Bonferroni, FDR/BH, independent filtering/IHW, p-value histogram diagnosis | **Any analysis with more than one test** — differential expression, GWAS, marker screens, pairwise comparisons |
| `07_multivariate_analysis.md` | PCA, SVD, scaling/centering, scree plots, biplots, batch-confound-in-PC1 | Any PCA; deciding how many PCs to keep; checking whether a PC axis reflects a confound |
| `08_count_data_glm.md` | Poisson vs. negative-binomial, size-factor normalization, GLM design matrices, shrinkage, independent filtering | **RNA-seq/proteomics/spatial-transcriptomics differential expression or any count-based comparison** |
| `09_heterogeneous_data_integration.md` | MDS/PCoA, correspondence analysis, CCA/sparse CCA, t-SNE/diffusion maps, multi-table integration | Multi-omics integration; non-PCA ordination; t-SNE/diffusion map interpretation |
| `10_networks_trees.md` | Enrichment/hypergeometric tests, permutation tests, phylogenetics, hierarchical multiple testing | Pathway/GO enrichment analysis; permutation-based tests; phylogenetic comparisons; network layout claims |
| `11_image_data.md` | Thresholding, segmentation, connected components, spatial point processes (K/G/L/pcf functions) | TMA/IHC/HE image quantification, Xenium/spatial cell segmentation, any image-derived feature table |
| `12_supervised_learning.md` | LDA/QDA, regularization, curse of dimensionality, cross-validation, leakage, class imbalance | Any classifier/ML model; especially cross-validation design review |
| `13_experimental_design.md` | Controlled vs. observational studies, batch effects, pseudoreplication, blocking/randomization, power | Reviewing an experimental design before or after data collection; sample-size questions; confounding review |

## Helper scripts

Located in `scripts/`; each is both a CLI (accepts a CSV) and an importable
Python module. They implement the highest-value *quantitative* checks — the
ones worth automating rather than eyeballing. All three are Mode-2 tools
(they check data that already exists), but their docstrings are useful Mode-1
reading too — each explains the underlying assumption being tested.

| Script | What it does | Run when |
|---|---|---|
| `pvalue_histogram_check.py` | Plots/diagnoses a p-value histogram shape, estimates π0, applies BH/FDR, flags humps/edge-spikes/no-left-peak patterns | Any analysis producing many p-values (DE testing, GWAS, marker screens) |
| `confound_correlation_check.py` | For each candidate confounder, tests association with group (Kruskal-Wallis) and with outcome (Spearman); flags covariates significant on both | Pseudobulk/DE workflows, any group comparison where batch/technical covariates are available |
| `mean_variance_check.py` | Fits a robust log(variance) vs. log(mean) slope across replicate (feature, group) pairs; classifies Poisson / negative-binomial / super-quadratic regime | Before choosing Poisson vs. NB vs. Gaussian for count/intensity data; before deciding whether a VST is needed |

Example:
```bash
python scripts/confound_correlation_check.py pseudobulk_summary.csv \
    --group condition --outcome log2fc --confounders n_cells total_counts detection_rate
```

Each script's `--help` documents its exact CSV format; all three are also
importable (`from pvalue_histogram_check import check_pvalues`, etc.) for use
directly inside a notebook.

## Scope notes

- This skill deliberately ignores R/Bioconductor package syntax (the book's
  native ecosystem) — everything here is the underlying statistical concept
  plus, where confident, a Python equivalent. If no Python mapping is given
  for something, the concept still applies; find the matching tool yourself.
- Not covered: material specific to R package internals, and the book's
  closing "Statistical Concordance" (concept-to-chapter index),
  "Acknowledgements", and "References" chapters, which contain no additional
  checkable content.
- When something here conflicts with a more specific domain skill already in
  use (e.g. a proteomics-specific normalization skill), prefer the domain
  skill for implementation details and use this skill for the cross-cutting
  method-selection/rigor check.
