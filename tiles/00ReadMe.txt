siminos/tiles/00ReadMe.txt  cd ../current/ pdflatex GuBuCv17; bibtex GuBuCv17
$Author: predrag $ $Date: 2020-05-07 17:34:06 -0400 (Thu, 07 May 2020) $
===========================================================
Matthew N. Gudorf and Predrag Cvitanovi\'c
"Spatiotemporal tiling of the Kuramoto-Sivashinsky flow"

                    started writing:    Predrag    Mar 12 2019
                    final submission:   Matthew    ??? ?? 2020
		            accepted:                      ??? ?? 2020	

SIADS manuscript #??
arXiv.org/abs/20??.????
web, BibTex name:      GuBuCv17.pdf  \cite{GuBuCv17}


\HREF{https://doi.org/10.????/????-????/??????}{DOI}

ORCID iDs
P Cvitanovi{\'c}    https://orcid.org/0000-0001-6169-0509

====== Editing =================================================

    currently, edit the article inserts by running
siminos/spatiotemp/blog.tex  pdflatex blog; biber blog
    to see how the article looks like,
    make sure that you are in siminos/tiles/current/, then
pdflatex GuBuCv17; bibtex GuBuCv17; pdflatex GuBuCv17
    on linux (after editing the file update) run
> ./update

    for time being, the text to finalize is almost all in
siminos/spatiotemp/chapter/*.tex
    the old SCD07 article files in
siminos/tiles/current/*.tex
    are temporary, to be used for clip & paste

====== History    =========================================

    siminos/tiles/SIADS-v?/ contains the final version
    siminos/tiles/SIADS-v?/reviews ?. round of referee edits

arXiv:20??.???? (revised v3):                    5 ??? 2020
    siminos/tiles/arxiv-v3/ contains the final version
                             low resolution figs

arXiv:20??.???? (revised v2):                   11 ??? 2020
    siminos/tiles/arxiv-v2/

arXiv:20??.???? (submitted v1):                 19 ??? 2020
    siminos/tiles/arxiv-v1/

Matt using Predrag's whiteboard outline         Feb 28 2020
    outline = \Preliminary{*section{...}}

Predrag                                         Mar 12 2019
starting template is article bibID SCD07, arXiv.org/abs/0709.????
    siminos/rpo_ks/current/GuBuCv17.tex

====== Working titles =====================================

                                                Mar 15 2019
"Topology of a spatio-temporally chaotic Kuramoto-Sivashinsky system"
                                                Sep 15 2018
"Is space time? {A} spatiotemporal theory of transitional turbulence"
                                                Mar 15 2018
"Spatiotemporal tiling of the Kuramoto-Sivashinsky flow"
                                                Mar 10 2007
"On the state space geometry of
the Kuramoto-Sivashinsky flow in a spatiotemporally periodic  domain"

====== Submission   =========================================

=== submit arXiv - see arxiv-v1/00ReadMe.txt or below
    [ ] check here when done, enter date: Sept 19 2019


=== submit SIADS  - see SIADS-v?/00ReadMe.txt or below
    [ ] check here when done, enter date: Sept ? 2019

    SIAM Journal on Applied Dynamical Systems
    www.siam.org/journals/siads.php
    epubs.siam.org/SIADS

====== arXiv submission notes ==============================

submit arXiv
    arXiv article-id:       1909.????
    Article password: ????
    http://arxiv.org/abs/1909.????
    [ ] check here when done, enter date: Sept 18 2019

    add comment about high-resolution link at
    http://ChaosBook.org/~predrag/papers/preprints.html#GuBuCv17

PACS replaced by AMS codes pacs-ams.txt
35B05, 35B10, 37L05, 37L20, 76F20, 65H10, 90C53
    [ ] AMS codes rechecked, GNM Sept 18 2019

incorporated upload.tex into GuBuCv17.tex
    [ ] mark here when done

remove all footnotes and "edits" from the submission copy
    [ ] mark here when done

remove all % commented and incriminating text from the submission copy
    [ ] mark here when done

remove extraneous macros from defs.tex before submission
    [ ] mark here when done

svn rm  [all unused *.tex and other files]
    [ ] mark here when done

svn rm  [all unused figures and all *.pdf]
    [ ] mark here when done

Set bibstyle to alphabetical order, temporarily,
        and check for double entries.
    [ ] mark here when done

does SIAD want spaces between the initials?
PC fixed that once by using   bibclean fluid.bib; redo:
    [ ] mark here when done

do not submit a *.bib file, submit GuBuCv17.bbl.
    [ ] mark here when done

Consistent use of $\ldots$, (I)/(a)/(1)/itemize, others?
    [ ] mark here when done

    [ ] PostScript figures generated with sufficient
       line thickness?
	ES: Cannot find any specific instructions

svn copy all used and cleaned-up source files and figs from
current/tiles/figs to  arxiv-v1/
    [ ] mark here when done

submit to arXiv.org
    [ ] created GuBuCv17.tex for arXiv submission
    arxiv-v1/*.tex *.bst *.cls figs/*.pdf GuBuCv17.bbl
    [ ] 2019-09-?? mark here and date when done


!!! then DO NOT TOUCH arxiv-v1/* again, do all edits in tiles/current/

====== submission SIADS ====================================

see SIADS/00ReadMe.txt
    SIAM Journal on Applied Dynamical Systems
    www.siam.org/journals/siads.php
    epubs.siam.org/SIADS
    https://siads.siam.org/cgi-bin/main.plex?form_type=display_auth_instructions

Authors submitting papers to SIAM journals can log in to the
submission system through their ORCID account
        https://orcid.org/signin
        Predrag:    0000-0001-6169-0509 or
        predrag.cvitanovic@physics.gatech.edu
        passwd: i.........)                         2019-03-16

If the paper is published, SIAM Journals Online will display an
icon next to the author’s name which links to their ORCID page,
which can in turn list their published article.
ORCID’s capability is a DOI for an individual. Wherever it is used,
this unique identifier then pulls together the individual’s work
and professional activities from across publications, disciplines
and workplaces. The researcher controls, through her ORCID account,
which work and activities are publicly displayed.

editor: Dwight Barkley
        http://homepages.warwick.ac.uk/~masax/
    [ ] mark when read submission instructions,
        entered relevant notes here or into SIADS-v1/00ReadMe.txt

move all source files and figs from tiles/current/ to SIADS-v?/
    [ ] mark here when done

when submitting SIADS  prepare double spaced pdf
    [ ] mark here when done

Revisions SIADS-v?; when referees incorporated,
update arXiv.org with the revised version
    [ ] mark here when done
    [ ] mark final, revised submission, date:


====== Preparation of figures ===============================

SIAD style files: reformatted using SIAM macros
    www.siam.org/journals/auth-info.php
    [ ] mark here when done: Predrag Mar 10 2019


====== NOTES ================================================
                    Predrag Mar 10 2019
reformatted using SIAM macros
    www.siam.org/journals/auth-info.php
    downloaded siamonline_181217.zip                Mar 16 2019

check http://arxiv.org/hypertex/bibstyles/ for hyperref compatible
BiBTeX styles


When submitting, remember to
    1) Submit GuBuCv17.bbl file.
    2) All pdf/png figures should be sent in separate files.
    3) pdf figures should be generated with sufficient line thickness.


====== Fix these ============================================


==============================================================
FORMERLY OUTSTANDING ITEMS, NOW DISPOSED OFF:

= DONE:
= DONE:
