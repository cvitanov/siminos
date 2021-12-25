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

#mpl.rcParams['text.usetex']=True
#mpl.rcParams['text.latex.unicode']=True

from subprocess import call

rpo = np.array([3.70955584e-01,   1.59178104e-16,  -5.35414753e-01,   6.72233738e-01,
  -1.60102241e-01,   2.77492997e-01,   2.26119482e-01,   9.20202541e-02,
   1.01234154e-01,  -7.61348435e-02,   2.86999279e-03,  -5.71633872e-02,
  -2.19911067e-02,  -8.45432215e-03,  -9.70953085e-03,   5.74786687e-03,
   4.19544211e-04,   4.07227658e-03,   1.61695688e-03,   7.51275352e-04,
   5.51797781e-04,  -3.99001588e-04,  -2.26058837e-05,  -2.53441206e-04,
  -9.51845395e-05,  -3.49971067e-05,  -2.92711613e-05,   2.18049965e-05,
   5.41318900e-07,   1.12892181e-05], float)

rpo = np.array([3.75553820268049e-01, 5.00145471949682e-16, -1.16318112762086e-01,
  -2.75138291542745e-01, 4.98014744888981e-01, -2.61084549544602e-01,
   2.63249305002884e-02, 5.47881940614808e-02, 6.79067693226824e-02,
  -7.77434443829294e-02, 4.61139194205068e-02, 3.40247311597782e-02,
  -2.80026309458154e-03, 1.23863730919248e-03, 7.32296341258055e-03,
   1.65527969386703e-03, -5.23679491319272e-04, 2.77682791610979e-03,
   8.63573372755388e-05, -1.44474346812293e-04, 9.75826098379168e-05,
   3.78079166279577e-04, -1.10511584069682e-04, 2.64149399587027e-05,
   1.26640502043697e-05, 6.47700765741692e-06, -1.26600135032373e-05,
   1.08301101019014e-05, -1.32808096113333e-06, -2.79469850392735e-06], float)

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

tw = np.array([4.35443492272889e-01,    1.56040561014516e-12,    3.55754047628953e-01,
   3.69921945204375e-02,    2.65780537994421e-01,    1.23087719538253e-01,
   8.96316902608692e-02,    1.99746515999728e-01,   -5.05278191532214e-02,
   9.44414665319479e-02,   -3.97381527756165e-02,    1.50718395267157e-02,
  -1.69870689945677e-02,   -4.78697651628193e-03,   -4.29875817119712e-03,
  -6.15071731992920e-03,    3.91009855849272e-04,   -3.00082828998765e-03,
   8.69743855563895e-04,   -7.44157808695376e-04,    4.23666106072728e-04,
   2.32645089559688e-07,    1.19213221322225e-04,    1.01450332712896e-04,
   8.49941411591540e-06,    5.65307999135711e-05,   -1.12226349740213e-05,
   1.68333813386732e-05,   -6.47368700833886e-06,    9.28176293446561e-07], float)

rpo = rpo.reshape(-1,1)
xrand = xrand.reshape(-1,1)
tw = tw.reshape(-1,1)

tfrpo = 2*32.80617425
tfrpo = 2*33.5010341720007
tfrand = 200
tftw = 200

mfilesdir = os.getcwd()
oct2py.octave.addpath(mfilesdir)
	
xsolrpored, usolrpored, trpored, taurpored = oct2py.octave.ksETDRK4red(rpo, tfrpo)

xsoltwred, usoltwred, ttwred, tautwred = oct2py.octave.ksETDRK4red(tw, tftw)

#xsolrandred, usolrandred, trandred, taurandred = oct2py.octave.ksETDRK4red(xrand, tfrand)

#Reshapa tau to 1D:
taurpored = taurpored.reshape(np.size(taurpored))
tautwred = tautwred.reshape(np.size(tautwred))
#taurandred = taurandred.reshape(np.size(taurandred))

trpored = trpored.reshape(np.size(trpored))

ttwred = ttwred.reshape(np.size(ttwred))

#trandred = trandred.reshape(np.size(trandred))

#raw_input('press any key')

fig = plt.figure(figsize=(3, 6)) #Create a figure instance

#Plot rpo red:

x = np.arange(-np.size(usolrpored, 1)/2, np.size(usolrpored, 1)/2)
y = taurpored[range(0,np.size(taurpored),10)]

im = plt.pcolormesh(x, y, usolrpored[range(0,np.size(taurpored),10),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=32)
plt.ylabel('$\hat{\\tau}$', fontsize=32)

ax = plt.gca()
ax.yaxis.set_label_coords(-0.25, 0.6)

taufrpo = taurpored[-1]
	
#plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=24)
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$0$', '$L/2$', '$L$'), fontsize=24)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]],
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
plt.yticks([0,taufrpo/2,taufrpo],
('$'+str(0)+'$', '$'+str(taufrpo/2)[0:5]+'$', '$'+str(taufrpo)[0:5]+'$'), fontsize=24)
#plt.yticks([0,taufrpo/2,taufrpo], ('', '', ''))
#fig.text(-0.22, 0.0, '$(f)$', fontsize=32)
#savefig('ksconfrporedtau.pdf', bbox_inches='tight', dpi=10)
savefig('ksconfrporedtau.png', bbox_inches='tight', dpi=264)

fig.clf()

#Plot tw red:

x = np.arange(-np.size(usoltwred, 1)/2, np.size(usoltwred, 1)/2)
y = tautwred[range(0,np.size(tautwred),10)]

im = plt.pcolormesh(x, y, usoltwred[range(0,np.size(tautwred),10),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=32)
#plt.ylabel(r'$\hat{\tau}$', fontsize=32)
plt.ylabel('$\hat{\\tau}$', fontsize=32)

ax = plt.gca()
ax.yaxis.set_label_coords(-0.25, 0.6)
	
tauftw = tautwred[-1]
	
#plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=24)
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$0$', '$L/2$', '$L$'), fontsize=24)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]],
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
plt.yticks([0,tauftw/2,tauftw],
('$'+str(0)+'$', '$'+str(np.floor(tauftw/2))+'$', '$'+str(tauftw)+'$'), fontsize=24)
#plt.yticks([0,tauftw/2,tauftw], ('', '', ''))

#savefig('ksconftwredtau.pdf', bbox_inches='tight', dpi=10)
#fig.text(-0.22, 0.0, '$(c)$', fontsize=32)
savefig('ksconftwredtau.png', bbox_inches='tight', dpi=264)


#fig.clf()

#Plot rand red:

#x = np.arange(-np.size(usolrandred, 1)/2, np.size(usolrandred, 1)/2)
#y = taurandred[range(0,np.size(taurandred),10)]

#im = plt.pcolormesh(x, y, usolrandred[range(0,np.size(taurandred),10),:], shading='gouraud')

#plt.axis([x.min(), x.max(), y.min(), y.max()])

#plt.xlabel('$x$', fontsize=32)
#plt.ylabel(r'$\hat{\tau}$', fontsize=32)

#taufrand = taurandred[-1]
	
##plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=24)
#plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$0$', '$L/2$', '$L$'), fontsize=24)
##plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]],
##('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:3]+'$', '$'+str(y[-1])[0:3]+'$'))
#plt.yticks([0,taufrand/2,taufrand],
#('$'+str(0)+'$', '$'+str(np.floor(taufrand/2))+'$', '$'+str(taufrand)+'$'), fontsize=24)
##plt.yticks([0,taufrand/2,taufrand], ('', '', ''))

##savefig('ksconfrandredtau.pdf', bbox_inches='tight', dpi=10)
#savefig('ksconfrandredtau.png', bbox_inches='tight', dpi=100)

#fig.clf()

#plt.show()
