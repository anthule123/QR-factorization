

import numpy as np


class HouseholderVector:
    def __init__(self, vector_v, index_i=0):
        self.vector_v = vector_v
        self.vector_v_T = vector_v.T
        self.index_i = index_i
    
    def __str__(self):
        return f"HouseholderVector: v = {self.vector_v}, i = {self.index_i}\n"
    
    def __repr__(self):
        return f"HouseholderVector: v = {self.vector_v}, i = {self.index_i}\n"
    
    def left_multiply(self, vector_full):
        i = self.index_i
        v = self.vector_v
        value = 2 * np.dot(v, vector_full[i:]) * v
        vector_full[i:] = vector_full[i:] - value
    def left_multiply_small(self, vector_small):
        v = self.vector_v
        value = 2 * np.dot(v, vector_small) * v
        vector_small = vector_small - value
        return vector_small
    def right_multiply(self, vector_full): # vector_full is a row vector
        i = self.index_i
        v = self.vector_v
        value = 2 * np.dot(vector_full[i:], v) * v
        vector_full[i:] = vector_full[i:] + value
    def right_multiply_small(self, vector_small): # vector_small is a row vector
        v = self.vector_v
        value = 2 * np.dot(vector_small, v) * v
        vector_small = vector_small + value
        return vector_small



def calculate_householder_vector(vector_x):
    vector_v = vector_x.copy()
    norm_x = np.linalg.norm(vector_x)
    vector_v[0] = vector_x[0] + np.sign(vector_x[0]) * norm_x
    vector_v = vector_v / np.linalg.norm(vector_v)
    return vector_v