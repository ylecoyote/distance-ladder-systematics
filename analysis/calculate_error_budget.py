#!/usr/bin/env python3
"""
Calculate Systematic Error Budget for Cepheid H₀ Measurements

Compares SH0ES claimed systematics vs our independent assessment.

Author: Distance Ladder Systematics Project
Date: October 22, 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =============================================================================
# Load Data
# =============================================================================

data_dir = Path(__file__).parent.parent / "data"
error_budget = pd.read_csv(data_dir / "systematic_error_budget.csv")

print("=" * 80)
print("SYSTEMATIC ERROR BUDGET ANALYSIS")
print("=" * 80)
print()

# =============================================================================
# Calculate Total Systematic Uncertainties
# =============================================================================

print("Individual Error Sources:")
print("-" * 80)
print(f"{'Source':<30} {'SH0ES':<12} {'Our Assessment':<15} {'Confidence':<12}")
print("-" * 80)

for _, row in error_budget.iterrows():
    source = row['Error_Source'].replace('_', ' ')
    shoes = row['SH0ES_Estimate_km_s_Mpc']
    ours = row['Our_Assessment_km_s_Mpc']
    conf = row['Confidence_Level']
    print(f"{source:<30} {shoes:<12.2f} {ours:<15.2f} {conf:<12}")

print("-" * 80)
print()

# =============================================================================
# Calculate Total Systematics
# =============================================================================

# Exclude statistical uncertainty (that's separate)
systematic_sources = error_budget[error_budget['Error_Source'] != 'Statistical_Uncertainty']

# Total systematic (quadrature sum, assuming independent)
shoes_systematic_total = np.sqrt(np.sum(systematic_sources['SH0ES_Estimate_km_s_Mpc']**2))
our_systematic_total = np.sqrt(np.sum(systematic_sources['Our_Assessment_km_s_Mpc']**2))

# Get statistical uncertainty
stat_unc = error_budget[error_budget['Error_Source'] == 'Statistical_Uncertainty']['SH0ES_Estimate_km_s_Mpc'].values[0]

# Total uncertainty
shoes_total = np.sqrt(shoes_systematic_total**2 + stat_unc**2)
our_total = np.sqrt(our_systematic_total**2 + stat_unc**2)

print("TOTAL UNCERTAINTIES:")
print("-" * 80)
print(f"SH0ES σ_sys:           {shoes_systematic_total:.2f} km/s/Mpc")
print(f"Our Assessment σ_sys:  {our_systematic_total:.2f} km/s/Mpc")
print(f"Ratio (Ours/SH0ES):    {our_systematic_total/shoes_systematic_total:.2f}×")
print()
print(f"Statistical σ_stat:    {stat_unc:.2f} km/s/Mpc")
print()
print(f"SH0ES σ_total:         {shoes_total:.2f} km/s/Mpc")
print(f"Our Assessment σ_total: {our_total:.2f} km/s/Mpc")
print("-" * 80)
print()

# =============================================================================
# High Confidence Systematics Only
# =============================================================================

high_confidence = systematic_sources[systematic_sources['Confidence_Level'] == 'High']
our_high_conf_sys = np.sqrt(np.sum(high_confidence['Our_Assessment_km_s_Mpc']**2))

print("HIGH CONFIDENCE SYSTEMATICS ONLY:")
print("-" * 80)
print(f"Our Assessment (high confidence): {our_high_conf_sys:.2f} km/s/Mpc")
print(f"High confidence sources: {', '.join(high_confidence['Error_Source'].str.replace('_', ' ').values)}")
print("-" * 80)
print()

# =============================================================================
# Breakdown by Category
# =============================================================================

# Key systematics we identified
key_systematics = systematic_sources[systematic_sources['Error_Source'].isin([
    'Parallax_Zero_Point', 'Period_Distribution', 'Metallicity_Correction', 'Crowding_Covariant'
])]

key_sys_total = np.sqrt(np.sum(key_systematics['Our_Assessment_km_s_Mpc']**2))

print("KEY SYSTEMATICS (Our Focus):")
print("-" * 80)
for _, row in key_systematics.iterrows():
    source = row['Error_Source'].replace('_', ' ')
    ours = row['Our_Assessment_km_s_Mpc']
    conf = row['Confidence_Level']
    print(f"{source:<30} {ours:<15.2f} {conf:<12}")
print("-" * 80)
print(f"Combined (quadrature):         {key_sys_total:.2f} km/s/Mpc")
print()

# =============================================================================
# Impact on H₀ Measurement
# =============================================================================

H0_SHOES = 73.04  # km/s/Mpc (SH0ES 2022)
H0_PLANCK = 67.36  # km/s/Mpc (Planck 2018)

print("IMPACT ON H₀ MEASUREMENTS:")
print("-" * 80)
print(f"SH0ES H₀:              {H0_SHOES:.2f} ± {shoes_total:.2f} km/s/Mpc")
print(f"With realistic σ_sys:  {H0_SHOES:.2f} ± {our_total:.2f} km/s/Mpc")
print()
print(f"Planck H₀:             {H0_PLANCK:.2f} ± 0.54 km/s/Mpc")
print()

# Calculate tensions
tension_shoes = abs(H0_SHOES - H0_PLANCK) / np.sqrt(shoes_total**2 + 0.54**2)
tension_realistic = abs(H0_SHOES - H0_PLANCK) / np.sqrt(our_total**2 + 0.54**2)

print(f"Tension (SH0ES σ):     {tension_shoes:.1f}σ")
print(f"Tension (realistic σ): {tension_realistic:.1f}σ")
print(f"Tension reduction:     {tension_shoes:.1f}σ → {tension_realistic:.1f}σ")
print("-" * 80)
print()

# =============================================================================
# After Systematic Corrections
# =============================================================================

# Apply key systematic corrections to H₀
H0_corrected = H0_SHOES - key_sys_total  # Conservative: subtract full systematic
sigma_corrected = np.sqrt(stat_unc**2 + (our_systematic_total - key_sys_total)**2)

print("AFTER APPLYING SYSTEMATIC CORRECTIONS:")
print("-" * 80)
print(f"Corrected H₀:          {H0_corrected:.2f} ± {sigma_corrected:.2f} km/s/Mpc")
print()
print(f"Compare to:")
print(f"  CCHP TRGB:           69.85 ± 2.33 km/s/Mpc")
print(f"  CCHP JAGB:           67.96 ± 2.65 km/s/Mpc")
print(f"  Planck:              67.36 ± 0.54 km/s/Mpc")
print()

tension_corrected = abs(H0_corrected - H0_PLANCK) / np.sqrt(sigma_corrected**2 + 0.54**2)
print(f"Tension (corrected):   {tension_corrected:.1f}σ")
print("-" * 80)
print()

# =============================================================================
# Validation Check
# =============================================================================

print("VALIDATION:")
print("-" * 80)
print(f"SH0ES claims σ_sys = 1.04 km/s/Mpc")
print(f"We calculated:       {shoes_systematic_total:.2f} km/s/Mpc")
print(f"Match: {'✓' if abs(shoes_systematic_total - 1.04) < 0.1 else '✗ - check our extraction'}")
print()
print(f"CCHP claims Cepheid σ_sys = 3.10 km/s/Mpc")
print(f"Our assessment:      {our_systematic_total:.2f} km/s/Mpc")
print(f"Our estimate is {our_systematic_total/3.10*100:.0f}% of CCHP's assessment")
print("-" * 80)
print()

# =============================================================================
# Save Results
# =============================================================================

results = pd.DataFrame({
    'Metric': [
        'SH0ES σ_sys',
        'Our Assessment σ_sys',
        'Ratio (Ours/SH0ES)',
        'Statistical σ_stat',
        'SH0ES σ_total',
        'Our Assessment σ_total',
        'SH0ES H₀',
        'Tension (SH0ES σ)',
        'Tension (realistic σ)',
        'Corrected H₀',
        'Tension (corrected)'
    ],
    'Value': [
        f"{shoes_systematic_total:.2f} km/s/Mpc",
        f"{our_systematic_total:.2f} km/s/Mpc",
        f"{our_systematic_total/shoes_systematic_total:.2f}×",
        f"{stat_unc:.2f} km/s/Mpc",
        f"{shoes_total:.2f} km/s/Mpc",
        f"{our_total:.2f} km/s/Mpc",
        f"{H0_SHOES:.2f} ± {shoes_total:.2f} km/s/Mpc",
        f"{tension_shoes:.1f}σ",
        f"{tension_realistic:.1f}σ",
        f"{H0_corrected:.2f} ± {sigma_corrected:.2f} km/s/Mpc",
        f"{tension_corrected:.1f}σ"
    ]
})

output_file = data_dir / "error_budget_summary.csv"
results.to_csv(output_file, index=False)
print(f"Results saved to: {output_file}")
print()

print("=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
