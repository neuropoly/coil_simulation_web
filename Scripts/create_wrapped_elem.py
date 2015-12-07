
"""This function returns the new X position of the element around the cylinder"""

import numpy as np
import math

PI = math.pi

"""angle generation between -180 to 180 degrees"""

def create_wrapped_elem(radc, ne):
    ang = np.linspace(-PI/2, PI/2, ne+2)
    size = np.shape(ang)
    angelem = np.zeros(ne)


    for i in range(1, size[0]-1):
        angelem[i-1] = ang[i]

    newxpos = np.sin(angelem)*radc

    """the new X position of the element"""
    return newxpos
