import numpy as np
from scipy import math

PI = math.pi

"""The Phantom class modify default parameters such as current (I), frequency, permittivity (u0) and conductivity"""


class Phantom:
    def __init__(self, u0, I, cond, freq):
        self.u0 = float(u0)
        self.I = float(I)
        self.cond = float(cond)
        self.freq = float(freq)

    def info(self):
        print("Permittivity: ", self.u0)
        print("Current: ", self.I)
        print("Conductivity: ", self.cond)
        print("Frequency: ", self.freq)

    @property
    def u0(self):
        return self.u0

    @u0.setter
    def u0(self, value):
        self.u0 = value

    @property
    def I(self):
        return self.I

    @I.setter
    def I(self, value):
        self.I = value

    @property
    def cond(self):
        return self.cond

    @cond.setter
    def cond(self, value):
        self.cond = value

    @property
    def freq(self):
        return self.freq

    @freq.setter
    def freq(self, value):
        self.freq = value
