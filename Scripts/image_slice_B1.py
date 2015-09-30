__author__ = 'Pier-Luc'
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def image_slice_B1(B1f, axis_dict):

    fig, (ax1) = plt.subplots(nrows=1, figsize=(6,10))

    img = ax1.imshow(B1f, extent=[axis_dict['Xmin'],axis_dict['Xmax'],axis_dict['Zmin'],axis_dict['Zmax']], aspect=1)
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    ax1.set_title('B1 Sensitivity Profile')
    ax1.set_xlabel('X Axis [cm]', fontsize=16, labelpad=20)
    ax1.set_ylabel('Z Axis [cm]', fontsize=16, labelpad=20)
    plt.tight_layout()
    cbar = fig.colorbar(img, cax=cax)
    cbar.ax.set_ylabel('verbosity coefficient', labelpad=20)
    plt.show()