siminos/schur/SIAM-v1/00ReadMe.txt
$Author: predrag $
$Date: 2016-03-05 21:17:58 -0500 (Sat, 05 Mar 2016) $
===========================================================
Journal:  SIAM Journal on Numerical Analysis
          SINUM manuscript #097596
                    rejected by editor               Sep 22 2014
               SIAM-v1 submission: #1   Xiong Ding   Jul 03 2014
                    finished writing:   Predrag      May 24 2014
                    started writing:    Xiong Ding   Feb 21 2014

Periodic eigendecomposition and its application to
Kuramoto-Sivashinsky system

Xiong Ding, Predrag Cvitanovi\'c
-----------------------------------------------------------

arXiv submission notes
----------------------
----------------------
SIAM-v1 is submitted on July 03 2014.
SIAM-v1.tar.gz contains all the file related to this submission.
Only DingCvit14.pdf and coverLetter.pdf are uploaded.



1) Information gathered when submitting:

Title: Periodic eigendecomposition and its application
        to Kuramoto-Sivashinsky system

Running Tile: PERIODIC EIGENDECOMPOSITION

2) Editorial Policy compliance statement

   *1. What is the decisive advance in this paper in the
    design and/or analysis of a numerical method or class of methods?

    Periodic Schur decomposition is capable obtaining all the
    eigenvalues of a product of a sequence of matrices, but the
    eigenvector algorithm receives little attention then. On the
    other hand, forward iteration followed by backward iteration is
    used for a few years to calculate covariant vectors in an
    ergodic system, which is indeed not efficient for periodic
    orbits. So in this manuscript, I introduce periodic
    eigendecomposition, extened from periodic Schur decomposition,
    and point out its efficiency and the ability to resolve complex
    eigenvector pairs, compared with existing algorithms. Finally,
    an example is used to illustrate its effectiveness.
	
   *2. Why is the method or class of methods considered in the paper
   of significant and broad interest to the readers of SINUM?

   This algorithm is a general to calculate eigenvalues and
   eigenvectors of the product of a sequence of matrices. It could
   be applied to nonlinear dynamics where covariant vectors serve
   as an important tool to visualize the attractor structure in a
   chaotic system. Also some investigations in atmospheric sciences
   and geophysics demand good algorithms for the accurate
   computation of Floquet vectors.

----------------------------------
submission confirmation         Jul 7, 2014

From: sinum@siam.org

Dear Xiong Ding,

Thank you for submitting "Periodic eigendecomposition and its
application to Kuramoto-Sivashinsky system." Your paper has been
assigned MS#097596.

You can check on the status of the paper by logging in at
http://sinum.siam.org and following the live manuscripts link.

You will receive notice after the review process has been
completed. You can send inquiries to sinum@siam.org at any time.
It's helpful if you refer to your paper by title, by the manuscript
number, and by your name.

The authors listed for your submission are Xiong Ding and Predrag Cvitanovi\'{c}, and as
Corresponding Author you represent that any and all co-authors are
aware of and agree with this submission. The Editor-in-Chief has
been notified of your submission and all further correspondence
will be sent only to you as the Corresponding Author.

We are including additional information below that we encourage you
keep on hand as reference. Please do not hesitate to write if you
have any questions.

Heather Blythe
Senior Publications Coordinator
SIAM
E-mail: blythe@siam.org
Phone: 215-382-9800, ext. 352
Fax: 215-386-7999

---------------------

see SINUM online instructions:

Style of articles:

      1) written to be accessible to a broad scientific audience.
      2) a clear physical motivation, and the results should enhance
      	 fundamental understanding of the underlying scientific problem.
      3) must contain substantially new results and relate them to existing
      	  literature in other disciplines.
      4) sufficient introductory material.
      5) introduction and conclusion sections summarize and explain the
      	  results comprehensively to readers in other disciplines.
      6) the scientific importance of the paper and its conclusion should
      	 be made clear.
      7) minimize the use of technical jargon from their subfield.

    [X] prepare coverLetter.tex


register as a SIAM journal author
    [X] mark here when done

copy all source files and figs from schur/ to schur/SIAM-v1
    [X] mark here when done [Xiong Ding July 03 2014]

recheck Pacs codes
    [ ] Pacs codes rechecked    [Predrag May 24 2014]
    Xiong: I don't know what it is.

remove all % commented and incriminating text from the submission copy
    [ ] mark here when done

??.bst as the bibliographic,  hyperref version, with eprint
    [ ] mark here when done

at submission DO NOT generate pruned file #.bib
    [ ] slice.bbl added to repository
       (we didn't submit source yet
        and didn't need to touch bibliography at all)

does SIAM want spaces between the initials? PC fixed that once by
using bibclean fluid.bib; redo:
    [ ] mark here when done

Consistent use of $\ldots$, (I)/(a)/(1)/itemize, others?
    [ ] mark here when done

Revisions SIAM; when referees incorporated, update arXiv.org with
the revised version
    [ ] mark here when done
    [ ] mark final, revised submission, date:

submit to SIAM
    [ ] created rpo.tex for SIAM submission
    arxiv-v?/*.tex *.bst *.cls figs/*.eps rpo.bbl [or rpo.bib]
    [ ] 2008-10-17 mark here and date when done


!!! then DO NOT TOUCH SIAM-v1/* again, edit only slice/*
===============================================================

NOTES
-----

Preparation of figures
----------------------

Fix these:
----------

==============================================================
FORMERLY OUTSTANDING ITEMS, NOW DISPOSED OFF:

= DONE:

SIAM style files: reformatted using APS macros
    [ ] mark here when done [Predrag  Jan  5 2014]
