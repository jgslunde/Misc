all: LatexNotes.pdf    #reference to pdf-file
LatexNotes.pdf: LatexNotes.tex cites.bib    #depedency files
	latexmk -pdf LatexNotes    #compiling
show: LatexNotes.pdf    #shows pdf-file
	evince LatexNotes.pdf &    #evince = pdf-reader
clean:
	latexmk -c    #
	rm *.bbl *.run.xml    #
