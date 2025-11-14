Overleaf Submission Package - Distance Ladder Systematics v8.6A
=================================================================

Version: 8.6A (M1 Peer Review Response - All Referee Feedback Incorporated)
Date: November 12, 2025
Status: Ready for ApJ Submission

PACKAGE CONTENTS
================
manuscript.tex              - Main manuscript file
aasjournal.bst             - AASTeX bibliography style
apj_v8.6A.bib              - Bibliography file

tables/                    - All data tables (LaTeX deluxetable format)
  - table1_systematic_budget.tex
  - table2_tension_evolution.tex
  - table3_h0_compilation.tex
  - table4_cchp_crossval.tex
  - table5_jwst_crossvalidation.tex
  - table6_cosmic_chronometers.tex
  - table_anchor_weights.tex
  - table_correlation_matrix.tex

figures/                   - All figures (PDF for publication, PNG for reference)
  - figure1_tension_evolution.pdf
  - figure2_error_budget.pdf
  - figure4_h0_compilation.pdf
  - [Additional PNG versions and supplementary figures]

REFEREE FEEDBACK INCORPORATED (v8.6A)
======================================
All referee feedback items have been addressed:

1. ✅ "9 vs 10" inconsistencies - Fixed throughout (Eq. 1, §2.2)
2. ✅ Stage-4 σ_combined = 1.65 - Corrected in text and Table 2
3. ✅ Mathematical validation variance values - Updated to current budget
4. ✅ Metallicity prior baseline vs sensitivity - Clarified in §4.4
5. ✅ Table 3 outdated σ_sys - Updated from 2.45 to 1.71 km/s/Mpc
6. ✅ SNe Ia coupling claims - Removed false claims, justified uncorrelated treatment
7. ✅ Correction scheme harmonization - All references use "0 -2.5 -1.0 = -3.5"
8. ✅ CCHP Independent row - Removed from Table 1, moved to comments
9. ✅ Notation & units consistency - Verified throughout
10. ✅ Literature updates - DESI, ACT, SPT, JWST cross-checks incorporated

KEY BASELINE VALUES (Scenario A + Prior 1)
===========================================
Stage 4: H₀ = 70.67 ± 1.65 km/s/Mpc, tension = 1.9σ
Stage 5: H₀ = 69.67 ± 1.89 km/s/Mpc, tension = 1.2σ

Systematic budget (9 sources):
- Uncorrelated: σ_sys = 1.45 km/s/Mpc (1.4× vs SH0ES)
- Correlated: σ_sys = 1.71 km/s/Mpc (1.6× vs SH0ES)
- 18% increase from correlations

Bias corrections: 0 (parallax) -2.5 (period) -1.0 (metallicity) = -3.5 km/s/Mpc cumulative
MAP estimate: -2.33 km/s/Mpc (consistent within 68% CI)

COMPILATION INSTRUCTIONS
========================
1. Upload all files to Overleaf maintaining directory structure
2. Set main document: manuscript.tex
3. Compiler: pdfLaTeX
4. Main document class: aastex631 (two-column ApJ format)
5. Compile sequence: pdflatex → bibtex → pdflatex → pdflatex

VALIDATION CHECKLIST
====================
✅ All 9 referee feedback items addressed
✅ Numeric spot-checks verified (Stage 4: 1.65, Planck-free: 0.6σ)
✅ Literature pulse check complete (DESI, ACT DR6, SPT-3G, JWST)
✅ Table references consistent (9×9 matrix, 9 sources)
✅ Unit notation consistent (km~s$^{-1}$~Mpc$^{-1}$)
✅ Correction scheme harmonized (0 -2.5 -1.0 = -3.5)
✅ All figures present and referenced
✅ Bibliography complete with recent 2024-2025 citations

CONTACT INFORMATION
===================
Repository: https://github.com/awiley-intel/distance-ladder-systematics
Commit: 85c56c3 (baseline) + v8.6A peer review revisions
License: Creative Commons CC-BY 4.0

For questions or issues with compilation, please refer to the project repository.
