import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


def setAxis(ax):
    # ax.set_xlabel(r'$\theta$', fontsize=20, labelpad=-40)
    ax.set_xticks([0., .125*np.pi, 0.25*np.pi, 0.375*np.pi, 0.5*np.pi])
    ax.set_xticklabels(["$0$", r"$\frac{1}{8}\pi$", r"$\frac{1}{4}\pi$",
                        r"$\frac{3}{8}\pi$", r"$\frac{1}{2}\pi$"],
                       fontsize=15)
    # ax.legend(loc='best', fontsize=12)
    ax.set_yscale('log')
    ax.set_ylim([0.01, 100])
    ax.text(0.02, 20, r'$\rho(\theta)$', fontsize=20)
    # ax.set_ylabel(r'$\rho(\theta)$', fontsize=20, labelpad=-55)

# load data first
data = np.load('ab.npz')
a = data['a']               # sin(theta) for k=1,2,...,29
b = data['b']               # bin locations
ns = data['ns']             # number of bins
angSpan = data['angSpan']   # max(sin(theta)) - min(sin(theta)) for k=1,2,...,29
angNum = data['angNum']     # the number of data points in for k=1,2,...,29

ixRange = range(0, 29)
labs = ['k='+str(i+1) for i in ixRange]

######################################################################

case = 1

if case == 1:
    """
    Fig 2(b)

    plot the angle distribution for k = 1, 2, 3, 4, 5, 6, 7
    """

    fig = plt.figure(figsize=(4, 1.5))
    ax = fig.add_subplot(111)
    for i in range(7):
        ax.plot(b[i][:-1], a[i]*ns/(angSpan[i]*angNum[i]), label=labs[i], lw=1.5)
    setAxis(ax)
    plt.tight_layout(pad=0)
    plt.show()

if case == 2:
    """
    Fig 2(c)

    plot the angle distribution for k = 8, 10, 12,..., 28
    """
    fig = plt.figure(figsize=(4, 1.5))
    ax = fig.add_subplot(111)
    colors = cm.rainbow(np.linspace(0, 1, 11))
    for ix in range(11):
        i = 7 + 2*ix
        ax.plot(b[i][:-1], a[i]*ns/(angSpan[i]*angNum[i]), c=colors[ix], lw=1.5)
    setAxis(ax)
    plt.tight_layout(pad=0)
    plt.show()
