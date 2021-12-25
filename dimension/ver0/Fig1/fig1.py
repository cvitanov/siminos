import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import ScalarFormatter


def setAxis(ax, xr, xlabel=r'$t$', ylabel=r'$\lambda_k(t)$'):
    # ax.get_yaxis().set_tick_params(which='both', direction='in', pad = -20)
    # ax.get_xaxis().set_tick_params(which='both', direction='in', pad = -20)

    # ax.set_xlabel(xlabel, fontsize=20)
    # ax.set_ylabel(ylabel, fontsize=20)
    ax.set_xlim([0, xr])
    ax.set_xticks([0, xr-1])
    ax.set_xticklabels([0, r'$T_p$'], fontsize=13)


# load data first
data = np.load('ppo1.npz')
T = data['T']          # period of ppo1
nstp = data['nstp']    # number of pieces of ppo1. T/nstp => time step
fe = data['fe']        # real part of Floquet exponents
expand = np.log(np.loadtxt('FVexpand1.dat')) / (5 * T / nstp)
# expand is the local expansion rate of Floquet vectors. here I use 5
# times of original time step

######################################################################
case = 1

if case == 1:
    """
    Fig 1(a)

    plot Floquet exponents for N = 64 with a insert plot
    """
    FE = fe
    N = 32
    d = 22
    x = np.arange(1, N, 0.01)
    qk = 2 * np.pi / d * x
    L = qk**2 - qk**4

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)
    ax.plot(x, L, 'g--', lw=1.8)
    ax.scatter(np.arange(1, N), FE[::2], c='r',
               marker='o', s=22, edgecolors='none')
    ax.scatter(np.arange(1, N), FE[1::2], c='r',
               marker='s', s=30, facecolors='none',
               edgecolors='k')
    yfmt = ScalarFormatter()
    yfmt.set_powerlimits((0, 1))
    ax.yaxis.set_major_formatter(yfmt)

    ax.set_yticks((-7e3, -3e3, 0, 1e3))
    ax.set_xlim((0, 35))
    ax.set_ylim((-7e3, 1e3))
    ax.grid('on')

    axin = inset_axes(ax, width="45%", height="50%", loc=3)
    axin.scatter(np.arange(1, N), FE[::2], c='r',
                 marker='o', s=22, edgecolors='none')
    axin.scatter(np.arange(1, N), FE[1::2], c='r',
                 marker='s', s=30, facecolors='none',
                 edgecolors='k')
    axin.set_xlim(0.5, 4.5)
    axin.set_ylim(-0.4, 0.1)
    axin.yaxis.set_ticks_position('right')
    axin.xaxis.set_ticks_position('top')
    axin.set_xticks((1, 2, 3, 4))
    axin.set_yticks((-0.4, -0.2, 0))
    axin.grid('on')

    mark_inset(ax, axin, loc1=1, loc2=2, fc="none")

    fig.tight_layout(pad=0)
    plt.show()
    
if case == 2:
    """
    Fig 1(b)

    plot the local Flouqet exponents of ppo1
    """
    # load data

    fig = plt.figure(figsize=[3, 2])
    ax = fig.add_subplot(111)
    ax.plot(expand[0], lw=1.5, ls='-')
    ax.plot(expand[2], lw=1.5, ls='-')
    ax.plot(expand[3], lw=1.5, ls='-')
    ax.plot(expand[4], lw=1.5, ls='-')
    ax.plot(expand[5], lw=1.5, ls='-')
    ax.plot(expand[7], lw=1.5, ls='-')

    ax.plot(expand[8], lw=1.5, ls='-')
    ax.plot(expand[9], lw=1.5, ls='-')

    ax.text(expand.shape[1]/50, 0.4, r'$\lambda_k(t)$', fontsize=18)
    ax.text(expand.shape[1]/3, -0.8, r'$k=1, 3, 4, 5, 6, 8$', fontsize=18)
    ax.text(expand.shape[1]/2, -1.8, r'$k=9, 10$', fontsize=18)

    setAxis(ax, expand.shape[1])
    ax.set_ylim([-2.5, 1])
    ax.set_yticks([-2, -1, 0, 1])
    fig.tight_layout(pad=0)
    plt.show()

if case == 3:
    """
    Fig 1(c)
    
    plot $\lambda_i(t) -\lambda$ for a small subset
    """
    fig = plt.figure(figsize=[3, 2])
    ax = fig.add_subplot(111)
    ix = [8, 9, 10, 11]
    for i in ix:
        ax.plot(expand[i]-fe[i], lw=1.5, ls='-', label='k='+str(i+1))

    setAxis(ax, expand.shape[1], ylabel=r'$\lambda_k(t) - \lambda_k$')
    ax.set_yticks([-0.03, 0, 0.03, 0.06])
    ax.legend(loc='best', fontsize=13, frameon=False)
    fig.tight_layout(pad=0)
    plt.show()

if case == 4:
    """
    Fig 1(d)

    plot $\lambda_i(t) -\lambda$ for the remaining set
    """
    fig = plt.figure(figsize=[3, 2])
    ax = fig.add_subplot(111)
    ix = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    for i in ix:
        ax.plot(expand[i]-fe[i], lw=1.5, ls='-')

    ax.arrow(expand.shape[1]/20, 0.009, 0, -0.003,
             width=20, head_length=0.001, head_width=80,
             fc='k')
    setAxis(ax, expand.shape[1], ylabel=r'$\lambda_k(t) - \lambda_k$')
    ax.set_yticks([-0.008, -0.002, 0.004, 0.01])
    fig.tight_layout(pad=0)
    plt.show()

