# Undefined Table Reference Fix (§4.4)

**Date:** November 13, 2025
**Status:** ✅ **COMPLETE**

---

## Issue Identified

In §4.4 (Limitations and Caveats), there was an undefined table reference that would render as "Table ??" in the compiled PDF:

**Location:** [manuscript/manuscript.tex:592](manuscript/manuscript.tex#L592)

**Problem:**
```latex
We explore mid-range $\gamma \approx -0.35$ mag/dex and null $\gamma = 0$
in sensitivity tests only (Prior 2 and Prior 3; Table~\ref{tab:scenarios_summary}),
spanning correction range $[-1.8, 0]$ km~s$^{-1}$~Mpc$^{-1}$.
```

The label `tab:scenarios_summary` does not exist anywhere in the manuscript, causing the reference to be undefined.

---

## Context

The sentence is referring to the metallicity priors (Prior 2 and Prior 3) used in sensitivity tests. These are shown in the six-row sensitivity table in §3.2 (lines 426-432):

```latex
\begin{table}[h]
\centering
\small
\begin{tabular}{llcc}
\hline
Parallax & Metallicity Prior & H$_0$ (km~s$^{-1}$~Mpc$^{-1}$) & Tension \\
\hline
\textbf{Scenario A} & Prior 1 ($\gamma=-0.2$, baseline) & $69.54 \pm 1.89$ & \textbf{1.2$\sigma$} \\
(Baseline) & Prior 2 ($\gamma=-0.35$, sensitivity) & $68.87 \pm 2.02$ & \textbf{0.7$\sigma$} \\
 & Prior 3 ($\gamma=0$, sensitivity) & $70.54 \pm 1.89$ & \textbf{1.7$\sigma$} \\
\hline
\textbf{Scenario B} & Prior 1 ($\gamma=-0.2$, baseline) & $68.67 \pm 2.12$ & \textbf{0.6$\sigma$} \\
(Sensitivity) & Prior 2 ($\gamma=-0.35$, sensitivity) & $68.00 \pm 2.22$ & \textbf{0.3$\sigma$} \\
 & Prior 3 ($\gamma=0$, sensitivity) & $69.67 \pm 2.12$ & \textbf{1.1$\sigma$} \\
\hline
\end{tabular}
\end{table}
```

However, this table is an inline table in the main text without a formal label or table number.

---

## Solution

Changed the undefined table reference to a section reference pointing to §3.2 ("H₀ Tension Reduced from 5.9σ to 1.2σ"), which contains the sensitivity table showing all six parallax × metallicity prior combinations.

**Before:**
```latex
(Prior 2 and Prior 3; Table~\ref{tab:scenarios_summary})
```

**After:**
```latex
(Prior 2 and Prior 3; \S\ref{sec:results_tension})
```

The label `sec:results_tension` is defined at line 391:
```latex
\subsection{H$_0$ Tension Reduced from 5.9$\sigma$ to 1.2$\sigma$}
\label{sec:results_tension}
```

---

## Changes Applied

### 1. Source Manuscript (manuscript/manuscript.tex)

**Line 592:**
```latex
We explore mid-range $\gamma \approx -0.35$ mag/dex and null $\gamma = 0$
in sensitivity tests only (Prior 2 and Prior 3; \S\ref{sec:results_tension}),
spanning correction range $[-1.8, 0]$ km~s$^{-1}$~Mpc$^{-1}$.
```

### 2. Overleaf Package (overleaf_package_v8.6B/manuscript.tex)

Applied identical fix to line 592.

### 3. Package README (overleaf_package_v8.6B/README.txt)

Added item #7 to "RECENT CHANGES (v8.6C)" section:
```
7. §4.4 Limitations (Line 592)
   - Fixed undefined table reference: Table~\ref{tab:scenarios_summary} → \S\ref{sec:results_tension}
   - Now correctly references §3.2 where Prior 2/3 sensitivity tests are shown
   - Prevents "Table ??" from appearing in compiled PDF
```

---

## Verification

```bash
$ unzip -p manuscript_overleaf_v8.6C.zip manuscript.tex | grep -n "Prior 2 and Prior 3"
592:... (Prior 2 and Prior 3; \S\ref{sec:results_tension}), spanning ...
```

✅ **Reference now points to §3.2 correctly**

---

## Impact

**Before:** The compiled PDF would show "Table ??" in §4.4, causing confusion.

**After:** The compiled PDF will show "§3.2" (or the appropriate section number), correctly directing readers to where the sensitivity scenarios are presented.

**Scientific impact:** None - this is purely a formatting/reference fix. The content is unchanged.

---

## Files Modified

1. **manuscript/manuscript.tex** (line 592)
2. **overleaf_package_v8.6B/manuscript.tex** (line 592)
3. **overleaf_package_v8.6B/README.txt** (added item #7)
4. **manuscript_overleaf_v8.6C.zip** (recreated with all updates)

---

## Summary

**Problem:** Undefined table reference `\ref{tab:scenarios_summary}` would render as "Table ??" in compiled PDF.

**Solution:** Changed to section reference `\S\ref{sec:results_tension}` pointing to §3.2 where the sensitivity scenarios are shown.

**Status:** ✅ Complete and verified in v8.6C package

---

**Created:** November 13, 2025
**Purpose:** Document fix for undefined LaTeX table reference
**Part of:** v8.6C submission package finalization
