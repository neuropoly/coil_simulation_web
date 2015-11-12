import numpy as np
from scipy import math

PI = math.pi

"""The Phantom class modify default parameters such as current (I), frquency, permitivity (u0), number of points for coil and conductivity"""
class Phantom:

    def __init__(self, u0, coil_definition, I, cond, freq):
        self.u0 = float(u0)
        self.coil_definition = int(coil_definition)
        self.I = float(I)
        self.cond = float(cond)
        self.freq = float(freq)


    def info(self):
        print("Permitivity: ", self.u0)
        print("Number of points: ", self.coil_definition)
        print("Current: ", self.I)
        print("Conductivity: ", self.cond)
        print("Frequency: ", self.freq)




			
		
		