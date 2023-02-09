import numpy as np
def mean(X):
    """
    Compute the mean of the columns of X
    Arguments:
        X: np.ndarray
    Returns: 
        mean_X : np.ndarray
    """
    mean_X = np.mean(X, axis=0)
    return mean_X