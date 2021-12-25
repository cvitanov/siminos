siminos/williams/python/00ReadMe.txt
$Author: swilliams425 $
$Date:2010-04-21 18:36:47 -0400 (Wed, 21 Apr 2010) $
----------------------------------------------------------------------------

Sidney V.  Williams     sidneywilliams1231@gmail.com
        the newest code on top of this page

----------------------------------------------------
2021-05-17 relax/Orbit Jacobian.py
	This is the same code as relax, but with the 
	addition of scaling the orbits (introducing
	the change of variable phi=ax) and a function
	which takes a scaled orbit and gives you the
	orbit Jacobian, this function ONLY works for
	scaled cycles.
----------------------------------------------------
2021-03-16 relax/Henon.py
        python code that finds the periodic points of the
        Henon map, and the 2-cycle

If case=1
    * calculate the (non-Hamiltonian) Henon map's prime cycles
    * Cycle_length = length of the cycles to be found.
    * Tested, found accurate up to Cycle_length = 13.
If case=2
    * calculate the cycles, Fourier modes, and
      expanding eigenvalues of the Hamiltonian Henon map.
    * n is the length of prime cycle that will be calculated up to
      If n=6 all prime cycles of length 1-6 will be found and stored,
      and then the discrete Fourier transform of each cycle is taken.
    * n2 = cycle length that will be plotted,
    * mode = the Fourier mode to plot in the complex plane
      mode goes from 0 to n2-1.

----------------------------------------------------
2021-01-05 relax/relax1.py
        crude python code that can find the fixed points of the
        Henon map, and the 2-cycle

----------------------------------------------------
2021-01-05 siminos/williams/python/XXX.py
        blah blah
