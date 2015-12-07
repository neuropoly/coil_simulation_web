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
        coil_array = np.array([[0.0 for j in range(3)] for j in range(N)]) # columns then rows
        t = -PI/2

        for i in range(N):
            x_coord = self.posinix+self.rada*math.cos(t)
            y_coord = self.posiniy+self.radb*math.sin(t)
            z_coord = self.posiniz

            coil_array[i][0] = x_coord
            coil_array[i][1] = y_coord
            coil_array[i][2] = z_coord

            t += 2*PI/(N-1)

        return coil_array

    """Print info on coil"""

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

    """Rotates the coil around the cylinder"""
    def rotation(self, radc):
        theta = -(np.arcsin(self.posinix/radc))
        """generate rotation matrix for Y axis"""
        Ry = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])

        """Transfrom in matrix and transpose it"""
        Ry_matrix = np.asmatrix(Ry)
        coil_array_matrix = np.asmatrix(self.coil_array)
        coil_array_matrix = np.transpose(coil_array_matrix)
        coil_rotated_matrix = Ry_matrix * coil_array_matrix
        coil_rotated_matrix = np.transpose(coil_rotated_matrix)

        """Go back to array"""
        coil_rotated = np.squeeze(np.asarray(coil_rotated_matrix))
        self.coil_array = coil_rotated

    """Translate the coil"""
    def translation(self, radc):
        Tx = self.posinix
        Ty = 0
        Tz = radc - np.cos(np.arcsin(self.posinix/radc))*radc
        Tr = np.array([[1, 0, 0, Tx], [0, 1, 0, Ty], [0, 0, 1, Tz], [0, 0, 0, 1]])

        temp = self.coil_array.reshape(self.coil_definition, 3)
        temp = np.insert(temp, 3, 1, axis=1)

        """Transfrom in matrix and transpose it"""
        temp_matrix = np.asmatrix(temp)
        Tr_matrix = np.asmatrix(Tr)
        temp_matrix = np.transpose(temp_matrix)
        coil_translated_matrix = Tr_matrix * temp_matrix
        coil_translated_matrix = np.transpose(coil_translated_matrix)
        coil_translated_matrix = np.delete(coil_translated_matrix, 3, 1)

        """Go back to array"""
        coil_translated = np.squeeze(np.asarray(coil_translated_matrix))

        return coil_translated
