#!/usr/bin/env python3
"""
p-value histogram diagnostic (MSMB ch06 "Testing", ch08 "Count Data & GLMs").

Under a true null, p-values are Uniform(0,1). Across many tests, the shape of
the p-value histogram is the single most informative multiple-testing
diagnostic there is -- plot it before trusting any BH/FDR result.

Shapes and what they mean (see references/06_testing_multiple_comparisons.md):
  - flat/uniform everywhere        -> little/no signal (or underpowered)
  - uniform floor + peak near 0    -> healthy: null component + real signal
  - peak near 0 with a right shoulder -> mix of well- and under-powered tests;
                                          consider independent filtering / IHW
  - spikes at the right edge (near 1) -> discreteness artifact (low counts/n)
  - hump/bulge in the middle, or any non-uniform shape when tests are known
    to be (nearly) all null          -> broken independence / batch effect /
                                          null-model misspecification

Usage:
    python pvalue_histogram_check.py pvalues.csv --column pval --alpha 0.1
    python pvalue_histogram_check.py pvalues.csv --column pval --plot out.png

Or import:
    from pvalue_histogram_check import check_pvalues
    report = check_pvalues(pvals, alpha=0.1)
"""
import argparse
import sys

import numpy as np


def estimate_pi0(pvals):
    """Visual/quick pi0 estimate: pi0 ~= 2 * mean(p > 0.5), assuming null p-values
    are uniform so half of them exceed 0.5. Clipped to [0, 1]."""
    p = np.asarray(pvals, dtype=float)
    p = p[~np.isnan(p)]
    if p.size == 0:
        return np.nan
    return float(np.clip(2 * np.mean(p > 0.5), 0.0, 1.0))


def bh_reject(pvals, alpha=0.1):
    """Benjamini-Hochberg step-up procedure. Returns (reject_mask, threshold_pvalue).
    Equivalent to statsmodels.stats.multitest.multipletests(method='fdr_bh') --
    reimplemented here so this script has no external dependency beyond numpy."""
    p = np.asarray(pvals, dtype=float)
    n = np.sum(~np.isnan(p))
    order = np.argsort(np.where(np.isnan(p), np.inf, p))
    ranked = p[order]
    m = n
    thresh_line = np.arange(1, len(p) + 1) / m * alpha
    below = ranked <= thresh_line
    if not np.any(below):
        k = 0
    else:
        k = np.max(np.where(below)[0]) + 1
    reject = np.zeros_like(p, dtype=bool)
    if k > 0:
        reject[order[:k]] = True
    cutoff_p = ranked[k - 1] if k > 0 else 0.0
    return reject, float(cutoff_p)


def diagnose_shape(pvals, nbins=20):
    """Bin the p-values and flag the shape patterns described in the module
    docstring. Returns a list of (flag_name, message) tuples; empty if the
    histogram looks like a healthy null+signal mixture."""
    p = np.asarray(pvals, dtype=float)
    p = p[~np.isnan(p)]
    n = p.size
    if n == 0:
        return [("no_data", "No non-NaN p-values supplied.")]

    counts, edges = np.histogram(p, bins=nbins, range=(0, 1))
    expected_per_bin = n / nbins
    flags = []

    # Right-edge spike (last bin much higher than the second-to-last few bins)
    tail_bins = counts[-3:]
    body_bins = counts[3:-3] if nbins > 6 else counts
    body_mean = np.mean(body_bins) if len(body_bins) else expected_per_bin
    if body_mean > 0 and counts[-1] > 3 * body_mean:
        flags.append((
            "right_edge_spike",
            f"Spike near p=1 (last bin count={counts[-1]}, typical body bin~={body_mean:.1f}). "
            "Often a discreteness artifact from low counts/small n -- check whether the "
            "asymptotic null approximation is valid for those tests, or filter them out.",
        ))

    # Middle hump (a bin in the interior is a clear local maximum relative to its neighbors
    # and to the flat baseline expected under the null)
    interior = counts[2:-2] if nbins > 4 else counts
    if len(interior) >= 3:
        baseline = np.median(counts[-int(nbins * 0.3):]) if nbins >= 4 else expected_per_bin
        interior_max = interior.max()
        if baseline > 0 and interior_max > 1.5 * baseline and np.argmax(counts) not in (0, 1, nbins - 1, nbins - 2):
            flags.append((
                "middle_hump",
                f"Hump/bulge away from 0 or 1 (peak bin count={interior_max}, baseline~={baseline:.1f}). "
                "If these tests are assumed/known to be (nearly) all null, this signals a broken "
                "independence assumption, an unmodeled batch effect, or null-model misspecification. "
                "Simulate an all-null dataset with the same dependence structure to check.",
            ))

    # Overall flatness vs peak-at-zero
    left_bins = counts[:3]
    baseline_bins = counts[-int(nbins * 0.3):] if nbins >= 4 else counts
    baseline_mean = np.mean(baseline_bins) if len(baseline_bins) else expected_per_bin
    left_mean = np.mean(left_bins)
    if baseline_mean > 0 and left_mean <= 1.3 * baseline_mean:
        flags.append((
            "no_left_peak",
            "No visible peak near p=0 relative to the baseline -- consistent with little/no "
            "detected signal. Could be a true negative result, or the test could be underpowered; "
            "check power separately before concluding 'nothing is going on'.",
        ))

    return flags


def check_pvalues(pvals, alpha=0.1, nbins=20, plot=False, plot_path=None):
    """Run the full diagnostic and return a report dict. If plot=True, also
    draws (and optionally saves to plot_path) the histogram with a BH
    reference line -- requires matplotlib."""
    p = np.asarray(pvals, dtype=float)
    n_total = p.size
    n_valid = int(np.sum(~np.isnan(p)))

    pi0 = estimate_pi0(p)
    reject, cutoff_p = bh_reject(p, alpha=alpha)
    n_reject = int(np.sum(reject))
    flags = diagnose_shape(p, nbins=nbins)

    report = {
        "n_total": n_total,
        "n_valid": n_valid,
        "pi0_estimate": pi0,
        "bh_alpha": alpha,
        "bh_cutoff_pvalue": cutoff_p,
        "n_rejected": n_reject,
        "frac_rejected": n_reject / n_valid if n_valid else float("nan"),
        "shape_flags": flags,
    }

    if plot:
        try:
            import matplotlib
            if plot_path:
                matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(figsize=(5, 4))
            ax.hist(p[~np.isnan(p)], bins=nbins, range=(0, 1), color="#4C72B0", edgecolor="white")
            ax.axhline(n_valid / nbins, color="gray", linestyle="--", linewidth=1, label="uniform expectation")
            if n_reject > 0:
                ax.axvline(cutoff_p, color="crimson", linestyle=":", linewidth=1.5,
                           label=f"BH cutoff @ alpha={alpha} (p<={cutoff_p:.2g})")
            ax.set_xlabel("p-value")
            ax.set_ylabel("count")
            ax.set_title(f"p-value histogram (pi0~={pi0:.2f}, {n_reject}/{n_valid} rejected)")
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
    print(f"n tested (valid p-values): {report['n_valid']} / {report['n_total']}")
    print(f"pi0 estimate (fraction of true nulls): {report['pi0_estimate']:.3f}")
    print(f"BH rejections at alpha={report['bh_alpha']}: {report['n_rejected']} "
          f"({report['frac_rejected']:.1%}), cutoff p-value <= {report['bh_cutoff_pvalue']:.3g}")
    if report["shape_flags"]:
        print("\nShape diagnostics flagged:")
        for name, msg in report["shape_flags"]:
            print(f"  [{name}] {msg}")
    else:
        print("\nNo shape anomalies flagged (healthy uniform-baseline + left-peak pattern, "
              "or too few bins/tests to tell).")
    if "plot_path" in report:
        print(f"\nHistogram saved to {report['plot_path']}")
    if "plot_error" in report:
        print(f"\n{report['plot_error']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path", help="CSV file containing a column of p-values")
    ap.add_argument("--column", default="pval", help="column name holding p-values (default: pval)")
    ap.add_argument("--alpha", type=float, default=0.1, help="BH/FDR target level (default: 0.1)")
    ap.add_argument("--bins", type=int, default=20, help="number of histogram bins (default: 20)")
    ap.add_argument("--plot", nargs="?", const="__show__", default=None,
                     help="show a histogram plot, or save to the given path if provided")
    args = ap.parse_args()

    try:
        import pandas as pd
        df = pd.read_csv(args.csv_path)
    except ImportError:
        print("pandas is required for CSV input; `pip install pandas` or import check_pvalues() directly.",
              file=sys.stderr)
        sys.exit(1)

    if args.column not in df.columns:
        print(f"Column '{args.column}' not found. Available columns: {list(df.columns)}", file=sys.stderr)
        sys.exit(1)

    plot = args.plot is not None
    plot_path = args.plot if (args.plot and args.plot != "__show__") else None

    report = check_pvalues(df[args.column].values, alpha=args.alpha, nbins=args.bins,
                            plot=plot, plot_path=plot_path)
    _print_report(report)


if __name__ == "__main__":
    main()
