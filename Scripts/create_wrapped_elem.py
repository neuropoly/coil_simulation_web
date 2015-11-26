#function [xelem]=create_wrapped_elem(radc,ne)
#
# This function returns the new X position of the element around the cylinder:
# radc = cylinder radius
# ne = the number of elements
#size = np.shape(xsample)
#size(0) = dimension du premier element de xsample

import numpy as np
import math

PI = math.pi

"""angle generation between -180 to 180 degrees"""

def create_wrapped_elem(radc, ne):
    ang = np.linspace(-PI/2, PI/2, ne+2)
    size = np.shape(ang)
    angelem = np.zeros(ne)

    for i in range(2, size[0] - 1):
        angelem[i-1] = ang[i]

    newxpos = np.sin(angelem)*radc

    """the new X position of the element"""
    return newxpos
