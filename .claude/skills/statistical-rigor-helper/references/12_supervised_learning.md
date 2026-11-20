# Chapter 12: Supervised Learning
*Source: Holmes & Huber, Modern Statistics for Modern Biology, https://www.huber.embl.de/msmb/12-chap.html*

## Core concepts

- Supervised learning = learn a rule from labeled **training data** (predictors X, response/objective Y) that generalizes to new, unseen data. Continuous Y → **regression**; categorical Y → **classification**. The central question is always: does the rule generalize, or did it just memorize the training set (**overfitting**)?
- **Discriminant analysis** (LDA/QDA): partition feature space into class regions.
  - LDA assumes **one shared covariance matrix** across all classes → linear decision boundaries. QDA fits a **separate covariance matrix per class** → quadratic boundaries, but needs enough observations per class to estimate that covariance; if a class is too small, QDA fails outright (`some group is too small for 'qda'`), while LDA merely warns about collinearity when p ≥ n.
  - Default class **priors** = empirical class frequencies in the training data. This shifts the decision boundary toward the more prevalent class. If deployment prevalence differs from training prevalence, re-fit with different/uniform priors or explicitly account for it — don't assume the boundary is "unbiased."
  - Predictions far from all training cluster centers are extrapolations — treat with lower confidence; resampling/CV-based uncertainty is more reliable than a naive distance-to-center heuristic.
- **Objective/risk/cost functions** (population and finite-sample forms):
  - Misclassification rate: MCR = E[𝟙(ŷ≠y)]; empirical MCR = (1/n)Σ𝟙(ŷᵢ≠yᵢ).
  - Confusion matrix (`table(truth, predicted)` / `sklearn.metrics.confusion_matrix`) — always prefer this over a single accuracy number.
  - Binary asymmetric-cost setting: **sensitivity/recall/TPR = TP/P**; **specificity/TNR = TN/N**. Sweeping a threshold gives **ROC** or **precision-recall curves** (`sklearn.metrics.roc_curve`/`roc_auc_score`, `precision_recall_curve`).
  - **Jaccard index** J(A,B) = |A∩B| / |A∪B| (A = true positives set, B = predicted positives set). Ignores true negatives entirely — well-suited to rare-event/imbalanced detection where TN swamps everything else (`sklearn.metrics.jaccard_score`).
  - **Log loss** (binary): −(1/n)Σ[yᵢlog(p̂ᵢ) + (1−yᵢ)log(1−p̂ᵢ)]. Goes to **infinity** if a prediction is fully confident (p̂ᵢ = 0 or 1) and wrong — a hard warning against unclipped, overconfident probability outputs (`sklearn.metrics.log_loss`).
  - Regression: **MSE** = (1/n)Σ(Ŷᵢ−Yᵢ)².
- **Bias–variance decomposition**: MSE = Var(Ŷ) + Bias(Ŷ)². Trading a little bias for a large variance reduction can lower overall MSE (shrinkage, Ch. 8). For classification, the discreteness of the response tolerates pushing this trade further — bias costs almost nothing while variance still drops (Friedman 1997).
- **Penalization/regularization** (glmnet-style logistic/multinomial regression, more general than LDA in high dimensions): fit β̂ = argmax_β [loglik(β; x) + λ·pen(β)].
  - Ridge: pen(β) = ‖β‖² (L2). Lasso: pen(β) = ‖β‖¹ (L1, induces sparsity/feature selection). **Elastic net**: pen(β) = (1−α)‖β‖¹ + α‖β‖², α∈[0,1] mixes the two. Python: `sklearn.linear_model.LogisticRegression(penalty='l1'/'l2'/'elasticnet', C=1/λ)`, `ElasticNet`, `glmnet`-equivalent `sklearn.linear_model.LogisticRegressionCV`.
  - **Penalized regression is NOT scale-invariant** (unpenalized regression is). Rescaling one feature changes how much of the penalty budget it "costs" to give that feature a nonzero coefficient — so features must be standardized (consistently, i.e., fit the scaler only on the training fold) before penalizing, and raw coefficient magnitudes cannot be read as "importance" unless scales are comparable.
- **Curse of dimensionality** (Bellman 1961): high-dimensional space is nearly impossible to sample densely. Concrete facts worth citing:
  - A hypercube needing to contain 10 of 10⁶ uniformly-distributed points has side length → 1 (i.e., "local neighborhood" ≈ whole range) as p grows.
  - The fraction of a unit cube's volume within 0.01 of its surface → 1 as p grows (almost everything is near the boundary/is an extrapolation region).
  - The coefficient of variation of pairwise distances → 0 as p grows (everyone becomes equally far from everyone else).
  - Practical consequence: as irrelevant features are added, misclassification rate first improves (bias falls as p approaches the true number of informative features) then **gets worse again** as p keeps growing past that, because some irrelevant features spuriously look predictive *in the training data* and mislead the classifier on test data. This is the empirical bias–variance sweet-spot curve — don't expect "more features = better."
- **Cross-validation (CV)**: naive single train/test split is both high-variance (depends on how the split falls) and inefficient (less data → worse-performing model, so the estimate underestimates achievable performance).
  - **k-fold CV**: train on ~n(k−1)/k, test on ~n/k, repeat k times, average.
  - **Leave-one-out CV (LOOCV)**: k = n. Maximizes training-set size per fold (best when n is scarce) but folds are nearly identical (higher variance/less diverse resampling of what a "new dataset" would look like) and can be slow for large n.
  - Neither is universally best; there is a genuine trade-off, not a default answer.
  - `cv.glmnet`-style output gives **lambda.min** (λ minimizing the CV curve) and **lambda.1se** (largest λ whose CV performance is within 1 SE of the minimum) — see Common mistakes for why 1se, not min, is usually the better choice.

## Common mistakes / pitfalls

- **Reporting training-set performance as generalization performance.** Demonstrated directly: fitting LDA to *pure noise* (random labels, random features) with n=20 drives training misclassification rate to ~0 as p→n — the model is memorizing, not learning. Any accuracy/error number must be computed on data not used to fit the model.
- **Feature selection, normalization, or any data-dependent preprocessing done on the full dataset (including future test folds) before splitting/cross-validating.** This is the single most damaging and most common leakage pattern in omics ML pipelines. The canonical citation is Ambroise & McLachlan (2002), "Selection Bias in Gene Extraction on the Basis of Microarray Gene-Expression Data" (PNAS) — selecting "top" discriminating genes/features using all samples, then cross-validating a classifier only on those pre-selected features, produces a wildly optimistic performance estimate because the test fold's information already leaked into which features were chosen. Fix: every preprocessing step that looks at the response or estimates parameters from the data (gene/feature filtering, scaling, imputation, PCA, batch correction) must be fit **only on the training fold** and re-applied (not re-fit) to the held-out fold, inside the CV loop. Python: wrap the whole pipeline (imputer → scaler → feature selector → model) in `sklearn.pipeline.Pipeline` and pass the *pipeline* to `cross_val_score`/`cross_validate`/`GridSearchCV` — never call `.fit_transform()` on the full X before splitting.
- **Selecting a hyperparameter (λ, k in kNN, tree depth, neural net size/decay, SVM C/γ) by cross-validation and then reporting that same CV score as the generalization estimate.** The CV score at the chosen hyperparameter is itself optimized over, so it's biased upward — you looked at many candidate models and kept the best-scoring one on the same data used to score it. Fix: **nested cross-validation** — an inner CV loop tunes hyperparameters, an outer CV loop (or a genuinely separate held-out set) evaluates the tuned pipeline's performance, and only the outer loop's number is reported as the generalization estimate. Python: `GridSearchCV`/`RandomizedSearchCV` as the estimator passed into an outer `cross_val_score`/`cross_validate`.
- **Using `lambda.min` uncritically.** Because it's chosen by finding the minimum of a *noisy, estimated* CV curve, `lambda.min` systematically tends to under-penalize (pick too little regularization) — it overfits the tuning criterion itself. The `lambda.1se` heuristic (largest λ with CV performance within 1 SE of the minimum) is more conservative and usually the better default, especially in small-n-large-p settings.
- **"Method hacking"** (the ML analogue of p-value hacking): trying many combinations of preprocessing, algorithms, and tuning parameters until the result "looks good," then reporting only the winning configuration. Even with a technically correct CV loop, the reported accuracy will still be optimistic if the space of things tried (transformations, outlier handling, algorithm choice, etc.) wasn't itself formalized and validated inside that loop — not all analyst choices can be automated into the CV procedure. Mitigations: validate on truly independent/unseen data as the gold standard; prefer interpretable models tied to domain knowledge over black boxes; report the complete computational workflow (not just summary statistics) so choices and their influence are auditable (Holmes 2018).
- **Trusting in-dataset CV to catch everything.** A CV loop only ever resamples *within one dataset* — it cannot detect failure modes that only show up with truly new data (new batch, site, patient population, technical artifact). Worked example: on one embryo dataset, even a trivial 1-nearest-neighbor classifier using *all* features achieves near-perfect classification and CV shows monotonically *decreasing* error as λ→0 (no regularization "needed") — this reflects that the data are unusually easy / possibly contain near-duplicate or highly correlated samples, not that the biology is trivially separable in general. A CV curve that looks "too good" (monotonic improvement with no penalty at all) is itself a diagnostic prompt to check the data, not a green light.
- **Non-independent folds from repeated/related samples (same patient, same TMA core, same batch, technical replicates) split across train and test.** k-fold/LOOCV assume each held-out unit is an independent draw representative of new/future data; if related samples end up split across folds, the model can "cheat" using sample-identity/batch signal, inflating CV performance. Use grouped/blocked CV (e.g., `sklearn.model_selection.GroupKFold`/`StratifiedGroupKFold` keyed on patient/core/batch ID) whenever such structure exists.
- **Reporting overall accuracy/MCR alone under class imbalance.** A classifier can post high accuracy while recall on the minority class is poor (e.g., rare-event/disease detection). Report the full confusion matrix, per-class sensitivity/specificity, and/or the Jaccard index (which ignores true negatives and is specifically suited to rare-event performance) rather than one aggregate number. Python: `sklearn.metrics.classification_report`, `balanced_accuracy_score`, `class_weight='balanced'`.
- **Mismatched training/deployment class prevalence.** Good sensitivity/specificity measured on a case-control study with artificially balanced classes does not mean a test is ready for real-world screening, where the target condition is much rarer — PPV/real-world performance depends heavily on the deployment prevalence, and specificity in particular needs validation on a much larger, truly representative "normal" population before any screening claim.
- **Small-n-large-p CV instability.** With few observations, a single CV run's misclassification-rate-vs-model-complexity curve is visibly noisy/"wiggly"; don't over-interpret one CV curve's shape from a small dataset — repeat/average over resamples (or simulate replicate datasets) before drawing conclusions about where performance peaks.
- **Interpreting penalized-model coefficients as feature importance without checking feature scaling.** Because penalization is scale-dependent, a feature with a larger numeric range will be penalized differently than one with a small range purely as an artifact of scale, not biological effect size.

## Assumptions to verify

- Does every response-dependent or data-dependent step (feature/gene selection, scaling, imputation, batch correction, dimensionality reduction) happen strictly inside the CV training-fold fit, or was any of it computed once on the full dataset beforehand?
- Is hyperparameter tuning nested inside an outer evaluation loop (or validated on a separate held-out set), rather than sharing the same CV score used to pick the hyperparameter?
- Do observations in different folds correspond to genuinely independent sampling units, or do repeated measures / shared patient / shared TMA core / shared batch create leakage across the train-test boundary?
- Is the class distribution in the training/CV data representative of the deployment population, or does it need re-weighting / different priors / a specificity-focused validation on a larger normal cohort?
- Are features on comparable scales before any penalized (ridge/lasso/elastic net) model is fit?
- Is n large enough relative to p for the chosen method (LDA tolerates p up to ~n with a warning; QDA needs enough samples *per class* to estimate a full covariance and can fail outright; unregularized methods in general are unreliable once p approaches or exceeds n)?
- Is the reported performance metric matched to the actual cost structure (symmetric MCR/accuracy vs. sensitivity/specificity/Jaccard/log loss for asymmetric or rare-event costs)?
- Has more than one preprocessing/algorithm/tuning combination been tried? If so, is the final reported number still an honest, once-touched holdout estimate, or is it the best of many looks (method hacking)?

## Diagnostic checks

- Compare training-set error/accuracy to cross-validated (or held-out) error/accuracy; a large gap is the signature of overfitting.
- Plot CV performance vs. model complexity/regularization strength (λ, k, tree depth, etc.). Expect a U-shaped or hook-shaped curve (improves then worsens) when there's a mix of informative and irrelevant features; a suspiciously monotonic "more complexity is always better" curve is a prompt to check for leakage, near-duplicate samples, or genuinely saturating signal.
- Inspect `lambda.min` vs `lambda.1se` (or the equivalent 1-SE-rule point on any tuning curve) — if only `lambda.min`/the bare optimum is used, flag it.
- Always look at the full confusion matrix, not just a single accuracy/MCR number; compute sensitivity, specificity, and/or Jaccard index per class, especially with imbalance.
- Check for probability predictions of exactly 0 or 1 (or values that will blow up log loss) — a sign of overconfident, likely overfit, probability calibration.
- Trace the code: does any `.fit()`/`.fit_transform()` (scaler, imputer, feature selector, PCA, differential-expression filter) run on the full X/y before the train/test or CV split? If yes, that's leakage regardless of downstream CV correctness.
- Check whether grouping identifiers (patient/core/batch/replicate ID) exist in the metadata and whether the CV splitter respects them (`GroupKFold`) rather than plain random/stratified k-fold.
- Sanity-check with a trivial baseline (e.g., 1-nearest-neighbor on all features, or a majority-class classifier): if a trivial method already achieves near-perfect performance, ask why before trusting a more complex model's apparent success.
- For small-n-large-p data, rerun CV across several random splits/seeds and check the between-run spread of the performance curve before trusting its shape from a single run.
- Verify whether test-set/held-out performance has been looked at more than once during model/parameter selection (repeated peeking is test-set leakage via multiple comparisons, structurally identical to p-hacking).

## Quick checklist

- [ ] No preprocessing step (scaling, imputation, feature/gene selection, batch correction, PCA) was fit on data outside the current training fold.
- [ ] Hyperparameter tuning is nested inside (or otherwise separated from) the final performance-evaluation loop — no double-dipping on the same CV score.
- [ ] Folds/splits respect sample groupings (patient, TMA core, batch, replicate) where relevant — no related samples split across train/test.
- [ ] Reported performance is cross-validated or held-out, never computed on the training set.
- [ ] `lambda.1se` (or an equivalent 1-SE-rule choice), not just the bare `lambda.min`/optimum, considered for the final regularization strength.
- [ ] Full confusion matrix and per-class sensitivity/specificity/Jaccard reported, not just overall accuracy — especially under class imbalance.
- [ ] Training/CV class prevalence checked against intended deployment prevalence before making any real-world performance claim.
- [ ] Features standardized before any penalized (ridge/lasso/elastic net) fit, with scaler fit only on the training fold.
- [ ] p vs n checked for the chosen method (QDA needs enough samples per class; unregularized methods are unreliable once p ≳ n).
- [ ] Number of preprocessing/algorithm/tuning combinations tried is disclosed; the final number isn't the best of many undisclosed looks at held-out performance.
- [ ] A trivial baseline was checked for suspiciously perfect performance before trusting a complex model.

## Key terms

- **Misclassification rate (MCR)**: fraction of wrong predictions; population version E[𝟙(ŷ≠y)], empirical version the sample mean of the indicator.
- **Sensitivity/recall/TPR**, **specificity/TNR**: TP/P and TN/N respectively; the two axes of an ROC curve.
- **Jaccard index**: |A∩B|/|A∪B| between true- and predicted-positive sets; ignores true negatives, suited to rare-event performance.
- **Log loss**: negative log-likelihood of probabilistic binary predictions; infinite penalty for a confident-and-wrong prediction.
- **Bias–variance trade-off**: MSE = variance + bias²; shrinkage/regularization trades a little bias for a large variance reduction.
- **Curse of dimensionality**: high-dimensional spaces cannot be densely sampled; distances concentrate, and adding irrelevant features first helps then hurts classification.
- **Penalization/regularization**: adding λ·pen(β) to the fitting objective to control variance; ridge (L2), lasso (L1, sparsity-inducing), elastic net (mix).
- **k-fold CV / LOOCV**: resampling schemes for out-of-sample performance estimation; trade-off between training-set size per fold and fold diversity/computational cost.
- **Nested cross-validation**: inner loop tunes hyperparameters, outer loop evaluates the tuned pipeline — required whenever tuning and evaluation both use CV, to avoid optimistic bias.
- **Selection bias (Ambroise & McLachlan 2002)**: the classic demonstration that feature selection performed outside (before) the CV loop inflates apparent classifier accuracy.
- **Method hacking**: iteratively trying preprocessing/algorithm/tuning combinations until a result looks good — the ML analogue of p-value hacking; degrades the honesty of a reported performance number even under correct CV.
- **lambda.min / lambda.1se**: the CV-error-minimizing λ vs. the more conservative largest λ within 1 SE of the minimum; prefer the latter as a default.
- **Scale (in)variance**: ordinary (unpenalized) regression is invariant to feature rescaling; penalized regression is not — rescaling changes shrinkage per feature.
