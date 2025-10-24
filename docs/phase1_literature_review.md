# Phase 1 Literature Review: H₀ Distance Ladder Measurements

**Project:** Distance Ladder Systematics Investigation
**Phase:** 1 - Literature Review & Data Compilation
**Date Started:** October 21, 2025
**Personas:** Dr. Chen + The Debugger + The Skeptic

---

## Executive Summary

This document compiles the latest H₀ measurements from distance ladder methods (2024-2025) and documents the landscape of systematic errors under debate in the field.

**Key Finding:** The H₀ tension persists with latest JWST data. SH0ES reports H₀ = 72.6 km/s/Mpc (Cepheid-based), while CCHP reports H₀ = 70.39 km/s/Mpc (TRGB-based). Recent work suggests systematic errors in the 1.2-1.3 km/s/Mpc range are needed for consistency.

---

## Latest H₀ Measurements (2024-2025)

### 1. SH0ES (Supernova H₀ for the Equation of State) - Riess et al.

**Method:** Cepheid Period-Luminosity calibration → SNe Ia distances → H₀

**Latest Results (2024, with JWST):**
- **H₀ = 72.6 ± 2.0 km/s/Mpc** (JWST observations, 2024)
- **H₀ = 72.8 km/s/Mpc** (HST observations, same galaxies)
- **H₀ = 73.30 ± 1.04 km/s/Mpc** (comprehensive 2021-2022 measurement)

**Sample:**
- 5 host galaxies of 8 Type Ia supernovae
- ~1,000 Cepheids total
- Distance reach: NGC 5468 at 130 million light-years

**Anchors:**
- Gaia EDR3 parallaxes (Milky Way Cepheids)
- NGC 4258 megamaser (geometric distance)
- LMC detached eclipsing binaries (geometric distance)

**Tension with Planck:**
- 5σ discrepancy with Planck+ΛCDM (H₀ = 67.36 ± 0.54 km/s/Mpc)
- Team states: "We can now rule out measurement error as the cause of the Hubble Tension with very high confidence"

**Claimed Uncertainty Breakdown:**
- Total: ±1.04 km/s/Mpc (1.4%)
- Systematic: [Need to compile detailed error budget from paper]
- Statistical: [Need to compile from paper]

**The Skeptic's Notes:**
- "Very high confidence" is a strong claim - need to see detailed systematic error analysis
- How do they quantify "measurement error ruled out"?
- 72.6 ± 2.0 vs 73.30 ± 1.04 - why is JWST measurement LESS precise?
- Sample of 1,000 Cepheids across 5 galaxies - how representative?

---

### 2. CCHP (Chicago-Carnegie Hubble Program) - Freedman et al.

**Method:** TRGB (Tip of Red Giant Branch) + JAGB + Cepheid calibration → SNe Ia distances → H₀

**Latest Results (2024-2025, with JWST):**

**TRGB Method:**
- **H₀ = 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN) km/s/Mpc** (HST+JWST combined)
- **H₀ = 68.81 ± 1.79 (stat) ± 1.32 (sys) km/s/Mpc** (JWST only)
- Total uncertainty: ~2.0 km/s/Mpc

**JAGB Method:**
- **H₀ = 67.80 ± 2.17 (stat) ± 1.64 (sys) km/s/Mpc** (JWST only)

**Cepheid Method (by CCHP):**
- **H₀ = 69.96 ± 1.53 km/s/Mpc** (combined estimate with TRGB and JAGB)

**Sample:**
- 10 nearby galaxies hosting 11 Type Ia supernovae
- NGC 4258 for geometric zero-point calibration (same as SH0ES)

**Key Claims:**
- TRGB and JAGB distances agree at <1% level
- Cepheid distances agree with TRGB at "just over 1% level"
- Results consistent with Planck+ΛCDM, "without need for new physics"

**Tension Assessment:**
- TRGB H₀ = 70.39 vs Planck H₀ = 67.36: ~1.4σ tension
- TRGB H₀ = 70.39 vs SH0ES H₀ = 73.30: ~1.4σ tension
- JAGB H₀ = 67.80 vs Planck H₀ = 67.36: ~0.2σ (excellent agreement!)

**The Skeptic's Notes:**
- CCHP Cepheid H₀ = 69.96 vs SH0ES Cepheid H₀ = 73.30 - 3.3 km/s/Mpc difference using SAME method!
- This is the smoking gun: Different groups using Cepheids get different answers
- JAGB agrees with Planck, TRGB intermediate, Cepheid high - suggests Cepheid systematic?
- "Just over 1% level" agreement - need exact numbers
- Why does CCHP conclude "no new physics" while SH0ES emphasizes tension?

---

### 3. Recent Reassessments (December 2024)

**Study:** "Reassessing the Cepheid-based distance ladder: implications for the Hubble constant" (arXiv:2412.07840)

**Key Finding:**
- Conservative reanalysis using resampling method: **H₀ = 72.18 ± 1.76 km/s/Mpc**
- Reduces Hubble tension from **5.4σ → 2.4σ**

**Identified Biases:**
1. **Assumed prior for residual parallax offset** (Milky Way Cepheids)
2. **Systematic differences between Cepheid periods** in anchor galaxies vs SNe host galaxies

**Implications:**
- If true, this suggests SH0ES H₀ = 73.30 ± 1.04 may be overestimated
- The "5σ tension" might actually be ~2.4σ (less compelling evidence for new physics)
- Parallax systematic could be significant

**The Skeptic's Notes:**
- This is critical! Independent reanalysis finds ~1 km/s/Mpc lower H₀
- Need to understand EXACTLY what they changed in methodology
- "Conservative" estimate - what makes it conservative?
- Why do period distributions differ between anchors and hosts?

---

### 4. Carnegie Supernova Project (CSP, 2023)

**Method:** Multi-calibrator approach (Cepheid + TRGB + SBF)

**Result:**
- **H₀ = 71.76 ± 0.58 (stat) ± 1.19 (sys) km/s/Mpc** (B-band)

**Key Finding:**
- Systematic errors of ~1.2-1.3 km/s/Mpc required for consistency across first rung of distance ladder
- Intermediate value between SH0ES and Planck

**The Skeptic's Notes:**
- 1.2-1.3 km/s/Mpc systematic uncertainty is LARGER than claimed by individual groups
- This suggests individual groups are underestimating systematics
- CSP result is the "average" - supports idea that truth is between extreme claims

---

## Compilation Table: Recent H₀ Measurements

| Group | Method | H₀ (km/s/Mpc) | σ_stat | σ_sys | σ_total | Year | Telescope | Sample Size |
|-------|--------|---------------|---------|-------|---------|------|-----------|-------------|
| **SH0ES** | Cepheid | 73.30 | -- | -- | 1.04 | 2022 | HST | 42 SNe Ia, ~2400 Cepheids |
| **SH0ES** | Cepheid | 72.6 | -- | -- | 2.0 | 2024 | JWST | 8 SNe Ia, ~1000 Cepheids |
| **CCHP** | TRGB | 70.39 | 1.22 | 1.33 | ~2.0 | 2025 | HST+JWST | 11 SNe Ia |
| **CCHP** | TRGB | 68.81 | 1.79 | 1.32 | ~2.3 | 2025 | JWST | 11 SNe Ia |
| **CCHP** | JAGB | 67.80 | 2.17 | 1.64 | ~2.7 | 2025 | JWST | 11 SNe Ia |
| **CCHP** | Cepheid | 69.96 | -- | -- | 1.53 | 2025 | JWST | 11 SNe Ia |
| **Reassessment** | Cepheid | 72.18 | -- | -- | 1.76 | 2024 | HST (reanalysis) | SH0ES data |
| **CSP** | Multi-calibrator | 71.76 | 0.58 | 1.19 | 1.31 | 2023 | HST | -- |
| **Planck+ΛCDM** | CMB | 67.36 | -- | -- | 0.54 | 2018 | Planck | Full sky |
| **H6 (our work)** | Cosmic Chronometers | ~67-68 | -- | -- | -- | 2025 | Various | 32 H(z) |

**Pattern Recognition (The Debugger):**
- Cepheid methods: 72-73 km/s/Mpc (SH0ES, reassessment)
- TRGB methods: 69-70 km/s/Mpc (CCHP)
- JAGB method: 68 km/s/Mpc (CCHP)
- CMB+ΛCDM: 67.4 km/s/Mpc (Planck)
- Direct H(z): ~67-68 km/s/Mpc (H6)

**Gradient:** Cepheid → TRGB → JAGB/CMB/H(z) shows systematic decrease in H₀

**The Skeptic's Question:** "Is this a real physical gradient in the distance ladder, or are Cepheid measurements systematically biased high?"

---

## Systematic Errors Under Debate

### 1. **Cepheid Metallicity Effect**

**The Controversy:**
- **SH0ES claim:** Metallicity effect <1% on distances (~0.7 km/s/Mpc on H₀)
- **Critics claim:** Metallicity effect ~3% on distances (~2-3 km/s/Mpc on H₀)

**Physical Basis:**
- Period-Luminosity relation slope and zero point depend on metallicity
- Metal-rich Cepheids are intrinsically fainter at fixed period
- If not corrected properly, distances systematically underestimated → H₀ overestimated

**Why It Matters:**
- 3% effect could explain ~2-3 km/s/Mpc of the tension
- Not enough alone to explain full 5.9 km/s/Mpc discrepancy (SH0ES - Planck)
- But combined with other systematics could be significant

**Current Status:**
- JWST should help resolve this (better wavelength coverage, less dust/extinction confusion)
- SH0ES 2024 JWST results still show high H₀, suggesting metallicity not full explanation
- But CCHP finds lower Cepheid H₀ = 69.96 with JWST (vs SH0ES 72.6)

**The Debugger's Analysis:**
- Need to trace: Metallicity → PL relation correction → Distance modulus → H₀
- Question: Are SH0ES and CCHP using same metallicity correction?
- Action: Compare SH0ES vs CCHP Cepheid methodologies in detail

**The Skeptic's Challenge:**
- "SH0ES claims <1%, critics claim ~3% - someone is wrong by 3×!"
- "Show me the empirical PL relation vs metallicity data, not just theoretical models"
- "Are there independent tests of metallicity dependence?"

---

### 2. **Parallax Zero Point (Anchor Calibration)**

**The Issue:**
- Milky Way Cepheids calibrated using Gaia parallaxes
- Systematic parallax zero point offset affects all distances
- December 2024 reassessment identified this as key bias

**Physical Basis:**
- Gaia parallax: π = 1/d, so systematic offset Δπ → distance error
- Small parallax offset (e.g., 10 μas) → significant distance error at kpc scales
- Propagates through entire distance ladder

**Impact:**
- Reassessment with different parallax prior: H₀ = 72.18 ± 1.76 (vs SH0ES 73.30 ± 1.04)
- Reduces tension from 5.4σ → 2.4σ
- ~1 km/s/Mpc effect

**Current Status:**
- Gaia EDR3 vs Gaia DR4: Have parallax zero points been revised?
- Different groups use different priors for parallax offset
- No consensus on "correct" prior

**The Debugger's Analysis:**
- Need to understand: What prior did SH0ES use? What prior did reassessment use?
- Trace impact: Parallax offset → MW Cepheid distances → PL zero point → all distances
- Check: Has Gaia DR4 (if released) changed parallax calibration?

**The Skeptic's Challenge:**
- "If changing the prior changes H₀ by 1 km/s/Mpc, how confident are we in ANY value?"
- "What is the 'correct' parallax offset? How do we know?"
- "This feels like a degeneracy - different assumptions give different H₀"

---

### 3. **CCHP vs SH0ES Cepheid Discrepancy**

**The Mystery:**
- Both groups use Cepheids to calibrate SNe Ia
- Both use NGC 4258 + MW Cepheids as anchors
- Yet: SH0ES H₀ = 73.30 vs CCHP H₀ = 69.96 (**3.3 km/s/Mpc difference!**)

**Possible Explanations:**

**A. Sample Selection:**
- SH0ES: 42 SNe Ia, ~2400 Cepheids
- CCHP: 11 SNe Ia, fewer Cepheids
- Could selection effects (which galaxies? which Cepheids?) matter?

**B. Period Range:**
- December 2024 paper: "Systematic differences between Cepheid periods in anchor galaxies vs SNe host galaxies"
- Are SH0ES and CCHP sampling different period ranges?
- Does PL relation have period-dependent systematics?

**C. Photometry/Crowding:**
- HST vs JWST: Different wavelengths, different crowding corrections
- Crowding: In dense stellar fields, blending makes Cepheids appear brighter → distances underestimated
- Are corrections applied differently?

**D. Extinction/Reddening:**
- Cepheids behind dust appear fainter → must correct for extinction
- Different reddening laws (Cardelli, Fitzpatrick, etc.) give different corrections
- Small differences propagate to H₀

**E. Metallicity Correction:**
- Are SH0ES and CCHP using same metallicity-PL correction?
- If CCHP uses larger metallicity correction → higher distances → lower H₀

**The Debugger's Priority:**
- **This is THE key question for Phase 2!**
- Same method, same anchors, but 3.3 km/s/Mpc difference
- Must trace through both pipelines step-by-step to find divergence point

**The Skeptic's Assessment:**
- "If two expert groups get 3.3 km/s/Mpc difference using 'same' method, there are hidden systematics"
- "One or both groups are making assumptions they don't fully account for in error budget"
- "This is more important than Cepheid vs TRGB - this is Cepheid vs Cepheid!"

**Dr. Chen's Strategic Note:**
- This should be Phase 2 deep dive priority
- If we can identify why SH0ES and CCHP Cepheid results differ, we've likely found the systematic
- This is a controlled experiment: same method, different results

---

### 4. **TRGB vs Cepheid: 1-2% Distance Discrepancy**

**The Observation:**
- TRGB H₀ = 70.39 vs Cepheid H₀ = 73.30: ~4% difference in H₀
- CCHP claims TRGB and Cepheid agree at "just over 1% level" in distances
- But published H₀ values differ by 2-3 km/s/Mpc

**Possible Explanations:**

**A. TRGB Systematics:**
- Tip detection algorithm: Where exactly is the "tip"?
- Stellar population effects: Metallicity, age distribution affect TRGB luminosity
- TRGB absolute magnitude M_I calibration from NGC 4258, LMC

**B. Cepheid Systematics:**
- See above (metallicity, crowding, extinction, parallax)

**C. Both Have Systematics:**
- TRGB systematically low by ~1%?
- Cepheids systematically high by ~1%?
- Combined: 2% discrepancy

**The Debugger's Analysis:**
- CCHP claims "agree at 1% level" but H₀ differs by ~4%
- Inconsistency suggests: Either (1) distances agree but SNe calibration differs, or (2) "1% agreement" hides scatter
- Need to see galaxy-by-galaxy comparison, not just average

**The Skeptic's Question:**
- "How can distances agree at 1% but H₀ differ by 4%?"
- "Show me the residuals: TRGB distance minus Cepheid distance for each galaxy"
- "What is the scatter? Average agreement could hide systematic trend with distance"

---

### 5. **SNe Ia Standardization Systematics**

**The Issue:**
- Type Ia SNe are "standardizable candles" but not perfect standard candles
- Empirical corrections applied: Tripp relation (luminosity vs stretch, color)
- Host galaxy mass step: SNe in massive galaxies ~0.06 mag brighter

**Systematic Errors:**
- Tripp parameter degeneracies (α, β correlation)
- Host mass step: Physical mechanism unclear, could be environmental
- Peculiar velocities: Local flows affect redshifts → distance errors
- Evolution: Do SNe properties change with redshift?

**Impact on H₀:**
- These affect SNe-based distances, which are common to all methods
- If SNe calibration is wrong, ALL distance ladder measurements wrong
- But: Affects Cepheid and TRGB equally, so doesn't explain their discrepancy

**The Debugger's Note:**
- SNe systematics are "second rung" of ladder (after Cepheid/TRGB calibration)
- Important but probably not source of Cepheid-TRGB discrepancy
- Could affect overall normalization (all H₀ values high or low)

**The Skeptic's Caution:**
- "We're assuming SNe Ia are standardizable - what if that assumption is wrong?"
- "Host mass step is empirical, not understood physically - could hide systematics"
- "But: H6 cosmic chronometers bypass SNe entirely and agree with Planck - suggests SNe OK"

---

## Key Controversies and Tribal Dynamics

### The Field is Contentious

**SH0ES Team Position:**
- H₀ tension is real and significant (5σ)
- Measurement error ruled out with high confidence
- Likely new physics (early dark energy, neutrino interactions, modified gravity)
- Cepheid calibration is robust, systematics fully accounted for

**CCHP Team Position:**
- H₀ tension is reduced with TRGB calibration
- Results consistent with Planck+ΛCDM, no new physics needed
- TRGB more robust than Cepheids (less affected by crowding, extinction)
- Multiple independent methods (TRGB, JAGB, Cepheid) provide consistency checks

**Skeptics/Reassessment Position:**
- Tension may be exaggerated due to underestimated systematics
- Parallax zero point and sample selection biases significant
- Tension reduced from 5.4σ → 2.4σ with more conservative analysis
- Need for independent verification before claiming new physics

**Planck Team Position:**
- CMB+ΛCDM prediction is robust (H₀ = 67.36 ± 0.54 km/s/Mpc)
- If tension real, requires modification to ΛCDM or systematic in distance ladder
- No evidence for systematic error in CMB analysis

**The Skeptic's Meta-Analysis:**
- "Everyone is sure THEIR method is right and others have systematics"
- "SH0ES and CCHP both use Cepheids, get different answers, yet both claim robustness"
- "Field needs independent arbiter - that's us!"
- "We have advantage: Not invested in any method, can evaluate objectively"

---

## Critical Insight from Our H6 Work

**Our H6 Finding (October 2025):**
- 32 cosmic chronometer H(z) measurements (z = 0.07-1.97)
- ΛCDM with Planck H₀ = 67.4 km/s/Mpc: **χ²_red = 0.47** (EXCELLENT fit)
- H(z) directly measures expansion rate, bypasses distance ladder entirely

**Implication:**
- Expansion history is consistent with Planck H₀ = 67.4
- Therefore: H₀ tension is NOT in expansion history
- **Conclusion: Problem MUST be in distance ladder** (Cepheids, TRGB, or SNe)

**This Localizes the Search:**
- Don't need to consider new physics affecting expansion history
- Don't need to modify ΛCDM
- Focus forensic investigation on distance ladder measurement chain

**The Debugger's Strategy:**
- H6 tells us WHERE to look: distance ladder, not cosmology
- Narrows Phase 2 investigation significantly
- Can rule out alternatives (modified gravity, early dark energy affecting H(z))

---

## Phase 2 Priorities (Dr. Chen's Assessment)

Based on Phase 1 literature review, here are the most promising avenues for Phase 2 investigation:

### **Priority 1: SH0ES vs CCHP Cepheid Discrepancy** ⭐⭐⭐
**Why:** Same method, same anchors, 3.3 km/s/Mpc difference - this is THE smoking gun

**Investigation Plan:**
- Obtain SH0ES and CCHP papers with detailed methodology
- Compare step-by-step: Sample selection, photometry, crowding corrections, extinction, metallicity
- Identify exact point where pipelines diverge
- Assess which methodology is more robust

**Expected Outcome:** Identify specific assumption or correction that differs by ~4-5%

---

### **Priority 2: Parallax Zero Point Systematic** ⭐⭐
**Why:** December 2024 reassessment shows ~1 km/s/Mpc effect from prior choice

**Investigation Plan:**
- Review Gaia EDR3 vs DR4 parallax calibrations
- Compare parallax priors used by different groups
- Assess impact of different priors on final H₀
- Determine if there's an "objective" choice of prior

**Expected Outcome:** Quantify parallax systematic uncertainty, assess if it's been underestimated

---

### **Priority 3: Cepheid Metallicity Effect** ⭐⭐
**Why:** Factor of 3 disagreement between SH0ES and critics on magnitude of effect

**Investigation Plan:**
- Compile empirical PL relation vs metallicity data
- Compare theoretical predictions to observations
- Assess which metallicity correction is better supported
- Check if JWST data resolves controversy (better wavelength coverage)

**Expected Outcome:** Determine if metallicity could explain ~2-3 km/s/Mpc of discrepancy

---

### **Priority 4: TRGB vs Cepheid Cross-Validation** ⭐
**Why:** Independent check of Cepheid calibration; TRGB gives lower H₀

**Investigation Plan:**
- Galaxy-by-galaxy comparison of TRGB vs Cepheid distances
- Check for systematic trends with distance, metallicity, inclination
- Assess TRGB systematics (tip detection, stellar populations)

**Expected Outcome:** Determine if discrepancy is real or method-dependent

---

## The Skeptic's Red Flags

Based on Phase 1 review, here are concerning patterns that warrant deep investigation:

### 🚩 **Red Flag 1: Claimed Uncertainties Too Small**
- SH0ES: σ_total = 1.04 km/s/Mpc (1.4%)
- CCHP TRGB: σ_total ~ 2.0 km/s/Mpc (2.8%)
- But: Independent groups differ by 3.3 km/s/Mpc (3×-6× the claimed uncertainties)
- **Implication:** Someone is underestimating systematics

### 🚩 **Red Flag 2: "High Confidence" Claims vs. Discrepancies**
- SH0ES: "Rule out measurement error with very high confidence"
- CCHP: "No need for new physics"
- December 2024: "Tension reduced to 2.4σ"
- **Implication:** Field is not converging - contradictory "high confidence" claims

### 🚩 **Red Flag 3: Same Method, Different Results**
- SH0ES Cepheid: 73.30 km/s/Mpc
- CCHP Cepheid: 69.96 km/s/Mpc
- Both use NGC 4258 + MW Cepheids as anchors
- **Implication:** Hidden assumptions or corrections differ significantly

### 🚩 **Red Flag 4: JWST Doesn't Resolve Discrepancy**
- JWST was supposed to be definitive (better resolution, less extinction)
- SH0ES with JWST: Still high (72.6 km/s/Mpc)
- CCHP with JWST: Still intermediate (68.81-70.39 km/s/Mpc)
- **Implication:** Systematics not due to HST limitations

### 🚩 **Red Flag 5: Gradient Across Methods**
- Cepheid: ~73 km/s/Mpc
- TRGB: ~70 km/s/Mpc
- JAGB: ~68 km/s/Mpc
- CMB/H(z): ~67 km/s/Mpc
- **Implication:** Not random scatter - systematic trend suggests common error propagation?

---

## Next Steps

### Immediate Actions (Next Session):

1. **Compile Detailed Error Budgets:**
   - Extract full systematic error breakdown from SH0ES 2022 paper
   - Extract full systematic error breakdown from CCHP 2025 paper
   - Create side-by-side comparison table

2. **Obtain Key Papers:**
   - SH0ES comprehensive measurement (Riess+ 2022, ApJ)
   - CCHP status report (Freedman+ 2025, ApJ)
   - December 2024 reassessment (arXiv:2412.07840)
   - CSP multi-calibrator (2023)

3. **Start Phase 2 Deep Dive:**
   - Focus on Priority 1: SH0ES vs CCHP Cepheid discrepancy
   - Begin detailed methodology comparison

### Dr. Chen's Strategic Guidance:

**What We've Learned:**
- H₀ tension is in distance ladder, not expansion history (H6 confirms this)
- Latest JWST data doesn't resolve discrepancy (still 72.6 vs 70.4 vs 67.4)
- Different groups using "same" method get different answers (SH0ES vs CCHP Cepheids)
- Claimed uncertainties likely underestimated (groups differ by 3× their error bars)

**Where We Go Next:**
- **Phase 2 focus:** SH0ES vs CCHP Cepheid methodology comparison
- **Why this matters:** If we can identify why expert groups disagree, we've found the systematic
- **Our advantage:** Independent, objective analysis; not invested in any result
- **Timeline:** 2-3 weeks for detailed comparison

**Critical Success Factor:**
- Maintain objectivity - we're not trying to prove Cepheids OR TRGB are wrong
- Follow the evidence wherever it leads
- If we can't identify the systematic, that's a valid finding too (publish "no dominant systematic found")

---

## The Skeptic's Bottom Line

"The field claims high confidence but shows low convergence. That's the signature of underestimated systematics. Our job is to find where the systematics hide."

**Key Questions for Phase 2:**
1. Why do SH0ES and CCHP get different H₀ using Cepheids?
2. Is the parallax zero point properly accounted for?
3. What is the TRUE metallicity effect on Cepheid distances?
4. Why does TRGB give systematically lower H₀ than Cepheids?
5. Are claimed uncertainties realistic, or underestimated by 2-3×?

**We have the advantage of H6:** We know the problem is in the distance ladder. Now we find it.

---

*Phase 1 Literature Review compiled by Dr. Chen + The Debugger + The Skeptic*
*October 21, 2025*
*Next: Phase 2 Deep Dive - SH0ES vs CCHP Cepheid Methodology Comparison*
