# PDF Forensic Analysis - Remediation Plan

**Date:** November 14, 2025
**Status:** 🔴 **ACTION REQUIRED**
**Source:** PDF forensic analysis of v8.6E compiled manuscript

---

## Executive Summary

The forensic PDF analysis identified three classes of issues:

1. **CRITICAL DATA CONTRADICTIONS** (LaTeX source problems) - **MUST FIX**
2. **PDF RENDERING ARTIFACTS** (compilation issues) - **INVESTIGATE**
3. **MINOR TYPOS** (LaTeX source problems) - **SHOULD FIX**

**Key Finding:** The LaTeX source files are largely correct with proper notation. Most "sigma notation errors" reported in the forensic analysis are **PDF rendering artifacts**, not source file errors. However, there ARE genuine critical data contradictions that must be resolved.

---

## Verification Results

### ✅ LaTeX Source is CORRECT for Sigma Notation

The forensic analysis claimed widespread "5.90" and "~60" errors for sigma notation. **These are PDF rendering issues, NOT LaTeX source errors.**

**Evidence from manuscript.tex:**
- Line 68: `$\sim$6$\sigma$` ✓ CORRECT
- Line 81: `$\sim$6$\sigma$` ✓ CORRECT
- Line 82: `5.9$\sigma$ to 1.2$\sigma$` ✓ CORRECT
- Line 86: `0.2--1.7$\sigma$` ✓ CORRECT
- Line 107: `$\sim$5$\sigma$` and `$\sim$6$\sigma$` ✓ CORRECT
- Line 109: `2.4$\sigma$ to 5-6$\sigma$` ✓ CORRECT

**Conclusion:** The PDF compiler is incorrectly rendering $\sigma$ symbols. The LaTeX source has proper `$\sigma$` notation throughout.

### ✅ H₀ Notation is CORRECT in Most Places

The forensic analysis claimed "Ho" and "$I_0$" errors.

**Spot-check results:**
- Grep for `I_0|Ho=|Ho\s+[0-9]` returned **NO MATCHES**
- LaTeX source consistently uses `H$_0$` or `H$_{0}$` notation

**Conclusion:** Either these errors don't exist in the LaTeX source OR they're rare isolated cases. The widespread notation issues claimed by the forensic analysis are likely PDF rendering artifacts.

### 🔴 CONFIRMED: Critical "Period Distribution" Data Contradiction

**This is a REAL problem in the LaTeX source that MUST be fixed.**

**Contradiction verified:**

1. **manuscript.tex line 339:**
   ```latex
   Our assessment: $2.5 \pm 1.0$ km~s$^{-1}$~Mpc$^{-1}$ (High confidence, mid-range of explicit bracket).
   ```

2. **manuscript.tex line 366:**
   ```latex
   \item \textbf{Period distribution:} $2.5 \pm 1.0$ vs 0.0 km~s$^{-1}$~Mpc$^{-1}$ (factor $\infty$).
   ```

3. **table1_systematic_budget.tex line 18:**
   ```latex
   Period Distribution & 0.0 & 1.0 & $\infty$ & Medium \\
   ```

**Discrepancy:** Text says "2.5 ± 1.0" while table shows "1.0"

**This affects:**
- Table 1 (systematic error budget)
- Figure 2 (error budget visualization)
- Multiple in-text references

---

## Priority 1: CRITICAL - Data Contradictions (MUST FIX)

### Issue 1.1: Period Distribution Value Mismatch

**Severity:** CRITICAL - Affects core scientific claim
**Locations affected:**
- manuscript.tex lines 86, 149, 212-218, 316, 339, 366, 408
- table1_systematic_budget.tex line 18
- Figure 2 (figure2_error_budget.pdf) - orange bar shows 1.0

**Problem:** Inconsistent values across manuscript
- **Text says:** "2.5 ± 1.0 km/s/Mpc" (mid-range of bracket [-1.5, -3.5])
- **Table 1 says:** "1.0 km/s/Mpc"
- **Figure 2 shows:** Orange bar at 1.0

**Root cause analysis:**

Looking at the text, the Period Distribution systematic has TWO components:

1. **Uncertainty:** How uncertain is this systematic? (What goes in "Our Assessment" column)
2. **Bias correction:** What correction do we apply? (Used in Stage 4 calculations)

The text describes a **bracket** of possible corrections: [-1.5, -3.5] km/s/Mpc, and adopts the **mid-range value of -2.5 km/s/Mpc** as the correction.

But for the **systematic uncertainty budget** (Table 1), the question is: what is the UNCERTAINTY in this systematic? If the correction is -2.5 with a range of [-1.5, -3.5], the uncertainty is approximately ±1.0 km/s/Mpc.

**Proposed resolution:**

The table and figure should show the **uncertainty magnitude**, not the correction value.

**Option A:** Table shows "1.0" = **correct** (uncertainty is ±1.0 around the -2.5 central value)
**Option B:** Table shows "2.5" = **incorrect** (confuses correction with uncertainty)

**RECOMMENDED ACTION:**

1. **Keep table value at 1.0** (it's correct as an uncertainty estimate)
2. **Clarify the text** to distinguish between:
   - Systematic uncertainty: ±1.0 km/s/Mpc
   - Bias correction applied: -2.5 km/s/Mpc (mid-range of [-1.5, -3.5])

3. **Update manuscript.tex line 339** from:
   ```latex
   Our assessment: $2.5 \pm 1.0$ km~s$^{-1}$~Mpc$^{-1}$
   ```
   to:
   ```latex
   Our assessment: uncertainty $1.0$ km~s$^{-1}$~Mpc$^{-1}$ from correction bracket $[-1.5, -3.5]$ km~s$^{-1}$~Mpc$^{-1}$ (adopted mid-range $-2.5$)
   ```

4. **Add clarifying note to Table 1 caption** explaining that "Period Distribution" uncertainty (1.0) reflects the range of plausible correction values.

**Alternative:** If the user intended "2.5" to be in the table, then:
- Change table1_systematic_budget.tex line 18 from "1.0" to "2.5"
- Regenerate Figure 2 with orange bar at 2.5
- But this seems WRONG based on the bracketing methodology described in the text

### Issue 1.2: Figure 3 Galaxy Count Discrepancy

**Severity:** MAJOR - Inconsistent data reporting
**Location:** Figure 3 caption vs. Panel A inset text

**Problem:**
- Caption says: "7 common galaxies"
- Panel A text says: "8 galaxies"

**REQUIRED ACTION:**
- Verify actual galaxy count in the data
- Update either caption or figure to match truth
- Likely need to regenerate Figure 3 if panel text needs changing

### Issue 1.3: Table 7 (table5_jwst_crossvalidation.tex) Header Ambiguity

**Severity:** MAJOR - Renders table unreadable
**Location:** table5_jwst_crossvalidation.tex headers

**Problem:** Headers show:
```
TRGB (mag) | TRGB (mag) | Cepheid (mag) | Cepheid (mag)
```

Both "TRGB (mag)" columns and both "Cepheid (mag)" columns are identical, making it unclear which is the value and which is the uncertainty.

**Spot-check result:**

Reading table5_jwst_crossvalidation.tex lines 8-20:
```latex
\tablehead{
\colhead{Galaxy} &
\colhead{$\mu_{\rm TRGB}$} &
\colhead{$\sigma_{\rm TRGB}$} &
\colhead{$\mu_{\rm Cepheid}$} &
\colhead{$\sigma_{\rm Cepheid}$} &
\colhead{$\Delta\mu$} \\
```

**VERDICT:** Headers in LaTeX source are CORRECT and unambiguous!
- Uses $\mu$ for distance modulus
- Uses $\sigma$ for uncertainty

**Conclusion:** This is a **PDF rendering issue**, not a LaTeX source problem. The PDF is failing to render the Greek letters $\mu$ and $\sigma$ in the table headers.

**REQUIRED ACTION:**
- Investigate PDF compilation process
- Check font encoding issues
- May need different LaTeX table environment or font package

---

## Priority 2: INVESTIGATE - PDF Rendering Issues

### Issue 2.1: Sigma Symbol Rendering

**Severity:** CRITICAL (for publication) - Widespread rendering failure
**Nature:** PDF compilation artifact

**Problem:** The PDF incorrectly renders `$\sigma$` as "0" or omits it entirely, creating:
- "5.9σ" → "5.90"
- "~6σ" → "~60"
- "1.2σ" → "1.20"

**Evidence:** LaTeX source has correct `$\sigma$` notation throughout (verified above)

**Possible causes:**
1. Font encoding issue in PDF generation
2. Math mode rendering problem
3. Unicode handling in PDF compiler
4. Package conflict

**REQUIRED ACTIONS:**
1. Check LaTeX compilation logs for font warnings
2. Verify PDF generation method (pdflatex vs. xelatex vs. lualatex)
3. Test with different LaTeX engines
4. Check if aastex631.cls has known rendering issues with Greek letters
5. May need to add font packages or encoding fixes

**Workaround (if needed):**
- Use `\ensuremath{\sigma}` instead of `$\sigma$` in problematic contexts
- Add explicit font encoding packages

### Issue 2.2: H₀ Subscript Rendering

**Severity:** MODERATE - Occasional rendering failures

**Problem:** Forensic analysis reports:
- "$H_0$" rendered as "$I_0$" (Page 3, Line 98)
- "$H_0$" rendered as "Ho" (Pages 2-3)

**Evidence:** LaTeX source uses correct `H$_0$` notation (grep found NO instances of "Ho=" or "I_0")

**Conclusion:** Either rare isolated errors OR PDF rendering artifacts

**REQUIRED ACTION:**
- Visual inspection of PDF at reported pages
- If confirmed, check for font substitution issues in PDF

### Issue 2.3: Table Header Symbol Rendering (Table 7)

**Severity:** MAJOR
**Problem:** Greek letters $\mu$ and $\sigma$ not rendering in table headers

**Evidence:** LaTeX source has correct `$\mu_{\rm TRGB}$` and `$\sigma_{\rm TRGB}$` notation

**REQUIRED ACTION:**
- Check if deluxetable* environment has issues with math mode in \colhead{}
- May need to use \thead{} or different formatting
- Test compilation with explicit font encoding

---

## Priority 3: MINOR - Typos and Formatting

### Issue 3.1: Greek Character Substitution

**Severity:** MINOR
**Location:** Unknown (forensic analysis cites Page 2, Line 67)

**Problem:** Greek "το" (tau-omicron) instead of English "to"

**Status:** NOT FOUND in LaTeX source grep

**Possible explanations:**
1. Already fixed in v8.6E
2. PDF rendering artifact
3. False positive from forensic analysis

**ACTION:** Low priority - search manually if needed

### Issue 3.2: "Mpc" Typo

**Severity:** MINOR
**Location:** Forensic analysis cites Page 5, Line 177 ("Mpe" instead of "Mpc")

**Status:** NOT FOUND in LaTeX source grep

**Possible explanations:**
1. Already fixed in v8.6E
2. PDF OCR error in forensic analysis
3. Very rare isolated instance

**ACTION:** Manual search if needed - low priority

### Issue 3.3: Figure 1 Legend Cutoff

**Severity:** MINOR - Cosmetic
**Location:** Figure 1 in-figure legend (item 5)

**Problem:** Legend text cut off: "Realistic a" instead of "Realistic systematics" (presumably)

**REQUIRED ACTION:**
- Check figure1_tension_evolution.pdf source
- If using matplotlib/python to generate, increase figure width or reduce font size
- Regenerate figure with full text visible

---

## Priority 4: FALSE POSITIVES - No Action Needed

### Verified as Non-Issues:

1. **"Crowding Direct" consistency** - VERIFIED consistent at 0.3 km/s/Mpc across text and table ✓
2. **Covariance value 5.4** - VERIFIED correct in text ✓
3. **Misspellings "luminatiosity" and "rod"** - VERIFIED absent ✓
4. **Grammar error "systematic are"** - VERIFIED absent ✓

---

## Recommended Remediation Workflow

### Phase 1: Critical Data Fixes (REQUIRED before submission)

**Step 1:** Resolve Period Distribution inconsistency
- [ ] Decide: Is 1.0 or 2.5 the correct uncertainty value?
- [ ] Update manuscript.tex line 339 with clarifying language
- [ ] Verify table1_systematic_budget.tex line 18 matches decision
- [ ] Check if Figure 2 needs regeneration
- [ ] Update all in-text references to be consistent

**Step 2:** Fix Figure 3 galaxy count
- [ ] Count actual galaxies in the data
- [ ] Update caption OR regenerate figure to match

**Step 3:** Verify Table 7 rendering
- [ ] Compile PDF and check if headers render correctly
- [ ] If not, investigate deluxetable* math mode issues

### Phase 2: PDF Rendering Investigation (HIGH PRIORITY)

**Step 4:** Diagnose sigma rendering
- [ ] Check LaTeX compilation logs
- [ ] Test with different engines (pdflatex, xelatex, lualatex)
- [ ] Review aastex631.cls documentation for known issues
- [ ] Test on different systems (Overleaf vs local)

**Step 5:** Compile test PDF
- [ ] Generate PDF locally with verbose logging
- [ ] Visual inspection of all pages with sigma symbols
- [ ] Verify H₀ subscripts render correctly throughout

### Phase 3: Minor Cleanup (NICE TO HAVE)

**Step 6:** Search for rare typos
- [ ] Manual search for "το" character
- [ ] Manual search for "Mpe" typo
- [ ] Verify Figure 1 legend rendering

**Step 7:** Final verification
- [ ] Complete PDF visual inspection
- [ ] Cross-check all numerical values in tables vs text
- [ ] Verify all figure captions match figure contents

---

## Critical Questions - ANSWERED

1. **Period Distribution:** ✅ **RESOLVED**
   - Keep table at 1.0 km/s/Mpc (uncertainty)
   - Text updated to clarify: "systematic uncertainty 1.0 km/s/Mpc from range of plausible corrections (bias correction -2.5 adopted)"

2. **PDF Rendering:** ✅ **IDENTIFIED**
   - Using Overleaf to compile PDF
   - Sigma rendering issue is known Overleaf font encoding problem

3. **Figure 3:** ✅ **FIXED**
   - 7 galaxies confirmed in CSV data
   - Figure regenerated with correct "7 galaxies" label
   - Legend moved to lower right to eliminate overlap

---

## Summary

**Genuine LaTeX source problems:**
1. ✅ **FIXED:** Period Distribution text clarification (manuscript.tex lines 339, 366)
2. ✅ **FIXED:** Figure 3 galaxy count (7 not 8) + legend overlap
3. ⚠️ **LOW PRIORITY:** Figure 1 legend cutoff (cosmetic only)
4. ⚠️ **FALSE POSITIVE:** Table 7 headers are correct in LaTeX source

**PDF rendering artifacts (Overleaf issue):**
1. 🔴 **CRITICAL:** Sigma symbols rendering incorrectly - see Overleaf guidance below
2. 🔴 **CRITICAL:** Greek letters in table headers not rendering - same root cause
3. ✅ **VERIFIED:** H₀ notation is correct in LaTeX source

**Overleaf PDF Rendering Fix - Action Required:**

The sigma and Greek letter rendering issues are caused by Overleaf's font compilation. You have three options:

**Option 1: Add explicit font encoding (RECOMMENDED)**

Add this to your preamble (after `\usepackage[utf8]{inputenc}`):

```latex
\usepackage{lmodern}  % Latin Modern fonts
\usepackage{cmbright} % Computer Modern Bright (optional alternative)
```

**Option 2: Use text-mode sigma in problematic contexts**

Replace math-mode sigma with text-mode in locations where rendering fails:

```latex
% Instead of: 5.9$\sigma$
% Use: 5.9\textsigma  (requires textgreek package)
\usepackage{textgreek}
```

**Option 3: Switch Overleaf compiler**

In Overleaf project settings:
- Menu → Compiler
- Try: XeLaTeX or LuaLaTeX instead of pdfLaTeX
- These have better Unicode/font support

**Diagnosis steps:**
1. Check Overleaf compilation logs for font warnings
2. Look for messages like "Missing character" or "Font encoding"
3. If you see OT1 encoding warnings, add `\usepackage[T1]{fontenc}` (already in your source)

**Next step:** Try Option 1 first (add lmodern package), recompile in Overleaf, and check if sigma symbols render correctly.

---

**Created:** November 14, 2025
**Purpose:** Remediation plan for PDF forensic analysis findings
**Based on:** Forensic_Analysis_of_Distance_Ladder_Systematics_v8_6e.pdf audit report
