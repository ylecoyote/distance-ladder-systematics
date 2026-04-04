#!/usr/bin/env python3
"""
Calculate the manuscript baseline systematic error budget.

This script is the repository-facing summary for the Scenario A + Prior 1
baseline used throughout the manuscript:
  - uncorrelated systematic budget: 1.45 km/s/Mpc
  - correlated systematic budget: 1.71 km/s/Mpc
  - corrected Cepheid value: 69.54 ± 1.89 km/s/Mpc
  - Planck-relative tension: 1.1σ
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

SYSTEMATIC_NAME_MAP = {
    "Parallax_Zero_Point": "Parallax Zero Point",
    "Period_Distribution": "Period Distribution",
    "Metallicity_Correction": "Metallicity Correction",
    "Crowding_Direct": "Crowding Direct",
    "Photometric_Calibration": "Photometric Calibration",
    "Extinction_Reddening": "Extinction Reddening",
    "LMC_Distance": "LMC Distance",
    "NGC4258_Distance": "NGC4258 Distance",
    "SNe_Ia_Standardization": "SNe Ia Standardization",
}

H0_SHOES = 73.04
H0_PLANCK = 67.36
SIGMA_PLANCK = 0.54
PARALLAX_CORRECTION = 0.0
PERIOD_CORRECTION = -2.5
METALLICITY_CORRECTION = -1.0


def quadrature(values: np.ndarray) -> float:
    return float(np.sqrt(np.sum(values**2)))


def calculate_tension(h0_local: float, sigma_local: float) -> float:
    return abs(h0_local - H0_PLANCK) / np.sqrt(sigma_local**2 + SIGMA_PLANCK**2)


def load_budget() -> tuple[pd.DataFrame, pd.DataFrame]:
    budget = pd.read_csv(DATA_DIR / "systematic_error_budget.csv", comment="#")
    correlation = pd.read_csv(
        DATA_DIR / "correlation_matrix_updated.csv",
        index_col=0,
        comment="#",
    )
    return budget, correlation


def build_vectors(budget: pd.DataFrame, correlation: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    # Statistical uncertainty is handled separately. Crowding_Covariant was removed
    # as a standalone term and is represented only through the correlation matrix.
    filtered = budget[
        ~budget["Error_Source"].isin(["Statistical_Uncertainty", "Crowding_Covariant"])
    ].copy()
    filtered["Matrix_Name"] = filtered["Error_Source"].map(SYSTEMATIC_NAME_MAP)
    filtered = filtered.set_index("Matrix_Name").loc[correlation.index]

    shoes = filtered["SH0ES_Estimate_km_s_Mpc"].to_numpy(dtype=float)
    ours = filtered["Our_Assessment_km_s_Mpc"].to_numpy(dtype=float)
    return shoes, ours


def main() -> None:
    budget, correlation = load_budget()
    shoes_vector, our_vector = build_vectors(budget, correlation)
    corr_matrix = correlation.to_numpy(dtype=float)

    stat_unc = float(
        budget.loc[
            budget["Error_Source"] == "Statistical_Uncertainty",
            "SH0ES_Estimate_km_s_Mpc",
        ].iloc[0]
    )

    shoes_systematic_uncorr = quadrature(shoes_vector)
    our_systematic_uncorr = quadrature(our_vector)
    shoes_systematic_corr = float(np.sqrt(shoes_vector.T @ corr_matrix @ shoes_vector))
    our_systematic_corr = float(np.sqrt(our_vector.T @ corr_matrix @ our_vector))

    shoes_total = float(np.sqrt(stat_unc**2 + shoes_systematic_uncorr**2))
    our_total_uncorr = float(np.sqrt(stat_unc**2 + our_systematic_uncorr**2))
    our_total_corr = float(np.sqrt(stat_unc**2 + our_systematic_corr**2))

    h0_corrected = H0_SHOES + PARALLAX_CORRECTION + PERIOD_CORRECTION + METALLICITY_CORRECTION
    tension_shoes = calculate_tension(H0_SHOES, shoes_total)
    tension_realistic_sigma_only = calculate_tension(H0_SHOES, our_total_corr)
    tension_corrected = calculate_tension(h0_corrected, our_total_corr)

    planck_independent_h0 = 68.22
    planck_independent_sigma = 1.36
    planck_independent_tension = abs(h0_corrected - planck_independent_h0) / np.sqrt(
        our_total_corr**2 + planck_independent_sigma**2
    )

    print("=" * 80)
    print("SYSTEMATIC ERROR BUDGET ANALYSIS")
    print("=" * 80)
    print()
    print("Baseline: Scenario A + Prior 1")
    print()
    print("Systematic totals:")
    print(f"  SH0ES σ_sys (uncorrelated):       {shoes_systematic_uncorr:.2f} km/s/Mpc")
    print(f"  SH0ES σ_sys (correlated):         {shoes_systematic_corr:.2f} km/s/Mpc")
    print(f"  Our σ_sys (uncorrelated):         {our_systematic_uncorr:.2f} km/s/Mpc")
    print(f"  Our σ_sys (correlated):           {our_systematic_corr:.2f} km/s/Mpc")
    print(f"  Correlation inflation:            {our_systematic_corr / our_systematic_uncorr:.2f}×")
    print()
    print("Total uncertainties:")
    print(f"  Statistical σ_stat:               {stat_unc:.2f} km/s/Mpc")
    print(f"  SH0ES σ_total:                    {shoes_total:.2f} km/s/Mpc")
    print(f"  Our σ_total (uncorrelated):       {our_total_uncorr:.2f} km/s/Mpc")
    print(f"  Our σ_total (correlated):         {our_total_corr:.2f} km/s/Mpc")
    print()
    print("Impact on H₀:")
    print(f"  SH0ES published:                  {H0_SHOES:.2f} ± {shoes_total:.2f} km/s/Mpc")
    print(f"  Realistic σ only:                 {H0_SHOES:.2f} ± {our_total_corr:.2f} km/s/Mpc")
    print(
        f"  Corrected baseline:               {h0_corrected:.2f} ± {our_total_corr:.2f} km/s/Mpc"
    )
    print()
    print("Tension vs Planck:")
    print(f"  With SH0ES published σ_total:     {tension_shoes:.1f}σ")
    print(f"  With realistic correlated σ only: {tension_realistic_sigma_only:.1f}σ")
    print(f"  After baseline corrections:       {tension_corrected:.1f}σ")
    print()
    print("Planck-independent comparison:")
    print(
        f"  JAGB + cosmic chronometers:       {planck_independent_h0:.2f} ± {planck_independent_sigma:.2f} km/s/Mpc"
    )
    print(f"  Corrected Cepheid vs JAGB+CC:     {planck_independent_tension:.1f}σ")
    print()

    summary_rows = [
        ("SH0ES σ_sys (uncorrelated)", shoes_systematic_uncorr),
        ("SH0ES σ_sys (correlated)", shoes_systematic_corr),
        ("Our σ_sys (uncorrelated)", our_systematic_uncorr),
        ("Our σ_sys (correlated)", our_systematic_corr),
        ("Correlation inflation factor", our_systematic_corr / our_systematic_uncorr),
        ("Statistical σ_stat", stat_unc),
        ("SH0ES σ_total", shoes_total),
        ("Our σ_total (uncorrelated)", our_total_uncorr),
        ("Our σ_total (correlated)", our_total_corr),
        ("Corrected H₀", h0_corrected),
        ("Tension vs Planck (SH0ES σ_total)", tension_shoes),
        ("Tension vs Planck (realistic σ only)", tension_realistic_sigma_only),
        ("Tension vs Planck (corrected baseline)", tension_corrected),
        ("Tension vs JAGB+CC (corrected baseline)", planck_independent_tension),
    ]

    summary_df = pd.DataFrame(summary_rows, columns=["Metric", "Value"])
    summary_csv = DATA_DIR / "error_budget_summary.csv"
    summary_df.to_csv(summary_csv, index=False)
    print(f"Summary CSV saved to: {summary_csv}")

    summary_json = {
        "metric": "systematic_error_budget",
        "baseline": "Scenario A + Prior 1",
        "shoes_systematic_uncorrelated": round(shoes_systematic_uncorr, 2),
        "shoes_systematic_correlated": round(shoes_systematic_corr, 2),
        "our_systematic_uncorrelated": round(our_systematic_uncorr, 2),
        "our_systematic_correlated": round(our_systematic_corr, 2),
        "correlation_inflation_factor": round(our_systematic_corr / our_systematic_uncorr, 2),
        "statistical": round(stat_unc, 2),
        "shoes_total": round(shoes_total, 2),
        "our_total_uncorrelated": round(our_total_uncorr, 2),
        "our_total_correlated": round(our_total_corr, 2),
        "bias_corrections": {
            "parallax": PARALLAX_CORRECTION,
            "period_distribution": PERIOD_CORRECTION,
            "metallicity": METALLICITY_CORRECTION,
        },
        "tensions": {
            "shoes_published_sigma": round(tension_shoes, 2),
            "realistic_sigma_only": round(tension_realistic_sigma_only, 2),
            "corrected_baseline_planck": round(tension_corrected, 2),
            "corrected_baseline_jagb_cc": round(planck_independent_tension, 2),
        },
        "h0_corrected": round(h0_corrected, 2),
        "sigma_corrected": round(our_total_corr, 2),
    }

    summary_json_path = DATA_DIR / "error_budget_summary.json"
    with open(summary_json_path, "w") as f:
        json.dump(summary_json, f, indent=2)
    print(f"Summary JSON saved to: {summary_json_path}")
    print()
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
