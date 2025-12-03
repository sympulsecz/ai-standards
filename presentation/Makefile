# Makefile for LaTeX presentation
# Usage: make        # Compile the presentation
#        make clean  # Remove auxiliary files
#        make view   # Open the PDF (macOS)

.PHONY: all clean view help

# Main target
all: presentation.pdf

# Compile the presentation (run twice for TOC and references)
presentation.pdf: presentation.tex
	/Library/TeX/texbin/pdflatex -interaction=nonstopmode presentation.tex
	/Library/TeX/texbin/pdflatex -interaction=nonstopmode presentation.tex

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb missfont.log

# Clean everything including PDF
cleanall: clean
	rm -f presentation.pdf

# View the PDF (macOS)
view: presentation.pdf
	open presentation.pdf

# Display help
help:
	@echo "Available targets:"
	@echo "  make          - Compile the presentation"
	@echo "  make clean    - Remove auxiliary files"
	@echo "  make cleanall - Remove all generated files including PDF"
	@echo "  make view     - Open the PDF (macOS)"
	@echo "  make help     - Display this help message"
