# function [SNR]=calc_SNR(B1,ne,R)
#
# This function computes the SNR

import numpy as np
import calc_R
from scipy import math

PI = np.pi


def calc_SNR(B1, ne, R, axis_dict):
    x_len = (axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec']
    y_len = (axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec']
    z_len = (axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec']

    B1_temp = np.reshape(B1, (x_len, 1, z_len, ne))
    size = np.shape(B1_temp)
    B = np.zeros(ne, 1)

    SNR = np.zeros(size(0), size(2))

    for i in size(0):
        for j in size(2):
            for k in ne:
                B[k, 1] = B1_temp[i, 1, j, k]

            R_inv = np.linalg.inv(R)
            SR = np.sqrt(R_inv * B)
            SR_tran = SR.transpose()
            B_conj = np.conjugate(B)
            SNR[i, j] = SR_tran * B_conj
    return SNR
