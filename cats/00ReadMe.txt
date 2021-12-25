siminos/cats/00ReadMe.txt
$Author: predrag $
$Date: 2021-02-26 22:57:30 -0500 (Fri, 26 Feb 2021) $
------------------------------------------------------------

siminos/cats/GHJSC16.tex
========================

"Linear encoding of the spatiotemporal cat"

Boris Gutkin,
Predrag Cvitanovi{\'c}
Rana Jafari,
Adrien K. Saremi,
         and
Li Han,

\HREF{https://doi.org/10.1088/????-????/??????}{DOI}

ORCID iDs
P Cvitanovi{\'c}    https://orcid.org/0000-0001-6169-0509
L Han               https://orcid.org/0000-0001-7181-8166
R Jafari            https://orcid.org/0000-0001-7360-5527	(?)
A Saremi            https://orcid.org/0000-0003-1142-8478

Nonlinearity emails:
boris.gutkin@uni-due.de
rjafari7@gatech.edu
asaremi3@gatech.edu
hanli@gatech.edu


===== HISTORY  ==========================================
                        (newest on the top)

Predrag ver. 2.0                                    Nov 18 2020
Boris   ver. 2.0                                    Oct 16 2020
Predrag ver. 1.0                                    Oct 30 2019
Predrag ver. 0.1                                    Aug 20 2016
    ioppublishing.org/img/landingPages/guidelines-and-policies/
    fetched ioplatexguidelines.tar.gz

siminos/cats/05figs.txt
    list of figures

===== FOLDERS  ==========================================

- ../figs/
    all figs
- ../figsSrc/
    all fig source programs
- ../bibtex/siminos.bib
    the one and only BibTeX data base

===== NOTES     ==========================================
    check and enter date when done:

[x] Feb 26 2021 Mathematics Subject Classification
    37-	Dynamical systems and ergodic theory
        37K60, 37L60   	Lattice dynamics; integrable lattice equations
        37L60           Uniformly hyperbolic systems (expanding, Anosov, Axiom A, etc.)
        37D45           Strange attractors, chaotic dynamics of systems with hyperbolic behavior
        82B20   	    Lattice systems (Ising, dimer, Potts, etc.) and systems on graphs arising in equilibrium statistical mechanics
        39A23   	    Periodic solutions of difference equations
        82M20   	    Finite difference methods applied to problems in statistical mechanics
        37K60, 37L60, 37L60, 37D45, 82B20, 39A23, 82M20

[X] Dec 9 2019 RECHECK pacs!
[ ] DateHere spellChecked (UK spelling is required!)

[ ] there is an incompatibility between amsmath.sty and iopart.cls
    which cannot be completely worked around. If your article
    relies on commands in amsmath.sty that are not available in
    iopart.cls, you may wish to consider using a different class
    file.

===== SUBMISSIONS  =======================================

arXiv submission
================
arXiv-v1/GHJSC16.zip
arxiv article-id:       1912.02940                   Dec 9 2019
     details: enter them in siminos/cats/arXiv-v1/00ReadMe.txt

arXiv update v2
================
arXiv-v2/GHJSC16.zip
arxiv article-id:       1912.02940                   Nov 17 2020
     details: enter them in siminos/cats/arXiv-v2/00ReadMe.txt

Nonlinearity submission
=======================
nonlin-v1/
Nonlinearity Manuscript ID: NON-104197,         now NON-104197.R1
Date Submitted                                      Dec 29 2019
    As the submitting author, follow the article on Author Centre
    https://mc04.manuscriptcentral.com/non
    Editor-in-Chief: Tasso Kaper and Carlangelo Liverani

    [details - enter them here:]
    https://mc04.manuscriptcentral.com/non or orcid.org
    predrag.cvitanovic@physics.gatech.edu   9..........e!
    [x] submit a new article: only a PDF
        [x] PACS finalized - www.aip.org/pacs
        [x] The first letter of the title capitalized, rest lower case
        [x] abstract: a single paragraph of around 200 words
        [x] Keywords are required, min 3 (max 7)
    [x] 2 referee reports received                  Sep 21 2020
        [x] in cats/nonlin-v1/reviews/

nonlin-v2/                                          NON-104197.R1
    [x] revised version:                            Nov 18 2020
        [x] submitted GHJSC16_highlight.pdf
        [x] to editor: response-v1.pdf
        [x] to referees: response1-v1.pdf response2-v1.pdf
            [x] reupload response*-v1.pdf renamed response*-v2.pdf
        [x] saved their numbered proof GHJSC16Proof.pdf
        [x] saved their numbered proof NON-104197.R1_Proof_hi.pdf
            includes referee responses (not the letter to the editor),
            GHJSC16_highlight.pdf, renamed it GHJSC16Proof.pdf
    [x] submit the source files through arXiv-v2
        [x] indicate: the `master' LaTeX file is GHJSC16.tex
        [x] do not read in files from a different:
            store submitted files all together in a single
            directory with no subdirectories.
        [x] include the GHJSC16.bib file
        [x] include the XXX.bst
        [x] At the start of the `master' LaTeX file
            identify the journal, author, and (if a revised version)
            the reference number given to the submission.
        [ ] Caption comes before the table, with a period at the end.
        [ ] include Supplementary Data?

==== Ignored the rest===========================

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

make sure that you are in repository siminos/cats/
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
