import numpy as np


class GivenRotation:
    def __init__(self, cos=1, sin=0, index_i=1, index_j=1):
        self.cos = cos
        self.sin = sin
        self.index_i = index_i
        self.index_j = index_j
    
    def __repr__(self):
        return f"GivenRotation({self.cos}, {self.sin}, {self.index_i}, {self.index_j})\n"
    
    def __str__(self):
        return f"GivenRotation({self.cos}, {self.sin}, {self.index_i}, {self.index_j})\n"
    
    def left_multiply(self, vector):
        i = self.index_i
        j = self.index_j
        c = self.cos
        s = self.sin
        a, b = vector[i], vector[j]
        vector[i] = c * a - s * b
        vector[j] = s * a + c * b



def calculate_cos_and_sin( a, b):
        if b == 0:
            c = 1
            s = 0
        else:
            if abs(b) > abs(a):
                r = a / b
                s = 1 / np.sqrt(1 + r**2)
                c = s * r
            else:
                r = b / a
                c = 1 / np.sqrt(1 + r**2)
                s = c * r
        return c, s  