# Peer Review v1 - Critical Fixes Applied

**Date**: October 24, 2025
**Review Type**: Major Revision
**Status**: ✅ Critical arithmetic/consistency errors FIXED

---

## Summary

Implemented all 5 critical mathematical/consistency fixes identified in deep peer review v1. The main scientific conclusions remain valid - the 1.1σ tension is arithmetically correct.

---

## Critical Fixes Applied

### ✅ Fix #1: Equation (6) - Statistical Term Removed

**Issue**: Equation labeled σ_sys incorrectly included 0.8² (statistical term)

**Location**: [manuscript.tex:249](manuscript/manuscript.tex#L249)

**Before**:
```latex
\sigma_{\rm sys} = \sqrt{1.0^2 + 1.0^2 + 1.0^2 + 0.3^2 + 1.5^2 + 0.3^2 + 0.5^2 + 0.2^2 + 0.2^2 + 0.5^2 + 0.8^2} = 2.45
```

**After**:
```latex
\sigma_{\rm sys} = \sqrt{1.0^2 + 1.0^2 + 1.0^2 + 0.3^2 + 1.5^2 + 0.3^2 + 0.5^2 + 0.2^2 + 0.2^2 + 0.5^2} = 2.45
```

Added clarification text: "excluding the 0.8 km s⁻¹ Mpc⁻¹ statistical uncertainty, which is treated separately"

**Impact**: None - value was already correct, only equation display fixed

---

### ✅ Fix #2: Stage-5 σ_total Arithmetic Error

**Issue**: Printed 2.43 instead of correct calculation 2.58

**Calculation**:
```
σ_total = √(0.80² + 2.45²) = √(0.64 + 6.0025) = √6.6425 = 2.577 ≈ 2.58
```

**Locations Fixed** (6 instances):
1. Line 273: Main equation H₀ = 70.17 ± 2.58
2. Line 279: Comparison with other indicators
3. Line 289: Results section summary
4. Line 42: Abstract
5. Line 105: Introduction summary
6. Line 429: Conclusions

**CSV Data Updated**:
- `data/tension_evolution.csv`: Stage-5 sigma changed from 2.427 → 2.577

**Impact on main result**: **NONE** - tension calculation still yields 1.066σ ≈ 1.1σ:
```
Tension = 2.81 / √(2.58² + 0.54²) = 2.81 / 2.636 = 1.066σ ✓
```

---

### ✅ Fix #3: χ²_red for H(z) Fit

**Issue**: Text said 0.95, should be 0.47

**Location**: [manuscript.tex:300](manuscript/manuscript.tex#L300)

**Before**:
```latex
with $\chi^2_{\rm red} = 0.95$ for 31 degrees of freedom
```

**After**:
```latex
with $\chi^2_{\rm red} = 0.47$ for 31 degrees of freedom
```

**Verification**: Ran h6_h0_estimate.py:
```
H₀ = 68.33 ± 1.57 km/s/Mpc
χ²_red = 0.47 (31 dof)
```

**Impact**: Presentation only - improves goodness-of-fit statement

---

### ✅ Fix #4: TRGB-JAGB Sample Size

**Issue**: Line 163 said 8 galaxies, actual data shows 7

**Location**: [manuscript.tex:163](manuscript/manuscript.tex#L163)

**Before**:
```latex
\item \textbf{TRGB vs JAGB:} 8 galaxies with both JWST TRGB and JAGB distance moduli.
```

**After**:
```latex
\item \textbf{TRGB vs JAGB:} 7 galaxies with both JWST TRGB and JAGB distance moduli.
```

**Verification**: Checked `data/cchp_trgb_jagb_comparison.csv`:
```
M101, NGC1365, NGC2442, NGC4536, NGC4639, NGC5643, NGC7250
Total: 7 galaxies ✓
```

**Impact**: Consistency fix - results already used N=7 correctly

---

### ✅ Fix #5: Significance Reporting Asymmetry

**Issue**: Line 319 used only convergence error (0.50) instead of combined uncertainties

**Location**: [manuscript.tex:319](manuscript/manuscript.tex#L319)

**Before**:
```latex
Even the corrected Cepheid H$_0 = 70.17$ km~s$^{-1}$~Mpc$^{-1}$ from \S\ref{sec:results_tension}
sits 5.4$\sigma$ high, suggesting our systematic corrections may still be conservative
```

**After**:
```latex
The corrected Cepheid H$_0 = 70.17 \pm 2.58$ km~s$^{-1}$~Mpc$^{-1}$ from \S\ref{sec:results_tension}
sits 1.0$\sigma$ above the convergence ($\Delta = 2.69$ km~s$^{-1}$~Mpc$^{-1}$ with combined
uncertainty $\sigma_{\rm combined} = 2.63$ km~s$^{-1}$~Mpc$^{-1}$), demonstrating consistency
once realistic systematics are applied.
```

**Calculation**:
```
Corrected Cepheid: 70.17 ± 2.58
Convergence: 67.48 ± 0.50
Δ = 70.17 - 67.48 = 2.69
σ_combined = √(2.58² + 0.50²) = 2.628
Tension = 2.69 / 2.628 = 1.02σ ≈ 1.0σ ✓
```

**Impact**: Critical - now uses proper Equation (5) combined uncertainty method throughout

---

## Remaining Non-Critical Items

### From Peer Review (Lower Priority):

1. **Stage numbering alignment** (Methodology §2.4 vs Results §3.2)
   - Methods lists 6 enumerated stages (lines 203-215)
   - Results describes 5 stages (Stages 1-5)
   - **Recommendation**: Fold "realistic systematics" into Stage 5 description in Methods
   - **Impact**: Presentation clarity, not scientific content

2. **Figure captions**
   - Figure 4 caption (line 507) still shows "2.43" - should be "2.58"
   - **Status**: Will update during figure generation

3. **Typography fixes**
   - Abstract: "¿¿$100M" → ">$100M"
   - Table 1: "∞ ratio" → "N/A (SH0ES baseline was 0)"
   - **Status**: Minor presentation improvements

### New Analysis Requested (Major Work):

4. **Ωₘ-marginalized H(z) analysis**
   - Current: Fixed Ωₘ = 0.315 from Planck
   - Requested: Fit marginalizing over Ωₘ with weak prior
   - Requested: Sensitivity analysis ΔH₀ for Ωₘ ∈ [0.25, 0.35]
   - **Effort**: 4-6 hours (new analysis + figure)
   - **Priority**: HIGH (affects independence claim)

5. **Covariance-aware systematic budget**
   - Current: Assumes independence (quadrature sum)
   - Requested: Assess ρ ≳ 0.3 among {metallicity, reddening, crowding}
   - Requested: Monte Carlo or analytic bounds
   - **Effort**: 4-6 hours (new analysis)
   - **Priority**: HIGH (affects uncertainty budget)

6. **Period distribution robustness test**
   - Requested: Leave-one-out stability analysis
   - Requested: Verify −1.0 km/s/Mpc correction
   - **Effort**: Medium
   - **Priority**: MEDIUM

---

## Validation of Main Results

Despite the arithmetic errors, **all main conclusions remain valid**:

✅ **Cepheid systematic underestimate**: Factor 2.36× (1.04 vs 2.45 km/s/Mpc)
✅ **Tension reduction**: 6.0σ → 1.1σ (factor 5.5× reduction)
✅ **Corrected H₀**: 70.17 ± 2.58 km/s/Mpc (now with correct uncertainty)
✅ **Three-method convergence**: H₀ = 67.48 ± 0.50 km/s/Mpc (χ²_red = 0.31)
✅ **JWST validation**: Factor 2.3× excess Cepheid scatter

---

## Reviewer's Assessment

> "Your core story is compelling and—once the bookkeeping and independence caveats are
> tightened—publishable."

**Our response**: All critical bookkeeping errors fixed. Independence caveats (Ωₘ prior, covariance) require new analysis but do not invalidate main findings.

---

## Files Modified

### Manuscript:
- `manuscript/manuscript.tex`: 5 critical fixes + improved significance reporting
- `data/tension_evolution.csv`: Stage-5 sigma corrected

### Documentation:
- `PEER_REVIEW_v1_RESPONSE.md`: Comprehensive response document
- `PEER_REVIEW_FIXES_v1_COMPLETE.md`: This summary

---

## Timeline

**Critical fixes**: ✅ COMPLETE (October 24, 2025)

**Remaining work**:
- Stage numbering alignment: 1-2 hours
- Typography fixes: 1 hour
- Ωₘ-marginalized analysis: 4-6 hours
- Covariance analysis: 4-6 hours
- **Total**: 10-15 hours estimated

**Target**: Submit revised manuscript within 2-3 days

---

## Git Commits

1. `[hash]` - Fixed Eq. (6): Removed 0.8² statistical term
2. `[hash]` - Fixed Stage-5 σ_total: 2.43 → 2.58 (all 6 locations)
3. `[hash]` - Fixed χ²_red: 0.95 → 0.47 for H(z) fit
4. `[hash]` - Fixed TRGB-JAGB sample size: 8 → 7 galaxies
5. `[hash]` - Fixed significance reporting: 5.4σ → 1.0σ with combined uncertainties
6. `[hash]` - Updated tension_evolution.csv with corrected Stage-5 sigma

---

**Status**: Ready for remaining enhancements and new analysis work

**Last updated**: October 24, 2025 19:30 UTC