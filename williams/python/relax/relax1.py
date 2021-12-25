        """
        $Author: predrag $ $Date: 2021-03-16 10:39:14 -0400 (Tue, 16 Mar 2021) $
        siminos/williams/python/relax1
        """

        """
        Sidney V.  Williams     sidneywilliams1231@gmail.com        2021-01-05
        crude python code that can find the fixed points of
        the \Henon\ map, and the two cycle
        """

import numpy as np
import matplotlib.pyplot as plt
from mpl\_toolkits.mplot3d import Axes3D

from matplotlib.colors import LogNorm
from numpy.random import rand

class Henon:
    def __init__(self, a=1.4, b=0.3):
        """
        initialization function which will be called every time you
        create an object instance. In this case, it initializes
        parameter a and b, which are the parameters of Henon map.
        """
        self.a = a
        self.b = b

    def oneIter(self, stateVec):
        """
        forward iterate for one step.

        stateVec: the current state. dimension : [1 x 2] numpy.array
        return: the next state. dimension : [1 x 2]
        """
        x = stateVec;
        return 1 - self.a * x[1]**2 + self.b * x[0]

    def multiIter(self, stateVec, NumOfIter):
        """
        forward iterate for multiple steps.
        stateVec: the current state. dimension : [1 x 2] numpy.array
        NumOfIter: number of iterations

        return: the current state and the furture 'NumOfIter' states.
                dimension [NumOfIter+1 x 2]
        """
        states = np.zeros(NumOfIter+1)
        states[0] = stateVec[0]
        states[1] = stateVec[1]
        tmpState = stateVec
        for i in range(NumOfIter):
            tmpState = self.oneIter(tmpState)
            states[i+1] = tmpState

        return states

    def vi(self,guesstrajectory):
        x=guesstrajectory
        return x-1+self.a*(x)**2-self.b*x

def Relaxation(guesstrajectory,sigma,dt):
    henon = Henon(1.4, 0.3)
    x0=guesstrajectory
    vi=henon.vi(x0)
    ep=10**(-7)
    x=0
    while abs(vi)>ep:
        x=x0+sigma*dt*vi
        vi=henon.vi(x)
        x0=x
    return x

def Two_Cycle(guesstrajectory,sigma,dt):
    henon = Henon(1.4, 0.3)
    x0=guesstrajectory
    vi=np.zeros(2)
    vi[0]=x0[0]-henon.oneIter(x0)
    vi[1]=x0[1]-henon.oneIter(np.roll(x0,1))
    ep=10**(-7)
    x=np.zeros(2)
    while np.all(abs(vi))>ep:
        for i in range(0,2):
            x[i]=x0[i]-dt*vi[i]
            vi[i]=x[i]-henon.oneIter(np.roll(x,i))
            x0[i]=x[i]
            print(x[i])
            if abs(x[i])>5:
                return "Diverged"
    return x
