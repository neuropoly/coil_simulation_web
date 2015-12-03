import numpy as np
from scipy import math
PI = np.pi

"""Define physics constants of the coils"""
u0 = 4*PI*(10**-7)  # relative permittivity for air
I = 1.0  # constant current distribution in each coil
cond = 0.7  # define conductivity
freq = 123.2*10**6  # define frequency

"""This function computes the B1 magnetic field and magentic potential vector"""


def calc_field(arrays_list, axis_dict, nb_elem, coil_definition):
    """Define each axis length"""

    x_len = int((axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec'])
    y_len = int((axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec'])
    z_len = int((axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec'])

    x_matrix = np.zeros((x_len, y_len, z_len))
    y_matrix = np.zeros((x_len, y_len, z_len))
    z_matrix = np.zeros((x_len, y_len, z_len))

    """Generate mesh that will contain the magnetic field matrix. Mesh contains all the
    values of the axis for X, Y, Z."""
    for i in range(x_len):
        x_matrix[i, :, :] = axis_dict['Xmin'] + i*axis_dict['Xprec']
    for l in range(y_len):
        y_matrix[:, l, :] = axis_dict['Ymin'] + l*axis_dict['Yprec']
    for k in range(z_len):
        z_matrix[:, :, k] = axis_dict['Zmin'] + k*axis_dict['Zprec']

    """Declaring r and dl vectors for future Biot-Savart computation"""
    r = np.zeros(3)  # , coil_definition))

    dl = np.zeros(3)  # , coil_definition))

    b1x_sum = np.zeros((x_len, y_len, z_len))
    b1y_sum = np.zeros((x_len, y_len, z_len))
    b1z_sum = np.zeros((x_len, y_len, z_len))

    ax_sum = np.zeros((x_len, y_len, z_len))
    ay_sum = np.zeros((x_len, y_len, z_len))
    az_sum = np.zeros((x_len, y_len, z_len))

    # TODO Verify outputs by cmparing with MATLAB results
    for a in range(x_len):
        for b in range(y_len):
            for c in range(z_len):
                for j in range(coil_definition - 1):
                    dl[0] = (0.5*(arrays_list[nb_elem][j][0]+arrays_list[nb_elem][j+1][0]))
                    dl[1] = (0.5*(arrays_list[nb_elem][j][1]+arrays_list[nb_elem][j+1][1]))
                    dl[2] = (0.5*(arrays_list[nb_elem][j][2]+arrays_list[nb_elem][j+1][2]))

                    r[0] = (x_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][j][0]+arrays_list[nb_elem][j+1][0])))
                    r[1] = (y_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][j][1]+arrays_list[nb_elem][j+1][1])))
                    r[2] = (z_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][j][2]+arrays_list[nb_elem][j+1][2])))

                    cross = np.cross(dl, r)
                    norm = np.linalg.norm(r)

                    b1x_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm, 3)), cross[0])
                    b1y_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm, 3)), cross[1])
                    b1z_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm, 3)), cross[2])
                    b1x_sum[a, b, c] = b1x_sum[a, b, c] + b1x_tmp
                    b1y_sum[a, b, c] = b1y_sum[a, b, c] + b1y_tmp
                    b1z_sum[a, b, c] = b1z_sum[a, b, c] + b1z_tmp

                    ax_tmp = np.divide(I*u0, 4*PI*np.power(norm, 3))
                    ay_tmp = np.divide(I*u0, 4*PI*np.power(norm, 3))
                    az_tmp = np.divide(I*u0, 4*PI*np.power(norm, 3))

                    ax_sum[a, b, c] = ax_sum[a, b, c] + ax_tmp
                    ay_sum[a, b, c] = ay_sum[a, b, c] + ay_tmp
                    az_sum[a, b, c] = az_sum[a, b, c] + az_tmp

    b1 = np.sqrt(np.power(b1x_sum, 2) + np.power(b1y_sum, 2) + np.power(b1z_sum, 2))
    a = np.sqrt(np.power(ax_sum, 2) + np.power(ay_sum, 2) + np.power(az_sum, 2))

    return b1, a