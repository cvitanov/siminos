siminos/00ReadMe.txt
$Author: predrag $
$Date: 2021-06-22 07:48:14 -0400 (Tue, 22 Jun 2021) $
--------------------------------------------------------

Budanur, Ding, Gudorf, Liang, Siminos
thesis, publications and working notes
========================================================

bibtex/siminos.bib
	one bibliography for all projects
figs/
    one directory for thesis and blog figures .eps figures
    needed for compatibility with articles, ChaosBook.
    When creating a new version, please use the SAME name (so
    it propagates to publications etc. as well, without messing
    around with renaming it)
Fig/
    copied from ChaosBook.org (do not edit here)
figsSrc/
	one directory for source programs for all figures
	(or .txt files explain how to regenerate them if needed
     from the other repositories, with code)
inputs/
	one directory for all macros

blog/
    all general matters pertaining to symmetry reduction

presentations/
    most symmetry reduction talks and posters

han/
    Han Liang               thesis, project code, etc.
spatiotemp/blogCats.tex
    spatiotemporal cats, led by Han Liang
cats/GHJSC16.tex (published)
    Gutkin et al            spatiotemporal cat paper
kittens/CL18.tex
    Cvitanovic and Liang    spatiotemporal cat paper
reversal/LC21.tex
    Liang and Cvitanovic    temporal cat time reversal paper

spatiotemp/blog.tex
    spatiotemporal PDEs, led by Matt Gudorf
tiles/GC19.tex
    Gudorf and Cvitanovic   spatiotemporal KS paper
gudorf/
    Matt Gudorf thesis, presentations, etc
    2020-11-20 Matt has decided not to share
    anything here, so only he has the thesis, talks etc.
    [codes and data are in a separate repository gudorf]

xiong/
    Xiong Ding blog, thesis, etc
lyapunov/
    all matters pertaining to 'covariant Lyapunov vectors'
schur/DingCvit14.tex
    Ding and Cvitanovic (published)
dimension/DCTSCD14.tex
    Ding etal PR Lett (published)
cGL/
    all matters complex Ginzburg Landau
explosion/DingCvit16.tex    (unpublished)
    X. Ding and P. Cvitanovic cubic-quintic cGL
aETD/DingKang16.tex    (arXiv, but unpublished)
    X. Ding and S. H. Kang
ksRecycled/tex/BuDiCv15.tex (unpublished draft)
    Recycling Kuramoto-Sivashinsky
    Budanur, Ding and Cvitanovic

budanur/
    Nazmi Burak Budanur thesis, etc
slice/BudCvi14.tex
    Budanur Phys Rev Letter on 1. mode slice  (published)
ksReduced/
    Siminos, Budanur, Cvitanovi\'c and Davidchack (draft)
    "Kuramoto-Sivashinsky attractor revealed"
ksTorus/BudCvi15.tex  (published)
    Unstable manifolds of relative periodic orbits in
    the symmetry-reduced state space of the Kuramoto-Sivashinsky
    Budanur and Cvitanovic
see also
GitHub/reducesymm/cgang/2modes.tex
    BuBoCvSi14              (published)
    Budanur and Borrero-Echeverry and Cvitanovi{\'c}
    Periodic orbit analysis of a system with continuous symmetry
    - A tutorial

blog/marginal.tex & marginalAckn.tex
    The meaning of it all
    0.1 Predrag attempt to explain inertial manifold as nearly
        marginal, entangled modes           2013-08-08

ksConnected/
    ??

baroclinic/
    Annalisa Bracco, Cvitanovi\'c and Ortega blog

rpo_ks/current/
    Cvitanovi\'c, Davidchack and Siminos
    "State space geometry of a spatio-temporally chaotic
     Kuramoto-Sivashinsky flow" (published)

CLE/00ReadMe.txt
    Siminos and Cvitanovi\'c (published)
    "Continuous symmetry reduction
        and return maps for higher-dimensional flows"

atlas/atlas12.tex
    "High-dimensional cartography" (published)
    Cvitanovi{\'c}, Borrero-Echeverry, Carroll, Robbins, Siminos

thesis/
    Siminos thesis
WWW/
    (renamed so in Predrag's setup)
    Siminos home pages (tres elegantes)
	repository siminoswww
CV/
	Siminos CV
jobs/
	Siminos jobs
    [codes and data are in repository vaggelis]
conf/
    organization of Siminos conferences

tex/
	customized tex and bibtex style files

scripts/
    potentially useful scripts

kazz/
    Kazumasa A Takeuchi KS code, data

froehlich/slice/FrCv11  (published)
    Stefan Froehlich blog, papers

chao/
    Chao Shi's blog (abandoned)

---------------------------------------------------------------
TO FIX:

---------------------------------------------------------------
NOTES:

-- maths classification for a paper about Lorenz system:
   MSC: Primary: 37C45, 37D40; Secondary: 37D45


Time stamp:
----------

To have svn time-stamp file "someFile.type", include the contents of
	thesis/chapter/svnHeader.txt
into the file, and then
	svn propset svn:keywords "Date Author" someFile.type

----------------------------------------------------------------
HISTORY:
						Predrag Jul 26 2008
    created this file

2ChaosBook/2CB.tex (eliminated)
    was one of staging grounds for insertions to ChaosBook.org

----------------------------------------------------------------
FIXED:
						Evangelos Dec 4 2010	
	emaildict for correct reply-to address

-- made ...
