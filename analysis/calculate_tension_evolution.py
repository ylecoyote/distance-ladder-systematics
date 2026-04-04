#!/usr/bin/env python3
"""
Calculate Tension Evolution: Step-by-Step Corrections (Scenario A + Prior 1 Baseline)

Shows how H₀ tension reduces from 5.9σ to 1.1σ as we apply systematic corrections.

Values must match manuscript (manuscript.tex §3.2) and YAML contract
(config/numerical_claims.yaml → tension_evolution).

Scenario A + Prior 1 baseline:
  - Stage 1: Statistical only (H₀ = 73.04, σ = 0.80)
  - Stage 2: quoted SH0ES systematic budget + statistical uncertainty (H₀ = 73.04, σ = 1.31)
  - Stage 3: Scenario A parallax ZP — no bias correction (H₀ = 73.04, σ = 1.31)
  - Stage 4: Period distribution correction −2.5 km/s/Mpc (H₀ = 70.54, σ = 1.65)
  - Stage 5: Metallicity −1.0 + realistic correlated σ_sys (H₀ = 69.54, σ = 1.89)

Author: Distance Ladder Systematics Project
"""

import numpy as np
import pandas as pd
import json
from pathlib import Path

# =============================================================================
# Constants (from manuscript and YAML contract)
# =============================================================================

H0_SHOES = 73.04       # km/s/Mpc (SH0ES 2022, Riess et al.)
H0_PLANCK = 67.36      # km/s/Mpc (Planck 2018 + ΛCDM)
SIGMA_PLANCK = 0.54    # km/s/Mpc

# SH0ES uncertainties
SIGMA_SHOES_STAT = 0.80   # km/s/Mpc (statistical)
SIGMA_SHOES_SYS = 1.04    # km/s/Mpc (systematic, claimed)

# Bias corrections (Scenario A + Prior 1 baseline)
PARALLAX_CORRECTION = 0.0    # Scenario A: adopt SH0ES internal ZP, no bias correction
PERIOD_CORRECTION = -2.5     # mid-range of bracket [−1.5, −3.5] km/s/Mpc
METALLICITY_CORRECTION = -1.0  # Prior 1: γ = −0.2 ± 0.1, Δ[Fe/H] = +0.15

# Our systematic assessment (Scenario A + Prior 1, correlated)
SIGMA_SYS_CORR = 1.71   # km/s/Mpc (from 9×9 correlated error budget)

# =============================================================================
# Helper Functions
# =============================================================================

def calculate_tension(H0_local, sigma_local, H0_early=H0_PLANCK, sigma_early=SIGMA_PLANCK):
    """Calculate tension in sigma between local and early universe H₀"""
    diff = abs(H0_local - H0_early)
    combined_sigma = np.sqrt(sigma_local**2 + sigma_early**2)
    return diff / combined_sigma

def quadrature(*args):
    """Add uncertainties in quadrature"""
    return np.sqrt(sum(x**2 for x in args))

# =============================================================================
# Tension Evolution: 5 Stages (Scenario A + Prior 1)
# =============================================================================

print("=" * 80)
print("TENSION EVOLUTION: SCENARIO A + PRIOR 1 BASELINE")
print("=" * 80)
print()

# Stage 1: Baseline (statistical only)
h0_s1 = H0_SHOES
sigma_s1 = SIGMA_SHOES_STAT
tension_s1 = calculate_tension(h0_s1, sigma_s1)

print(f"Stage 1: Statistical only")
print(f"  H₀ = {h0_s1:.2f} ± {sigma_s1:.2f} km/s/Mpc")
print(f"  Tension = {tension_s1:.1f}σ")
print()

# Stage 2: SH0ES total uncertainty (stat + sys in quadrature)
h0_s2 = H0_SHOES
sigma_s2 = quadrature(SIGMA_SHOES_STAT, SIGMA_SHOES_SYS)  # sqrt(0.80² + 1.04²) = 1.31
tension_s2 = calculate_tension(h0_s2, sigma_s2)

print(f"Stage 2: quoted SH0ES systematic budget + statistical uncertainty")
print(f"  H₀ = {h0_s2:.2f} ± {sigma_s2:.2f} km/s/Mpc")
print(f"  Tension = {tension_s2:.1f}σ")
print()

# Stage 3: Scenario A parallax — no bias correction, same uncertainty
h0_s3 = H0_SHOES + PARALLAX_CORRECTION  # 73.04 + 0.0 = 73.04
sigma_s3 = sigma_s2  # unchanged
tension_s3 = calculate_tension(h0_s3, sigma_s3)

print(f"Stage 3: Scenario A parallax (no bias correction)")
print(f"  H₀ = {h0_s3:.2f} ± {sigma_s3:.2f} km/s/Mpc")
print(f"  Tension = {tension_s3:.1f}σ")
print()

# Stage 4: Period distribution correction
h0_s4 = h0_s3 + PERIOD_CORRECTION  # 73.04 − 2.5 = 70.54
# Uncertainty grows: add period correction uncertainty (±1.0) in quadrature
sigma_s4 = quadrature(SIGMA_SHOES_STAT, SIGMA_SHOES_SYS, 1.0)  # sqrt(0.80² + 1.04² + 1.0²) = 1.65
tension_s4 = calculate_tension(h0_s4, sigma_s4)

print(f"Stage 4: After period distribution correction ({PERIOD_CORRECTION:+.1f} km/s/Mpc)")
print(f"  H₀ = {h0_s4:.2f} ± {sigma_s4:.2f} km/s/Mpc")
print(f"  Tension = {tension_s4:.1f}σ")
print()

# Stage 5: Metallicity correction + realistic correlated systematics
h0_s5 = h0_s4 + METALLICITY_CORRECTION  # 70.54 − 1.0 = 69.54
# Replace SH0ES systematics with our correlated assessment
sigma_s5 = quadrature(SIGMA_SHOES_STAT, SIGMA_SYS_CORR)  # sqrt(0.80² + 1.71²) = 1.89
tension_s5 = calculate_tension(h0_s5, sigma_s5)

print(f"Stage 5: After metallicity correction ({METALLICITY_CORRECTION:+.1f} km/s/Mpc) + realistic σ_sys")
print(f"  H₀ = {h0_s5:.2f} ± {sigma_s5:.2f} km/s/Mpc")
print(f"  σ_sys,corr = {SIGMA_SYS_CORR:.2f} km/s/Mpc")
print(f"  Tension = {tension_s5:.1f}σ")
print()

# =============================================================================
# Summary
# =============================================================================

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"  Tension reduction: {tension_s1:.1f}σ → {tension_s5:.1f}σ")
print(f"  Factor:            {tension_s1/tension_s5:.1f}×")
print(f"  Corrected H₀:     {h0_s5:.2f} ± {sigma_s5:.2f} km/s/Mpc")
print("=" * 80)
print()

# =============================================================================
# Save Results
# =============================================================================

data_dir = Path(__file__).parent.parent / "data"

# CSV
evolution_data = pd.DataFrame({
    'Stage': [
        'Statistical only',
        'Quoted SH0ES sys. + stat.',
        'Scenario A parallax',
        'After period distribution',
        'After metallicity + realistic σ'
    ],
    'H0_km_s_Mpc': [h0_s1, h0_s2, h0_s3, h0_s4, h0_s5],
    'Sigma_km_s_Mpc': [sigma_s1, sigma_s2, sigma_s3, sigma_s4, sigma_s5],
    'Tension_sigma': [tension_s1, tension_s2, tension_s3, tension_s4, tension_s5],
    'Description': [
        'Baseline SH0ES H₀ with statistical uncertainty only',
        'Reconstructed from SH0ES statistical uncertainty plus quoted systematic budget',
        'Scenario A: adopt SH0ES internal parallax ZP, no bias correction',
        'Period distribution correction −2.5 km/s/Mpc (mid-range of bracket)',
        'Metallicity correction −1.0 km/s/Mpc (Prior 1) + realistic correlated σ_sys = 1.71'
    ]
})

csv_path = data_dir / "tension_evolution.csv"
evolution_data.to_csv(csv_path, index=False)
print(f"CSV saved to: {csv_path}")

# JSON summary
summary_data = {
    "metric": "tension_evolution",
    "scenario": "Scenario A + Prior 1 (baseline)",
    "initial_tension": round(tension_s1, 2),
    "final_tension": round(tension_s5, 2),
    "reduction_factor": round(tension_s1 / tension_s5, 2),
    "stages": {
        "1": {"name": "Statistical only", "h0": round(h0_s1, 2), "sigma": round(sigma_s1, 2), "tension": round(tension_s1, 2)},
        "2": {"name": "Quoted SH0ES sys. + stat.", "h0": round(h0_s2, 2), "sigma": round(sigma_s2, 2), "tension": round(tension_s2, 2)},
        "3": {"name": "Scenario A parallax", "h0": round(h0_s3, 2), "sigma": round(sigma_s3, 2), "tension": round(tension_s3, 2)},
        "4": {"name": "Period distribution", "h0": round(h0_s4, 2), "sigma": round(sigma_s4, 2), "tension": round(tension_s4, 2)},
        "5": {"name": "Metallicity + realistic σ", "h0": round(h0_s5, 2), "sigma": round(sigma_s5, 2), "tension": round(tension_s5, 2)}
    }
}

json_path = data_dir / "tension_evolution_summary.json"
with open(json_path, 'w') as f:
    json.dump(summary_data, f, indent=2)
print(f"JSON saved to: {json_path}")
print()

# =============================================================================
# Comparison with Alternative Distance Indicators
# =============================================================================

H0_TRGB = 69.85
SIGMA_TRGB = 2.33
H0_JAGB = 67.96
SIGMA_JAGB = 2.65
H0_CC = 68.33
SIGMA_CC = 1.57

print("COMPARISON WITH ALTERNATIVE DISTANCE INDICATORS:")
print("=" * 80)
print(f"  Corrected Cepheid: {h0_s5:.2f} ± {sigma_s5:.2f} km/s/Mpc")
print(f"  CCHP TRGB:         {H0_TRGB:.2f} ± {SIGMA_TRGB:.2f} km/s/Mpc  (Δ = {abs(h0_s5 - H0_TRGB):.2f}, {abs(h0_s5 - H0_TRGB)/np.sqrt(sigma_s5**2 + SIGMA_TRGB**2):.1f}σ)")
print(f"  CCHP JAGB:         {H0_JAGB:.2f} ± {SIGMA_JAGB:.2f} km/s/Mpc  (Δ = {abs(h0_s5 - H0_JAGB):.2f}, {abs(h0_s5 - H0_JAGB)/np.sqrt(sigma_s5**2 + SIGMA_JAGB**2):.1f}σ)")
print(f"  Cosmic Chron.:     {H0_CC:.2f} ± {SIGMA_CC:.2f} km/s/Mpc  (Δ = {abs(h0_s5 - H0_CC):.2f}, {abs(h0_s5 - H0_CC)/np.sqrt(sigma_s5**2 + SIGMA_CC**2):.1f}σ)")
print(f"  Planck:            {H0_PLANCK:.2f} ± {SIGMA_PLANCK:.2f} km/s/Mpc  (Δ = {abs(h0_s5 - H0_PLANCK):.2f}, {tension_s5:.1f}σ)")
print("=" * 80)
print()
print("ANALYSIS COMPLETE")
