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
    x_len = (axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec']
    y_len = (axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec']
    z_len = (axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec']

    x_matrix = np.zeros((x_len, y_len, z_len))
    y_matrix = np.zeros((x_len, y_len, z_len))
    z_matrix = np.zeros((x_len, y_len, z_len))

    """Generate mesh"""
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

    r = np.zeros((N, 3))
    dl = np.zeros((N, 3))
    dl_cross_r = np.zeros((N, 3))
    norm_r = np.zeros((N, 1))

    for a in range(x_len):
        for b in range(y_len):
            for c in range(z_len):
                for i in range(N-2):
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

                for i in range(N):
                    dl_cross_r[i] = np.cross(r[i], dl[i])

                for i in range(N):
                    norm_r[i] = np.linalg.norm(r[i])

                """B1tmp = np.multiply(1/(4*PI*(norm_r**3)), (I*u0))
                B1tmp = np.multiply(B1tmp, dl_cross_r)
                Atmp = np.multiply(1/(4*PI*(norm_r)), (I*u0))"""