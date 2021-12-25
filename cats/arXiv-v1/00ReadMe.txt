siminos/cats/arXiv-v1/00ReadMe.txt
$Author: predrag $
$Date: 2019-12-13 00:18:02 -0500 (Fri, 13 Dec 2019) $
===========================================================
		    arXiv-v1 submission:   Dec 9 2019

++++++ FROZEN - DO NOT CHANGE THIS zip FILE +++++++++++++++
       siminos/cats/arXiv-v1/GHJSC16.zip

================================
"Linear encoding of the spatiotemporal cat"

Boris Gutkin,
Li Han,
Rana Jafari,
Adrien K. Saremi,
         and
Predrag Cvitanovic

===== HISTORY  ==========================================
                        (newest on the top)

Predrag ver. 1.0                                    Dec 9 2019

arXiv submission notes
----------------------

predrag H.......s

arXiv identifier: 1912.02940
The paper password for this article is: zxswt
Please share this with your co-authors. They may use it to claim ownership.

you might want to add your orcid ID to your arXiv account
    and this paper

MSC class: (http://www.ams.org/msc/)
    28D05; Measure-preserving transformations
    60J10; Markov chains
    70K43; Quasi-periodic motions and invariant tori
    70S05; Lagrangian formalism and Hamiltonian formalism
    76F20; Dynamical systems approach to turbulence
    82C20; Dynamic lattice systems
----------------------------------------------------------------------

submission notes
---------------------
                                                     2019-12-05
Error # 2
=========
! LaTeX Error: Option clash for package hyperref.

Package biblatex Warning: File 'GHJSC16.bbl' is wrong format version
    - expected 2.8.
GHJSC16.bbl says: $ biblatex bbl format version 3.0 $
zero.gatech says: $ biblatex version 2.3 $

https://github.com/plk/biblatex/wiki/biblatex-and-the-arXiv
    "At the moment the arXiv runs biblatex 3.7, which expects .bbl
    file version 2.8. That means that the .bbl file you upload
    should be produced by biblatex 3.7 and Biber 2.7 (biblatex 3.5
    or 3.6 with Biber 2.6 would also be OK). So the only way to
    satisfy the arXiv is to obtain those biblatex and Biber
    versions and run your document with them."

    "As far as biblatex and Biber are concerned the best fit for
    that task is an un-updated TeX live 2017 installation."

current zero.physics /usr/share/texlive/release-texlive.txt
is "TeX Live version 2013", W10 has "TeX Live version 2019"

on Matt's light.physics.gatech.edu, installed
ftp://tug.org/texlive/historic/2017/texlive2017-20170524.iso
www.cyberciti.biz/tips/how-to-mount-iso-image-under-linux.html
	mkdir /mnt/iso ; cd /mnt/iso/ ; ./install-tl
	sudo umount /mnt/iso/
results in
 	/usr/local/texlive/2017/index.html
Possibly add /usr/local/texlive/2017/texmf-dist/doc/man  to MANPATH.
             /usr/local/texlive/2017/texmf-dist/doc/info to INFOPATH.
Possibly add /usr/local/texlive/2017/bin/x86_64-linux
    to your PATH for current and future sessions.

without paths:
    /usr/local/texlive/2017/bin/x86_64-linux/pdflatex,  etc.
now have $ biblatex version 2.3 $
arXiv works!
    arXiv:submit/2959328  [nlin.CD]  6 Dec 2019


Error # 1
=========
! Package pdftex.def Error: PDF mode expected, but DVI mode detected!
(pdftex.def) If you are using `latex', then call `pdflatex'.
    FIXED: \usepackage[pdftex]{graphicx} -> \usepackage{graphicx}

[verbose]: tex 'GHJSC16.tex' failed.
[verbose]: TEXMFCNF is unset.
[verbose]: ~~~~~~~~~~~ Running tex for the first time ~~~~~~~~
[verbose]: Running: "(export HOME=/tmp PATH=/texlive/2016/bin/arch:/bin; cd /submissions/2958781/ && tex 'GHJSC16.tex' < /dev/null)" 2>&1
[verbose]: This is TeX, Version 3.14159265 (TeX Live 2016) (preloaded format=tex)
(./GHJSC16.tex
! Undefined control sequence.
l.8 \documentclass
[12pt]{iopart}
?
! Emergency stop.
l.8 \documentclass
[12pt]{iopart}


--------------------------------------------------------------------

    * biblatex.tex  'firstinits'  is deprecated; so now 'giveninits'
    * removed all \ifboyscout  \ifsubmission



Figures:
========
SingleCatMultiSymbol.pdf
BorisCatRegion1.pdf
BorisCatRegion2.pdf
BorisCatRegion3.pdf
BorisCatRegion4.pdf
BorisCatRegion5.pdf
rectangular_domain.pdf
symbol_block_one.pdf
symbol_block.pdf
RJsymbol-a.pdf
RJsymbol-b.pdf
RJsymbol-c.pdf
RJsymbol-d.pdf
AKSs7BlockBorderM1.pdf
AKSs7BlockBorderM2.pdf
AKSLPS12.pdf
AKSLPS12_1.pdf
AKSs13TwoBlocksM2.pdf
AKSs13TwoBlocksG1.pdf
AKSs13TwoBlocksG2.pdf
AKSs7ThreeDiamondsM1.pdf
AKSs7ThreeDiamondsM2.pdf
AKSs7ThreeDiamondsM3.pdf
AKSs7ThreeDiamondsG1.pdf
AKSs7ThreeDiamondsG2.pdf
RJentropy_s3_s4.png
