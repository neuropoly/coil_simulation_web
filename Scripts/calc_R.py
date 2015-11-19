# coding=utf-8
#function [R]=calc_R(A,ne,radc,xpmin,xpmax,px,ypmin,ypmax,py,zpmin,zpmax,pz)
#
#
# This function calculates the mutual impedence caused by sample
# A = magnetic potential vector
# ne = number of elements
# radc = cylinder radius
# xpmin,xpmax,px,ypmin,ypmax,py,zpmin,zpmax,pz = request limits and precision 
# R = matrix 2-D

import numpy as np
from scipy import math
PI = np.pi

"""Define physics constants of the coils"""
u0=4*PI*(10**-7) #relative permitivity for air
N=100 #points used to define coil
I=1 #constant current distribution in each coil
cond=0.7 #define conductivity
freq=123.2*10**6 #define frequency
omega=2*PI*freq #define omega

"""This function computes the B1 magnetic field and magentic potential vector"""

def calc_R(A, ne, radc, axis_dict):

    x_len = (axis_dict['Xmax'] - axis_dict['Xmin']) / axis_dict['Xprec']
    y_len = (axis_dict['Ymax'] - axis_dict['Ymin']) / axis_dict['Yprec']
    z_len = (axis_dict['Zmax'] - axis_dict['Zmin']) / axis_dict['Zprec']

    x_sample = np.zeros(x_len)
    y_sample = np.zeros(y_len)
    z_sample = np.zeros(z_len)

    for i in range(x_len):
        x_sample[i] = axis_dict['Xmin'] + i*axis_dict['Xprec']
    for i in range(y_len):
        y_sample[i] = axis_dict['Ymin'] + i*axis_dict['Yprec']
    for i in range(z_len):
        z_sample[i] = axis_dict['Zmin'] + i*axis_dict['Zprec']


    #Msk(1:size(xsample),1,1:size(zsample))=ones

    Msk = np.ones((x_sample, 1, z_sample))

    #size(1) = dimension du deuxième element de Msk
    size_msk = np.shape(Msk)
    size_xs = np.shape(x_sample)
    size_zs = np.shape(z_sample)

    Mskd = np.zeros((x_sample, z_sample))
    Mskf = np.zeros((x_sample, z_sample))

    A_temp = np.reshape(A, (x_len, 1, z_len, ne))

    Ai = np.zeros((x_len, z_len))
    Aj = np.zeros((x_len, z_len))

    g = np.zeros((size_xs(1), size_zs(1)))

    """definition of the mask"""
    for k in size_msk(1):
        Mskd[:,:] = Msk[:,k,:]

        for i in size_xs(1):
            for j in size_zs(1):
                d = np.sqrt((x_sample(i)-0)**2+(z_sample(j)-radc)^2) #pourquoi le -0 ???
                if d <= radc:
                    g[i, j]=1
                else:
                    g[i, j]=0




        Mskf= np.cross(Mskd, g)

        h=1
        size_mskf = np.shape(Mskf)
        for i in size_mskf:
            for j in size_mskf(1):
                if  Mskf[i,j]!=0:
                    Xprec(h)=i
                    Yprec(h)=j
                    h=h+1





    # compute R
    R = np.zeros((ne, ne))
    for i in ne:
        for j in ne:
            Ai[:,:] = A_temp[:,1,:,i]
            Aj[:,:] = A_temp[:,1,:,j]

            cAi = np.cross(Ai, Mskf)
            cAj = np.cross(Aj, Mskf)
            result = np.cross(cAj, cAi)
            #integrate over mask
            R[i][j] = cond*(omega**2)*(sum((sum((result)))))

    return R


