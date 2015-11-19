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

# TODO make the function compile with the rest of the code. As of 15/11/16, this script is not tested or used.


def create_wrapped_elem(radc, ne):
    ang = np.linspace(-PI/2, PI/2, ne+2)
    size = np.shape(ang)
    angelem = np.array([[0 for j in range(ne+2)] for j in range(1)])

    for i in size(1):
        angelem[1][i] = ang[1][i+1]

    newxpos = math.sin(angelem)*radc

    """the new X position of the element"""
    return newxpos
