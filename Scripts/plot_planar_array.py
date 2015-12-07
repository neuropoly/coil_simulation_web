
"""This function diplay the coil"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import math
from mpl_toolkits.mplot3d import Axes3D


def plot_planar_array(nb_elem, arrays_list, N, output_file):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = 0
    for n in range(nb_elem):
        for i in range(N):
            xs = arrays_list[n][i][0]
            ys = arrays_list[n][i][1]
            zs = arrays_list[n][i][2]
            ax.scatter(xs, ys, zs)

    ax.set_xlabel('X axis [m]')
    ax.set_ylabel('Y axis [m]')
    ax.set_zlabel('Z axis [m]')
    ax.set_title('Elements distribution around a cylinder')

    plt.savefig(output_file)