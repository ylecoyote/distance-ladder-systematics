#!/usr/bin/env python3
"""
Generate Manuscript Tables 1-3

Creates publication-ready tables for Distance Ladder Systematics manuscript.

Tables:
1. H₀ Measurements Compilation
2. Systematic Error Budget
3. Phase Findings Summary

Author: Distance Ladder Systematics Project
Date: October 22, 2025
"""

import numpy as np
import pandas as pd
from pathlib import Path

# =============================================================================
# Table 1: H₀ Measurements Compilation
# =============================================================================

print("=" * 80)
print("GENERATING TABLE 1: H₀ MEASUREMENTS COMPILATION")
print("=" * 80)
print()

table1 = pd.DataFrame({
    'Method': [
        'SH0ES Cepheid',
        'CCHP Cepheid',
        'CCHP TRGB',
        'CCHP JAGB',
        'Cosmic Chronometers H(z)',
        'Gravitational Lensing (H0LiCOW)',
        'Megamaser (NGC 4258)',
        'Mira Variables',
        'Surface Brightness Fluctuations',
        'Planck CMB + ΛCDM',
        'BAO + BBN'
    ],
    'H0_km_s_Mpc': [
        73.17,
        72.05,
        69.85,
        67.96,
        68.33,
        73.3,
        73.9,
        73.3,
        73.3,
        67.36,
        68.0
    ],
    'Sigma_stat_km_s_Mpc': [
        0.80,
        1.86,
        np.nan,  # Not separately reported
        np.nan,
        1.57,
        1.8,
        3.0,
        4.0,
        2.5,
        0.54,
        np.nan
    ],
    'Sigma_sys_km_s_Mpc': [
        1.04,
        3.10,
        np.nan,
        np.nan,
        np.nan,  # Model-independent
        np.nan,
        np.nan,
        np.nan,
        np.nan,
        np.nan,  # Model-dependent
        np.nan
    ],
    'Sigma_total_km_s_Mpc': [
        1.31,
        3.62,
        2.33,
        2.65,
        1.57,
        1.8,
        3.0,
        4.0,
        2.5,
        0.54,
        1.0
    ],
    'Category': [
        'Distance Ladder',
        'Distance Ladder',
        'Distance Ladder',
        'Distance Ladder',
        'Model-Independent',
        'Model-Independent',
        'Geometric',
        'Distance Ladder',
        'Distance Ladder',
        'Early Universe',
        'Early Universe'
    ],
    'Reference': [
        'Riess+ 2024',
        'Freedman+ 2025',
        'Freedman+ 2025',
        'Freedman+ 2025',
        'This work; Moresco+ 2022',
        'Wong+ 2020 (H0LiCOW)',
        'Pesce+ 2020',
        'Huang+ 2020',
        'Blakeslee+ 2021',
        'Planck 2018',
        'DES+DESI 2024'
    ]
})

# Save Table 1
output_dir = Path(__file__).parent.parent / "tables"
output_dir.mkdir(exist_ok=True)
output_file1 = output_dir / "table1_h0_measurements.csv"
table1.to_csv(output_file1, index=False)
print(f"Table 1 saved to: {output_file1}")
print()
print(table1.to_string(index=False))
print()

# =============================================================================
# Table 2: Systematic Error Budget
# =============================================================================

print("=" * 80)
print("GENERATING TABLE 2: SYSTEMATIC ERROR BUDGET")
print("=" * 80)
print()

table2 = pd.DataFrame({
    'Error_Source': [
        'Parallax Zero Point',
        'Period Distribution',
        'Metallicity Correction',
        'Crowding (Direct)',
        'Crowding (Covariant)',
        'Photometric Calibration',
        'Extinction/Reddening',
        'LMC Distance',
        'NGC 4258 Distance',
        'SNe Ia Standardization',
        '---',  # Separator
        'TOTAL (Quadrature)'
    ],
    'SH0ES_Estimate_km_s_Mpc': [
        0.3,
        0.0,
        0.4,
        0.5,
        0.0,
        0.3,
        0.4,
        0.2,
        0.2,
        0.5,
        np.nan,
        1.04
    ],
    'Our_Assessment_km_s_Mpc': [
        1.0,
        1.0,
        1.0,
        0.3,
        1.5,
        0.3,
        0.5,
        0.2,
        0.2,
        0.5,
        np.nan,
        2.45
    ],
    'Confidence_Level': [
        'High',
        'Medium',
        'Medium',
        'High',
        'Medium',
        'High',
        'Medium',
        'High',
        'High',
        'Medium',
        '',
        'High'
    ],
    'Notes': [
        'Dec 2024: ~0.017 mas Gaia offset',
        'Dec 2024: p < 0.001 significance',
        'γ range -0.2 to -0.5 mag/dex',
        'SH0ES JWST: no bias (-0.01±0.03 mag)',
        'Freedman: crowding→colors→dust→metallicity',
        'HST standards well-calibrated',
        'Dust law uncertainty',
        'Pietrzyński+ 2019 geometric',
        'Humphreys+ 2013 megamaser',
        'Tripp parameters, host mass',
        '',
        'Factor 2.4× larger than SH0ES'
    ]
})

output_file2 = output_dir / "table2_error_budget.csv"
table2.to_csv(output_file2, index=False)
print(f"Table 2 saved to: {output_file2}")
print()
print(table2.to_string(index=False))
print()

# =============================================================================
# Table 3: Phase Findings Summary
# =============================================================================

print("=" * 80)
print("GENERATING TABLE 3: PHASE FINDINGS SUMMARY")
print("=" * 80)
print()

table3 = pd.DataFrame({
    'Phase': [
        'Phase 1: Literature Review',
        'Phase 2: Cepheid Methodology',
        'Phase 3: Crowding Analysis',
        'Phase 4: Metallicity & Period'
    ],
    'Key_Finding': [
        'Factor 3× discrepancy in systematic error budgets (SH0ES 1.04 vs CCHP 3.10 km/s/Mpc)',
        'CCHP cross-validation: Cepheids 2.5-4% higher than TRGB/JAGB in same galaxies',
        'Crowding is NOT systematic bias (SH0ES JWST), but adds uncertainty via covariant effects (CCHP)',
        'Period distribution mismatch (p<0.001) and metallicity uncertainty combine for ~2 km/s/Mpc'
    ],
    'Impact_on_H0_km_s_Mpc': [
        'Establishes need for independent assessment',
        '~2.0 (Cepheid-TRGB difference)',
        '~1.5 (covariant propagation)',
        '~2.0 (parallax 1.0 + period 1.0)'
    ],
    'Confidence': [
        'High (literature consensus)',
        'High (CCHP data)',
        'High (SH0ES JWST) + Medium (covariant)',
        'High (parallax) + Medium (period, metallicity)'
    ],
    'References': [
        'Riess+ 2022, 2024; Freedman+ 2025',
        'Freedman+ 2025 CCHP',
        'Riess+ 2024 JWST; Freedman+ 2025',
        'arXiv:2412.07840; Empirical metallicity studies'
    ]
})

output_file3 = output_dir / "table3_phase_findings.csv"
table3.to_csv(output_file3, index=False)
print(f"Table 3 saved to: {output_file3}")
print()
print(table3.to_string(index=False))
print()

# =============================================================================
# Generate LaTeX Versions
# =============================================================================

print("=" * 80)
print("GENERATING LaTeX VERSIONS")
print("=" * 80)
print()

# Table 1 LaTeX
latex1 = table1[['Method', 'H0_km_s_Mpc', 'Sigma_total_km_s_Mpc', 'Category', 'Reference']].to_latex(
    index=False,
    float_format="%.2f",
    na_rep='---',
    caption='Compilation of Recent H₀ Measurements',
    label='tab:h0_measurements'
)

with open(output_dir / "table1_h0_measurements.tex", 'w') as f:
    f.write(latex1)
print("Table 1 LaTeX saved")

# Table 2 LaTeX
latex2 = table2[['Error_Source', 'SH0ES_Estimate_km_s_Mpc', 'Our_Assessment_km_s_Mpc', 'Confidence_Level']].to_latex(
    index=False,
    float_format="%.2f",
    na_rep='---',
    caption='Systematic Error Budget Comparison: SH0ES vs Our Independent Assessment',
    label='tab:error_budget'
)

with open(output_dir / "table2_error_budget.tex", 'w') as f:
    f.write(latex2)
print("Table 2 LaTeX saved")

# Table 3 LaTeX
latex3 = table3[['Phase', 'Key_Finding', 'Impact_on_H0_km_s_Mpc', 'Confidence']].to_latex(
    index=False,
    na_rep='---',
    caption='Summary of Key Findings from Phases 1-4',
    label='tab:phase_findings'
)

with open(output_dir / "table3_phase_findings.tex", 'w') as f:
    f.write(latex3)
print("Table 3 LaTeX saved")

print()
print("=" * 80)
print("ALL TABLES GENERATED")
print("=" * 80)
print()
print("Summary:")
print(f"  Table 1: {len(table1)} measurements compiled")
print(f"  Table 2: {len(table2)-2} error sources quantified (TOTAL: 1.04 → 2.45 km/s/Mpc)")
print(f"  Table 3: {len(table3)} phases summarized")
print()
print("Formats created:")
print("  - CSV (for analysis)")
print("  - LaTeX (for manuscript)")
print()
