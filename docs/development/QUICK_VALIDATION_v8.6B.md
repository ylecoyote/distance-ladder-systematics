# Quick Validation Checklist - v8.6B

## Before Upload

- [x] Package created: `manuscript_overleaf_v8.6B.zip` (4.5 MB)
- [x] All paths corrected (no `../` references)
- [x] R22 baseline (73.04 ± 1.04) throughout
- [x] Borghi 2022 reference added
- [x] SPT-3G softened to range
- [x] Crisis language tempered

## After Overleaf Upload

### Immediate Checks
- [ ] Project uploads without errors
- [ ] Click "Recompile" - compiles cleanly
- [ ] Check compilation log for warnings
- [ ] Verify PDF generates (~35-40 pages)

### Value Spot-Checks
Navigate to compiled PDF and verify:
- [ ] **Abstract line 5:** "73.04 ± 1.04, Riess et al. 2022" ✓
- [ ] **Line 107:** "~5σ by conventional accounting" (NOT ~6σ) ✓
- [ ] **Table 2 Stage 1:** Tension = 5.9σ (NOT 6.0σ) ✓
- [ ] **Table 2 Stage 4:** H₀ = 70.54 (NOT 70.67) ✓
- [ ] **Table 2 Stage 5:** H₀ = 69.54 (NOT 69.67) ✓
- [ ] **Line 291:** "extending the 31-point compilation... Borghi2022" ✓
- [ ] **Discussion §4.1:** "predominantly attributable" (NOT "likely artifact") ✓

### Figure Verification
- [ ] Figure 1: Tension evolution shows 5.9σ → 1.2σ (4.9× reduction)
- [ ] Figure 2: Error budget comparison renders correctly
- [ ] Figure 3: JWST CCHP cross-validation displays
- [ ] Figure 4: H₀ compilation forest plot renders
- [ ] Figure 5: Cosmic chronometer fit displays
- [ ] All other figures render without errors

### Table Verification
- [ ] Table 1: 9-source systematic budget displays
- [ ] Table 2: 5-stage evolution with correct values
- [ ] Table 3: Multi-method compilation renders
- [ ] Table 4: CCHP cross-validation displays
- [ ] Table 5: Per-galaxy JWST distances
- [ ] Table 6: 32 cosmic chronometer measurements
- [ ] Table (anchor weights) renders
- [ ] Table (correlation matrix) displays

### Cross-Reference Check
- [ ] All section references work (§2.1, §3.2, etc.)
- [ ] All figure references work (Fig. 1, Fig. 2, etc.)
- [ ] All table references work (Table 1, Table 2, etc.)
- [ ] All equation references work (Eq. 1, Eq. 2, etc.)
- [ ] All citations appear [Author Year] format

## Final Approval

Once all checks pass:
- [ ] Download PDF from Overleaf for archival
- [ ] Compare key values with this checklist
- [ ] Verify manuscript is ready for journal submission
- [ ] Note: Package is **v8.6B with R22 baseline**

## Quick Reference Values

**Use these to spot-check the compiled PDF:**

| Item | Correct Value | Wrong Value |
|------|---------------|-------------|
| SH0ES baseline | 73.04 ± 1.04 | 73.17 |
| Stage 1 tension | 5.9σ | 6.0σ |
| Stage 4 H₀ | 70.54 | 70.67 |
| Stage 5 H₀ | 69.54 | 69.67 |
| Reduction factor | 4.9× | 5.0× |
| Tension claim | ~5σ (reaching ~6σ) | ~6σ |
| SPT-3G | H₀ ≈ 67-69 | 66.7 ± 0.6 |

**If you see wrong values, DO NOT submit - use a different package!**

---

**Package:** manuscript_overleaf_v8.6B.zip
**Date:** November 13, 2025
**Status:** Ready for validation
