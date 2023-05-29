


import numpy as np


def find_eig_by_power_iteration(matrixA, x0, tol=1e-20, maxiter=1000, eigenvectors=[]):
    '''Find the dominant eigenvalue and eigenvector of matrixA by power iteration.

    Args:
        matrixA: a square matrix
        x0: the initial guess of the dominant eigenvector
        tol: the tolerance of the error
        maxiter: the maximum number of iterations
    '''
    x = x0.copy()
    for i in range(maxiter):
        #khu het eigen vector
        # for eigenvector in eigenvectors:
        #     x -= x.dot(eigenvector) * eigenvector
        # x /= np.linalg.norm(x)
        y = matrixA @ x
        eigen_value = y.dot(x)
        if eigen_value < tol:
            break
        x = y / np.linalg.norm(y)
        if np.linalg.norm(matrixA @ x - eigen_value* x) < tol:
            break
    return eigen_value, x
