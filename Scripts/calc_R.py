
"""This function calculates the mutual impedence caused by sample"""


import numpy as np
from scipy import math

PI = np.pi

"""Define physics constants of the coils"""
u0 = 4 * PI * (10 ** -7)  # relative permitivity for air
N = 100  # points used to define coil
I = 1  # constant current distribution in each coil
cond = 0.7  # define conductivity
freq = 123.2 * 10 ** 6  # define frequency
omega = 2 * PI * freq  # define omega


"""This function computes the B1 magnetic field and magentic potential vector"""


def calc_R(A, ne, radc, axis_dict):
    x_len = int((axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec'])
    y_len = int((axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec'])
    z_len = int((axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec'])

    x_sample = np.zeros(x_len)
    y_sample = np.zeros(y_len)
    z_sample = np.zeros(z_len)

    for i in range(x_len):
        x_sample[i] = axis_dict['Xmin'] + i * axis_dict['Xprec']
    for i in range(y_len):
        y_sample[i] = axis_dict['Ymin'] + i * axis_dict['Yprec']
    for i in range(z_len):
        z_sample[i] = axis_dict['Zmin'] + i * axis_dict['Zprec']


    Msk = np.ones((x_len,  1, z_len))

    # size(1) = Dimension of second element of mask
    size_msk = np.shape(Msk)
    size_xs = np.shape(x_sample)
    size_zs = np.shape(z_sample)

    Mskd = np.zeros((x_len, z_len))
    Mskf = np.zeros((x_len, z_len))

    Ai = np.zeros((x_len, z_len))
    Aj = np.zeros((x_len, z_len))

    g = np.zeros((size_xs[0], size_zs[0]))

    """definition of the mask"""
    for k in range(size_msk[1]):
        Mskd[:, :] = Msk[:, k, :]

        for i in range(size_xs[0]):
            for j in range(size_zs[0]):
                d = np.sqrt(x_sample[i] ** 2 + (z_sample[j] - radc) ** 2)
                if d <= radc:
                    g[i, j] = 1
                else:
                    g[i, j] = 0

        Mskf = Mskd * g

    """compute R"""
    R = np.zeros((ne, ne))
    for i in range(ne):
        for j in range(ne):
            Ai[:, :] = A[:, 1, :]
            Aj[:, :] = A[:, 1, :]

            cAi = Ai * Mskf
            cAj = Aj * Mskf
            result = cAj * cAi
            """integrate over mask"""
            R[i][j] = cond * (omega ** 2) * (sum((sum(result))))

    return R
