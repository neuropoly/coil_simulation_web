__author__ = 'Pier-Luc'
import numpy as np

def image_slice_B1(B1f):
    B1f = np.transpose(B1f)
    top = np.size(B1f,1)