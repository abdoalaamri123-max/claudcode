#!/usr/bin/env python3
"""
Confounder screen: does a candidate covariate correlate with BOTH group
assignment and the outcome? (MSMB ch08, ch13; see also references/
08_count_data_glm.md and 13_experimental_design.md).

This is the single most common real-world failure mode this skill exists to
catch: a nuisance variable -- batch, processing day, library size, total
counts, cell number per pseudobulk sample, detection rate, section/core ID --
that happens to correlate with both the group of interest and the measured
outcome. When that happens, the biological effect and the nuisance effect are
not statistically separable from the data alone (no downstream model fixes
this after the fact -- see ch13's disease-vs-batch example). This exact
pattern (pseudobulk summary statistics correlating with the number of cells
contributing to that summary, rho ~ 0.9) has been observed in real analyses
-- always check for it explicitly, don't assume it away.

For each candidate confounder column, this script reports:
  - association with GROUP  (Kruskal-Wallis across group levels; nonparametric,
    matches the book's preference for rank-based / distribution-free checks)
  - association with OUTCOME (Spearman correlation; robust to non-normality
    and monotonic-but-nonlinear relationships)
  - a flag if the confounder is significantly associated with BOTH

A flagged confounder does not necessarily invalidate the analysis, but it
must be addressed explicitly: add it as a covariate/offset in the model,
stratify, or otherwise justify why it can be ignored.

Usage:
    python confound_correlation_check.py data.csv --group condition \\
        --outcome log2fc --confounders n_cells total_counts detection_rate

Or import:
    from confound_correlation_check import check_confounders
    report = check_confounders(df, group_col="condition", outcome_col="log2fc",
                                confounder_cols=["n_cells", "total_counts"])
"""
import argparse
import sys

import numpy as np
from scipy import stats


def _association_with_group(confounder_values, group_labels):
    """Kruskal-Wallis test of the confounder's distribution across group levels.
    Works for 2+ groups; nonparametric (no normality assumption)."""
    conf = np.asarray(confounder_values, dtype=float)
    groups = np.asarray(group_labels)
    mask = ~np.isnan(conf)
    conf, groups = conf[mask], groups[mask]

    levels = np.unique(groups)
    if len(levels) < 2:
        return np.nan, np.nan, "only one group level present -- cannot test association"
    samples = [conf[groups == lvl] for lvl in levels]
    samples = [s for s in samples if len(s) > 0]
    if len(samples) < 2:
        return np.nan, np.nan, "fewer than 2 non-empty group levels"
    try:
        stat, p = stats.kruskal(*samples)
        return float(stat), float(p), None
    except ValueError as e:
        return np.nan, np.nan, str(e)


def _association_with_outcome(confounder_values, outcome_values):
    """Spearman correlation between the confounder and the outcome/test statistic."""
    conf = np.asarray(confounder_values, dtype=float)
    out = np.asarray(outcome_values, dtype=float)
    mask = ~(np.isnan(conf) | np.isnan(out))
    conf, out = conf[mask], out[mask]
    if len(conf) < 3:
        return np.nan, np.nan, "fewer than 3 paired observations"
    rho, p = stats.spearmanr(conf, out)
    return float(rho), float(p), None


def check_confounders(df, group_col, outcome_col, confounder_cols,
                       alpha=0.05, rho_threshold=0.3):
    """For each column in confounder_cols, test association with group_col
    (Kruskal-Wallis) and with outcome_col (Spearman). Flag confounders
    significantly (p < alpha) associated with group AND with |rho| >=
    rho_threshold (and p < alpha) with the outcome -- the confounding
    signature. Returns a list of per-confounder result dicts."""
    results = []
    for col in confounder_cols:
        if col not in df.columns:
            results.append({"confounder": col, "error": "column not found in dataframe"})
            continue

        kw_stat, kw_p, kw_err = _association_with_group(df[col].values, df[group_col].values)
        rho, rho_p, rho_err = _association_with_outcome(df[col].values, df[outcome_col].values)

        assoc_with_group = (kw_err is None) and (not np.isnan(kw_p)) and (kw_p < alpha)
        assoc_with_outcome = (rho_err is None) and (not np.isnan(rho_p)) and (rho_p < alpha) and (abs(rho) >= rho_threshold)
        flagged = assoc_with_group and assoc_with_outcome

        results.append({
            "confounder": col,
            "kw_stat_vs_group": kw_stat,
            "kw_pvalue_vs_group": kw_p,
            "kw_error": kw_err,
            "spearman_rho_vs_outcome": rho,
            "spearman_pvalue_vs_outcome": rho_p,
            "spearman_error": rho_err,
            "flagged_as_confounder": flagged,
        })
    return results


def _print_report(results, alpha, rho_threshold):
    print(f"Confounder screen (alpha={alpha}, |rho| threshold={rho_threshold})\n")
    any_flagged = False
    for r in results:
        if "error" in r:
            print(f"- {r['confounder']}: ERROR - {r['error']}")
            continue
        flag_str = "  <-- FLAGGED: correlates with BOTH group and outcome" if r["flagged_as_confounder"] else ""
        if r["flagged_as_confounder"]:
            any_flagged = True
        print(f"- {r['confounder']}:{flag_str}")
        if r["kw_error"]:
            print(f"    vs group: error - {r['kw_error']}")
        else:
            print(f"    vs group   (Kruskal-Wallis): stat={r['kw_stat_vs_group']:.3g}, "
                  f"p={r['kw_pvalue_vs_group']:.3g}")
        if r["spearman_error"]:
            print(f"    vs outcome: error - {r['spearman_error']}")
        else:
            print(f"    vs outcome (Spearman):        rho={r['spearman_rho_vs_outcome']:.3g}, "
                  f"p={r['spearman_pvalue_vs_outcome']:.3g}")
    print()
    if any_flagged:
        print("At least one candidate confounder is associated with both group and outcome.")
        print("This does not automatically invalidate the analysis, but must be addressed:")
        print("  - add it as a covariate/offset in the model, or")
        print("  - stratify the analysis by it, or")
        print("  - explicitly justify why it can be ignored (e.g., known mechanism, pilot data).")
    else:
        print("No candidate confounder was significantly associated with both group and outcome.")
        print("This is reassuring but not proof of no confounding -- it only rules out the")
        print("covariates you thought to check. Unmeasured/latent confounders are still possible.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path", help="CSV file with one row per sample/observation")
    ap.add_argument("--group", required=True, help="column name of the group/treatment variable")
    ap.add_argument("--outcome", required=True, help="column name of the outcome/test-statistic variable")
    ap.add_argument("--confounders", nargs="+", required=True,
                     help="one or more column names of candidate confounders to screen")
    ap.add_argument("--alpha", type=float, default=0.05, help="significance threshold (default: 0.05)")
    ap.add_argument("--rho-threshold", type=float, default=0.3,
                     help="minimum |Spearman rho| with outcome to flag (default: 0.3)")
    args = ap.parse_args()

    try:
        import pandas as pd
        df = pd.read_csv(args.csv_path)
    except ImportError:
        print("pandas is required for CSV input; `pip install pandas` or import check_confounders() directly.",
              file=sys.stderr)
        sys.exit(1)

    results = check_confounders(df, args.group, args.outcome, args.confounders,
                                 alpha=args.alpha, rho_threshold=args.rho_threshold)
    _print_report(results, args.alpha, args.rho_threshold)


if __name__ == "__main__":
    main()
