import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D


def setAxis(ax, xl, xr, yl, yr, px, py):
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_ylim([yl, yr])
    ax.set_xlim([xl, xr])
    # ax.legend(loc='upper left')
    # ax.set_title('(a)')

    ax.text(px, py, r'$\sin(\theta)$', fontsize=18)
    # ax.set_ylabel(r'$\sin(\theta)$', size='large')
    # ax.set_xlabel(r'$||\Delta \hat{u}||_2$', fontsize=15, labelpad=0)


def setAxis2(ax):
    ax.set_yscale('log')
    ax.set_xscale('log')
    # ax.text(px, py, r'$\langle \sin(\theta) \rangle$', fontsize=15)
    # ax.set_ylabel(r'$< \sin(\theta) >$', size='large')
    # ax.set_xlabel(r'$||\Delta \hat{u}||_2$', size='large')


######################################################################
# set case to 1, 2, 3, 4 for different figures.

case = 3 

if case == 1:
    """
    Fig 4(a)

    plot { norm of distance vector } vs { sin(theta) } only for one
    shadowing incidence of ppo4 with T = 33.39

    Note :
    the data points whose { norm of distance vector } is
    larger than 4 times of the orbit points spacing are ruled out
    in 'rpo4Scatter.npz'.
    The same is true for all other figures.
    """
    data = np.load('ppo4OneShadow.npz')  # data file
    dis = data['dis']                  # norm of distance vector
    ang = data['ang']                  # sin(theta) for K = 6, 7, 8

    spix = [6, 7, 8]        # subspace index
    colors = ['r', 'b', 'c', 'm']
    markers = ['o', 's', 'v', '*']

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)
    for i in range(len(spix)):
        ax.scatter(dis, ang[:,i], s=10, c=colors[i], marker=markers[i],
                   edgecolor='none', label='1-'+str(spix[i]))

    setAxis(ax, 7e-3, 1e-1, 5e-4, 8e-2, 8e-3, 4e-2)

    fig.tight_layout(pad=0)
    plt.show()

if case == 2:
    """
    Fig 4(b)

    plot only one shadowing incidence of rpo4 with T = 34.64
    """
    data = np.load('rpo4OneShadow.npz')  # data file
    dis = data['dis']                  # norm of distance vector
    ang = data['ang']                  # sin(theta) for K = 6, 7, 8

    spix = [6, 7, 8]        # subspace index
    colors = ['r', 'b', 'c', 'm']
    markers = ['o', 's', 'v', '*']

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)
    for i in range(len(spix)):
        ax.scatter(dis, ang[:,i], s=10, c=colors[i], marker=markers[i],
                   edgecolor='none', label='1-'+str(spix[i]))

    setAxis(ax, 7e-3, 1e-1, 1e-3, 5e-1, 8e-3, 2e-1)

    fig.tight_layout(pad=0)
    plt.show()

if case == 3:
    """
    Fig 4(c)

    plot { norm of distance vector } vs { sin(theta) } for total
    217 shadowing incidences of rpo4 with T = 34.64.
    """
    data = np.load('rpo4Scatter.npz')  # data file
    dis = data['dis']                  # norm of distance vector
    ang = data['ang']                  # sin(theta) for K = 6, 7, 8

    spix = [6, 7, 8]        # subspace index
    colors = ['r', 'b', 'c', 'm']
    markers = ['o', 's', 'v', '*']

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)
    for i in range(len(spix)):
        ax.scatter(dis, ang[:, i], s=7, c=colors[i], marker=markers[i],
                   edgecolor='none', label='1-'+str(spix[i]))
        
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_ylim([1e-4, 1e-0])
    ax.set_xlim([1e-3, 1e-1])
    # ax.legend(loc='upper left')
    # ax.set_title('(a)')

    ax.text(1.2e-3, 2e-1, r'$\sin(\theta)$', fontsize=18)
    # ax.set_ylabel(r'$\sin(\theta)$', size='large')
    # ax.set_xlabel(r'$||\Delta x||_2$', size='large')
    fig.tight_layout(pad=0)
    plt.show()


if case == 4:
    """
    Fig 4(d)

    plot the  the statistic avarage of Fig 4(c)
    """

    data = np.load('rpo4Average.npz')  # data file
    x = data['x']                      # norm of distance vector
    aver = data['aver']                # sin(theta) for K = 6, 7, 8

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)

    # I only select k = 4, 5, 6, 7, 9, 11, 17, 21, 25
    for i in range(3, 6) + range(6, 11, 2)+range(16, 25, 4):
        ax.plot(x, aver[:, i], '-o')

    setAxis2(ax)
    ax.set_yticks([1e-6, 1e-4, 1e-2, 1e0])
    fig.tight_layout(pad=0)
    plt.show()
