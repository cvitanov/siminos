#
# invpolsolver.py
#
"""
Use odeint to solve differential equations defined by vinvpol in twomode.py
"""

#from __future__ import unicode_literals

from scipy.integrate import odeint
import twomode
import numpy as np
import sspsolver
import onslicesolver

import matplotlib as mpl
from pylab import figure, plot, xlabel, ylabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#mpl.use("TKAGG")

#mpl.rcParams['text.usetex']=True
#mpl.rcParams['text.latex.unicode']=True
#mpl.rcParams['text.latex.preamble']=r"\usepackage{color}"

from subprocess import call

#Load parameters:
p = np.loadtxt('data/parameters.dat')

x01 = [0.43997, 0, -0.38627, 0.07020] #reqv
#x02 = [0.001, 0, 0.001, 0.001] #origin
x03 = [4.525719078826287434e-01, -2.791192295890519988e-18, 5.092565177630036660e-02, 3.354280141917114627e-02] #rpo 1 T= 22.1591782 

xphi01 = [0.43997, 0, -0.38627, 0.07020, 0] #reqv
#xphi02 = [0.001, 0, 0.001, 0.001, 0] #origin
xphi03 = [4.525719078826287434e-01, -2.791192295890519988e-18, 5.092565177630036660e-02, 3.354280141917114627e-02, 0] #rpo 1 T= 22.1591782 

t1 = np.linspace(0,150,10000)
t2 = np.linspace(0,15,1500)
t3 = np.linspace(0, 10*3.641511999233241426e+00, 10000)

xsol1 = sspsolver.integrate(x01, p, t1)
#xsol2 = sspsolver.integrate(x02, p, t2)
xsol3 = sspsolver.integrate(x03, p, t3)

xhatsol1 = onslicesolver.integrate(xphi01, p, t1)
#xhatsol2 = onslicesolver.integrate(x02, p, t2)
xhatsol3 = onslicesolver.integrate(xphi03, p, t3)

x04 = [0.0384074556708, 0.0, -1.90362452394, 0.0668631895808]
xsol4 = sspsolver.integrate(x04, p, t1/2)

xhat04 = [0.0384074556708, 0.0, -1.90362452394, 0.0668631895808, 0]
xhatsol4 = onslicesolver.integrate(xhat04, p, t1/2)

#print xhatsol3

#raw_input('press any key')


#Plot full state space:

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.w_xaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_yaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_zaxis.set_pane_color((1, 1, 1, 1.0))

ax.plot(xsol4[:,0], xsol4[:,2], xsol4[:,3], linewidth=0.5, color='#3c5f96')
ax.hold(True)
ax.plot(xsol3[:,0], xsol3[:,2], xsol3[:,3], linewidth=0.8, color='#f7464a')
ax.plot(xsol1[:,0], xsol1[:,2], xsol1[:,3], linewidth=2.5, color='#33CC33')
#ax.plot(xsol1[:,0], xsol1[:,2], xsol1[:,3], linewidth=2.5, color='#e500e5')
#ax.plot(xsol2[:,0], xsol2[:,2], xsol2[:,3], linewidth=1, color='#6a9c53')

#ax.set_xlabel(r' \color{red}{.} \newline \newline \newline  \newline  $ \\ x_1$', fontsize=48)
#ax.set_xlabel(r'\textcolor{red}{x} $  \\ \\ \\ \\ x_1 $', fontsize=48)
ax.set_xlabel('\n $x_1$ \t', fontsize=32)
ax.set_ylabel('\n $x_2$ \t', fontsize=32)
ax.set_zlabel('$y_2$   ', fontsize=32)

ax.xaxis.set_label_coords(0, 5, 0)

Nticks = 3

xticks = np.linspace(-1.5, 1.5, Nticks)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%.1f$" % xtik for xtik in xticks], fontsize=24); # use LaTeX formatted labels

yticks = np.linspace(-1.5, 1.5, Nticks)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], fontsize=24); # use LaTeX formatted labels

zticks = np.linspace(-1.5, 1.5, Nticks)
ax.set_zticks(zticks)
#ax.set_zticklabels(["$%.1f$ " % ztik for ztik in zticks], fontsize=24); # use LaTeX formatted labels
ax.set_zticklabels(["$-1.5$ \t", " $0.0$", " $1.5$"], fontsize=24); # use LaTeX formatted labels


ax.view_init(15,30)
savefig('twomode1.pdf', bbox_inches='tight', dpi=100)
savefig('twomode1.png', bbox_inches='tight', dpi=150)

#call(['pdfcrop', "twomode1.pdf", "twomode1.pdf"])
call(['convert', '-trim', "twomode1.png", "twomode1.png"])

#Plot reduced state space:
fig.clf()
ax = fig.gca(projection='3d')
ax.w_xaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_yaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_zaxis.set_pane_color((1, 1, 1, 1.0))

ax.plot(xhatsol4[:,0], xhatsol4[:,2], xhatsol4[:,3], linewidth=0.5, color='#3c5f96')
ax.hold(True)
ax.plot(xhatsol3[:,0], xhatsol3[:,2], xhatsol3[:,3], linewidth=3, color='#f7464a')
ax.plot(xhatsol1[:,0], xhatsol1[:,2], xhatsol1[:,3], linewidth=5, color='#33CC33')
#ax.plot(xhatsol1[:,0], xhatsol1[:,2], xhatsol1[:,3], linewidth=5, color='#e500e5')
#ax.plot(xhatsol2[:,0], xhatsol2[:,2], xhatsol2[:,3], linewidth=1, color='#6a9c53')
ax.set_xlabel('\n $\hat{x}_1$ \t  ', fontsize=32)
ax.set_ylabel('\n $\hat{x}_2$ \t', fontsize=32)
ax.set_zlabel('$\hat{y}_2$   ', fontsize=32)

xticks = np.linspace(0, 2, Nticks)
ax.set_xticks(xticks) 
ax.set_xticklabels(["$%.1f$" % xtik for xtik in xticks], fontsize=24); # use LaTeX formatted labels

yticks = np.linspace(-1.8, 0, Nticks)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], fontsize=24); # use LaTeX formatted labels

zticks = np.linspace(-0.3, 0.3, Nticks)
ax.set_zticks(zticks)
#ax.set_zticklabels(["$%.1f$ " % ztik for ztik in zticks], fontsize=24); # use LaTeX formatted labels
ax.set_zticklabels(["$-0.3$ \t", " $0.0$", " $0.3$"], fontsize=24); # use LaTeX formatted labels

ax.view_init(15,30)
savefig('twomode2.pdf', bbox_inches='tight', dpi=100)
savefig('twomode2.png', bbox_inches='tight', dpi=150)

#call(["pdfcrop", "twomode2.pdf", "twomode2.pdf"])
call(['convert', '-trim', "twomode2.png", "twomode2.png"])

call(['bash', 'cropscript.sh'])

#plt.show()
