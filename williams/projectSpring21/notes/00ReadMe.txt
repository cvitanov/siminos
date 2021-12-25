siminos/chen/projectFall17/notes/00ReadMe.txt
$Author: predrag $ $Date: 2021-01-22 16:12:00 -0500 (Fri, 22 Jan 2021) $
-----------------------------------------------------------------

	Andy Chen project Fall 2017

===========================================================

----------
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
