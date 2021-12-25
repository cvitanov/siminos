#
# invpolsolver.py
#
"""
Use odeint to solve differential equations defined by vinvpol in twomode.py
"""

from __future__ import unicode_literals

from scipy.integrate import odeint
import numpy as np

import matplotlib as mpl
from pylab import figure, plot, xlabel, ylabel, grid, hold, legend, title, savefig, imshow, colorbar
from matplotlib.font_manager import FontProperties
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import os
import oct2py

mpl.rcParams['text.usetex']=True
mpl.rcParams['text.latex.unicode']=True

from subprocess import call

rpo = np.array([3.70955584e-01,   1.59178104e-16,  -5.35414753e-01,   6.72233738e-01,
  -1.60102241e-01,   2.77492997e-01,   2.26119482e-01,   9.20202541e-02, 
   1.01234154e-01,  -7.61348435e-02,   2.86999279e-03,  -5.71633872e-02, 
  -2.19911067e-02,  -8.45432215e-03,  -9.70953085e-03,   5.74786687e-03, 
   4.19544211e-04,   4.07227658e-03,   1.61695688e-03,   7.51275352e-04, 
   5.51797781e-04,  -3.99001588e-04,  -2.26058837e-05,  -2.53441206e-04, 
  -9.51845395e-05,  -3.49971067e-05,  -2.92711613e-05,   2.18049965e-05, 
   5.41318900e-07,   1.12892181e-05], float)

xrand = np.array([1.081769255879405645e-01, 0.000000000000000000e+00,  -1.130645021532460798e-01, 
	2.735234400271993951e-02,  -2.300369007695817619e-02,  2.743365567776075153e-02,
	4.242109469805525057e-01,  -3.221375201839944691e-02,  3.517350195620121411e-01,
	4.196323928512094570e-01,  7.405822221667555938e-02,  -4.911698645198029345e-01,
	-2.619084037151255262e-01,  8.869647954573157966e-03,  2.667068425090810685e-02,
	-1.245857190912121742e-01,  1.848625450932936676e-01,  -1.886910780372257068e-01,
	-4.364329592632312099e-02,  -8.603322827952401136e-03,  -4.893648586116418342e-02,
	-4.227361593906937137e-02,  -5.743046880645331920e-02,  6.141174799787345318e-02,
	3.556320072237982056e-03,  -2.647610106987533310e-02,  -3.295731184608969265e-03,
	-1.760410218329051119e-02,  -1.449156681256755577e-02,  1.551927466950007474e-02], float)

#tw = np.array([4.19185108e-01,   2.55943357e-16,  -1.77530725e-01,
        #-1.46282501e-01,  -2.87443695e-01,  -4.21516320e-01,
         #9.33649938e-02,  -3.20489300e-01,   1.62361129e-02,
         #5.80747468e-03,  -4.93485521e-02,  -2.69378819e-02,
        #-7.64867193e-03,  -2.98815966e-02,   3.81954953e-03,
        #-5.09574672e-03,  -1.91533223e-03,   3.46492806e-04,
        #-1.26630256e-03,  -1.23563779e-03,   4.76928289e-05,
        #-5.13489813e-04,   2.22135119e-07,   9.94332808e-06,
        #-6.81917084e-05,  -1.31720259e-05,  -1.31699039e-05,
        #-2.57228901e-05,   1.76547599e-06,  -3.27286075e-06], float)

tw = np.array([  4.35443487e-01,   2.55718139e-16,   3.55754017e-01,
         3.69921902e-02,   2.65780484e-01,   1.23087691e-01,
         8.96316601e-02,   1.99746439e-01,  -5.05277891e-02,
         9.44414104e-02,  -3.97381177e-02,   1.50718227e-02,
        -1.69870437e-02,  -4.78697400e-03,  -4.29874538e-03,
        -6.15070596e-03,   3.91009306e-04,  -3.00081892e-03,
         8.69737447e-04,  -7.44165447e-04,   4.23685427e-04,
         1.94447859e-07,   1.19333832e-04,   1.01415612e-04,
         8.76041620e-06,   5.66807136e-05,  -1.10380807e-05,
         1.74490878e-05,  -7.02070045e-06,   2.11126404e-06], float)

rpo = rpo.reshape(-1,1)
xrand = xrand.reshape(-1,1)
tw = tw.reshape(-1,1)

tfrpo = 2*32.80617425
tfrand = 200
tftw = 180

mfilesdir = os.getcwd()
oct2py.octave.addpath(mfilesdir)
	
xsolrpored, usolrpored, t1red, taured = oct2py.octave.ksETDRK4red(rpo, tfrpo)
xsolrpo, usolrpo, t1 = oct2py.octave.ksETDRK4(rpo, tfrpo)
	
xsoltwred, usoltwred, ttwred, tautwred = oct2py.octave.ksETDRK4red(tw, tftw)
xsoltw, usoltw, ttw = oct2py.octave.ksETDRK4(tw, tftw)

xsolrandred, usolrandred, t2red = oct2py.octave.ksETDRK4red(xrand, tfrand)
xsolrand, usolrand, t2 = oct2py.octave.ksETDRK4(xrand, tfrand)

#raw_input('press any key')

#Plot full state space:

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.w_xaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_yaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_zaxis.set_pane_color((1, 1, 1, 1.0))

ax.plot(xsolrand[:,0], xsolrand[:,2], xsolrand[:,3], linewidth=0.5, color='#3c5f96')
ax.hold(True)
ax.plot(xsolrpo[:,0], xsolrpo[:,2], xsolrpo[:,3], linewidth=0.8, color='#f7464a')
ax.plot(xsoltw[:,0], xsoltw[:,2], xsoltw[:,3], linewidth=0.5, color='#e500e5')

ax.set_xlabel('$x_1$', fontsize=24)
ax.set_ylabel('$x_2$', fontsize=24)
ax.set_zlabel('$y_2$', fontsize=24)

Nticks = 4

xticks = np.linspace(-0.4, 0.4, Nticks)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%.1f$" % xtik for xtik in xticks], fontsize=16); # use LaTeX formatted labels

yticks = np.linspace(-0.8, 0.4, Nticks)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], fontsize=16); # use LaTeX formatted labels

zticks = np.linspace(-0.6, 0.6, Nticks)
ax.set_zticks(zticks)
ax.set_zticklabels(["$%.1f$" % ztik for ztik in zticks], fontsize=16); # use LaTeX formatted labels

ax.view_init(30,30)
savefig('ks1.pdf', bbox_inches='tight', dpi=100)
savefig('ks1.png', bbox_inches='tight', dpi=150)

#call(['pdfcrop', "twomode1.pdf", "twomode1.pdf"])
call(['convert', '-trim', "ks1.png", "ks1.png"])

#Plot reduced state space:
fig.clf()
ax = fig.gca(projection='3d')
ax.w_xaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_yaxis.set_pane_color((1, 1, 1, 1.0))
ax.w_zaxis.set_pane_color((1, 1, 1, 1.0))

ax.plot(xsolrandred[:,0], xsolrandred[:,2], xsolrandred[:,3], linewidth=0.5, color='#3c5f96')
ax.hold(True)
ax.plot(xsolrpored[:,0], xsolrpored[:,2], xsolrpored[:,3], linewidth=1, color='#f7464a')
ax.plot(xsoltwred[:,0], xsoltwred[:,2], xsoltwred[:,3], linewidth=1, color='#e500e5')

ax.set_xlabel('$x_1$', fontsize=22)
ax.set_ylabel('$x_2$', fontsize=22)
ax.set_zlabel('$y_2$', fontsize=22)

xticks = np.linspace(0, 0.4, Nticks)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%.1f$" % xtik for xtik in xticks], fontsize=16); # use LaTeX formatted labels

yticks = np.linspace(-0.6, 0.6, Nticks)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % ytik for ytik in yticks], fontsize=16); # use LaTeX formatted labels

zticks = np.linspace(-0.3, 0.6, Nticks)
ax.set_zticks(zticks)
ax.set_zticklabels(["$%.1f$" % ztik for ztik in zticks], fontsize=16); # use LaTeX formatted labels

ax.view_init(-165,-165)
savefig('ks2.pdf', bbox_inches='tight', dpi=100)
savefig('ks2.png', bbox_inches='tight', dpi=150)

#call(["pdfcrop", "twomode2.pdf", "twomode2.pdf"])
call(['convert', '-trim', "ks2.png", "ks2.png"])

plt.close()

fig = plt.figure() #Create a figure instance
