#function [SNR]=calc_SNR(B1,ne,R)
#
# This function computes the SNR

import numpy as np
from scipy import math
PI = np.pi

def calc_SNR(B1, ne, R):

size = np.shape(B1)

for i in size(0)
    for j in size(2)
        for k in ne
            B(k,1)=B1(i,1,j,k); #Même problème que calc_R           
     
    #SNR(i,j)=sqrt((inv(R)*B)'*conj(B)) ->  sqrt((inv(R)*B)' = la transposée de la matrice
		R_inv = np.linalg.inv(R)
		SR = math.sqrt(R_inv * B)
		SR_tran = SR.transpose()
		B_conj = np.conjugate(B)
		SNR(i,j) = SR_tran * B_conj

