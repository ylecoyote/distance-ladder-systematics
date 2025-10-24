#!/bin/bash
# LaTeX Compilation Verification Script

echo "======================================================================"
echo "LATEX COMPILATION VERIFICATION FOR DISTANCE LADDER MANUSCRIPT"
echo "======================================================================"
echo ""

# Check if we're in the right directory
if [ ! -f "manuscript.tex" ]; then
    echo "❌ Error: manuscript.tex not found in current directory"
    exit 1
fi

echo "Step 1: Check LaTeX Installation"
echo "----------------------------------------------------------------------"
if command -v pdflatex &> /dev/null; then
    echo "✓ pdflatex found: $(pdflatex --version | head -1)"
else
    echo "⚠ pdflatex not found - install TeX Live or MacTeX"
    echo "  macOS: brew install --cask mactex"
    echo "  Linux: sudo apt-get install texlive-full"
fi
echo ""

echo "Step 2: Verify File Structure"
echo "----------------------------------------------------------------------"
echo "Checking manuscript files..."
[ -f "manuscript.tex" ] && echo "✓ manuscript.tex" || echo "❌ manuscript.tex missing"
[ -f "references.bib" ] && echo "✓ references.bib" || echo "⚠ references.bib missing (needs creation)"
echo ""

echo "Checking figure directory..."
if [ -d "../figures" ]; then
    echo "✓ figures/ directory exists"
    echo "  Expected figures:"
    for fig in figure1_tension_evolution.png figure2_error_budget.png \
               figure3_cchp_crossval_real.png figure4_h0_compilation.png \
               figure5_h6_fit.png; do
        if [ -f "../figures/$fig" ]; then
            echo "    ✓ $fig"
        else
            echo "    ⚠ $fig missing (placeholder needed)"
        fi
    done
else
    echo "⚠ figures/ directory missing"
fi
echo ""

echo "Checking table files..."
if [ -d "../data/tables" ]; then
    echo "✓ data/tables/ directory exists"
    echo "  Expected tables:"
    for tbl in table1_systematic_budget.tex table2_tension_evolution.tex \
               table3_h0_compilation.tex table4_cchp_crossval.tex; do
        if [ -f "../data/tables/$tbl" ]; then
            echo "    ✓ $tbl ($(wc -l < ../data/tables/$tbl) lines)"
        else
            echo "    ❌ $tbl missing"
        fi
    done
else
    echo "❌ data/tables/ directory missing"
fi
echo ""

echo "Step 3: Check for Undefined References"
echo "----------------------------------------------------------------------"
grep -n "\\\\ref{" manuscript.tex | head -20
echo "  (showing first 20 references...)"
echo ""

echo "Step 4: Verify Table Input Statements"
echo "----------------------------------------------------------------------"
grep -n "\\\\input{" manuscript.tex
echo ""

echo "Step 5: Check for Missing Citations"
echo "----------------------------------------------------------------------"
grep -n "\\\\cite" manuscript.tex | wc -l | xargs echo "Total citations found:"
echo ""

echo "======================================================================"
echo "RECOMMENDED NEXT STEPS:"
echo "======================================================================"
echo ""
echo "1. CREATE PLACEHOLDER FIGURES (if missing):"
echo "   cd ../figures && ./create_placeholders.sh"
echo ""
echo "2. FIX TABLE INPUT PATHS:"
echo "   Current: \\input{../data/tables/table1_h0_measurements.tex}"
echo "   Should be: \\input{../data/tables/table1_systematic_budget.tex}"
echo ""
echo "3. CREATE references.bib FILE"
echo ""
echo "4. TEST COMPILATION:"
echo "   pdflatex manuscript.tex"
echo "   bibtex manuscript"
echo "   pdflatex manuscript.tex"
echo "   pdflatex manuscript.tex"
echo ""
echo "5. USE OVERLEAF (RECOMMENDED FOR FIRST COMPILATION):"
echo "   - Upload manuscript.tex + figures + tables to Overleaf"
echo "   - Automatic compilation with error highlighting"
echo "   - No local LaTeX installation needed"
echo ""
echo "======================================================================"

