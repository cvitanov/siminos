set terminal pdf color solid
set output "equi1.pdf"
set multiplot layout 1,3 title "equilibria"

unset key
set xlabel "x"
set ylabel "u"
set xrange [0:22]
set yrange [-0.1:0.1]
p 'equilibria.txt' u 1:2 w l


p 'equilibria.txt' u 1:4 w l


p 'equilibria.txt' u 1:5 w l

