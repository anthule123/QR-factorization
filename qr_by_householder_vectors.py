import numpy as np
from householder_vector import HouseholderVector
from householder_vector import calculate_householder_vector

class QRByHouseholderVector:
    def __init__(self, A):
        self.A = A
        #self.Q = np.identity(A.shape[0])
        self.R = A.copy()
        self.householder_vectors = []
    
    def decomposite(self):
        for i in range(self.R.shape[1]):
            vector_x = self.R[i:, i]
            vector_v = calculate_householder_vector(vector_x)
            householder_vector = HouseholderVector(vector_v, i)
            self.householder_vectors.append(householder_vector)
            householder_reverse = HouseholderVector(-vector_v, i)
            for j in range(i, self.R.shape[1]):
                householder_reverse.left_multiply(self.R[:, j])
            #self.Q = self.Q - 2 * np.outer(vector_v, vector_v.T @ self.Q)
        return self.R, self.householder_vectors
    
    def left_multiply_Q(self, vector):
        ans = vector.copy()
        for i in range(len(self.householder_vectors)- 1, -1, -1):
            self.householder_vectors[i].left_multiply(ans)
        return ans
    def right_multiply_Q(self, vector): # vector is a row vector
        ans = vector.copy()
        for i in range(len(self.householder_vectors)):
            self.householder_vectors[i].right_multiply(ans)
        return ans