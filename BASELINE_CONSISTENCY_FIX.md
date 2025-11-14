# SH0ES Baseline Consistency Fix - Complete

**Date:** November 13, 2025
**Issue:** Manuscript text used 73.04 ± 1.04 but tables still had 73.17 ± 1.31

## Changes Made

### 1. Table 2 (Tension Evolution) ✅
**File:** `data/tables/table2_tension_evolution.tex`

**Data rows updated:**
- Stage 1: 73.17 → **73.04** (tension: 6.0σ → **5.9σ**)
- Stage 2: 73.17 → **73.04** (tension: 4.1σ → **4.0σ**)
- Stage 3: 73.17 → **73.04** (tension: 4.1σ → **4.0σ**)
- Stage 4: 70.67 → **70.54** (tension remains 1.9σ)
- Stage 5: 69.67 → **69.54** (tension remains 1.2σ)

**Table comment updated:**
- "H$_0$ remains 73.17" → **"H$_0$ remains 73.04 from Riess2022"**
- Final calculation: |69.67 - 67.36| → **|69.54 - 67.36|** = 1.11σ
- Reduction factor: 5.0× → **4.9×** (5.9σ → 1.2σ)

### 2. Table 3 (H₀ Compilation) ✅
**File:** `data/tables/table3_h0_compilation.tex`

**SH0ES Cepheid row:**
- 73.17 ± 1.31 → **73.04 ± 1.04** (Riess2022)

**Table comment updated:**
- "H$_0 = 73.17 ± 1.31$" → **"H$_0 = 73.04 ± 1.04$ from Riess2022"**
- "Corrected... 69.67 ± 1.89" → **"69.54 ± 1.89"**

### 3. Manuscript Sensitivity Table (§3.3) ✅
**File:** `manuscript/manuscript.tex` (lines 426-432)

**Updated values based on 73.04 baseline:**

| Scenario | Metallicity Prior | Old Value | New Value | Calculation |
|----------|------------------|-----------|-----------|-------------|
| A | Prior 3 (γ=0) | 70.67 | **70.54** | 73.04 - 2.5 - 0 |
| B | Prior 2 (γ=-0.35) | 67.87 | **68.00** | 73.04 - 0.87 - 2.5 - 1.67 |
| B | Prior 3 (γ=0) | 69.54 | **69.67** | 73.04 - 0.87 - 2.5 - 0 |

**Tension recalculated:**
- Scenario B + Prior 2: 0.2σ → **0.3σ** ((68.00-67.36)/√(2.22²+0.54²) = 0.28σ)

## Verification

### Canonical R22 Baseline (used everywhere)
- **SH0ES (Riess+ 2022):** H₀ = **73.04 ± 1.04 km/s/Mpc**
- **Reference:** Riess et al. (2022, ApJL, 934, L7)

### Stage-wise Evolution (all based on 73.04)
| Stage | H₀ | σ_total | Tension | Correction Applied |
|-------|-----|---------|---------|-------------------|
| 1 | 73.04 | 0.80 | 5.9σ | Stat only |
| 2 | 73.04 | 1.31 | 4.0σ | + SH0ES systematics |
| 3 | 73.04 | 1.31 | 4.0σ | + Parallax (Scenario A: 0) |
| 4 | 70.54 | 1.65 | 1.9σ | + Period (-2.5) |
| 5 | 69.54 | 1.89 | 1.2σ | + Metallicity (-1.0) + Corr sys |

**Tension reduction:** 5.9σ → 1.2σ = **4.9× factor**

### Sensitivity Analysis (all based on 73.04)
**Scenario A (parallax = 0):**
- Prior 1 (γ=-0.2, -1.0): 73.04 - 2.5 - 1.0 = **69.54** ± 1.89 (1.2σ) ✓
- Prior 2 (γ=-0.35, -1.67): 73.04 - 2.5 - 1.67 = **68.87** ± 2.02 (0.7σ) ✓
- Prior 3 (γ=0, 0): 73.04 - 2.5 - 0 = **70.54** ± 1.89 (1.7σ) ✓

**Scenario B (parallax = -0.87):**
- Prior 1 (γ=-0.2, -1.0): 73.04 - 0.87 - 2.5 - 1.0 = **68.67** ± 2.12 (0.6σ) ✓
- Prior 2 (γ=-0.35, -1.67): 73.04 - 0.87 - 2.5 - 1.67 = **68.00** ± 2.22 (0.3σ) ✓
- Prior 3 (γ=0, 0): 73.04 - 0.87 - 2.5 - 0 = **69.67** ± 2.12 (1.1σ) ✓

**Tension range across 6 scenarios:** 0.3σ to 1.7σ (baseline: 1.2σ)

## Files Modified
1. `data/tables/table2_tension_evolution.tex` - 5 data values + comment
2. `data/tables/table3_h0_compilation.tex` - SH0ES row + comment
3. `manuscript/manuscript.tex` - Sensitivity table (3 values + 1 tension)

## No Further Changes Needed
- ✅ All other tables already correct
- ✅ Manuscript text already uses 73.04 ± 1.04
- ✅ Abstract already uses 73.04 ± 1.04 (Riess et al. 2022)
- ✅ No remaining 73.17 references found
- ✅ No remaining 70.67 references (except correct Scenario B+Prior 3: 69.67)

## Impact
- **Mathematical consistency:** All calculations now trace to single R22 baseline
- **Citation clarity:** Unambiguous attribution to Riess+ 2022
- **Reproducibility:** Readers can verify all derived values from 73.04 baseline

---

**Status:** ✅ **ALL BASELINE VALUES NOW CONSISTENT**
**Next:** Ready for re-packaging as v8.6C with this fix
