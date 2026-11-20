#!/usr/bin/env python3
"""
Mean-variance relationship check for count/intensity data (MSMB ch04 "Mixture
Models", ch08 "Count Data & GLMs", ch13 "Experimental Design"). See also
references/08_count_data_glm.md and references/04_mixture_models.md.

Real replicate count/intensity data almost never has constant variance
(homoskedasticity), and it is essentially never plain-Poisson (variance =
mean) once you look across biological replicates. Fitting a model that
assumes the wrong mean-variance relationship (Poisson when the data are
overdispersed; a plain t-test/Gaussian linear model on raw heteroskedastic
counts) makes p-values anti-conservative. This script fits a robust log(var)
vs log(mean) slope across (feature, group) replicate sets and reports which
regime the data are in:

    slope ~= 0   variance independent of mean (already stabilized / constant)
    slope ~= 1   Poisson-like (variance ~ mean)          -> v(m) = m,   g(x)=sqrt(x)
    slope ~= 2   quadratic / negative-binomial-dominated  -> v(m) = a*m^2, g(x)=log(x)
    in between   gamma-Poisson / negative-binomial mixed regime (v = mu + alpha*mu^2)
                  -> use a proper NB/GLM, not Poisson or plain Gaussian

Input: long-format table with one row per (feature, group, replicate) value,
e.g. columns "feature", "group", "sample", "value" -- exactly what a
pseudobulk or per-condition replicate table usually looks like.

Usage:
    python mean_variance_check.py pseudobulk_long.csv \\
        --feature-col gene --group-col condition --value-col expr --plot out.png

Or import:
    from mean_variance_check import check_mean_variance
    report = check_mean_variance(df, feature_col="gene", group_col="condition",
                                  value_col="expr")
"""
import argparse
import sys

import numpy as np
from scipy import stats


def _per_feature_group_stats(df, feature_col, group_col, value_col, min_replicates=2):
    """Compute mean and variance of value_col within each (feature, group),
    keeping only groups with at least min_replicates observations."""
    means, variances, ns = [], [], []
    grouped = df.groupby([feature_col, group_col])[value_col]
    for _, values in grouped:
        v = np.asarray(values, dtype=float)
        v = v[~np.isnan(v)]
        if len(v) < min_replicates:
            continue
        means.append(np.mean(v))
        variances.append(np.var(v, ddof=1))
        ns.append(len(v))
    return np.array(means), np.array(variances), np.array(ns)


def check_mean_variance(df, feature_col, group_col, value_col, min_replicates=2,
                         plot=False, plot_path=None):
    """Compute per-(feature,group) mean/variance across replicates, fit a
    robust log-log slope (Theil-Sen, resistant to outlier features), and
    classify the regime. Returns a report dict."""
    means, variances, ns = _per_feature_group_stats(df, feature_col, group_col, value_col, min_replicates)

    # drop non-positive means/variances (can't take log; e.g. all-zero replicate sets)
    valid = (means > 0) & (variances > 0)
    n_dropped = int(np.sum(~valid))
    log_m = np.log(means[valid])
    log_v = np.log(variances[valid])
    n_points = len(log_m)

    if n_points < 5:
        return {
            "n_feature_group_pairs": n_points,
            "n_dropped_nonpositive": n_dropped,
            "error": "fewer than 5 usable (feature, group) pairs with >0 mean and variance "
                     "-- need more replicates per group or more features.",
        }

    slope, intercept, low_slope, high_slope = stats.theilslopes(log_v, log_m)

    if slope < 0.5:
        regime = "constant-variance (homoskedastic already, or over-transformed)"
        recommendation = ("Variance looks roughly independent of the mean. A Gaussian/linear model "
                           "may be appropriate on this scale, or the data have already been "
                           "variance-stabilized.")
    elif slope < 1.5:
        regime = "Poisson-like (variance ~ mean)"
        recommendation = ("Consistent with sampling-limited count data. Still verify against real "
                           "biological replicates (this analysis mixes any groups you supplied) -- "
                           "between-replicate variance is often higher than within-run Poisson noise. "
                           "If in doubt, prefer a negative-binomial/GLM over a plain Poisson model.")
    elif slope < 2.5:
        regime = "gamma-Poisson / negative-binomial-dominated (variance grows faster than the mean)"
        recommendation = ("This is the norm for biological replicate count/intensity data. Use a "
                           "negative-binomial GLM (e.g. pydeseq2, statsmodels NegativeBinomial) rather "
                           "than plain Poisson or a Gaussian linear model on raw values. For "
                           "visualization/clustering, apply a variance-stabilizing transform (VST) or "
                           "log rather than a naive log(x+1).")
    else:
        regime = "super-quadratic (variance grows faster than mean^2)"
        recommendation = ("Steeper than the standard negative-binomial regime -- check for a few "
                           "high-variance outlier features/samples dominating the fit, or a genuinely "
                           "different noise process (e.g. multiplicative technical noise, batch effects "
                           "not accounted for). Re-run after removing suspected outlier features.")

    report = {
        "n_feature_group_pairs": n_points,
        "n_dropped_nonpositive": n_dropped,
        "fitted_slope": float(slope),
        "slope_ci_low": float(low_slope),
        "slope_ci_high": float(high_slope),
        "intercept": float(intercept),
        "regime": regime,
        "recommendation": recommendation,
    }

    if plot:
        try:
            import matplotlib
            if plot_path:
                matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(figsize=(5, 5))
            ax.scatter(log_m, log_v, s=8, alpha=0.4, color="#4C72B0", label="(feature, group) pairs")

            xline = np.linspace(log_m.min(), log_m.max(), 50)
            mid_m, mid_v = np.median(log_m), np.median(log_v)
            ax.plot(xline, mid_v + 1.0 * (xline - mid_m), "--", color="green", linewidth=1.5,
                     label="slope=1 (Poisson)")
            ax.plot(xline, mid_v + 2.0 * (xline - mid_m), "--", color="darkorange", linewidth=1.5,
                     label="slope=2 (quadratic/NB)")
            ax.plot(xline, intercept + slope * xline, "-", color="crimson", linewidth=2,
                     label=f"fitted slope={slope:.2f}")

            ax.set_xlabel("log(mean) across replicates")
            ax.set_ylabel("log(variance) across replicates")
            ax.set_title(f"Mean-variance relationship (n={n_points} feature x group pairs)")
            ax.legend(fontsize=8)
            fig.tight_layout()
            if plot_path:
                fig.savefig(plot_path, dpi=150)
                report["plot_path"] = plot_path
            else:
                plt.show()
        except ImportError:
            report["plot_error"] = "matplotlib not available; skipped plotting."

    return report


def _print_report(report):
    if "error" in report:
        print(f"ERROR: {report['error']}")
        return
    print(f"(feature, group) pairs used: {report['n_feature_group_pairs']} "
          f"(dropped {report['n_dropped_nonpositive']} with non-positive mean/variance)")
    print(f"Fitted log(var) ~ log(mean) slope (Theil-Sen, robust): {report['fitted_slope']:.2f} "
          f"[{report['slope_ci_low']:.2f}, {report['slope_ci_high']:.2f}]")
    print(f"\nRegime: {report['regime']}")
    print(f"\nRecommendation: {report['recommendation']}")
    if "plot_path" in report:
        print(f"\nPlot saved to {report['plot_path']}")
    if "plot_error" in report:
        print(f"\n{report['plot_error']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path", help="long-format CSV: one row per (feature, group, replicate) value")
    ap.add_argument("--feature-col", required=True, help="column name identifying the feature (gene/protein/etc.)")
    ap.add_argument("--group-col", required=True, help="column name identifying the replicate group/condition")
    ap.add_argument("--value-col", required=True, help="column name holding the count/intensity value")
    ap.add_argument("--min-replicates", type=int, default=2,
                     help="minimum replicates per (feature, group) to include (default: 2)")
    ap.add_argument("--plot", nargs="?", const="__show__", default=None,
                     help="show a mean-variance plot, or save to the given path if provided")
    args = ap.parse_args()

    try:
        import pandas as pd
        df = pd.read_csv(args.csv_path)
    except ImportError:
        print("pandas is required for CSV input; `pip install pandas` or import check_mean_variance() directly.",
              file=sys.stderr)
        sys.exit(1)

    for col in (args.feature_col, args.group_col, args.value_col):
        if col not in df.columns:
            print(f"Column '{col}' not found. Available columns: {list(df.columns)}", file=sys.stderr)
            sys.exit(1)

    plot = args.plot is not None
    plot_path = args.plot if (args.plot and args.plot != "__show__") else None

    report = check_mean_variance(df, args.feature_col, args.group_col, args.value_col,
                                  min_replicates=args.min_replicates, plot=plot, plot_path=plot_path)
    _print_report(report)


if __name__ == "__main__":
    main()
