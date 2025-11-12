#!/usr/bin/env python3
"""
Recalculate Systematic Error Budget with Phase 1 Revisions
===========================================================

Implements updated systematic error budget after peer review (M1) revisions:
- Removed covariant crowding as standalone term (AWI-152)
- Updated period distribution to explicit bracket [-1.5, -3.5], mid-range -2.5±1.0 (AWI-153)
- Parallax ZP two scenarios: A (baseline, 0.3) and B (sensitivity, 1.0) (AWI-154)
- Metallicity three priors: Prior 1 (γ=-0.2±0.1, baseline) (AWI-155)

Calculates correlated systematic uncertainty: σ²_sys,corr = σᵀ R σ

Author: Distance Ladder Systematics Project
Date: 2025-11-05
Linear: AWI-156
"""

import numpy as np
import pandas as pd
from pathlib import Path

# =============================================================================
# Configuration
# =============================================================================

DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = DATA_DIR

# Updated σ-vector (Scenario A + Prior 1 baseline)
# Units: km/s/Mpc
SIGMA_VECTOR_BASELINE = {
    'Parallax Zero Point': 0.3,       # Scenario A: adopt SH0ES internal fit
    'Period Distribution': 1.0,        # Uncertainty in -2.5 correction
    'Metallicity Correction': 0.5,     # Prior 1: γ=-0.2±0.1
    'Crowding Direct': 0.3,            # Unchanged from v8.5
    'Photometric Calibration': 0.3,    # Unchanged
    'Extinction Reddening': 0.5,       # Unchanged
    'LMC Distance': 0.2,               # Unchanged
    'NGC4258 Distance': 0.2,           # Unchanged
    'SNe Ia Standardization': 0.5,     # Unchanged
}

# Scenario B sensitivity (external Gaia ZP prior)
SIGMA_VECTOR_SCENARIO_B = SIGMA_VECTOR_BASELINE.copy()
SIGMA_VECTOR_SCENARIO_B['Parallax Zero Point'] = 1.0

# Prior 2 sensitivity (γ=-0.35±0.08, mid-range)
SIGMA_VECTOR_PRIOR2 = SIGMA_VECTOR_BASELINE.copy()
SIGMA_VECTOR_PRIOR2['Metallicity Correction'] = 0.7

# Prior 3 sensitivity (γ=0±0.1, null)
SIGMA_VECTOR_PRIOR3 = SIGMA_VECTOR_BASELINE.copy()
SIGMA_VECTOR_PRIOR3['Metallicity Correction'] = 0.5  # Same uncertainty as Prior 1

# Statistical uncertainty (separate from systematics)
STAT_UNC = 0.8  # km/s/Mpc

# =============================================================================
# Load Correlation Matrix
# =============================================================================

def load_correlation_matrix():
    """Load updated 9×9 correlation matrix (crowding_covariant removed)."""
    R = pd.read_csv(DATA_DIR / "correlation_matrix_updated.csv", index_col=0)
    return R

# =============================================================================
# Calculate Correlated Systematic Uncertainty
# =============================================================================

def calculate_correlated_systematic(sigma_dict, R_matrix):
    """
    Calculate correlated systematic uncertainty: σ²_sys,corr = σᵀ R σ

    Parameters
    ----------
    sigma_dict : dict
        Dictionary mapping systematic source names to uncertainties (km/s/Mpc)
    R_matrix : pd.DataFrame
        Correlation matrix (must have same index/columns as sigma_dict keys)

    Returns
    -------
    dict
        Results containing:
        - sigma_sys_uncorr: Quadrature sum (independence assumption)
        - sigma_sys_corr: Correlated propagation
        - inflation_factor: sigma_sys_corr / sigma_sys_uncorr
        - sigma_total: Combined systematic + statistical
    """
    # Ensure ordering matches
    sources = list(sigma_dict.keys())
    sigma_vec = np.array([sigma_dict[s] for s in sources])

    # Reorder correlation matrix to match
    R = R_matrix.loc[sources, sources].values

    # Uncorrelated (independence) calculation
    sigma_sys_uncorr = np.sqrt(np.sum(sigma_vec**2))

    # Correlated calculation: σ²_sys,corr = σᵀ R σ
    sigma_sys_corr_sq = sigma_vec.T @ R @ sigma_vec
    sigma_sys_corr = np.sqrt(sigma_sys_corr_sq)

    # Inflation factor from correlations
    inflation_factor = sigma_sys_corr / sigma_sys_uncorr

    # Total uncertainty (systematic + statistical in quadrature)
    sigma_total = np.sqrt(sigma_sys_corr**2 + STAT_UNC**2)

    return {
        'sigma_sys_uncorr': sigma_sys_uncorr,
        'sigma_sys_corr': sigma_sys_corr,
        'inflation_factor': inflation_factor,
        'sigma_total': sigma_total,
    }

# =============================================================================
# Main Analysis
# =============================================================================

def main():
    print("="*80)
    print("RECALCULATED SYSTEMATIC ERROR BUDGET (Post Peer Review M1)")
    print("="*80)
    print()

    # Load correlation matrix
    R = load_correlation_matrix()
    print("Loaded 9×9 correlation matrix (crowding_covariant removed)")
    print(f"Dimensions: {R.shape}")
    print()

    # Calculate for all scenarios
    scenarios = {
        'Baseline (Scenario A + Prior 1)': SIGMA_VECTOR_BASELINE,
        'Scenario B (External Gaia ZP)': SIGMA_VECTOR_SCENARIO_B,
        'Prior 2 (γ=-0.35, mid-range)': SIGMA_VECTOR_PRIOR2,
        'Prior 3 (γ=0, null)': SIGMA_VECTOR_PRIOR3,
    }

    results_all = {}

    for scenario_name, sigma_dict in scenarios.items():
        print("-"*80)
        print(f"SCENARIO: {scenario_name}")
        print("-"*80)
        print()

        # Display σ-vector
        print("σ-vector (km/s/Mpc):")
        for source, sigma in sigma_dict.items():
            print(f"  {source:30s} {sigma:5.2f}")
        print()

        # Calculate correlated systematics
        results = calculate_correlated_systematic(sigma_dict, R)
        results_all[scenario_name] = results

        # Display results
        print("Results:")
        print(f"  σ_sys (uncorrelated):  {results['sigma_sys_uncorr']:.3f} km/s/Mpc")
        print(f"  σ_sys (correlated):    {results['sigma_sys_corr']:.3f} km/s/Mpc")
        print(f"  Inflation factor:       {results['inflation_factor']:.3f}×")
        print(f"  σ_stat:                 {STAT_UNC:.3f} km/s/Mpc")
        print(f"  σ_total:                {results['sigma_total']:.3f} km/s/Mpc")
        print()

    # Summary table
    print("="*80)
    print("SUMMARY TABLE")
    print("="*80)
    print()
    print(f"{'Scenario':<40s} {'σ_sys,corr':<12s} {'Inflation':<10s} {'σ_total':<10s}")
    print("-"*80)
    for scenario_name, results in results_all.items():
        print(f"{scenario_name:<40s} {results['sigma_sys_corr']:>10.3f}   "
              f"{results['inflation_factor']:>8.3f}×  {results['sigma_total']:>8.3f}")
    print("-"*80)
    print()

    # Save baseline results
    baseline_results = results_all['Baseline (Scenario A + Prior 1)']

    summary = pd.DataFrame({
        'Quantity': [
            'σ_sys (uncorrelated)',
            'σ_sys (correlated)',
            'Inflation factor',
            'σ_stat',
            'σ_total',
        ],
        'Value_km_s_Mpc': [
            baseline_results['sigma_sys_uncorr'],
            baseline_results['sigma_sys_corr'],
            baseline_results['inflation_factor'],
            STAT_UNC,
            baseline_results['sigma_total'],
        ],
        'Notes': [
            'Quadrature sum assuming independence',
            'Correlated propagation: σᵀRσ',
            'Correlated / Uncorrelated',
            'Statistical uncertainty (fixed)',
            'Combined systematic + statistical',
        ]
    })

    output_file = OUTPUT_DIR / "systematic_budget_recalculated.csv"
    summary.to_csv(output_file, index=False)
    print(f"Saved baseline results to: {output_file}")
    print()

    # Compare to v8.5 values
    print("="*80)
    print("COMPARISON TO V8.5")
    print("="*80)
    print()
    print("V8.5 values (with crowding_covariant):")
    print("  σ_sys (correlated):  3.14 km/s/Mpc")
    print("  σ_total:             3.24 km/s/Mpc")
    print()
    print(f"Updated baseline (Scenario A + Prior 1):")
    print(f"  σ_sys (correlated):  {baseline_results['sigma_sys_corr']:.2f} km/s/Mpc")
    print(f"  σ_total:             {baseline_results['sigma_total']:.2f} km/s/Mpc")
    print()

    delta_sys = baseline_results['sigma_sys_corr'] - 3.14
    delta_total = baseline_results['sigma_total'] - 3.24

    print(f"Change:")
    print(f"  Δσ_sys:  {delta_sys:+.2f} km/s/Mpc")
    print(f"  Δσ_total: {delta_total:+.2f} km/s/Mpc")
    print()

    # Impact on tension
    H0_SHOES = 73.17  # km/s/Mpc (SH0ES 2022, with stat unc)
    H0_PLANCK = 67.36  # km/s/Mpc (Planck 2018)
    SIGMA_PLANCK = 0.54  # km/s/Mpc

    # Baseline corrections (Scenario A + Prior 1)
    # Parallax: 0 (Scenario A adopts SH0ES internal fit)
    # Period: -2.5 km/s/Mpc
    # Metallicity: -1.0 km/s/Mpc (Prior 1)
    CORRECTION_BASELINE = 0 - 2.5 - 1.0  # = -3.5 km/s/Mpc

    H0_corrected = H0_SHOES + CORRECTION_BASELINE
    sigma_combined = np.sqrt(baseline_results['sigma_total']**2 + SIGMA_PLANCK**2)

    tension = abs(H0_corrected - H0_PLANCK) / sigma_combined

    print("="*80)
    print("IMPACT ON HUBBLE TENSION (Baseline: Scenario A + Prior 1)")
    print("="*80)
    print()
    print(f"H₀ (SH0ES 2022):           {H0_SHOES:.2f} km/s/Mpc")
    print(f"Corrections:")
    print(f"  Parallax (Scenario A):   {0:+.2f} km/s/Mpc")
    print(f"  Period distribution:     {-2.5:+.2f} km/s/Mpc")
    print(f"  Metallicity (Prior 1):   {-1.0:+.2f} km/s/Mpc")
    print(f"  Total correction:        {CORRECTION_BASELINE:+.2f} km/s/Mpc")
    print()
    print(f"H₀ (corrected):            {H0_corrected:.2f} ± {baseline_results['sigma_total']:.2f} km/s/Mpc")
    print(f"H₀ (Planck):               {H0_PLANCK:.2f} ± {SIGMA_PLANCK:.2f} km/s/Mpc")
    print()
    print(f"Combined uncertainty:      {sigma_combined:.2f} km/s/Mpc")
    print(f"Tension:                   {tension:.2f}σ")
    print()
    print("="*80)
    print("✅ Recalculation complete!")
    print("="*80)
    print()

if __name__ == "__main__":
    main()
