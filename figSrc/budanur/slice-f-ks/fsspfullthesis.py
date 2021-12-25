#tw.py

import numpy as np

import matplotlib as mpl
from pylab import figure, plot, xlabel, ylabel, grid, hold, legend, title, savefig, imshow, colorbar, xlim
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from subprocess import call

#mpl.rcParams['text.usetex']=True
#mpl.rcParams['text.latex.unicode']=True

numoftrajec = 20

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.hold(True)

ax.w_xaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_yaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_zaxis.set_pane_color((1, 1, 1, 1.0))

nmax = 6000

for i in range(1,numoftrajec+1):
    
    fname = 'data/xsolsspfull'+str(i)+'.dat'
    solssp = np.loadtxt(fname)
    nmax = np.int(np.size(solssp,0))  # *0.95)
    
    fname2 = 'data/xsolfull'+str(i)+'.dat'
    solhat = np.loadtxt(fname2)
    
    iborder = np.argwhere(solhat[0:nmax,0] < 0.05)
    
    #ax.plot(solssp[0:nmax,0], solssp[0:nmax,1], solssp[0:nmax,2], linewidth=0.5, alpha = 0.4, color='#3c5f96')
    ax.plot(solssp[0:nmax,0], solssp[0:nmax,1], solssp[0:nmax,2], linewidth=0.5, alpha = 0.85, color='#778FB6')
    #ax.plot(solssp[iborder,0].reshape(np.size(iborder,0)).reshape(np.size(iborder,0)), 
    #solssp[iborder,1].reshape(np.size(iborder,0)), solssp[iborder,2].reshape(np.size(iborder,0)), 
    #linewidth=0.5, color='#FF0000')

fnamerpo = 'data/rposolsspfull.dat'
rposspfull = np.loadtxt(fnamerpo)

irpo = np.size(rposspfull, 0)
nperiod = np.floor(irpo / 3);

nplotper = 2;

#ax.plot(rposspfull[0:nplotper*nperiod,0], rposspfull[0:nplotper*nperiod,1], 
#rposspfull[0:nplotper*nperiod,2], alpha=1.0, linewidth=2.5, color='#f7464a')

#ax.scatter(rposspfull[0,0], rposspfull[0,1], rposspfull[0,2], s= 30, c='#000000')
#ax.scatter(rposspfull[0,0], rposspfull[0,1], rposspfull[0,2], s= 30, c='#000000')
#ax.scatter(rposspfull[0,0], rposspfull[0,1], rposspfull[0,2], s= 30, c='#000000')
#ax.scatter(rposspfull[0,0], rposspfull[0,1], rposspfull[0,2], s= 30, c='#000000')
#ax.scatter(rposspfull[nperiod,0], rposspfull[nperiod,1], rposspfull[nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[nperiod,0], rposspfull[nperiod,1], rposspfull[nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[nperiod,0], rposspfull[nperiod,1], rposspfull[nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[nperiod,0], rposspfull[nperiod,1], rposspfull[nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[2*nperiod,0], rposspfull[2*nperiod,1], rposspfull[2*nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[2*nperiod,0], rposspfull[2*nperiod,1], rposspfull[2*nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[2*nperiod,0], rposspfull[2*nperiod,1], rposspfull[2*nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[2*nperiod,0], rposspfull[2*nperiod,1], rposspfull[2*nperiod,2], s= 30, c='#000000')
#ax.scatter(rposspfull[3*nperiod,0], rposspfull[3*nperiod,1], rposspfull[3*nperiod,2], c='#000000')

ax.xaxis.set_rotate_label(False)
ax.yaxis.set_rotate_label(False)
ax.zaxis.set_rotate_label(False)

#ax.set_xlabel('$e_1$\n', 
              #fontsize=32, 
              #verticalalignment='top', 
              #linespacing=4.8)
#ax.set_ylabel('\t\t\t     $e_2$\n', fontsize=32, linespacing=0.8)
#ax.set_zlabel('    $e_3$\n',
              #multialignment='right',
              #fontsize=32, linespacing=8.0)

ax.set_xlabel('    $e_1$', 
              fontsize=32, 
              verticalalignment='top', 
              linespacing=4.8)
ax.set_ylabel('\n $e_2$', fontsize=32, linespacing=0.2)
ax.set_zlabel('$e_3$  ',
              multialignment='right',
              fontsize=32, linespacing=8.0)
              
#tw1ssp = np.loadtxt('data/tw2sspfull.dat')
#ax.scatter(tw1ssp[0], tw1ssp[1], tw1ssp[2], c='#e500e5')
#ax.text(tw1ssp[0], tw1ssp[1], tw1ssp[2], "$TW_2$", fontsize=16, color='red')

gtw1 = np.loadtxt('data/gtw1sspfull.dat')
gtw2 = np.loadtxt('data/gtw2sspfull.dat')

#ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], c='#e500e5')
#ax.text(gtw1[0,0], gtw1[0,1], gtw1[0,2], "$TW_1$", fontsize=16, color='red')

#ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], c='#e500e5')
#ax.text(gtw2[0,0], gtw2[0,1], gtw2[0,2], "$TW_2$", fontsize=16, color='red')

ax.plot(gtw1[:,0], gtw1[:,1], gtw1[:,2], linewidth=2, color='#890089')
#ax.plot(gtw2[:,0], gtw2[:,1], gtw2[:,2], linewidth=2, color='#33CC33')
#ax.plot(gtw2[:,0], gtw2[:,1], gtw2[:,2], linewidth=2, color='#008000')


Nticks = 4;

#xticks = np.linspace(-0.7, 0.2, Nticks)
#ax.set_xticks(xticks)
#ax.set_xticklabels(["$%.1f$" % xtik for xtik in xticks], fontsize=18); # use LaTeX formatted labels

#yticks = np.linspace(-0.6, 0.6, Nticks)
#ax.set_yticks(yticks)
#ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], fontsize=18); # use LaTeX formatted labels

#zticks = np.linspace(0, 1, 3)
#ax.set_zticks(zticks)
#ax.set_zticklabels(["$%.1f$" % ztik for ztik in zticks], fontsize=18); # use LaTeX formatted labels

xticks = np.linspace(-1, 0, 2)
ax.set_xticks(xticks)
ax.set_xticklabels(["  $%.1f$" % xtik for xtik in xticks], 
                   verticalalignment='baseline',
                   horizontalalignment='center', 
                   fontsize=24); # use LaTeX formatted labels

yticks = np.linspace(-0.4, 0.8, Nticks)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], 
                   verticalalignment='top',
                   horizontalalignment='center',
                   fontsize=24); # use LaTeX formatted labels

zticks = np.linspace(0, 0.8, 3)
ax.set_zticks(zticks)
ax.set_zticklabels(["$%.1f$" % ztik for ztik in zticks], fontsize=24); # use LaTeX formatted labels

ax.set_autoscale_on(False)

ax.set_xlim([-1.5, 0.5])
ax.set_ylim([-0.6,0.9])
ax.set_zlim([-0.1,1])

#ax.view_init(77,-140)
ax.view_init(-155,140)
ax.view_init(-160,175)
savefig('kstwsspfull.pdf', bbox_inches='tight', dpi=100)
savefig('kstwsspfull.png', bbox_inches='tight', dpi=150)
call(['convert', '-trim', "kstwsspfull.png", "kstwsspfull.png"])
call(['bash', 'cropkstwsspfull.sh'])
call(['bash','pdf2grayscale.sh','BudCvi-kssspfull.pdf','BudCvi-kssspfullBW.pdf'])

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.hold(True)

for i in range(1,numoftrajec+1):
    
    fname = 'data/xsolfull'+str(i)+'.dat'
    solssp = np.loadtxt(fname)
    nmax = np.size(solssp,0)
    
    ax2.plot(solssp[0:nmax,0], solssp[0:nmax,2], solssp[0:nmax,3], linewidth=0.5, color='#3c5f96')

#plt.show()
