siminos/xiong/matlab/00ReadMe.txt
$Author: predrag $
$Date:2010-04-21 18:36:47 -0400 (Wed, 21 Apr 2010) $
----------------------------------------------------------------------------

ks1025_le2_cv.m is my matlab code to calculate the Covariant 
Lyapunov Vectors ( Characteristic Vectors ? ).

avfe.mat is the matlab data file which stores local lyapunov 
exponents for orbit T10.25. To get lyapunov exponents, load the file 
in matlab and run "mean(avfe,2)".

cv.mat is the file for me to store the first fifteen 
Covariant Lyapunov Vectors. It has 1500 columns corresponding to
100 points on the orbit.
