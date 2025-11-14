# Legacy "2.36× Underestimate" Reference Fix

**Date:** November 13, 2025
**Issue:** Inconsistency 2.4 - Legacy "2.36× underestimate" reference in Table 4
**Status:** ✅ **FIXED**

---

## Problem

**Table 4 (CCHP cross-validation)** contained a legacy reference to v8.5 pre-revision values:

> "...validating our error budget assessment of **factor 2.36× systematic underestimate** (Table~\ref{tab:systematic_budget})."

However, the **current post-revision values** (after M1 peer review) are:
- **1.4×** (uncorrelated systematics)
- **1.6×** (correlated systematics)

The 2.36× factor was from v8.5 with the 10×10 matrix before:
1. Removing covariant crowding as standalone term (9×9 matrix)
2. Adopting 2025 metallicity consensus (γ = -0.2 ± 0.1)

This legacy reference was inconsistent with Table 1 and body text, which now correctly state 1.4×/1.6×.

---

## Solution

**File:** `data/tables/table4_cchp_crossval.tex`

**Change (Line 22):**
```diff
- Factor 2.3× larger Cepheid scatter provides direct observational evidence for
- excess Cepheid systematic uncertainties, validating our error budget
- assessment of factor 2.36× systematic underestimate (Table~\ref{tab:systematic_budget}).

+ Factor 2.3× larger Cepheid scatter provides direct observational evidence for
+ excess Cepheid systematic uncertainties, broadly consistent with our
+ 1.4× (uncorrelated) / 1.6× (correlated) systematic underestimate in
+ Table~\ref{tab:systematic_budget} after revisions.
```

**Reasoning:**
- "Broadly consistent" acknowledges that 2.3× scatter ratio and 1.4×/1.6× systematic factors are related but not identical measurements
- Explicitly states current post-revision values (1.4× / 1.6×)
- References Table 1 correctly
- Adds temporal context ("after revisions") to distinguish from v8.5 values

---

## Context: Why 2.36× Changed to 1.4×/1.6×

### v8.5 (Pre-revision)
- **10×10 systematic budget** (included covariant crowding as standalone term)
- **Metallicity prior:** Wider range (γ = -0.2 to -0.5)
- **Result:** σ_sys = 2.46 km/s/Mpc uncorrelated (vs SH0ES 1.04 = **2.36× factor**)

### v8.6+ (Post-M1 peer review)
- **9×9 systematic budget** (removed covariant crowding standalone term per JWST validation)
- **Metallicity prior:** 2025 consensus (γ = -0.2 ± 0.1, narrower uncertainty)
- **Result:**
  - σ_sys,uncorr = 1.45 km/s/Mpc (vs SH0ES 1.04 = **1.4× factor**)
  - σ_sys,corr = 1.71 km/s/Mpc (vs SH0ES 1.04 = **1.6× factor**)

**Why the reduction?**
1. **Covariant crowding removal:** JWST data showed no direct crowding bias (Riess+ 2024), so standalone term removed
2. **Metallicity consensus narrowing:** Updated literature converged on γ ≈ -0.2 ± 0.1 (down from -0.2 to -0.5 range)
3. Both changes reduced total systematic budget while maintaining realistic assessment

---

## Verification

### Current Table 1 Values ✅
From `data/tables/table1_systematic_budget.tex`:
- SH0ES total (uncorrelated): 1.04 km/s/Mpc
- Our assessment (uncorrelated): 1.45 km/s/Mpc → **1.4× factor**
- Our assessment (correlated): 1.71 km/s/Mpc → **1.6× factor**

### Manuscript Body Text ✅
Line 337 (§3.1):
> "Our independent assessment... yields σ_sys,corr = 1.71 km s⁻¹ Mpc⁻¹—a **factor of 1.6× larger** (1.4× under independence assumption: σ_sys,uncorr = 1.45 km s⁻¹ Mpc⁻¹)."

### Figure Captions ✅
Figures 6 and 7 correctly note old v8.5 values with "(v8.5 pre-revision)" labels.

### Table 4 (Now Fixed) ✅
Now references **1.4× / 1.6×** instead of legacy 2.36×.

---

## Relationship: 2.3× Scatter vs 1.4×/1.6× Systematics

**Important distinction:**
- **2.3× scatter ratio:** Direct JWST observation of Cepheid RMS scatter vs JAGB/TRGB
  - Cepheid: 0.108 mag RMS
  - JAGB/TRGB: 0.048 mag RMS
  - Ratio: 0.108 / 0.048 ≈ 2.25 → 2.3×

- **1.4×/1.6× systematic factor:** Our systematic error budget assessment vs SH0ES
  - SH0ES claimed: σ_sys = 1.04 km/s/Mpc
  - Our uncorrelated: σ_sys = 1.45 km/s/Mpc → 1.4× factor
  - Our correlated: σ_sys = 1.71 km/s/Mpc → 1.6× factor

These are **related but distinct** measurements:
1. **Scatter ratio (2.3×):** Empirical observation of method precision
2. **Systematic factor (1.4×/1.6×):** Independent systematic budget reconstruction

They **"broadly consistent"** in the sense that both indicate Cepheid systematics are underestimated, but the exact numerical values differ due to:
- Different measurement approaches (scatter vs uncertainty budget)
- Systematic correlations (not captured in simple scatter ratios)
- Completeness of systematic catalog

Hence the revised wording: **"broadly consistent with"** rather than **"validating"** (which implied exact agreement).

---

## Complete Fix Summary

| Aspect | Before | After |
|--------|--------|-------|
| **Table 4 reference** | "2.36× systematic underestimate" | "1.4× (uncorr) / 1.6× (corr) after revisions" |
| **Temporal context** | None | "after revisions" (distinguishes from v8.5) |
| **Relationship claim** | "validating" (implies exact match) | "broadly consistent" (acknowledges related but distinct) |
| **Consistency with Table 1** | ❌ Inconsistent (2.36× not in Table 1) | ✅ Consistent (1.4×/1.6× matches Table 1) |
| **Consistency with body text** | ❌ Inconsistent (body says 1.4×/1.6×) | ✅ Consistent |

---

## All Four Inconsistencies Now Resolved

1. ✅ **SH0ES baseline:** 73.04 vs 73.17 (fixed in Tables 2, 3, sensitivity table, Figure 4)
2. ✅ **Corrected Cepheid H₀:** 69.54 vs 69.67 (verified correct usage)
3. ✅ **Stage-1/Stage-4 values:** Text vs Table 2 (verified consistent)
4. ✅ **Legacy 2.36× reference:** Updated to 1.4×/1.6× in Table 4

---

## Files Modified

1. **data/tables/table4_cchp_crossval.tex** (Line 22)
   - Changed "2.36×" → "1.4× (uncorrelated) / 1.6× (correlated) after revisions"
   - Changed "validating" → "broadly consistent with"

---

## No Remaining Legacy v8.5 References

**Grep verification:**
```bash
grep -rn "2\.36" data/tables/ manuscript/
```
**Result:** ✅ **NONE FOUND** (only in archived overleaf_package directories)

**All v8.5 references now properly contextualized:**
- Figures 6/7 captions: Explicitly labeled "(v8.5 pre-revision)"
- Table 4: Updated to current values (1.4×/1.6×)
- Body text: Consistently uses post-revision values throughout

---

## Final Status

**Package:** All source files now consistent with post-M1 peer review values
**Documentation:** This fix completes the series of citation/value consistency corrections
**Validation:** No remaining legacy v8.5 values without proper context

---

**Fixed:** November 13, 2025
**Result:** Table 4 now references current post-revision systematic factors (1.4×/1.6×)
**Status:** ✅ **ALL FOUR INCONSISTENCIES RESOLVED**
