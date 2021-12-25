siminos/gudorf/thesis/notes00ReadMe.txt $Author: predrag $ $Date:
2017-02-22 22:28:53 -0500 (Wed, 22 Feb 2017) $
---------------------------------------------------------------

Matt Gudorf
===========================================================

----------      			                             July 3 2018
Processing of eps figures with mathematica [and other] fonts

PROBLEM:
> dvips rpo
dvips: Font Mathematica1Mono used in file figs/rpo22-55-4.eps is not in the mapping file.
dvips: Font Mathematica2Mono used in file figs/rpo22-55-4.eps is not in the mapping file.

SOLUTION:

./removecache.sh rpo22-55-4.eps rpo22-55-4-clean.eps

Mathematica uses its own fonts for any mathematical symbol, even + and -.
Script removecache.sh fixes the problem by converting the fonts to curves.
The resulting figure is much smaller

> ls -s
168 rpo22-55-4.eps
 40 rpo22-55-4-clean.eps

but have to inspect it - fonts do look different. Also
it destroys some pictures.  Use it with caution. The script is just one
line but I have no idea what it exactly does!
