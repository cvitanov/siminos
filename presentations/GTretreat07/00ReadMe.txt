siminos/posters/00ReadMe.txt
$Author: siminos $ $Date: 2012-05-14 04:13:48 -0400 (Mon, 14 May 2012) $
-----------------------------------------------------------

To reproduce poster.pdf file (where 'poster' is 'GTretreat07', for example):

1. First latex poster.tex to produce all text in the poster separated in pages. Use:

 ./update

2. Split text.dvi to separate eps documents with dvi_split script:

 ./dvi_split

In figs/ directory we should now have text$i.eps files that contain text fragments.

3. Open xfig:

 xfig poster.fig &

4. Export the poster in pdf format using xfig menus.
