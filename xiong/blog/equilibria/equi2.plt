set terminal pdf color solid
set output "equi2.pdf"

set samples 100
set isosamples 100
unset key; 
unset surface
set view map
set pm3d at b

unset colorbox; 


set tics out; 

set multiplot layout 1,3  title "equibrium evolution"

set xrange [0:22]; 
set xlabel 'x';
set ylabel 't';

sp 'v1.txt' w l
sp 'v3.txt'  w l
sp 'v4.txt' w l


