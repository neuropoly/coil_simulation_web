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
omega=2*pi*freq #define omega

"""This function computes the B1 magnetic field and magentic potential vector"""

def calc_R(A, ne, radc, Xmax, Xmin, Xprec, Ymax, Ymin, Yprec, Zmax, Zmin, Zprec):

#generate sample mask
#xsample=xpmin:px:xpmax;
#ysample=ypmin:py:ypmax;
#zsample=zpmin:pz:zpmax;

xsample = np.array(Xmin, Xprec, Xmax)
ysample = np.array(Ymin, Yprec, Ymax)
zsample = np.array(Zmin, Zprec, Zmax)


#Msk(1:size(xsample),1,1:size(zsample))=ones

Msk = np.ones(xsample, 1, xsample)

#size(1) = dimension du deuxième element de Msk
size_msk = np.shape(Msk)
size_xs = np.shape(xsample)
size_ys = np.shape(ysample)
size_zs = np.shape(zsample)



"""definition of the mask"""
for k in size_msk(1)
    #*** Mskd(:,:)=Msk(:,k,:)
	
    for i in size_xs(1)
        for j in size_zs(1)
            d = m.sqrt((xsample(i)-0)**2+(zsample(j)-radc)^2) #pourquoi le -0 ???
            if d <= radc
                g(i,j)=1;
            else
                g(i,j)=0;
            
        
    
    
    Mskf= np.cross(Mskd, g)
    
    h=1;
	size_mskf = np.shape(mskf)
    for i in size_mskf(0)
        for j in size_mskf(1)
            if  Mskf(i,j)~=0; #*** le ~= en python?
                Xprec(h)=i;
                Yprec(h)=j;
                h=h+1;
            
        
    


# compute R
R = np.zeros((ne,ne))
for i in ne
    for j in ne
		#*** Ai(:,:)=A(:,1,:,ii)
		#*** Aj(:,:)=A(:,1,:,jj)
        
        cAi = np.cross(Ai, Mskf)
        cAj = np.cross(Aj, Mskf)
        result = np.cross(cAj, cAi)
        #integrate over mask
        R[i][j] = cond*(omega**2)*(sum((sum((result)))));
        
return R    

