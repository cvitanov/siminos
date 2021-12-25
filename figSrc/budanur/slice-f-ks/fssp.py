#tw.py

import numpy as np

import matplotlib as mpl
from pylab import figure, plot, xlabel, ylabel, grid, hold, legend, title, savefig, imshow, colorbar
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

nmax = 3000
ni = 1830

for i in range(1,numoftrajec+1):
    
    fname = 'data/xsolssp'+str(i)+'.dat'
    solssp = np.loadtxt(fname)
    nmax = np.int(np.size(solssp,0)) ##*0.95)
    
    #fname2 = 'data/xsol'+str(i)+'.dat'
    #solhat = np.loadtxt(fname2)
    
    #iborder = np.argwhere(solhat[0:nmax,0] < 0.05)
    
    #ax.plot(solssp[ni:nmax,0], solssp[ni:nmax,1], solssp[ni:nmax,2], linewidth=0.5, alpha = 0.4, color='#3c5f96')
    ax.plot(solssp[ni:nmax,0], solssp[ni:nmax,1], solssp[ni:nmax,2], linewidth=0.5, alpha = 0.4, color='#778FB6')
    #ax.plot(solssp[iborder,0].reshape(np.size(iborder,0)).reshape(np.size(iborder,0)), 
    #solssp[iborder,1].reshape(np.size(iborder,0)), solssp[iborder,2].reshape(np.size(iborder,0)), 
    #linewidth=0.5, color='#FF0000')

fnamerpo = 'data/rposolsspred.dat'
rposspred = np.loadtxt(fnamerpo)

irpo = np.size(rposspred, 0)
nperiod = np.floor(irpo / 3);

nplotper = 1;

ax.plot(rposspred[:,0], rposspred[:,1], rposspred[:,2], linewidth=2.5, color='#f7464a')
ax.scatter(rposspred[0,0], rposspred[0,1], rposspred[0,2], s= 30, c='#000000')
ax.scatter(rposspred[0,0], rposspred[0,1], rposspred[0,2], s= 30, c='#000000')
ax.scatter(rposspred[0,0], rposspred[0,1], rposspred[0,2], s= 30, c='#000000')
ax.scatter(rposspred[0,0], rposspred[0,1], rposspred[0,2], s= 30, c='#000000')

ax.xaxis.set_rotate_label(False)
ax.yaxis.set_rotate_label(False)
ax.zaxis.set_rotate_label(False)
ax.set_xlabel('$e_1$\n', 
              fontsize=32, 
              verticalalignment='top', 
              linespacing=4.8)
ax.set_ylabel('\t\t\t     $e_2$\n', fontsize=32, linespacing=0.8)
ax.set_zlabel('    $e_3$\n',
              multialignment='right',
              fontsize=32, linespacing=8.0)

gtw1 = np.loadtxt('data/gtw1sspfull.dat')
gtw2 = np.loadtxt('data/gtw2sspfull.dat')

#ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], linewidth='0', s= 20, c='#e500e5')
#ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], linewidth='0', s= 20, c='#e500e5')
ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], edgecolor='#890089', s= 30, c='#890089')
ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], edgecolor='#890089', s= 30, c='#890089')
ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], edgecolor='#890089', s= 30, c='#890089')
ax.scatter(gtw1[0,0], gtw1[0,1], gtw1[0,2], edgecolor='#890089', s= 30, c='#890089')
#ax.text(gtw1[0,0], gtw1[0,1]+0.1, gtw1[0,2]-0.03, "$\mathbf{TW_{1}}$", fontsize=24, color='#e500e5')
ax.text(gtw1[0,0], gtw1[0,1]+0.2, gtw1[0,2]-0.03, "$\mathbf{TW_{1}}$", fontsize=24, color='#890089')

#ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#33CC33', s= 30,  c='#33CC33')
#ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#33CC33', s= 30,  c='#33CC33')
#ax.text(gtw2[0,0]*1.0, gtw2[0,1]*1.8, gtw2[0,2]*1.2, "$\mathbf{TW_{2}}$", fontsize=24, color='#33CC33')

ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#008000', s= 30,  c='#008000')
ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#008000', s= 30,  c='#008000')
ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#008000', s= 30,  c='#008000')
ax.scatter(gtw2[0,0], gtw2[0,1], gtw2[0,2], edgecolor='#008000', s= 30,  c='#008000')
ax.text(gtw2[0,0]*1.0, gtw2[0,1]*1.8, gtw2[0,2]*1.2, "$\mathbf{TW_{2}}$", fontsize=24, color='#008000')

#tw1ssp = np.loadtxt('data/tw2ssp.dat')

#ax.scatter(tw1ssp[0], tw1ssp[1], tw1ssp[2], c='#e500e5')
#ax.text(tw1ssp[0], tw1ssp[1], tw1ssp[2], "$TW_2$", fontsize=16, color='red')

#ax.scatter(solssp[0,0], solssp[0,1], solssp[0,2], c='#e500e5')
#ax.text(solssp[0,0], solssp[0,1], solssp[0,2], "$TW_1$", fontsize=16, color='red')

Nticks = 4;

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
ax.view_init(40,-70)
ax.view_init(-160,175)
savefig('kstwsspred.pdf', bbox_inches='tight', dpi=100)
savefig('kstwsspred.png', bbox_inches='tight', dpi=150)
call(['convert', '-trim', "kstwsspred.png", "kstwsspred.png"])
call(['bash', 'cropkstwssp.sh'])
call(['bash','pdf2grayscale.sh','BudCvi-kssspred.pdf','BudCvi-kssspredBW.pdf'])

#fig2 = plt.figure()
#ax2 = fig2.gca(projection='3d')
#ax2.hold(True)

#for i in range(1,numoftrajec+1):
    
    #fname = 'data/xsol'+str(i)+'.dat'
    #solssp = np.loadtxt(fname)
    #nmax = np.size(solssp,0)
    
    #ax2.plot(solssp[0:nmax,0], solssp[0:nmax,2], solssp[0:nmax,3], linewidth=0.5, color='#3c5f96')


#plt.show()
