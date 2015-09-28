import numpy as np
from scipy import math
PI = np.pi

"""Define physics constants of the coils"""
u0=4*PI*(10**-7) #relative permitivity for air
N=100 #points used to define coil
I=1 #constant current distribution in each coil
cond=0.7 #define conductivity
freq=123.2*10**6 #define frequency

"""This function computes the B1 magnetic field and magentic potential vector"""

def calc_field(arrays_list, axis_dict, ne, N=100):

    """Define each axis length"""
    x_len = (axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec']
    y_len = (axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec']
    z_len = (axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec']

    x_matrix = np.zeros((x_len, y_len, z_len))
    y_matrix = np.zeros((x_len, y_len, z_len))
    z_matrix = np.zeros((x_len, y_len, z_len))

    """Generate mesh that will contain the magnetic field matrix. Mesh contains all the
    values of the axis for X, Y, Z."""
    for i in range(x_len):
        for j in range(y_len):
            for k in range(z_len):
                x_matrix[i][j][k] = axis_dict['Xmin'] + i*axis_dict['Xprec']
    for i in range(y_len):
        for j in range(x_len):
            for k in range(z_len):
                y_matrix[j][i][k] = axis_dict['Ymin'] + i*axis_dict['Yprec']
    for i in range(z_len):
        for j in range(x_len):
            for k in range(y_len):
                z_matrix[j][k][i] = axis_dict['Zmin'] + i*axis_dict['Zprec']

    """Declaring r and dl vectors for future Biot-Savart computation"""
    r = np.zeros((N, 3))
    dl = np.zeros((N, 3))
    dl_cross_r = np.zeros((N, 3))
    norm_r = np.zeros((N, 1))

    for a in range(x_len):
        for b in range(y_len):
            for c in range(z_len):
                for i in range(N-1):
                    """Computes vector R between point on the coil and the observation point
                    We use the middle point between each point of the coil's array"""
                    r[i][0] = (x_matrix[a, b, c] - (0.5*(arrays_list[ne][i][0]+arrays_list[ne][i+1][0])))
                    r[i][1] = (y_matrix[a, b, c] - (0.5*(arrays_list[ne][i][1]+arrays_list[ne][i+1][1])))
                    r[i][2] = (z_matrix[a, b, c] - (0.5*(arrays_list[ne][i][2]+arrays_list[ne][i+1][2])))

                    """Computes vector dl along the coil in direction of flow of current
                    We use the middle point between each point of the coil's array"""
                    dl[i][0] = arrays_list[ne][i+1][0]+arrays_list[ne][i][0]
                    dl[i][1] = arrays_list[ne][i+1][1]+arrays_list[ne][i][1]
                    dl[i][2] = arrays_list[ne][i+1][2]+arrays_list[ne][i][2]

                """We compute vectors between final and initial points outside of the loop"""
                r[N-1][0] = (x_matrix[a, b, c] - (0.5*(arrays_list[ne][N-1][0]+arrays_list[ne][0][0])))
                r[N-1][1] = (y_matrix[a, b, c] - (0.5*(arrays_list[ne][N-1][1]+arrays_list[ne][0][1])))
                r[N-1][2] = (z_matrix[a, b, c] - (0.5*(arrays_list[ne][N-1][2]+arrays_list[ne][0][2])))

                dl[N-1][0] = arrays_list[ne][N-1][0]+arrays_list[ne][0][0]
                dl[N-1][1] = arrays_list[ne][N-1][1]+arrays_list[ne][0][1]
                dl[N-1][2] = arrays_list[ne][N-1][2]+arrays_list[ne][0][2]
    """Computing dl cross r and norm of r"""
    for i in range(N):
        dl_cross_r[i] = np.cross(r[i], dl[i])
        norm_r[i] = np.linalg.norm(r[i])
    
    """Biot-Savart's law analytical resolution"""
    A_tmp = np.divide(I*u0, np.power(norm_r, 3))
    B1_tmp = np.multiply(A_tmp, dl_cross_r)

    B1x_sum = np.zeros((x_len, y_len, z_len))
    B1y_sum = np.zeros((x_len, y_len, z_len))
    B1z_sum = np.zeros((x_len, y_len, z_len))

    Ax_sum = np.zeros((x_len, y_len, z_len))
    Ay_sum = np.zeros((x_len, y_len, z_len))
    Az_sum = np.zeros((x_len, y_len, z_len))

    for a in range(x_len):
        for b in range(y_len):
            for c in range(z_len):
                for i in range(N):
                    B1x_sum[a, b, c] = B1x_sum[a, b, c] + B1_tmp[i, 0]
                    B1y_sum[a, b, c] = B1y_sum[a, b, c] + B1_tmp[i, 1]
                    B1z_sum[a, b, c] = B1z_sum[a, b, c] + B1_tmp[i, 2]
                    Ax_sum[a, b, c] = Ax_sum[a, b, c] + A_tmp[i]
                    Ay_sum[a, b, c] = Ay_sum[a, b, c] + A_tmp[i]
                    Az_sum[a, b, c] = Az_sum[a, b, c] + A_tmp[i]

    B1 = np.zeros(x_len)
    A = np.zeros(x_len)

    B1 = np.sqrt(np.power(B1x_sum, 2) + np.power(B1y_sum, 2) + np.power(B1z_sum, 2))
    A = np.sqrt(np.power(Ax_sum, 2) + np.power(Ay_sum, 2) + np.power(Az_sum, 2))
