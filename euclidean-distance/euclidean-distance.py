import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)

    return float(np.linalg.norm(x - y))

    # if len(x) != len(y):
    #     raise ValueError
    
    # dist = 0
    # for i in range(len(x)):
    #     dist += (x[i]-y[i])**2

    # return dist**(1/2)