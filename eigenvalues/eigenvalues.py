import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        # For non-square matrix exception would be thrown
        mat = np.asarray(matrix)
        m,n = mat.shape
        # If an exception is not thrown above, below check would cover non-square matrix
        if m!=n:
            return None
        # Calculate EigenValues using np.linalg.eigvals function from numpy
        eigenvalues = np.linalg.eigvals(mat)
        # Using np.lexsort for consistent sorting by real then imaginary parts
        idx = np.lexsort((eigenvalues,)) # Returns sorted indices
        eigenvalues = eigenvalues[idx]
        # Returning the final eigen values array
        return eigenvalues
    except ValueError:
        return None