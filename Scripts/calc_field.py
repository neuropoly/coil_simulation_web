import numpy as np
from scipy import math
PI = np.pi

"""Define physics constants of the coils"""
u0 = 4*PI*(10**-7)  # relative permittivity for air
coil_definition = 100  # points used to define coil
I = 1.0  # constant current distribution in each coil
cond = 0.7  # define conductivity
freq = 123.2*10**6  # define frequency

"""This function computes the B1 magnetic field and magentic potential vector"""


def calc_field(arrays_list, axis_dict, nb_elem, coil_definition = 100):
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
    for i in range(y_len):
        y_matrix[:, i, :] = axis_dict['Ymin'] + i*axis_dict['Yprec']
    for i in range(z_len):
        z_matrix[:, :, i] = axis_dict['Zmin'] + i*axis_dict['Zprec']

    """Declaring r and dl vectors for future Biot-Savart computation"""
    r = np.zeros((3, coil_definition))

    dl = np.zeros((3, coil_definition))
    dl_cross_r = np.zeros((3, coil_definition))
    norm_r = np.zeros(coil_definition)

    B1x_sum = np.zeros((x_len, y_len, z_len))
    B1y_sum = np.zeros((x_len, y_len, z_len))
    B1z_sum = np.zeros((x_len, y_len, z_len))

    Ax_sum = np.zeros((x_len, y_len, z_len))
    Ay_sum = np.zeros((x_len, y_len, z_len))
    Az_sum = np.zeros((x_len, y_len, z_len))
    for a in range(x_len):
        for b in range(y_len):
            for c in range(z_len):
                for i in range(coil_definition-1):
                    """Computes vector R between point on the coil and the observation point
                    We use the middle point between each point of the coil's array"""
                    r[0, i] = (x_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][i][0]+arrays_list[nb_elem][i+1][0])))
                    r[1, i] = (y_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][i][1]+arrays_list[nb_elem][i+1][1])))
                    r[2, i] = (z_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][i][2]+arrays_list[nb_elem][i+1][2])))

                    """Computes vector dl along the coil in direction of flow of current
                    We use the middle point between each point of the coil's array"""
                    dl[0, i] = arrays_list[nb_elem][i+1][0]+arrays_list[nb_elem][i][0]
                    dl[1, i] = arrays_list[nb_elem][i+1][1]+arrays_list[nb_elem][i][1]
                    dl[2, i] = arrays_list[nb_elem][i+1][2]+arrays_list[nb_elem][i][2]

                """We compute vectors between final and initial points outside of the loop"""
                r[0, coil_definition-1] = (x_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][coil_definition-1][0]+arrays_list[nb_elem][0][0])))
                r[1, coil_definition-1] = (y_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][coil_definition-1][1]+arrays_list[nb_elem][0][1])))
                r[2, coil_definition-1] = (z_matrix[a, b, c] - (0.5*(arrays_list[nb_elem][coil_definition-1][2]+arrays_list[nb_elem][0][2])))

                dl[0, coil_definition-1] = arrays_list[nb_elem][coil_definition-1][0]+arrays_list[nb_elem][0][0]
                dl[1, coil_definition-1] = arrays_list[nb_elem][coil_definition-1][1]+arrays_list[nb_elem][0][1]
                dl[2, coil_definition-1] = arrays_list[nb_elem][coil_definition-1][2]+arrays_list[nb_elem][0][2]
                """Computing dl cross r and norm of r"""
                for i in range(coil_definition):
                    dl_cross_r[:, i] = np.cross(dl[:, i], r[:, i])
                    # dl_cross_r[0, i] = dl[1, i] * r[2, i] - dl[2, i] * r[1, i]
                    # dl_cross_r[1, i] = dl[2, i] * r[0, i] - dl[0, i] * r[2, i]
                    # dl_cross_r[2, i] = dl[0, i] * r[1, i] - dl[1, i] * r[0, i]
                    norm_r[i] = np.linalg.norm(r[:, i])

                    B1x_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm_r[i], 3)), dl_cross_r[0, i])
                    B1y_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm_r[i], 3)), dl_cross_r[1, i])
                    B1z_tmp = np.multiply(np.divide(I*u0, 4*PI*np.power(norm_r[i], 3)), dl_cross_r[2, i])
                    B1x_sum[a, b, c] = B1x_sum[a, b, c] + B1x_tmp[i]
                    B1y_sum[a, b, c] = B1y_sum[a, b, c] + B1y_tmp[i]
                    B1z_sum[a, b, c] = B1z_sum[a, b, c] + B1z_tmp[i]

                """Biot-Savart's law analytical resolution"""
                # A_tmp = np.divide(float(I*u0), 4.0*PI*norm_r)

                """for i in range(coil_definition):
                    B1x_sum[a, b, c] = B1x_sum[a, b, c] + B1x_tmp[i]
                    B1y_sum[a, b, c] = B1y_sum[a, b, c] + B1y_tmp[i]
                    B1z_sum[a, b, c] = B1z_sum[a, b, c] + B1z_tmp[i]
                    Ax_sum[a, b, c] = Ax_sum[a, b, c] + A_tmp[i]
                    Ay_sum[a, b, c] = Ay_sum[a, b, c] + A_tmp[i]
                    Az_sum[a, b, c] = Az_sum[a, b, c] + A_tmp[i]"""

    B1 = np.zeros((x_len, y_len, z_len))
    A = np.zeros((x_len, y_len, z_len))

    B1 = np.sqrt(np.power(B1x_sum, 2) + np.power(B1y_sum, 2) + np.power(B1z_sum, 2))
    A = np.sqrt(np.power(Ax_sum, 2) + np.power(Ay_sum, 2) + np.power(Az_sum, 2))

    print(B1)
    return B1, A