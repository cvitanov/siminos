siminos/reversal/00ReadMe.txt
$Author: predrag $
$Date: 2021-07-21 14:06:30 -0400 (Wed, 21 Jul 2021) $
------------------------------------------------------------

siminos/reversal/LC21.tex
========================
    Time reversal for discrete time dynamical systems

Han Liang
         and
Predrag Cvitanovi{\'c}

===== PRESENTATION (to be prepared) ==================================
    siminos/presentations/kittens/reversal.tex

===== HISTORY  ==========================================
                        (newest LC21 on the top)
Old working titles
------------------
{Temporal cat's miaw} %PC 21 Jul 2021

Predrag ver. 0.1                                    21 Jul 2021
    forked off siminos/kittens/CL18.tex
iopscience.iop.org/journal/1751-8121/page/advances-in-quantum-chaos-random-matrix-theory-and-the-semiclassical-limit-in-memory-of-fritz-haake
The issue will be published incrementally, whereby articles will be
published as soon as they are ready. Earlier submissions are
welcome and your article will not be delayed by waiting for other
papers in the collection.

publishingsupport.iopscience.iop.org/authoring-for-journals/writing-journal-article/
    fetched ioplatexguidelines
publishingsupport.iopscience.iop.org/wp-content/uploads/2017/10/ioplatexguidelines.zip

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

jphysa submission
=======================

jphysa-v1/
jphysa article-id:      ????                  DateHere
     details: enter them here:
Submissions via the https://mc04.manuscriptcentral.com/jphysa-iop
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
    [ ] vector graphics gives the best possible quality at all
        output resolutions. Fonts used should be restricted to the
        standard font families (Times, Helvetica, Courier or
        Symbol)
    [ ] Naming figure files: give each figure file a name which
        indicates the number of the figure it contains;
        figure1.pdf, figure2a.png, etc. If the figure file contains
        a figure with multiple parts, for example figure 2(a) to
        2(e), give it a name such as figure2a_2e.pdfe.





===========================================================
Processing
==========

make sure that you are in repository siminos/reversal/
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
