# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:47:22 2021

@author: Sidney Williams
"""
#Instructions: If case=1 calculate the non-Hamiltonian Henon map's prime cycles
#If case=2 calculate the cycles, fourier modes, and expanding eigenvalues of the
#Hamiltonian Henon map. For case=1 Cycle_length sets the length of the cycle 
#that will be found. It has been tested, and found accurate up to cycle length
#13. For case=2, n is the length of prime cycle that will be calculated up to
#If n=6 all prime cycles of length 1-6 will be found and stored, and then the
#discrete Fourier transform of each cycle is taken. n2 Is the cycle lenth that
#will be plotted, mode is the Fourier mode that will be plotted in the complex
#plane, mode goes from 0 to n2-1.
#The Orbit Jacobian function only works for scaled orbits, so make sure to use
#One of the scaled cycles 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from numpy.random import rand
from json import dumps
from IPython.display import display, Math
from itertools import product

case=2

class Henon:
    def __init__(self, x_n=None, sigma=None, cycle_length=2, a=1.4, b=0.3):
        """
        initialization function which will be called every time you
        create an object instance. self.XXXX = VAL assigns the value VAL to the attribute XXXX
        Examples
        --------
        >>> self.XXXX = 0
        >>> print(self.XXXX)
        0
        """
        self.a = a
        self.b = b
        self.sigma = sigma
        self.cycle_length = cycle_length
        # If you do not provide an initial x_n, simply take the "zeros" guess. 
        # This is the new container for "guess trajectory" and can be accessed

        if x_n is None:
            self.x_n = np.zeros(cycle_length)
        else:
            self.x_n = x_n
            
        if sigma is None:
            sigma_array = np.empty(self.cycle_length)
            sigma_array[::2] = 1
            sigma_array[1::2] = -1
            self.sigma=sigma_array
        else:
            self.sigma=sigma
    
    # memory not an issue, would want to be careful with having multiple states in memory otherwise.
    @property
    def x_n_plus_1(self):
        """ Explicit notation for the rotated vector
        """
        return np.roll(self.x_n, -1)
        
    # memory not an issue, would want to be careful with having multiple states in memory otherwise.
    @property
    def x_n_minus_1(self):
        """ Explicit notation for the rotated vector
        """
        return np.roll(self.x_n, 1)
        
    # Avoid the usage of "iter" as it means something specific in python
    def deviation(self):
        """ Return the vector of deviations (v_i from chaosbook) 
        """
        # Compute vi and return vector. 
        # vi = x_{n+1} - (1 + ax_n^2 - bx_{n-1})
        return self.x_n_plus_1 - 1 + self.a * self.x_n**2 - self.b * self.x_n_minus_1
    def residual(self):
        """ The norm of the deviation; only useful if fictitious flow is monotonic.
        """
        # The norm of vi
        return np.linalg.norm(self.deviation())
    
    def plot(self):
        """Line plot of the current state
        """
        plt.plot(np.arange(self.cycle_length), self.x_n, linestyle='--', marker='o')
        y = np.abs([self.x_n.min(), self.x_n.max()]).max()
        plt.ylim([-y-0.1, y+0.1])
        plt.grid(True)
        # make the y ticks integers, not floats
        xint = []
        locs, labels = plt.xticks()
        for each in locs:
            xint.append(int(each))
        plt.xticks(xint)
        plt.show()
    
def sigma_generator(cycle_length):
    """ Generates all possible sigmas for a cycle length n as a list of arrays
        of integers"""
    sigma=[]
    nums=np.zeros(cycle_length)
    nums[:]=int(1)
    float_list=list(product(*((x, -x) for x in nums)))
    for array in float_list:
        array=np.array([int(i) for i in array])
        sigma.append(array)
    return sigma

def relaxation(cycle, dt=1e-1, maxiter=10000, ep=1e-7, verbose=True):
    """ Relaxation method for temporal Henon
    
    Parameters
    ----------
    cycle : Henon instance
    dt : float
        Step size. Large values may fail
    maxiter : int
        maximum number of iterations
    ep : float
        tolerance
    verbose : bool
        If True, print stuff, if False, suppress printing stuff.
        
    Returns
    -------
    cycle :
        Henon which may or may not have converged; residual must be checked. 
    """    
    # Count how many iterations we're computing so we don't get into an infinite loop. 
    n_iter = 0
    
    # now vi is a vector, to compare to a scalar, use its norm. 
    # This is assuming a monotonic decrease in vi. 
    while np.any(abs(cycle.deviation())) > ep and n_iter < maxiter:
        # Chaosbook says x_{i+1}, x_{i-1} fixed; so the MUST be fixed? Somewhat confusing statement.
        # Presumably the fictitious flow described in terms of x_i is not for a single i. 
        # Euler's method gives new x_n state
        new_x_n = cycle.x_n + (cycle.sigma * dt * cycle.deviation())
        # Store in a new Henon instance; this overwrites cycle but only in the current scope (this function)
        tmp_cycle = Henon(x_n=new_x_n, sigma=cycle.sigma, cycle_length=cycle.cycle_length,
                          a=cycle.a, b=cycle.b)
        if tmp_cycle.residual() > cycle.residual():
            # Could also insert a "backtracking" loop here
            break
        else:
            # Overwrite current state with new state
            cycle = tmp_cycle
        n_iter += 1
        #if verbose:
            # If we want to print stuff to watch while relaxation is happening
    
    if verbose:
        print('\nRelaxation terminated with residual = {}'.format(cycle.residual()))

    return cycle


if case==1:
    cycle_length=6
    ep=1e-7
    #Filtering list
    b=[]

    for sigma in sigma_generator(cycle_length):
        cycle = Henon(sigma=sigma, cycle_length=cycle_length)
        cycle_post_relaxation = relaxation(cycle,verbose=False)
        if (cycle_post_relaxation.residual() <= ep and 
            len(cycle_post_relaxation.x_n_minus_1) == len(set(cycle_post_relaxation.x_n_minus_1))
            and cycle_post_relaxation.x_n_minus_1[0] not in b):
                b.extend(cycle_post_relaxation.x_n_minus_1)
                print(cycle_post_relaxation.x_n_minus_1)
        

if case==2:
    plot=True
    Gallas=False
    a=6
    n=6
    n2=6
    mode=5
    def cycle_inverse(symbols):
        signs=[]
        ep=1e-7
        cycle=np.zeros(len(symbols))
        maxiter=1000
        n_iter=0
        deviation=np.zeros(len(symbols))
        deviation[:]=1
        for symbol in symbols:
            if symbol==0:
                signs.append(-1)
            if symbol==1:
                signs.append(1)
        while any(np.greater(abs(deviation),ep)) and n_iter<maxiter:
            n_iter+=1
            for i in range(0,len(symbols)):
                cycle[i]=signs[i]*np.sqrt(abs(1-np.roll(cycle,1)[i]-np.roll(cycle,-1)[i])/a)
            for i in range(0,len(symbols)):
                deviation[i]=np.roll(cycle,-1)[i]-(1-a*(cycle[i])**2-np.roll(cycle,1)[i])
        return(cycle)
    
    def prime_cycle_itinerary(cyclelength):
        itineraries=[]
        current_cyclelength=1
        for i in range(1,cyclelength+1):
            itinerary=np.zeros(i)
            itinerary[:]=int(1)
            cycle_list=list(product(*((x, 0) for x in itinerary)))
            if itineraries:
                for cycle in cycle_list:
                    add='yes'
                    cyclearray=[]
                    for item in cycle:
                        cyclearray.append(item)
                    if itineraries[0]*current_cyclelength==cycle:
                        add='no'
                    if itineraries[1]*current_cyclelength==cycle:
                        add='no'
                    for item in itineraries:
                        for i in range(0,cyclelength):
                            if list(np.roll(item,i))==cyclearray:
                                add='no'
                            if int(current_cyclelength/len(item))*list(np.roll(item,i))==cyclearray:
                                add='no'
                        if int(current_cyclelength/len(item))*item==cycle:
                            add='no'
                    if add=='yes':
                        itineraries.append(cycle)
            else:
                itineraries.append((0,))
                itineraries.append((1.0,))
            current_cyclelength+=1
        return(itineraries)
    
    def orbit_jacobian(orbit,orbitlength):
        J=np.arange((orbitlength)**2,dtype='float').reshape(orbitlength,orbitlength)
        c=a
        if(Gallas):
            c=1
        for i in range(0,orbitlength):
            Jrow=[1,2*c*orbit[i],1]
            Jrow.extend(np.zeros(orbitlength-3))
            Ji=np.roll(Jrow,i-1)
            for j in range(0,orbitlength):
                J[i][j]=Ji[j]
        return(J)
    
    orbits=[]
    fourier=[]
    
    scaled=[]
    scaled_cycle=[]
    fourier_scaled=[]
    
    X=[]
    Y=[]
    
    for cycle in prime_cycle_itinerary(n):
        c=cycle_inverse(cycle)
        for i in range(len(cycle)):
            aprime=np.roll(c,i)
            f=np.fft.fft(aprime)
            fourier.append(f)
        orbits.append(c)
    
    for cycle in orbits:
        for item in cycle:
            scaled_cycle.append(a*item)
        for i in range(len(cycle)):
            aprime=np.roll(scaled_cycle,i)
            f=np.fft.fft(aprime)
            fourier_scaled.append(f)
        scaled.append(scaled_cycle)
        scaled_cycle=[]
    
    if(Gallas):
        fouriers=fourier_scaled
        gencycle=scaled
    else:
        fouriers=fourier
        gencycle=orbits
    
    for cycle in fouriers:
        if len(cycle)==n2:
            X.append(cycle[mode].real)
            Y.append(cycle[mode].imag)
    
    dets=[]
    eigenvals=[]
    for item in gencycle:
        n=len(item)
        if n==5:
            M=orbit_jacobian(item,n)
            eigen=np.linalg.eig(M)
            det=np.linalg.det(M)
            eigenvals.append(eigen[0])
            print item
            print eigen[0]

time_reversible=[]

for cycle in gencycle:
    cyclerev=cycle[::-1]
    for i in range(0,len(cycle)):
        if all(cycle)==all(np.roll(cyclerev,i)):
            time_reversible.append(cycle)
            break

if(plot):
    
    plt.scatter(X,Y)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.show()
    
    fig, axes = plt.subplots(3,2,figsize=(14,14)) 

    fig.suptitle('Lattice States of 5-Cycles',fontsize=20)
    axes[0,0].axhline(y=0,color='black')
    axes[0,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-10],color=['gold','maroon','maroon','maroon','maroon'],width=0.4)
    axes[0, 0].set_title(r'$\overline{10000}$')
    axes[1,0].axhline(y=0,color='black')
    axes[1,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-11],color=['maroon','gold','maroon','maroon','maroon'],width=0.4)
    axes[1, 0].set_title(r'$\overline{10100}$')
    axes[2,0].axhline(y=0,color='black')
    axes[2,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-12],color=['maroon','maroon','maroon','gold','maroon'],width=0.4)
    axes[2, 0].set_title(r'$\overline{11000}$')
    axes[0,1].axhline(y=0,color='black')
    axes[0,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-13],color=['maroon','maroon','maroon','gold','maroon'],width=0.4)
    axes[0, 1].set_title(r'$\overline{11010}$')
    axes[1,1].axhline(y=0,color='black')
    axes[1,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-14],color=['maroon','gold','maroon','maroon','maroon'],width=0.4)
    axes[1, 1].set_title(r'$\overline{11100}$')
    axes[2,1].axhline(y=0,color='black')
    axes[2,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        gencycle[-15],color=['maroon','maroon','maroon','maroon','gold'],width=0.4)
    axes[2, 1].set_title(r'$\overline{11110}$')
    plt.show
    plt.savefig('5latt.png',dpi=300)

    fig, axes = plt.subplots(3,2,figsize=(14,14)) 

    fig.suptitle('Eigenvalues of 5-Cycles',fontsize=20)
    axes[0,0].axhline(y=0,color='black')
    axes[0,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[0],color='maroon',width=0.4)
    axes[0, 0].set_title(r'$\overline{10000}$')
    axes[1,0].axhline(y=0,color='black')
    axes[1,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[1],color='maroon',width=0.4)
    axes[1, 0].set_title(r'$\overline{10100}$')
    axes[2,0].axhline(y=0,color='black')
    axes[2,0].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[2],color='maroon',width=0.4)
    axes[2, 0].set_title(r'$\overline{11000}$')
    axes[0,1].axhline(y=0,color='black')
    axes[0,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[3],color='maroon',width=0.4)
    axes[0, 1].set_title(r'$\overline{11010}$')
    axes[1,1].axhline(y=0,color='black')
    axes[1,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[4],color='maroon',width=0.4)
    axes[1, 1].set_title(r'$\overline{11100}$')
    axes[2,1].axhline(y=0,color='black')
    axes[2,1].bar(np.array([r'$\phi_0$',r'$\phi_1$',r'$\phi_2$',r'$\phi_3$',r'$\phi_4$']),
        eigenvals[5],color='maroon',width=0.4)
    axes[2, 1].set_title(r'$\overline{11110}$')
    plt.show
    plt.savefig('5eigen.png',dpi=300)