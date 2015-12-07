
"""This function computes the SNR"""

import numpy as np
import calc_R
from scipy import math

PI = np.pi


def calc_SNR(B1, ne, R, axis_dict):

    size = np.shape(B1)
    B = np.zeros((ne, 1))

    SNR = np.zeros((size[0], size[2]))

    for i in range(size[0]):
        for j in range(size[2]):
            for k in range(ne):
                B[k, 1] = B1[i, 1, j]

            R_inv = np.linalg.inv(R)
            SR = np.sqrt(R_inv * B)
            SR_tran = SR.transpose()
            B_conj = np.conjugate(B)
            SNR[i, j] = SR_tran * B_conj
    return SNR
