import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        mat = np.asarray(matrix)
        m,n = mat.shape
        if m!=n:
            return None
        eigenvalues = np.linalg.eigvals(mat)
        # print(f'eigen vals = {eigenvalues}')
        idx = np.lexsort((eigenvalues,))
        # print(f'idx = {idx}')
        eigenvalues = eigenvalues[idx]
        # print(f'eigen vals = {eigenvalues}')
    except ValueError:
        return None
    return eigenvalues