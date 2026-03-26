import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A_t = np.zeros((len(A[0]), len(A)))

    for i in range(len(A)):
        for j in range(len(A[0])):
            A_t[j][i] = A[i][j]

    return np.array(A_t)