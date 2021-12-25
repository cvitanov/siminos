siminos/kittens/00ReadMe.txt
$Author: predrag $
$Date: 2019-01-09 08:42:06 -0500 (Wed, 09 Jan 2019) $
------------------------------------------------------------

siminos/kittens/CL18.tex
========================
    Spatiotemporal cat: an exact classical field theory

Predrag Cvitanovi{\'c}
         and
Han Liang

===== PRESENTATION  =====================================
    siminos/presentations/kittens/kittens.tex

===== HISTORY  ==========================================
                        (newest on the top)
Old working titles
------------------
{Spatiotemporal cat map: an exact classical field theory} %PC 2018-03-23
[Cats can do]{Is there anything cats cannot do?} % PC 2018-02-12
{A spatiotemporal herding of coupled lattice cats}
{Linear encoding of cat map lattices}
{A \catlatt\ encoded} %PC 2016-11-27
{A spatiotemporal code for a coupled maps lattice} %PC 2016-11-27
{A spatiotemporal symbolic dynamics for a coupled maps lattice} %PC 2016-11-27
{A spatiotemporal symbolic dynamics for a coupled cat maps lattice} %PC 2016-11-14
{A linear symbolic dynamics for coupled cat maps lattices}

Predrag ver. 0.1                                    Mar 14 2018
    forked off siminos/cats/GHJSC16.tex
    ioppublishing.org/img/landingPages/guidelines-and-policies/
    fetched ioplatexguidelines.tar.gz

===== FOLDERS  ==========================================

- ../figs/
    all figs
- ../figsSrc/
    all fig source programs
- ../bibtex/siminos.bib
    the one and only BibTeX data base

===== NOTES     ==========================================
    check and enter date when done:

[ ] DateHere RECHECK pacs!
[ ] DateHere spellChecked (UK spelling is required!)

[ ] there is an incompatibility between amsmath.sty and iopart.cls
    which cannot be completely worked around. If your article
    relies on commands in amsmath.sty that are not available in
    iopart.cls, you may wish to consider using a different class
    file.

===== SUBMISSIONS  =======================================

arXiv submission (here for future use)
================
arXiv-v1/
arxiv article-id:       1601.????                   DateHere
     details: enter them here

Nonlinearity submission
=======================
nonlin-v1/
Nonlinearity article-id:      ????                  DateHere
     details: enter them here:
Submissions via the ScholarOne
    [ ] submit a new article: only a PDF
    [ ] a revised version: submit the source files
        [ ] indicate: the `master' LaTeX file is GHJSC16.tex
        [ ] do not read in files from a different:
            store submitted files all together in a single
            directory with no subdirectories.
        [ ] include the XXX.bib file
        [ ] include the XXX.bst
        [x] At the start of the `master' LaTeX file
            identify the journal, author, and (if a revised version)
            the reference number given to the submission.
        [ ] The first letter of the title capitalized, rest lower case
        [ ] abstract: a single paragraph of around 200 words
        [ ] PACS finalized? www.aip.org/pacs
        [ ] Keywords are required, min 3 (max 7)
        [ ] Caption comes before the table, with a period at the end.
        [ ] include Supplementary Data?

    [ ] use \LaTeX\ default Computer Modern fonts, avoid
        packages that change the standard \LaTeX\ fonts.
        AMSTeX is acceptable.
        (published articles use fonts in the Times family)
    [ ] PDF or bitmap figures: PDF version 1.4 or lower
        You can do this by putting \pdfminorversion=4
        at the very start of your TeX file
    [ ] Naming figure files: give each figure file a name which
        indicates the number of the figure it contains;
        figure1.pdf, figure2a.png, etc. If the figure file contains
        a figure with multiple parts, for example figure 2(a) to
        2(e), give it a name such as figure2a_2e.pdfe.





===========================================================
Processing
==========

make sure that you are in repository siminos/kittens/
    then:
./update   (on linux)
    or
pdflatex main; bibtex GHJSC16; pdflatex GHJSC16; pdflatex GHJSC16

Things to fix
=============
    [when fixed, move the line to the FIXED section at the end]

= see 00edits.txt

==============================================================
FORMERLY OUTSTANDING ITEMS, NOW DISPOSED OFF:

    XXX[to be renamed]XXXXXXX

[x] iopart.cls class file etc are on ftp://ftp.iop.org/pub/journals/
