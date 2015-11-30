__author__ = 'Pier-Luc'

#######################################################################################
# funky 2d plot
# LINK: http://matplotlib.org/examples/pylab_examples/hist2d_log_demo.html
#######################################################################################

# from matplotlib.colors import LogNorm
# from pylab import *
#
# #normal distribution center at x=0 and y=5
# x = randn(100000)
# y = randn(100000)+10
#
# hist2d(x, y, bins=40, norm=LogNorm())
# colorbar()
# show()

#######################################################################################
# stack overflow example :
# LINK: http://stackoverflow.com/questions/13384653/imshow-extent-and-aspect
#######################################################################################

import matplotlib.pyplot as plt
import numpy as np

grid = np.random.random((10,10))
print("grid :", grid)

fig, (ax1) = plt.subplots(nrows=1, figsize=(6,10))

ax1.imshow(grid, extent=[-10,10,0,20], aspect=1)
ax1.set_title('Manually Set Aspect')

plt.tight_layout()
plt.show()

#######################################################################################
# TEST
#######################################################################################

print( "B1f !!!!!: ", B1f.shape)
fig, (ax1) = plt.subplots(nrows=1, figsize=(6,10))

img = ax1.imshow(B1f, extent=[x_axis_min,x_axis_max,z_axis_min,z_axis_max], aspect=1)
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)
ax1.set_title('B1 Sensitivity Profile')
ax1.set_xlabel('X Axis [cm]', fontsize=18, labelpad=20)
ax1.set_ylabel('Z Axis [cm]', fontsize=16, labelpad=20)
plt.tight_layout()
cbar = fig.colorbar(img, cax=cax)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('[Tesla]')
plt.show()