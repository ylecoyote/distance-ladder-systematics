---
name: Scientific Manuscript Review
description: Handles peer review responses for scientific manuscripts using AASTeX conventions. Use when responding to peer review, updating manuscript sections, adding derivations, or managing systematic uncertainty values across multiple sections.
allowed-tools: Read, Edit, Write, Grep, Bash
---

# Scientific Manuscript Review

This skill provides domain-specific expertise for responding to peer review comments on scientific manuscripts, with focus on astrophysics papers using AASTeX 6.31 format.

## MCP Tool Recommendations

### Sequential-Thinking
**Use when:**
- Creating novel derivation boxes (no existing template to follow)
- Multi-step causal reasoning with >3 physical mechanisms (e.g., crowding → color → reddening → metallicity)
- Complex reconciliation between sections (e.g., explaining why M1 correlations don't conflict with M2 independence)
- Designing new statistical analyses or bias corrections

**Example trigger**: "Add crowding bias derivation showing quantitative H₀ mapping"

**Why**: Novel derivations require iterative reasoning:
1. **Literature review** (thoughts 1-3): What prior work constrains this bias?
2. **Causal chain** (thoughts 4-7): Observable → mechanism → distance bias → H₀ impact
3. **Quantification** (thoughts 8-12): Numerical estimates with uncertainty propagation
4. **Integration** (thoughts 13+): How does this fit with existing corrections?

Sequential-thinking enables exploration of alternative physical mechanisms, revision when assumptions conflict with observations, and synthesis of literature constraints into unified bias correction.

### Vibe-Check
**Use when:**
- Before finalizing multi-section numerical updates (Abstract + §3.1 + §3.2 + Appendix)
- After implementing complex statistical analyses (correlation matrices, Bayesian fits)
- When reconciling potentially conflicting language between sections
- Before submission (comprehensive sanity check)

**Example trigger**: "Update all sections with new σ_sys = 3.14 km/s/Mpc"

**Common mistakes caught**:
- **Inconsistent values**: Abstract shows σ_sys = 2.45 but §3.2 shows 3.14
- **Sign convention confusion**: Mixing positive biases with negative corrections
- **Missing updates**: Updated Abstract but forgot Figure 1 caption
- **Correlation language**: Using "correlated" to describe both error budgets and correction degeneracies
- **Unit inconsistencies**: km/s/Mpc vs km s⁻¹ Mpc⁻¹

**Validation checklist**:
- All numerical values consistent across sections
- Sign conventions unified throughout (ΔH₀ ≡ H₀^corrected - H₀^SH0ES < 0)
- LaTeX formatting correct (no raw `$`, proper `\text{}` usage)
- Cross-references valid (\S\ref{}, Figure~\ref{})
- Significant figures appropriate for context

---

## Domain Knowledge: AASTeX Conventions

### LaTeX Formatting Rules

**Math mode**:
- Use `\(` and `\)` for inline math (not `$...$`)
- Use `\[` and `\]` or equation environment for display math
- Subscripts/superscripts: `H_0` not `H₀` (Unicode only in comments)
- Text in math mode: `\text{corrected}` not `{\text corrected}`
- Operators: `\sin`, `\log`, `\exp` (not sin, log, exp)

**Physical quantities**:
- H₀: `H_0` or `H$_0$` depending on context
- Systematic uncertainty: `\sigma_{\rm sys}` (roman for non-variables)
- Distance modulus: `\mu`
- Metallicity: `[{\rm Fe/H}]` (brackets require braces in LaTeX)
- Cepheid period: `\log P` or `\log_{10} P`

**Units**:
- Hubble constant: `km~s$^{-1}$~Mpc$^{-1}$` (non-breaking spaces, math mode for exponents)
- Alternative: `\mathrm{km\,s^{-1}\,Mpc^{-1}}` in math environments
- Avoid: `km/s/Mpc` in formal manuscript text (acceptable in code/data)

**Section references**:
- `\S\ref{sec:methods}` (capital S, tilde for non-breaking space)
- Not: `Section \ref{}` or `§\ref{}`

**Citations**:
- Parenthetical: `\citep{Riess2022}` → (Riess et al. 2022)
- Textual: `\citet{Riess2022}` → Riess et al. (2022)
- Multiple: `\citep{Riess2022,Planck2020}` (chronological order)

**Figure/Table references**:
- `Figure~\ref{fig:tension}` (capital F, non-breaking space)
- `Table~\ref{tab:error_budget}` (capital T)

**Common LaTeX errors to avoid**:
- ❌ Raw strings with `{\text -}` → ✅ `\text{-}`
- ❌ Unicode minus '−' in code → ✅ ASCII `-`
- ❌ Missing braces: `$\sigma_sys$` → ✅ `$\sigma_{\rm sys}$`
- ❌ Inconsistent spacing: `km s^{-1}Mpc^{-1}` → ✅ `km~s$^{-1}$~Mpc$^{-1}$`

---

## Domain Knowledge: Peer Review Response Format

### Response Structure

Each peer review item should follow this format:

```markdown
**[Item ID]**: [Brief summary of concern]

**Action**: [What was implemented]

**Changes**:
- [File/section]: [Specific change made]
- [File/section]: [Specific change made]

**Rationale**: [Why this addresses the concern]
```

**Example from M2**:
```markdown
**A2.1**: Establish unified sign convention for bias corrections

**Action**: Added explicit sign convention definition at start of §2.1.2

**Changes**:
- manuscript.tex:158: Added ΔH₀ ≡ H₀^corrected - H₀^SH0ES < 0 definition
- manuscript.tex:160-184: Updated all three derivations with unified convention

**Rationale**: Prevents confusion by defining convention once, then consistently applying
"uncorrected bias +X → correction -X" pattern across all derivations.
```

### Polish Request Patterns

**Pattern 1: Numerical Update**
```
Request: "Update Abstract with new σ_sys value"
Response: Check all sections, not just Abstract:
  - Abstract line ~8
  - §3.1 title (ratio calculation)
  - §3.2 title (tension value)
  - Figure captions
  - Appendix references
```

**Pattern 2: Add Derivation**
```
Request: "Provide quantitative derivation for X bias"
Response: Use derivation box template (see below)
  - Observable with typical value
  - Bias mechanism (causal chain)
  - H₀ mapping (∂H₀/∂X formula)
  - Numerical correction with sign convention
```

**Pattern 3: Reconcile Language**
```
Request: "Clarify difference between correlation in M1 vs M2"
Response: Add explicit paragraph explaining:
  - M1 correlations = covariance among uncertainty sources
  - M2 independence = degeneracies among correction amplitudes
  - These are different statistical objects (no contradiction)
```

---

## Domain Knowledge: Derivation Box Structure

Use this template when adding quantitative bias derivations:

```latex
\textbf{Observable:} [measured quantity with typical value and units]

\textbf{Bias mechanism:} [physical process creating systematic error,
with causal chain: X → Y → distance bias]

\textbf{H₀ mapping:} [quantitative formula: ∂H₀/∂X or ΔH₀/H₀ ≈ f(X)]

\textbf{Interpretation:} For [typical values], the uncorrected bias is
ΔH₀ ≈ +[value] km~s$^{-1}$~Mpc$^{-1}$ (positive = overestimation).
After [dilution/weighting], the net bias is +[value] km~s$^{-1}$~Mpc$^{-1}$,
yielding \textbf{correction ΔH₀ ≈ −[value] km~s$^{-1}$~Mpc$^{-1}$}.
```

**Example: Parallax Bias** (from M2.1):
```latex
\textbf{Observable:} Galactic Cepheid parallaxes $\varpi$ (Gaia EDR3),
$\bar{\varpi} \approx 0.7$ mas

\textbf{Bias mechanism:} Systematic offset $\Delta\varpi = +0.017$ mas
makes parallaxes appear larger $\rightarrow$ distances smaller $\rightarrow$
H$_0$ higher

\textbf{H₀ mapping:} $\Delta H_0 / H_0 \approx \Delta\varpi / \bar{\varpi}$

\textbf{Interpretation:} For Galactic Cepheid calibrators with
$\bar{\varpi} \approx 0.7$ mas and systematic offset $\Delta\varpi = +0.017$ mas,
we obtain uncorrected bias $\Delta H_0/H_0 \approx +0.024$ or
$+1.8$ km~s$^{-1}$~Mpc$^{-1}$. After dilution by LMC and NGC~4258 geometric
anchors (weighted $\sim$60\% MW, 40\% geometric), the bias is
$\approx +1.1$ km~s$^{-1}$~Mpc$^{-1}$, yielding \textbf{correction
$\Delta H_0 \approx -1.0$ km~s$^{-1}$~Mpc$^{-1}$}.
```

**Key principles**:
1. Always provide typical numerical values (not just formulas)
2. State sign convention explicitly (positive bias → negative correction)
3. Show dilution/weighting factors when applicable
4. Bold the final correction value for visibility
5. Use causal arrows (→) to show physical chain

---

## Domain Knowledge: Scientific Notation Standards

### Sign Conventions

**Standard convention** (use throughout):
```
ΔH₀ ≡ H₀^corrected - H₀^SH0ES
```
- **Negative values** reduce SH0ES measurement (ΔH₀ < 0)
- **Positive values** increase SH0ES measurement (ΔH₀ > 0)

**Bias correction pattern**:
- Bias causes overestimation → uncorrected bias is positive (+)
- Correction reduces measurement → correction is negative (−)
- Example: "Uncorrected bias +1.0 km/s/Mpc → correction −1.0 km/s/Mpc"

### Significant Figures

**Measurements**: 2-3 significant figures
- ✅ H₀ = 73.17 ± 1.31 km/s/Mpc
- ❌ H₀ = 73.1734 ± 1.314 km/s/Mpc (over-precision)

**Ratios**: 2 significant figures
- ✅ Ratio = 2.65× or 2.7×
- ❌ Ratio = 2.653×

**Tensions**: 2 significant figures
- ✅ Tension = 0.86σ or 0.9σ
- ❌ Tension = 0.8634σ

**Correlation coefficients**: 2 decimal places
- ✅ ρ = 0.35 or |ρ| < 0.01
- ❌ ρ = 0.3478

### Uncertainty Notation

**Symmetric uncertainties**:
- Format: `73.17 ± 1.31` (use ± not +/-)
- LaTeX: `$73.17 \pm 1.31$`

**Asymmetric uncertainties**:
- Format: `73.17 +1.45/-1.22`
- LaTeX: `$73.17^{+1.45}_{-1.22}$`

**Error budget breakdown**:
- Statistical: σ_stat
- Systematic: σ_sys
- Total: σ_total = √(σ²_stat + σ²_sys)

---

## Checklists for Common Operations

### When σ_sys Changes (M1 Correlated Analysis Update)

**Files to update** (check all):
1. **Abstract** (~line 8): Systematic uncertainty value
2. **§3.1 title** (~line 280): Ratio value (σ_sys/σ_stat)
3. **§3.2 title** (~line 310): Tension value (calculated from σ_total)
4. **Figure 1 caption** (~line 420): Stage-5 systematic value
5. **§3.1 body**: Ratio calculation and interpretation
6. **§3.2 body**: Tension formula and final value
7. **Appendix A** (if referenced): σ_sys value in correlation matrix discussion

**Calculation chain**:
```
σ_sys (new) → σ_total = √(σ²_stat + σ²_sys) →
ratio = σ_sys/σ_stat →
tension = |H₀,SH0ES - H₀,Planck| / σ_total
```

**Sanity checks**:
- σ_sys > σ_stat (ratio > 1.0 for this manuscript)
- σ_total > σ_sys (Pythagorean sum)
- Tension decreases as σ_total increases

### When Adding Bias Correction (M2 Pattern)

**Steps**:
1. **Literature review**: What constraints exist? (use sequential-thinking)
2. **Create derivation box**: Use template above
3. **Add to §2.1.2**: Insert after existing derivations
4. **Update correction sum**: Total ΔH₀ = Σ individual corrections
5. **Create validation analysis**: Joint Bayesian fit (if needed)
6. **Update Appendix A**: Add to validation section
7. **Create visualization**: Period histogram, sensitivity plot, etc.
8. **Cross-check**: Ensure sign conventions consistent

**Vibe-check before finalizing**:
- Is this bias independent of existing corrections?
- Are numerical values realistic given literature?
- Does sign convention match (positive bias → negative correction)?
- Have we provided quantitative H₀ mapping?

### When Reconciling Conflicting Language

**Common conflicts**:
1. **"Correlation" used for different concepts**:
   - M1: Error budget covariance (ρ ≈ 0.3)
   - M2: Correction degeneracy (|ρ| < 0.01)
   - Fix: Add explicit paragraph explaining these are different objects

2. **"Hierarchical" vs "Forward propagation"**:
   - Hierarchical implies data likelihoods + hyperpriors
   - Forward propagation = sample priors → propagate through model
   - Fix: Use accurate terminology for the actual method

3. **"Systematic" vs "Bias"**:
   - Systematic = uncertainty (error bar width)
   - Bias = shift in central value
   - Fix: Use precise terms, don't conflate

---

## Examples

### Example 1: Responding to M1 Polish Request

**User request**:
```
Reviewer asks: "Please add methodology one-liner for correlation assumptions in §2.1.1"
```

**Your response**:
1. Read manuscript.tex §2.1.1 (correlation matrix section)
2. Identify where to add one-liner (after matrix equation, before results)
3. Draft concise methodology:
   ```latex
   Correlations are estimated from shared astrophysical pathways: crowding affects
   photometry (→ color, reddening, metallicity), while parallax/period systematics
   propagate independently through calibration.
   ```
4. Use Edit tool to insert at appropriate location
5. Verify formatting (no raw `$`, proper spacing)

### Example 2: Adding New Bias Derivation

**User request**:
```
Add metallicity gradient bias derivation showing how radial gradients in host galaxies
affect H₀
```

**Your response**:
1. **Sequential-thinking**: Break down the physics
   - Thought 1-3: Literature review (radial gradients in spirals)
   - Thought 4-7: Causal chain (inner disk vs outer disk sampling)
   - Thought 8-12: Quantify ΔH₀ impact
2. **Draft derivation box**:
   ```latex
   \textbf{Observable:} Radial metallicity gradient d[Fe/H]/dr ≈ −0.05 dex/kpc

   \textbf{Bias mechanism:} SH0ES samples inner disks (r < 5 kpc, higher [Fe/H])
   vs calibrators span full disk → P-L zero-point brighter → distances underestimated
   → H₀ overestimated

   \textbf{H₀ mapping:} ΔH₀/H₀ ≈ 0.4605 × γ × (d[Fe/H]/dr) × Δr

   \textbf{Interpretation:} For γ = −0.35 mag/dex, gradient −0.05 dex/kpc,
   and sampling bias Δr ≈ 3 kpc, uncorrected bias is +0.5 km/s/Mpc,
   yielding correction ΔH₀ ≈ −0.5 km/s/Mpc.
   ```
3. **Vibe-check**: Is this independent of bulk metallicity correction? Yes (different physical mechanism)
4. Edit manuscript.tex to insert derivation
5. Update total correction sum if needed

### Example 3: Multi-Section Numerical Update

**User request**:
```
Update all sections with M1 correlated results: σ_sys = 3.14 km/s/Mpc
```

**Your response**:
1. **Read** manuscript.tex to find all occurrences
2. **Calculate** dependent values:
   - σ_stat = 1.18 km/s/Mpc (fixed)
   - σ_total = √(1.18² + 3.14²) = 3.36 km/s/Mpc
   - Ratio = 3.14/1.18 = 2.66 ≈ 2.7×
   - Tension = |73.17 - 67.36| / 3.36 = 1.73σ
3. **Update all sections** using Edit tool:
   - Abstract: "σ_sys = 3.14 km/s/Mpc"
   - §3.1 title: "Factor 2.7× Larger"
   - §3.2: "Tension = 1.7σ"
   - Figure caption: "Stage-5: σ_sys = 3.14"
4. **Vibe-check**: Run grep to find any missed instances
5. **Verify**: All values consistent, no pre-M1 numbers remain

---

## Summary

This skill provides:
- **Domain templates**: AASTeX conventions, derivation boxes, response formats
- **Numerical checklists**: Multi-section update procedures
- **Sign conventions**: Unified ΔH₀ notation throughout
- **Quality validation**: Vibe-check triggers for common mistakes
- **Reasoning support**: Sequential-thinking for novel derivations

Use this skill whenever working with peer review responses, manuscript revisions, or scientific writing requiring AASTeX formatting and systematic uncertainty analysis.