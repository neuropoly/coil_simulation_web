import numpy as np
from scipy import math

PI = math.pi

"""The Coil class defines methods to define, access and operate on coil arrays"""


class Coil:

    def __init__(self, posinix, posiniy, posiniz, rada, radb, coil_definition):
        self.posinix = float(posinix)
        self.posiniy = float(posiniy)
        self.posiniz = float(posiniz)
        self.rada = float(rada)
        self.radb = float(radb)
        self.coil_definition = int(coil_definition)
        self.coil_array = self.gen_array(coil_definition)


    """Setters and getters"""
    """coil_array"""
    def get_coil_array(self):
        return self.coil_array

    def set_coil_array(self, array):
        self.coil_array = array

    """Defines the array of points, which is a 100 x 3 matrix, used to trace the B1 field
    and the coil itself."""

    def gen_array(self, N):
        coil_array = np.array([[0.0 for j in range(3)] for j in range(N)]) #columns then lines
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

    @property
    def coil_definition(self):
        return self.coil_definition

    @coil_definition.setter
    def coil_definition(self, value):
        self.coil_definition = value

    def rotation(self, radc, coil_array):
        theta = -(math.asin(self.posinix/radc))
        """generate rotation matrix for Y axis"""
        Ry = np.matrix([[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]])
        # x = np.zeros((self.coil_definition, 1))
        # y = np.zeros((self.coil_definition, 1))
        # z = np.zeros((self.coil_definition, 1))
        # for i in range(self.coil_definition):
        #     x[i] = coil_array[i][0]
        #     y[i] = coil_array[i][1]
        #     z[i] = coil_array[i][2]
        #
        # rotate = np.append(x,y,axis=1)
        # rotate = np.append(rotate,z,axis=1)
        # coil_rotated = np.zeros((self.coil_definition, 3))
        coil_rotated = np.dot(coil_array, Ry)
        return coil_rotated

    def translation(self, radc, coil_rotated):
        Tx = self.posinix
        Ty = 0
        Tz = radc - math.cos(math.asin(self.posinix/radc))*radc
        Tr = np.matrix([[1, 0, 0, Tx], [0, 1, 0, Ty], [0, 0, 1, Tz], [0, 0, 0, 1]])

        x = np.zeros(1, 3)
        y = np.zeros(1, 3)
        z = np.zeros(1, 3)

        for i in range(3):
            x[i] = coil_rotated[1][i]
            y[i] = coil_rotated[2][i]
            z[i] = coil_rotated[3][i]

        size = np.shape(coil_rotated)
        """size(1) = columns size of coil_rotated"""
        lf = np.ones(1, size(1))

        temp = np.matrix([[x], [y], [z], [lf]])

        coil_translated = np.zeros(4, 4)
        coil_translated = np.dot(Tr, temp)

        return coil_translated

#Ancien code		
"""def rotation(self, posinix, radc)
        theta=-(m.asin(posinix(en)/radc)
        #generate rotation matrix for Y axis
        Ry = [[m.cos(theta), 0, m.sin(theta)], [0, 1, 0], [-m.sin(theta), 0, m.cos(theta)]]
        self.coil_rotated = dot(Ry, self.coil_init)
        return self.coil_rotated

    def translation(self, Tx, Ty, Tz, Tr):s
        Tx=self.posinix(en)
        Ty=0
        Tz=self.radc-m.cos(m.asin(self.posinix(en)/self.radc))*self.radc
        Tr=[[1, 0, 0, Tx], [0, 1, 0, Ty], [0, 0, 1, Tz], [0, 0, 0, 1]]

        temp = np.vstack((self.coil_rotated),(np.ones(100,1))

        self.coil_translated = dot(Tr, temp)

        return self.coil_translated"""




