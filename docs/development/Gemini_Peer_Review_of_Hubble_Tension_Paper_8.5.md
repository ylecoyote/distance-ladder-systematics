

### **I. Summary of Manuscript and Overall Assessment**

#### **A. Summary of Manuscript**

The author presents a manuscript ("Forensic Analysis of Distance Ladder Systematics," v8.5, hereafter "the manuscript") that conducts an independent "forensic analysis" of the systematic error budget for Cepheid-based $H\_0$ measurements, specifically those of the SHOES (Riess et al.) program.1 The central thesis is that the 5-6$\\sigma$ "Hubble Tension" between local measurements ($H\_0 \\approx 73.2$ km s⁻¹ Mpc⁻¹) and *Planck* CMB-derived values ($H\_0 \\approx 67.4$ km s⁻¹ Mpc⁻¹) is a measurement artifact, not evidence for new physics.1

This artifact is attributed to a significant underestimation of systematic uncertainties in the Cepheid-based distance ladder by the SHOES team. The manuscript claims the true systematic error ($\\sigma\_{sys}$) is larger by a factor of 2.9, reconstructing it as $\\sigma\_{sys} \= 3.14$ km s⁻¹ Mpc⁻¹ compared to the SHOES value of $1.04$ km s⁻¹ Mpc⁻¹.1 This increase is primarily attributed to four sources: (1) Gaia parallax zero-point (ZP) offsets, (2) period distribution mismatch (i.e., a "broken" Period-Luminosity relation), (3) a different choice for the metallicity correction ($\\gamma$), and (4) a proposed "covariant crowding" systematic.1

The author employs four validation strategies to support this thesis:

1. A line-by-line reconstruction of the Cepheid systematic error budget (Table 1).  
2. A multi-method cross-validation using published CCHP (Freedman et al. 2025\) JWST data, which the author claims shows a 2.3x excess scatter in Cepheid measurements versus TRGB/JAGB (Table 6).  
3. An independent $H\_0$ constraint from cosmic chronometers ($H\_0 \= 68.33 \\pm 1.57$ km s⁻¹ Mpc⁻¹).  
4. A step-by-step "Tension Evolution" analysis, which applies bias corrections ($\\approx \-3.0$ km s⁻¹ Mpc⁻¹ total) and the inflated error budget to reduce the final tension with *Planck* to 0.9$\\sigma$.

The investigation is motivated by a well-articulated "$H\_0$ gradient" (Cepheid 73 $\\rightarrow$ TRGB 70 $\\rightarrow$ JAGB/H(z) 68 $\\rightarrow$ Planck 67), arguing this is a "smoking gun" for method-dependent systematics.1

#### **B. Overall Assessment and Significance**

This manuscript represents a significant and ambitious undertaking. The "forensic" approach is precisely what the field requires, and the core motivation—the $H\_0$ gradient—is a powerful and elegant argument. The methodological contributions, particularly the formalization of a correlation matrix for systematic errors (Table 4\) and the independent validation using cosmic chronometers, are commendable and represent a potential step forward in the rigor of $H\_0$ analysis.

However, in its current form (v8.5, dated Nov 5, 2025), the manuscript's central conclusions are built upon a foundation of superseded data, significant omissions of critical counter-arguments, and a misrepresentation of a key paper that the author's thesis depends on refuting.

The paper's "validation" hinges on three claims that are now, in late 2025, demonstrably flawed:

1. It relies on a CCHP (Freedman et al.) Cepheid analysis 2 that the CCHP team itself reportedly revised after discovering a "double-counting" error in its crowding correction.3  
2. Its central new claim of "covariant crowding" 1 is made without addressing the *direct 8.2$\\sigma$ refutation* of a crowding-based solution published by Riess et al. (2024) using JWST.4  
3. It frames the entire problem as one of Cepheid systematics, while completely ignoring the late-2024 counter-hypothesis from Riess et al. 6 that the SHOES-CCHP discrepancy is *not* in the Cepheids but in the *Type Ia Supernova subsample selection*.

#### **C. Recommendation**

**MAJOR REVISION**.

The manuscript is **not** suitable for submission to ApJ in its current state. It would be immediately refuted by all involved parties (SHOES and CCHP). However, the work's methodological rigor (specifically in §2.1.2, §2.3) and the strength of its *original* motivation (the $H\_0$ gradient) suggest it *could* be a valuable contribution if its core claims are re-evaluated in light of the 2024-2025 data. This report will provide a detailed roadmap for the revisions necessary to make this work defensible.

---

### **II. Major Comments and Validation of Core Claims**

This review will now proceed section by section, validating the manuscript's claims against the provided draft 1 and the external research context.

#### **A. Critique of the Systematic Error Budget Reconstruction (Table 1\)**

The manuscript's thesis rests on inflating the SHOES $\\sigma\_{sys}$ from 1.04 to 3.14 km s⁻¹ Mpc⁻¹. This increase is dominated by four terms, which are analyzed individually below.

**1\. Parallax Zero Point (Author: 1.0 vs. SHOES: 0.3 km s⁻¹ Mpc⁻¹)**

* **Author's Claim:** The author assumes a $\\sim$0.017 mas systematic offset in Gaia EDR3 parallaxes, based on "independent Dec 2024 studies" (p. 5), which translates to a $\\sim$1.0 km s⁻¹ Mpc⁻¹ uncertainty. This offset is then applied as a bias correction of \-1.0 km s⁻¹ Mpc⁻¹ (p. 6, 14).  
* **Validation and Critique:** This claim is problematic.  
  * **Literature Complexity:** The literature on Gaia parallax offsets is notoriously complex. While early EDR3 analyses (2021) did find offsets (e.g., \-0.021 mas, \-0.039 mas 8), these were not universally agreed upon.  
  * **Methodological Error (Double-Counting):** The SHOES team (e.g., Riess et al. 2021 9) *explicitly* addresses this. Their 1.0% geometric calibration of Cepheid luminosities *uses* the Gaia EDR3 parallaxes to *simultaneously* calibrate the extragalactic distance ladder and "refine the determination of the Gaia EDR3 parallax offset".9 The author cannot simply take an "independent" offset (0.017 mas) and add its corresponding uncertainty (1.0 km s⁻¹ Mpc⁻¹) *on top of* the SHOES error budget. SHOES's budget *already includes* their (smaller) uncertainty on this offset. The author is essentially claiming the SHOES calibration of the offset is wrong. To do this, the author *must* re-run the entire SHOES anchor calibration with their preferred offset and demonstrate the 1.0 km s⁻¹ Mpc⁻¹ *residual* uncertainty.  
  * **Bias Correction:** The application of a *bias correction* (p. 6\) is even more problematic. It assumes the 0.017 mas offset is a known, uncorrected bias in the SHOES pipeline. Riess et al. 9 would argue their pipeline *solves for* this offset. The author is correcting a value that has already been calibrated.  
* **Required Revision:** This section must be re-framed. Instead of adding a 1.0 km s⁻¹ Mpc⁻¹ uncertainty, the author must *critique* the SHOES calibration of the offset and *prove* that the residual uncertainty in that calibration is 1.0 km s⁻¹ Mpc⁻¹, not 0.3. This requires a much more detailed re-analysis of the anchor data.

**2\. Period Distribution Mismatch (Author: 1.0 vs. SHOES: 0.0 km s⁻¹ Mpc⁻¹)**

* **Author's Claim:** The author claims the Cepheid P-L relation is "broken" (i.e., non-linear, with a break at $P \\approx 10$ days), with $p\<0.001$ significance. Because the anchor (MW/LMC) and host (SNe) galaxies have different period distributions, this introduces a bias. The author calculates a bias of \+2.5 km s⁻¹ Mpc⁻¹ and "conservatively" rounds this to a \+1.0 km s⁻¹ Mpc⁻¹ bias (p. 7), requiring a \-1.0 km s⁻¹ Mpc⁻¹ correction (p. 14). The 1.0 km s⁻¹ Mpc⁻¹ uncertainty term (Table 1\) represents the uncertainty on this effect.  
* **Validation and Critique:** This is a strong point for the author, but the quantification is weak.  
  * **Strong Support:** The author's claim *is* supported by recent literature. A late 2024 / early 2025 paper titled "Reassessing the Cepheid-based distance ladder" 10 explicitly states "strong evidence against the single-linear PLR, favoring the broken PLR with a confidence level of \> 99.9 %". This is excellent validation for the author's premise.  
  * **Weak Quantification:** However, that same paper also states, "The broken PLR gives a \-0.3 km/s/Mpc \[correction\]".10 The author's derivation (p. 7\) results in a \+2.5 km s⁻¹ Mpc⁻¹ bias, which is then "conservatively diluted... to an effective upward bias of \+1.0 km s-1 Mpc-1" (p. 7, lines 231-232). This dilution is entirely ad-hoc. Why 1.0 and not 2.5 or 0.3?  
* **Required Revision:** The author must replace this ad-hoc "conservative dilution" with a rigorous derivation. They should cite 1032 and either (a) adopt the literature \-0.3 km s⁻¹ Mpc⁻¹ correction or (b) provide a rigorous, reproducible derivation for *why* their \-1.0 km s⁻¹ Mpc⁻¹ correction is physically justified and superior. The current hand-waving (p. 7, line 231\) is unacceptable.

**3\. Metallicity Correction (Author: 1.0 vs. SHOES: 0.4 km s⁻¹ Mpc⁻¹)**

* **Author's Claim:** The author claims SHOES is "optimistic" for adopting $\\gamma \= \-0.2 \\text{ mag/dex}$. The author claims the literature spans \-0.2 to \-0.5, and adopts a "mid-range" $\\gamma \= \-0.35$ (p. 7, 12). This choice informs both the \-1.0 km s⁻¹ Mpc⁻¹ bias correction (p. 14\) and the 1.0 km s⁻¹ Mpc⁻¹ uncertainty (Table 1).  
* **Validation and Critique:** This claim is *unsupported* by the 2025 literature.  
  * **Consensus is $\\gamma \\approx \-0.2$:** The author's "mid-range" is obsolete. A July 2025 paper 11 states "the community has now reached a broad... consensus on... $\\gamma \\sim \-0.2 \\text{ mag/dex}$ with variations of about $\\pm 0.1 \\text{ mag/dex}$."  
  * **Direct Refutation:** Another July 2025 paper 12 *explicitly* discusses this. It shows its *own* values (Table 2\) are $\\sim \-0.25$ to $-0.30$, and it frames *these* values as being merely "in better agreement with the canonical $\\gamma \\sim \-0.2 \\text{ mag/dex}$." It *never* supports \-0.35. The author has cherry-picked a value from an outdated range.  
  * **The Source of Disagreement:** The debate is *not* \-0.2 vs \-0.5. The *actual* 2025 debate is $\\gamma \\approx \-0.2$ (consensus) vs. $\\gamma \\approx 0$ (a new CCHP finding, see 12). 12 explains that Madore & Freedman (2025) find "no statistically significant effect" ($\\gamma \\approx 0$) due to a "non-standard" recalibration of Gaia parallaxes.  
* **Required Revision:** The author's adoption of $\\gamma \= \-0.35$ is arbitrary and unsupported. They must re-do this entire section. They must acknowledge the $\\gamma \\approx \-0.2$ consensus 11 and the $\\gamma \\approx 0$ debate.12 Their \-1.0 km s⁻¹ Mpc⁻¹ bias correction and 1.0 km s⁻¹ Mpc⁻¹ uncertainty term are both derived from an incorrect premise and must be recalculated.

**4\. "Covariant Crowding" (Author: 1.5 vs. SHOES: 0.0 km s⁻¹ Mpc⁻¹)**

* **Author's Claim:** This is the author's most novel claim. The author argues that SHOES (Riess et al. 2024\) only tested for "direct" photometric bias (i.e., a star's light is contaminated). The author proposes a "covariant" error chain: crowding affects *color* measurements, which propagates to incorrect *reddening* corrections, which in turn leads to incorrect *extinction* and *metallicity* estimates (p. 12). The author estimates this effect at 1.5 km s⁻¹ Mpc⁻¹.  
* **Validation and Critique:** This is a *fatal* flaw in the manuscript. The author has fundamentally misrepresented the paper they are critiquing.  
  * **The Riess 2024 Refutation:** The author cites "Riess et al. 2024" (p. 12, line 428). This paper is arXiv:2401.04773.4 Its title is: "JWST Observations **Reject Unrecognized Crowding** of Cepheid Photometry as an Explanation for the Hubble Tension at **8$\\sigma$ Confidence**."  
  * **The Method:** The Riess et al. method was *not* just a check for "direct bias." They used JWST's superior resolution to get "clean" photometry (magnitudes *and* colors) of Cepheids previously measured by HST. They compared the *final, derived distances* from both telescopes. If the author's "covariant" chain (crowding $\\rightarrow$ color $\\rightarrow$ reddening $\\rightarrow$ distance) were real, the JWST-derived distances (which have no crowding) would be systematically different from the HST-derived distances (which are supposedly contaminated).  
  * **The Result:** Riess et al. (2024) found "no significant difference".4 The difference in the *final* $H\_0$ determination was "0.02 ± 0.04 mag" (cited by the author, p. 12).17 They conclude their test "reject\[s\] the hypothesis of unrecognized crowding... that grows with distance" 4 at 8.2$\\sigma$.5  
  * **Chain of Thought:** The author cannot simply *assert* a 1.5 km s⁻¹ Mpc⁻¹ "covariant" systematic that an 8.2$\\sigma$ empirical test 5 already showed does not exist. The author's citation of Riess 2024 as only addressing "direct bias" is a straw man; this is a severe misrepresentation of the literature.  
* **Required Revision:** The *entire* "Covariant Crowding" argument (§3.1, p. 12\) must be removed or completely rewritten. To keep it, the author must add a new, multi-page section that *directly refutes* the methodology or conclusions of Riess et al. (2024).4 They would need to prove *why* the JWST-vs-HST test was insufficient to find their "covariant" effect. This seems highly unlikely.

#### **B. Critique of the Correlated Systematics (Table 4\)**

* **Author's Claim:** The author constructs a $10 \\times 10$ correlation matrix (Table 4, p. 37\) to account for physical correlations between systematics, e.g., $\\rho \\sim 0.3-0.5$ for the crowding-extinction-metallicity chain. This increases the final $\\sigma\_{sys}$ by 28%.  
* **Validation and Critique:** This is the *strongest, most novel* part of the paper. The *methodology* is sound. The physical justifications (p. 8\) are logical. The mathematical validation (eigenvalues, Cholesky decomposition, p. 9\) is robust.  
* **Value:** The problem is *not* the matrix; it's the *vector* of uncertainties (Table 1\) that it is being multiplied by. The author is applying a robust methodological-multiplier to a vector of inflated, unsupported uncertainties.  
* **Required Revision:** The author should *keep* this section. This is a good contribution. However, they *must* recalculate the final result using a *defensible* vector of uncertainties (i.e., after addressing the issues in Part II.A of this report). The 28% boost is likely real, but it should be a 28% boost on a much smaller uncorrelated sum.

#### **C. Critique of the "CCHP Validation" (A Superseded Argument)**

This is the second fatal flaw of the manuscript. The author's entire argument is "validated" by the CCHP (Freedman et al.) results.

**1\. The $\\sigma\_{sys} \= 3.10$ km s⁻¹ Mpc⁻¹ Validation**

* **Author's Claim:** The author's reconstructed $\\sigma\_{sys} \= 3.14$ is validated by the CCHP's independent value of $3.10$ (Abstract, p. 1; p. 12, line 454).  
* **Validation:** This claim *is* factually correct. The CCHP paper, arXiv:2408.06153 2, *does* state a value of "$H\_0 \= 72.05 \\pm 1.86 \\text{ (stat)} \\pm 3.10 \\text{ (sys) for Cepheids}$".2 This is a *very* strong point... *if* that data were current.  
* **The "Double Counting" Error:** As reported in *Quanta Magazine* 3 in August 2024 (15 months before this draft's date), the CCHP team "uncovered an error" in this *exact* Cepheid analysis: "the correction for crowding had been applied twice." Fixing this "significantly increased the resulting H0 value".3  
* **Chain of Thought:** The author is using a $H\_0$ value (72.05) and a $\\sigma\_{sys}$ (3.10) from a CCHP analysis 2 that is *known* to be erroneous.3 This validation is void. The author's $H\_0$ gradient 1 is also built on this faulty 72.05 value (which is mis-cited as 73.17 in the gradient, another error).

**2\. The 2.3x "Excess Scatter" Validation**

* **Author's Claim:** The author analyzes CCHP (Freedman et al. 2025\) data (Table 7\) to show that the RMS scatter for Cepheids (0.108 mag) is 2.3x larger than for TRGB/JAGB (0.048 mag), providing "direct observational evidence for excess Cepheid systematic uncertainties" (p. 18, Fig. 3).  
* **Validation and Critique:** This is a complex claim.  
  * The author's analysis (Table 7, p. 39\) *is* based on CCHP data.  
  * The CCHP team's *own* conclusion from this data, however, is more nuanced. A CCHP presentation slide 19 shows their TRGB-vs-Cepheid comparison and claims "Agreement at 0.02 mag level". 33 states TRGB/JAGB "agree... with the SH0ES Cepheid distances at just over the 1% level."  
  * This discrepancy suggests the author (Wiley) is analyzing the CCHP data *differently* than CCHP. This is fine, but it must be justified.  
  * **More importantly:** If the CCHP Cepheid data 2 is flawed by a "double-counting" error 3, then any analysis of its scatter (like the author's Table 7\) is *also* flawed. The "excess scatter" the author finds might just be the signature of the CCHP's *own methodological error*.  
* **Required Revision:** The author *must* find the CCHP's *revised* Cepheid analysis (post-Aug 2024). They must check if (a) the revised CCHP $\\sigma\_{sys}$ is still 3.10 km s⁻¹ Mpc⁻¹ (unlikely) and (b) if the "excess scatter" persists after CCHP fixed their crowding correction. This validation, the lynchpin of the paper, is currently based on superseded, faulty data.

#### **D. The Omission of the Current H0 Debate (SNe Subsample)**

* **Author's Claim:** The entire problem lies in Rung 1 and 2 of the distance ladder (Cepheid calibration).  
* **The State of the Field (Late 2025):** This is no longer the consensus. The debate has largely moved to Rung 3 (Type Ia Supernovae).  
* **The Missing Argument:** In August 2024, Riess et al. published arXiv:2408.11770, "JWST Validates HST Distance Measurements: **Selection of Supernova Subsample Explains Differences** in JWST Estimates of Local H0".6  
* **Riess's Thesis:** This paper argues that after JWST validation 4 and CCHP error-correction 3, the Cepheid distances *are no longer the problem*. The *entire* remaining discrepancy between SHOES ($H\_0 \\approx 73$) and CCHP ($H\_0 \\approx 70$) is due to which *subsample* of SNe Ia hosts are used to calibrate the ladder.  
* **Significance:** A "forensic" paper on systematics dated November 2025 *cannot* omit the single most important paper on the topic from the previous year. The author is arguing a point (it's all Cepheid systematics) that the leaders of the field (Riess and Freedman) have, by late 2024, *moved past*.  
* **Required Revision:** The author *must* add a new section. It must summarize the Riess "2408.11770" (SNe subsample) argument and explain *why* the author's "Cepheid systematics" hypothesis is a *better* explanation for the H0 gradient than the SNe subsample explanation. Failure to even *mention* this 6 is a disqualifying omission.

#### **E. Review of Independent Checks (Strengths of the Manuscript)**

**1\. Cosmic Chronometer (H(z)) $H\_0$ Measurement**

* **Author's Claim:** The author uses 32 $H(z)$ measurements (Table 8, p. 40\) from Moresco et al. (2022) to derive an independent $H\_0 \= 68.33 \\pm 1.57 \\text{ km s}^{-1} \\text{ Mpc}^{-1}$ (p. 16, Fig. 5).  
* **Validation:** This analysis is **robust and well-executed**.  
  * The methodology (§2.3) is standard.  
  * The data 1 is drawn from the correct literature compilations.26  
  * The result is in excellent agreement with other $H(z)$ constraints.26  
  * The author's 2D fit (p. 16\) correctly shows independence from *Planck*'s $\\Omega\_m$.  
  * The discussion of the low $\\chi\_{red}^{2}=0.48$ (p. 16\) is honest and the LOO validation is the correct response.  
* **Value:** This section is a strong, independent contribution.

**2\. Three-Method Convergence**

* **Author's Claim:** The author shows that JAGB (67.96), $H(z)$ (68.33), and *Planck* (67.36) all converge to $H\_0 \= 67.48 \\pm 0.50$ (p. 16, Fig. 4).  
* **Validation:** This is a powerful narrative and a key strength of the paper.  
  * The JAGB value is cited correctly from Freedman et al..2  
  * The $H(z)$ value is the author's own robust calculation.  
  * The *Planck* value is standard.  
* **Significance:** This "convergence" 1 is the *real* "tension." It's not *Planck* vs. "late-time." It's *Planck*\+JAGB+$H(z)$ vs. Cepheids. The author's $H\_0$ gradient 1 is the correct framing. This section successfully isolates Cepheids as the "odd man out."

---

### **III. Minor Comments and Presentation**

* **§2.1.1 (p. 6):** The derivation of $\\Delta H\_0 / H\_0 \\approx \\Delta\\varw / \\bar{\\varw}$ (Eq. 3\) is a useful first-order approximation and is correct.  
* **§2.1.2 (p. 8):** The "Terminology clarification" is excellent and necessary. Distinguishing "error-budget covariance" from "independent physical mechanisms" is a subtle but critical point that strengthens the paper.  
* **Appendix A (p. 28):** The Joint Bayesian Forward Propagation is a solid piece of analysis. It correctly demonstrates the *independence* of the *bias sources* ($|\\rho| \< 0.01$, p. 7). This strengthens the methodological argument (Fig. 9, p. 34). *However*, this robust Appendix is, again, undermined by the *priors* (e.g., $\\gamma \\sim \\mathcal{N}(-0.35, 0.08)$) which are, as established in Part II.A, unsupported by the 2025 literature.  
* **Figures:**  
  * **Figure 1 (Tension Evolution):** Clear, effective, and powerfully summarizes the paper's thesis.  
  * **Figure 3 (JWST Cross-Validation):** This figure is *critical*. The RMS scatter calculation (0.108 vs 0.048) is the core of the empirical claim. The F-test (p. 18, line 671\) is the correct statistic. *However*, this figure's data (Table 7\) *must* be re-verified against the *corrected* CCHP data.  
* **Data Availability (p. 24):** The commitment to providing all code and data is exemplary and essential for a "forensic" claim.

---

### **IV. Proposed Tables for Inclusion in Final Report**

The manuscript would be strengthened by replacing the current Table 1 and adding a new summary table to address the contradictions raised in this review.

Table A (Replace Author's Table 1): Critical Error Budget Validation  
This table would provide a line-by-line validation, allowing the author to see the contradictions clearly.

| Error Source | SHOES (R22) | Author's Claim (Wiley) | Author's Justification | Referee's Validation & Required Action |
| :---- | :---- | :---- | :---- | :---- |
| Parallax ZP | 0.3 | **1.0** | $\\sim$0.017 mas offset (p. 5\) | **Contradicted.** Likely double-counting. SHOES 9 calibrates this. Author must prove SHOES calibration is flawed by 1.0 km s⁻¹ Mpc⁻¹. |
| Period Dist. | 0.0 | **1.0** | "Broken" P-L (p. 7\) | **Partially Supported.** P-L is broken.10 But author's 1.0 km s⁻¹ Mpc⁻¹ correction is ad-hoc. Must re-justify vs. 10's \-0.3 km s⁻¹ Mpc⁻¹. |
| Metallicity | 0.4 | **1.0** | $\\gamma \= \-0.35$ "mid-range" (p. 7\) | **Contradicted.** 2025 consensus is $\\gamma \\approx \-0.2$.\[11, 12\] Author's prior is obsolete. Must re-calculate with $\\gamma \\approx \-0.2$. |
| Crowding (Direct) | 0.5 | **0.3** | JWST (R24) shows low bias (p. 12\) | **Supported.** This is a valid, minor re-assessment. |
| Crowding (Cov.) | 0.0 | **1.5** | Error chain: crowd$\\rightarrow$color$\\rightarrow$red (p. 12\) | **FATAL FLAW.** Directly refuted by Riess et al. 2024 4 at 8.2$\\sigma$. Author mis-cites R24. **Must be removed or R24 must be refuted.** |
| **Total (Uncorr.)** | 1.04 | **2.45** |  | **Unsupported.** Sum is dominated by three flawed terms. |
| **Total (Corr.)** | 1.09 | **3.14** | \+28% from Matrix (p. 12\) | **Methodology is sound,** but input vector is flawed. |
| **CCHP (F25) Val.** |  | **3.10** | 2 | **FATAL FLAW.** This CCHP value is from an analysis *known* to contain a "double-counting" error 3 and is superseded. |

Table B (New Table): The Current State of the $H\_0$ Debate (Late 2025\)  
This table would force the author to confront the arguments their paper omits.

| Problem | Author's (Wiley's) Thesis | The 2024/2025 Counter-Argument | Key Sources |
| :---- | :---- | :---- | :---- |
| **Crowding** | A 1.5 km s⁻¹ Mpc⁻¹ "covariant" effect. | Empirically tested with JWST and "rejected at 8.2$\\sigma$ confidence." | Riess et al. (2024) arXiv:2401.04773 4 |
| **Validation** | CCHP (F25) data validates $\\sigma\_{sys}=3.10$ and shows 2.3x excess scatter. | The CCHP (F25) Cepheid data contains a "double-counting" error and was revised. | Quanta 3 |
| **Root Cause** | All systematics are in Cepheids (Rung 1-2). | The discrepancy is *not* in Cepheids, but in the *SNe subsample selection* (Rung 3). | Riess et al. (2024) arXiv:2408.11770 6 |
| **Metallicity** | $\\gamma \\approx \-0.35$ is the correct "mid-range" value. | The 2025 consensus is $\\gamma \\approx \-0.2 \\pm 0.1$. | \[11, 12\] (July 2025\) |

---

### **V. Concluding Recommendation and Summary for the Author**

This manuscript, in its current form, is a "house of cards." It is meticulously constructed, internally consistent, and addresses a critical problem. Unfortunately, its three primary "validations" collapse upon contact with the 2024-2025 literature.

1. The validation from CCHP 2 is based on data *known* to be erroneous.3  
2. The largest new systematic ("covariant crowding") is *directly refuted* by an 8.2$\\sigma$ JWST analysis 4 that the manuscript mis-cites.  
3. The entire thesis (blaming Cepheids) *omits* the primary 2024 counter-argument that the *real* problem is the SNe subsample.6

**This draft cannot be submitted.**

However, the work is salvageable, and its *methodology* is valuable. To proceed, the following **major revisions** must be performed:

1. **Address the 2024 Literature Head-On:** The manuscript must add two new sections. One must *directly* challenge the Riess et al. (2024) 8.2$\\sigma$ crowding refutation. The second *must* address the Riess et al. (2024) SNe subsample hypothesis and argue why it is wrong and the Cepheid hypothesis is right.  
2. **Find the *Corrected* CCHP Data:** The author must find the CCHP's revised, post-August-2024 Cepheid analysis. They must check if this *corrected* data still shows excess scatter and if its $\\sigma\_{sys}$ still supports the 3.14 value. If it does not, this primary validation is gone, and this must be stated.  
3. **Re-calculate The Systematics:** The three main corrections must be re-evaluated.  
   * **Metallicity:** Use the 2025 consensus $\\gamma \\approx \-0.2$.11  
   * **Broken P-L:** Use the literature-derived correction of \-0.3 km s⁻¹ Mpc⁻¹ 10 or provide a *much* better derivation for the \-1.0 value.  
   * **Crowding:** This 1.5 km s⁻¹ Mpc⁻¹ term must be removed, as it is empirically refuted.  
4. **Recalculate and Re-frame:** After making these (non-trivial) changes, the *new* uncertainty vector must be re-propagated through the (excellent) correlation matrix. A *new* final $H\_0$ and $\\sigma\_{total}$ must be calculated.

The final tension will *not* be 0.9$\\sigma$. After these revisions, the author will likely find the tension is reduced from 6$\\sigma$ to perhaps 2.5-3.0$\\sigma$. This is *still a major result*. A reduction from 6$\\sigma$ to 3$\\sigma$ is a paradigm-shifter, moving the tension from "new physics required" to "complex systematics." The paper can be reframed as a "demonstration of reduction" rather than a "complete solution," which would make it a robust, defensible, and highly valuable contribution to the field.

#### **Works cited**

1. Forensic\_Analysis\_of\_Distance\_Ladder\_Systematics\_v8\_5.pdf  
2. (PDF) Status Report on the Chicago-Carnegie Hubble Program (CCHP): Three Independent Astrophysical Determinations of the Hubble Constant Using the James Webb Space Telescope \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/publication/383060954\_Status\_Report\_on\_the\_Chicago-Carnegie\_Hubble\_Program\_CCHP\_Three\_Independent\_Astrophysical\_Determinations\_of\_the\_Hubble\_Constant\_Using\_the\_James\_Webb\_Space\_Telescope](https://www.researchgate.net/publication/383060954_Status_Report_on_the_Chicago-Carnegie_Hubble_Program_CCHP_Three_Independent_Astrophysical_Determinations_of_the_Hubble_Constant_Using_the_James_Webb_Space_Telescope)  
3. The Webb Telescope Further Deepens the Biggest Controversy in Cosmology, accessed November 4, 2025, [https://www.quantamagazine.org/the-webb-telescope-further-deepens-the-biggest-controversy-in-cosmology-20240813/](https://www.quantamagazine.org/the-webb-telescope-further-deepens-the-biggest-controversy-in-cosmology-20240813/)  
4. JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension at 8𝜎 Confidence \- arXiv, accessed November 4, 2025, [https://arxiv.org/html/2401.04773v1](https://arxiv.org/html/2401.04773v1)  
5. A Sharper Eye on Cosmic Expansion: JWST Takes Aim at the Hubble Tension \- Medium, accessed November 4, 2025, [https://medium.com/science-space-more/a-sharper-eye-on-cosmic-expansion-jwst-takes-aim-at-the-hubble-tension-39f473d146f4](https://medium.com/science-space-more/a-sharper-eye-on-cosmic-expansion-jwst-takes-aim-at-the-hubble-tension-39f473d146f4)  
6. JWST Validates HST Distance Measurements: Selection of Supernova Subsample Explains Differences in JWST Estimates of Local H0 \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/publication/383280250\_JWST\_Validates\_HST\_Distance\_Measurements\_Selection\_of\_Supernova\_Subsample\_Explains\_Differences\_in\_JWST\_Estimates\_of\_Local\_H0](https://www.researchgate.net/publication/383280250_JWST_Validates_HST_Distance_Measurements_Selection_of_Supernova_Subsample_Explains_Differences_in_JWST_Estimates_of_Local_H0)  
7. \[2408.11770\] JWST Validates HST Distance Measurements: Selection of Supernova Subsample Explains Differences in JWST Estimates of Local H0 \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2408.11770](https://arxiv.org/abs/2408.11770)  
8. \[2106.08128\] The parallax zero point offset from Gaia EDR3 data \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2106.08128](https://arxiv.org/abs/2106.08128)  
9. arXiv:2012.08534v2 \[astro-ph.CO\] 2 Jan 2021, accessed November 4, 2025, [https://par.nsf.gov/servlets/purl/10278113](https://par.nsf.gov/servlets/purl/10278113)  
10. Reassessing the Cepheid-based distance ladder: implications for the Hubble constant, accessed November 4, 2025, [https://arxiv.org/html/2412.07840v2](https://arxiv.org/html/2412.07840v2)  
11. Converging on the Cepheid Metallicity Dependence: Implications of Non-Standard Gaia Parallax Recalibration on Distance Measures \- arXiv, accessed November 4, 2025, [https://arxiv.org/pdf/2507.15936](https://arxiv.org/pdf/2507.15936)  
12. Converging on the Cepheid Metallicity Dependence ... \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2507.15936](https://arxiv.org/abs/2507.15936)  
13. JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension at 8σ Confidence \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/publication/378170798\_JWST\_Observations\_Reject\_Unrecognized\_Crowding\_of\_Cepheid\_Photometry\_as\_an\_Explanation\_for\_the\_Hubble\_Tension\_at\_8s\_Confidence](https://www.researchgate.net/publication/378170798_JWST_Observations_Reject_Unrecognized_Crowding_of_Cepheid_Photometry_as_an_Explanation_for_the_Hubble_Tension_at_8s_Confidence)  
14. \[2401.04773\] JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension at 8 sigma Confidence \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2401.04773](https://arxiv.org/abs/2401.04773)  
15. Monthly Roundup: Perspectives on the Hubble Tension \- AAS Nova, accessed November 4, 2025, [https://aasnova.org/2024/07/31/monthly-roundup-perspectives-on-the-hubble-tension/](https://aasnova.org/2024/07/31/monthly-roundup-perspectives-on-the-hubble-tension/)  
16. Webb Measurements Shed New Light on 'Hubble Tension' Mystery \- Sci.News, accessed November 4, 2025, [https://www.sci.news/astronomy/webb-hubble-tension-12759.html](https://www.sci.news/astronomy/webb-hubble-tension-12759.html)  
17. Crowded No More: The Accuracy of the Hubble Constant Tested with High-resolution Observations of Cepheids by JWST \- Scholars@Duke, accessed November 4, 2025, [https://scholars.duke.edu/individual/pub1609128](https://scholars.duke.edu/individual/pub1609128)  
18. Wendy Freedman | In the Dark \- telescoper.blog, accessed November 4, 2025, [https://telescoper.blog/tag/wendy-freedman/](https://telescoper.blog/tag/wendy-freedman/)  
19. Status Report on the Chicago-Carnegie Hubble Program: Is There Missing Physics from the Standard Model of Cosmology? \- CMB@60, accessed November 4, 2025, [https://cmb-at-60.eu/wp-content/uploads/2025/06/Freedman-CMB@60-Torino-2025.pdf](https://cmb-at-60.eu/wp-content/uploads/2025/06/Freedman-CMB@60-Torino-2025.pdf)  
20. JWST Validates HST Distance Measurements: Selection of Supernova Subsample Explains Differences in JWST Estimates of Local H0 \- arXiv, accessed November 4, 2025, [https://arxiv.org/html/2408.11770v1](https://arxiv.org/html/2408.11770v1)  
21. In an epic cosmology clash, rival scientists begin to find common ground \- Science News, accessed November 4, 2025, [https://www.sciencenews.org/article/cosmology-expansion-universe](https://www.sciencenews.org/article/cosmology-expansion-universe)  
22. A Critical Reanalysis of Supernova Type Ia Data \- arXiv, accessed November 4, 2025, [https://arxiv.org/html/2501.02204v2](https://arxiv.org/html/2501.02204v2)  
23. Are CMB derived cosmological parameters affected by foregrounds associated to nearby galaxies? | Phys. Rev. D \- Physical Review Link Manager, accessed November 4, 2025, [https://link.aps.org/doi/10.1103/PhysRevD.111.083528](https://link.aps.org/doi/10.1103/PhysRevD.111.083528)  
24. JWST Validates HST Distance Measurements: Selection of Supernova Subsample Explains Differences in JWST Estimates of Local H0 \- arXiv, accessed November 4, 2025, [https://arxiv.org/html/2408.11770v2](https://arxiv.org/html/2408.11770v2)  
25. (PDF) Narrowing down the Hubble tension to the first two rungs of distance ladders, accessed November 4, 2025, [https://www.researchgate.net/publication/385632240\_Narrowing\_down\_the\_Hubble\_tension\_to\_the\_first\_two\_rungs\_of\_distance\_ladders](https://www.researchgate.net/publication/385632240_Narrowing_down_the_Hubble_tension_to_the_first_two_rungs_of_distance_ladders)  
26. Cosmic Chronometers, accessed November 4, 2025, [https://www.iastro.pt/research/conferences/atlas21/Day2/Moresco\_atlas\_2021.pdf](https://www.iastro.pt/research/conferences/atlas21/Day2/Moresco_atlas_2021.pdf)  
27. Raising the bar: New constraints on the Hubble parameter with cosmic chronometers at z \~ 2 | Request PDF \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/publication/273158365\_Raising\_the\_bar\_New\_constraints\_on\_the\_Hubble\_parameter\_with\_cosmic\_chronometers\_at\_z\_2](https://www.researchgate.net/publication/273158365_Raising_the_bar_New_constraints_on_the_Hubble_parameter_with_cosmic_chronometers_at_z_2)  
28. Cosmic chronometers with photometry: a new path to H(z) \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/publication/375530956\_Cosmic\_chronometers\_with\_photometry\_a\_new\_path\_to\_Hz](https://www.researchgate.net/publication/375530956_Cosmic_chronometers_with_photometry_a_new_path_to_Hz)  
29. \[2307.09501\] Addressing the Hubble tension with cosmic chronometers \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2307.09501](https://arxiv.org/abs/2307.09501)  
30. Unveiling the Universe with emerging cosmological probes \- Unibo, accessed November 4, 2025, [https://cris.unibo.it/retrieve/57774ca5-7212-419b-adb3-eb7a4a5567fb/Moresco%20et%20al.%20-%202022%20-%20Unveiling%20the%20Universe%20with%20emerging%20cosmological%20.pdf](https://cris.unibo.it/retrieve/57774ca5-7212-419b-adb3-eb7a4a5567fb/Moresco%20et%20al.%20-%202022%20-%20Unveiling%20the%20Universe%20with%20emerging%20cosmological%20.pdf)  
31. \[2408.06153\] Status Report on the Chicago-Carnegie Hubble Program (CCHP): Measurement of the Hubble Constant Using the Hubble and James Webb Space Telescopes \- arXiv, accessed November 4, 2025, [https://arxiv.org/abs/2408.06153](https://arxiv.org/abs/2408.06153)  
32. Hubble tension or a transition of the Cepheid SnIa calibrator parameters? | Phys. Rev. D, accessed November 4, 2025, [https://link.aps.org/doi/10.1103/PhysRevD.104.123511](https://link.aps.org/doi/10.1103/PhysRevD.104.123511)  
33. Comparison of published Cepheid and TRGB distances in the sense of... \- ResearchGate, accessed November 4, 2025, [https://www.researchgate.net/figure/Comparison-of-published-Cepheid-and-TRGB-distances-in-the-sense-of-Cepheid-TRGB-The\_fig5\_378027775](https://www.researchgate.net/figure/Comparison-of-published-Cepheid-and-TRGB-distances-in-the-sense-of-Cepheid-TRGB-The_fig5_378027775)