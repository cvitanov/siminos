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
tfrand = 200
tftw = 180

mfilesdir = os.getcwd()
oct2py.octave.addpath(mfilesdir)
	
xsolrpored, usolrpored, trpored, taurpored = oct2py.octave.ksETDRK4red(rpo, tfrpo)
xsolrpo, usolrpo, trpo = oct2py.octave.ksETDRK4(rpo, tfrpo)

xsoltwred, usoltwred, ttwred, tautwred = oct2py.octave.ksETDRK4red(tw, tftw)
xsoltw, usoltw, ttw = oct2py.octave.ksETDRK4(tw, tftw)

xsolrandred, usolrandred, trandred, taurandred = oct2py.octave.ksETDRK4red(xrand, tfrand)
xsolrand, usolrand, trand = oct2py.octave.ksETDRK4(xrand, tfrand)

#Reshapa tau to 1D:
taurpored = taurpored.reshape(np.size(taurpored))
tautwred = tautwred.reshape(np.size(tautwred))
taurandred = taurandred.reshape(np.size(taurandred))

trpored = trpored.reshape(np.size(trpored))
trpo = trpo.reshape(np.size(trpo))

ttwred = ttwred.reshape(np.size(ttwred))
ttw = ttw.reshape(np.size(ttw))

trandred = trandred.reshape(np.size(trandred))
trand = trand.reshape(np.size(trand))

#raw_input('press any key')

fig = plt.figure(figsize=(6, 6)) #Create a figure instance

#Plot rpo eqv:

x = np.arange(-np.size(usolrpo, 1)/2, np.size(usolrpo, 1)/2)
y = trpo[range(0,np.size(trpo),20)]

plt.subplot(1,2,1)

im = plt.pcolormesh(x, y, usolrpo[range(0,np.size(trpo),20),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
plt.ylabel('$t$', fontsize=24)
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
plt.yticks([0,tfrpo/2,tfrpo], 
('$'+str(0)+'$', '$'+str(tfrpo/2)[0:4]+'$', '$'+str(tfrpo)[0:4]+'$'), fontsize=16)

#savefig('ksconfrpo.pdf', bbox_inches='tight', dpi=10)
#savefig('ksconfrpo.png', bbox_inches='tight', dpi=100)

#fig.clf()

#Plot rpo red:

x = np.arange(-np.size(usolrpored, 1)/2, np.size(usolrpored, 1)/2)
y = trpored[range(0,np.size(trpored),20)]

plt.subplot(1,2,2)

im = plt.pcolormesh(x, y, usolrpored[range(0,np.size(trpored),20),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
#plt.ylabel('$t$', fontsize=16)
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
#plt.yticks([0,tfrpo/2,tfrpo], 
#('$'+str(0)+'$', '$'+str(tfrpo/2)[0:4]+'$', '$'+str(tfrpo)[0:4]+'$'))
plt.yticks([0,tfrpo/2,tfrpo], ('', '', ''))


savefig('ksconfrposub.pdf', bbox_inches='tight', dpi=10)
savefig('ksconfrposub.png', bbox_inches='tight', dpi=100)

fig.clf()

#Plot tw eqv:

x = np.arange(-np.size(usoltw, 1)/2, np.size(usoltw, 1)/2)
y = ttw[range(0,np.size(ttw),30)]

plt.subplot(1,2,1)

im = plt.pcolormesh(x, y, usoltw[range(0,np.size(ttw),30),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
plt.ylabel('$t$', fontsize=24)
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
plt.yticks([0,tftw/2,tftw], 
('$'+str(0)+'$', '$'+str(np.floor(tftw/2))+'$', '$'+str(tftw)+'$'), fontsize=16)

#savefig('ksconftw.pdf', bbox_inches='tight', dpi=10)
#savefig('ksconftw.png', bbox_inches='tight', dpi=100)

#fig.clf()

#Plot tw red:

x = np.arange(-np.size(usoltwred, 1)/2, np.size(usoltwred, 1)/2)
y = ttwred[range(0,np.size(ttwred),10)]

plt.subplot(1,2,2)

im = plt.pcolormesh(x, y, usoltwred[range(0,np.size(ttwred),10),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
#plt.ylabel('$t$', fontsize=16)
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:4]+'$', '$'+str(y[-1])[0:4]+'$'))
#plt.yticks([0,tftw/2,tftw], 
#('$'+str(0)+'$', '$'+str(np.floor(tftw/2))+'$', '$'+str(tftw)+'$'))
plt.yticks([0,tftw/2,tftw], ('', '', ''), fontsize=16)

savefig('ksconftwsub.pdf', bbox_inches='tight', dpi=10)
savefig('ksconftwsub.png', bbox_inches='tight', dpi=100)

fig.clf()

#Plot rand eqv:

x = np.arange(-np.size(usolrand, 1)/2, np.size(usolrand, 1)/2)
y = trand[range(0,np.size(trand),40)]

plt.subplot(1,2,1)

im = plt.pcolormesh(x, y, usolrand[range(0,np.size(trand),40),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
plt.ylabel('$t$', fontsize=24)
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:3]+'$', '$'+str(y[-1])[0:3]+'$'))
plt.yticks([0,tfrand/2,tfrand], 
('$'+str(0)+'$', '$'+str(np.floor(tfrand/2))+'$', '$'+str(tfrand)+'$'), fontsize=16)

#savefig('ksconfrand.pdf', bbox_inches='tight', dpi=10)
#savefig('ksconfrand.png', bbox_inches='tight', dpi=100)

#Plot rand red:

x = np.arange(-np.size(usolrandred, 1)/2, np.size(usolrandred, 1)/2)
y = trandred[range(0,np.size(trandred),70)]

plt.subplot(1,2,2)

im = plt.pcolormesh(x, y, usolrandred[range(0,np.size(trandred),70),:], shading='gouraud')

plt.axis([x.min(), x.max(), y.min(), y.max()])

plt.xlabel('$x$', fontsize=24)
#plt.ylabel('$t$')
	
plt.xticks([x[0],x[np.floor(np.size(x)/2)],x[-1]], ('$- L/2$', '$0$', '$L/2$'), fontsize=16)
#plt.yticks([y[0],y[np.floor(np.size(y)/2)],y[-1]], 
#('$'+str(y[0])[0:5]+'$', '$'+str(y[np.floor(np.size(y)/2)])[0:3]+'$', '$'+str(y[-1])[0:3]+'$'))
#plt.yticks([0,tfrand/2,tfrand], 
#('$'+str(0)+'$', '$'+str(np.floor(tfrand/2))+'$', '$'+str(tfrand)+'$'))
plt.yticks([0,tfrand/2,tfrand], ('', '', ''), fontsize=16)

savefig('ksconfrandsub.pdf', bbox_inches='tight', dpi=10)
savefig('ksconfrandsub.png', bbox_inches='tight', dpi=100)

fig.clf()

#plt.show()
