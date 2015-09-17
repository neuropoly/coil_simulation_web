import numpy as np
from scipy import math

PI = math.pi

"""The Coil class defines methods to define, access and operate on coil arrays"""
class Coil:

    def __init__(self, posinix, posiniy, posiniz, rada, radb):
        self.posinix = posinix
        self.posiniy = posiniy
        self.posiniz = posiniz
        self.rada = rada
        self.radb = radb

    """Defines the array of points, which is a 100 x 3 matrix, used to trace the B1 field
    and the coil itself."""
    def gen_array(self, N):
        coil_array = np.array([[0 for j in range(3)] for j in range(N)]) #columns then lines
        t=-PI/2

        for i in range(N):
            x_coord = self.posinix+self.rada*math.cos(t)
            y_coord = self.posiniy+self.radb*math.sin(t)
            z_coord = self.posiniz

            coil_array[i][0] = x_coord
            coil_array[i][1] = y_coord
            coil_array[i][2] = z_coord

            t += 2*PI/(N-1)

        return coil_array

    def info(self):
        print("X: ", self.posinix)
        print("Y: ", self.posiniy)
        print("Z: ", self.posiniz)
        print("Radius a: ", self.rada)
        print("Radius b: ", self.radb)

    """def rotation(self, posinix, radc)
        theta=-(math.asin(posinix(en)/radc)
        #generate rotation matrix for Y axis
        Ry = [[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]]
        self.coil_rotated = dot(Ry, self.coil_init)
        return self.coil_rotated

    def translation(self, Tx, Ty, Tz, Tr):s
        Tx=self.posinix(en)
        Ty=0
        Tz=self.radc-math.cos(math.asin(self.posinix(en)/self.radc))*self.radc
        Tr=[[1, 0, 0, Tx], [0, 1, 0, Ty], [0, 0, 1, Tz], [0, 0, 0, 1]]

        temp = np.vstack((self.coil_rotated),(np.ones(100,1))

        self.coil_translated = dot(Tr, temp)

        return self.coil_translated"""



			
		
		