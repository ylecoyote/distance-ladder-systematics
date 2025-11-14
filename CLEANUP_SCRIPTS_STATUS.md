# Cleanup Scripts Status

**Date:** November 13, 2025
**Current State:** Two cleanup scripts available

---

## Summary

### cleanup_repo.sh (Original) - **OBSOLETE**
- **Status:** ❌ **Outdated - Do NOT use**
- **Created:** Before v8.6C inconsistency fixes
- **Purpose:** Archive initial submission prep documentation
- **Issue:** All files it tries to archive are already gone or archived

### cleanup_repo_v2.sh (Updated) - **CURRENT**
- **Status:** ✅ **Ready to use**
- **Created:** November 13, 2025 (post-v8.6C)
- **Purpose:** Archive v8.6C inconsistency fix documentation
- **Scope:** Handles new documentation from recent work

---

## What cleanup_repo.sh Does (Obsolete)

**Files it tries to archive (ALL MISSING):**
```
❌ CRITICAL_FIX_MISSING_FIGURES.md
❌ CITATION_FIXES.md
❌ LATEX_FORMATTING_FIXES.md
❌ OVERLEAF_SUBMISSION_STATUS.md
❌ PREPRINT_STYLE_CHANGE.md
❌ PRE_SUBMISSION_FIXES_COMPLETE.md
❌ APPENDIX_FIGURES_FIX.md
❌ CLEANUP_REPORT.md
❌ V8_0_RELEASE_SUMMARY.md
```

**Verdict:** These files no longer exist (likely already archived in previous cleanup).

---

## What cleanup_repo_v2.sh Does (Current)

**Files it will archive (ALL PRESENT):**
```
✅ BASELINE_CONSISTENCY_FIX.md
✅ CORRECTED_CEPHEID_FIX.md
✅ STAGE_VALUES_VALIDATION.md
✅ LEGACY_2.36X_FIX.md
✅ ALL_INCONSISTENCIES_RESOLVED.md
✅ OVERLEAF_PATH_FIX.md
✅ OVERLEAF_PACKAGE_SUMMARY.md
✅ OVERLEAF_PACKAGE_v8.6B_SUMMARY.md
✅ MD_FILES_ALIGNMENT_COMPLETE.md
✅ MD_FILES_VALIDATION_REPORT.md
✅ QUICK_VALIDATION_v8.6B.md
✅ REPO_CLEANUP_PLAN.md
```

**Intermediate packages it will archive:**
```
✅ manuscript_overleaf.zip (old)
✅ manuscript_overleaf_v8.6A.zip (intermediate)
✅ manuscript_overleaf_v8.6A_fixed.zip (intermediate)
✅ manuscript_overleaf_v8.6B.zip (intermediate, if exists)
✅ overleaf_package/ directory (compressed and removed)
```

**Files it will KEEP in root:**
```
✅ README.md
✅ FINAL_SUBMISSION_STATUS.md
✅ OVERLEAF_PACKAGE_v8.6C_SUMMARY.md (latest package summary)
✅ PLANCK_DEPENDENCE_ANALYSIS.md
✅ manuscript_overleaf_v8.6C.zip (final submission package)
```

---

## Key Differences

| Aspect | cleanup_repo.sh (OLD) | cleanup_repo_v2.sh (NEW) |
|--------|----------------------|--------------------------|
| **Target files** | Pre-submission prep docs | v8.6C inconsistency fixes |
| **All files exist?** | ❌ NO (all missing) | ✅ YES (12 files) |
| **Packages handled** | None | Archives old, keeps v8.6C |
| **Archive location** | submission_prep_logs/ | v8.6c_inconsistency_fixes/ |
| **Status** | Obsolete | Current |
| **Should use?** | ❌ NO | ✅ YES |

---

## What cleanup_repo_v2.sh Will Do

### Step 1: Create Archive Directory
```bash
mkdir -p _tmp/ARCHIVE/v8.6c_inconsistency_fixes
```

### Step 2: Archive Fix Documentation (12 files)
Moves all inconsistency fix documentation to archive:
- 4 primary fix documents (baseline, corrected Cepheid, stages, legacy factor)
- 1 comprehensive resolution summary
- 3 Overleaf package summaries (old versions)
- 2 validation reports
- 2 supporting documents

### Step 3: Archive Intermediate Packages
Creates archive directory:
```bash
mkdir -p _tmp/ARCHIVE/overleaf_intermediate_versions
```

Archives old packages:
- manuscript_overleaf.zip (original, pre-fixes)
- manuscript_overleaf_v8.6A.zip (first attempt)
- manuscript_overleaf_v8.6A_fixed.zip (path fix)
- manuscript_overleaf_v8.6B.zip (if exists)
- overleaf_package/ directory → compressed to .tar.gz

**KEEPS:** overleaf_package_v8.6B/ (source for v8.6C)

### Step 4: Update .gitignore
Adds patterns to exclude generated files:
```gitignore
# Generated Overleaf packages (keep only v8.6C tracked)
manuscript_overleaf*.zip
!manuscript_overleaf_v8.6C.zip
overleaf_package/
overleaf_package_v8.6B/
```

### Step 5-7: Track Essential Files
- Adds FINAL_SUBMISSION_STATUS.md
- Adds OVERLEAF_PACKAGE_v8.6C_SUMMARY.md
- Force-adds manuscript_overleaf_v8.6C.zip
- Updates .gitignore

---

## Current Repository State

### Untracked .md Files (12 total)
```
?? ALL_INCONSISTENCIES_RESOLVED.md
?? BASELINE_CONSISTENCY_FIX.md
?? CORRECTED_CEPHEID_FIX.md
?? LEGACY_2.36X_FIX.md
?? MD_FILES_ALIGNMENT_COMPLETE.md
?? MD_FILES_VALIDATION_REPORT.md
?? OVERLEAF_PACKAGE_SUMMARY.md
?? OVERLEAF_PACKAGE_v8.6B_SUMMARY.md
?? OVERLEAF_PACKAGE_v8.6C_SUMMARY.md  ← KEEP THIS
?? OVERLEAF_PATH_FIX.md
?? QUICK_VALIDATION_v8.6B.md
?? STAGE_VALUES_VALIDATION.md
```

### Modified Files (2 total)
```
M FINAL_SUBMISSION_STATUS.md  ← Track this
M README.md                    ← Track this
```

### ZIP Files (2 total)
```
manuscript_overleaf.zip         ← Archive (old)
manuscript_overleaf_v8.6C.zip   ← KEEP (final, 4.5 MB)
```

---

## Archive Directory Structure (After v2)

```
_tmp/ARCHIVE/
├── v8.6c_inconsistency_fixes/          ← NEW
│   ├── BASELINE_CONSISTENCY_FIX.md
│   ├── CORRECTED_CEPHEID_FIX.md
│   ├── STAGE_VALUES_VALIDATION.md
│   ├── LEGACY_2.36X_FIX.md
│   ├── ALL_INCONSISTENCIES_RESOLVED.md
│   ├── OVERLEAF_PATH_FIX.md
│   ├── OVERLEAF_PACKAGE_SUMMARY.md
│   ├── OVERLEAF_PACKAGE_v8.6B_SUMMARY.md
│   ├── MD_FILES_ALIGNMENT_COMPLETE.md
│   ├── MD_FILES_VALIDATION_REPORT.md
│   ├── QUICK_VALIDATION_v8.6B.md
│   └── REPO_CLEANUP_PLAN.md
├── overleaf_intermediate_versions/     ← NEW
│   ├── manuscript_overleaf.zip
│   ├── manuscript_overleaf_v8.6A.zip
│   ├── manuscript_overleaf_v8.6A_fixed.zip
│   ├── manuscript_overleaf_v8.6B.zip (if exists)
│   └── overleaf_package.tar.gz
└── submission_prep_logs/               ← OLD (from cleanup_repo.sh)
    └── (already archived files from previous cleanup)
```

---

## Recommendation

### **Use cleanup_repo_v2.sh**

**Why:**
1. ✅ All target files actually exist
2. ✅ Handles new v8.6C documentation
3. ✅ Cleans up intermediate Overleaf packages
4. ✅ Keeps only essential documentation
5. ✅ Prepares repository for final submission

**How to use:**
```bash
# Make executable (already done)
chmod +x cleanup_repo_v2.sh

# Run the script
./cleanup_repo_v2.sh

# Review changes
git status
git diff --cached

# Commit
git commit -m "Archive v8.6C inconsistency fix documentation"
```

---

## Final Repository State (After cleanup_repo_v2.sh)

### Root Directory Documentation
```
README.md                           (tracked, main docs)
FINAL_SUBMISSION_STATUS.md          (tracked, current status)
OVERLEAF_PACKAGE_v8.6C_SUMMARY.md   (tracked, latest package)
PLANCK_DEPENDENCE_ANALYSIS.md       (tracked, scientific analysis)
```

### Packages
```
manuscript_overleaf_v8.6C.zip       (tracked, final submission, 4.5 MB)
overleaf_package_v8.6B/             (untracked, source directory)
```

### Archive
```
_tmp/ARCHIVE/
├── v8.6c_inconsistency_fixes/      (12 .md files)
└── overleaf_intermediate_versions/ (4 .zip files + 1 .tar.gz)
```

**Total reduction:** 12 markdown files moved to archive, clean root directory

---

## What to Do with cleanup_repo.sh (Old)

**Option 1: Delete it**
```bash
rm cleanup_repo.sh
```

**Option 2: Archive it**
```bash
mv cleanup_repo.sh _tmp/ARCHIVE/submission_prep_logs/
```

**Recommendation:** Archive it for historical reference

---

## Summary

- ❌ **cleanup_repo.sh** is obsolete (all target files missing)
- ✅ **cleanup_repo_v2.sh** is current and ready to use
- ✅ Will archive 12 inconsistency fix .md files
- ✅ Will archive 4+ old Overleaf package files
- ✅ Will keep only 4 essential .md files in root
- ✅ Repository will be clean and ready for submission

**Status:** Ready to run cleanup_repo_v2.sh whenever you're ready to finalize the repository structure.

---

**Created:** November 13, 2025
**Purpose:** Compare cleanup scripts and provide guidance
