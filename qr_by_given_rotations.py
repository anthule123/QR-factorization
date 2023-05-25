


import numpy as np
from given_rotation import calculate_cos_and_sin, GivenRotation


class QRByGivenRotation:
    def __init__(self, A):
        self.A = A
        #self.Q = np.identity(A.shape[0])
        self.R = A.copy()
        self.rotations = []
        
    def decomposite(self):
        for i in range(self.R.shape[1]):
            for j in range(i+1, self.R.shape[0]):
               
                cos, sin = calculate_cos_and_sin(self.R[i, i], self.R[j,i])
                rotation = GivenRotation(cos, sin, i, j)
                rotation_reverse = GivenRotation(cos, -sin, i, j)
                self.rotations.append(rotation)
                for k in range(i, self.R.shape[1]):
                    a,b = self.R[i, k], self.R[j, k]
                    self.R[i, k], self.R[j, k] = rotation_reverse.left_multiply_2_by_2(a,b)
                #self.Q = rotation.left_multiply(self.Q)
        return self.R, self.rotations
    
    def left_multiply_Q(self, vector):
        ans = vector.copy()
        for i in range(len(self.rotations)- 1, -1, -1):
            self.rotations[i].left_multiply(ans)
        return ans
    def right_multiply_Q(self, vector): # vector is a row vector
        ans = vector.copy()
        for i in range(len(self.rotations)):
            self.rotations[i].right_multiply(ans)
        return ans