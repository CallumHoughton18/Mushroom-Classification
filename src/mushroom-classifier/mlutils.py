import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def add_intercept(X):
    intercept = np.ones((X.shape[0], 1))
    return np.concatenate((intercept, X), axis=1)