"""
Required to perform linear algebra with given arrays for util methods
"""
import numpy as np

def sigmoid(z_values):
    """Calculates sigmoid of values within z_values"""
    return 1 / (1 + np.exp(-z_values))

def add_intercept(x_matrix):
    """adds intercept to given x_matrix"""
    intercept = np.ones((x_matrix.shape[0], 1))
    return np.concatenate((intercept, x_matrix), axis=1)

def shuffle_arrays_in_unison(first_array, second_array):
    """Shuffles given arrays by same permutation"""
    assert len(first_array) == len(second_array)
    calcd_perm = np.random.permutation(len(first_array))
    return first_array[calcd_perm], second_array[calcd_perm]


def train_test_split(x_matrix, y_matrix, train_size=0.8):
    """Split given arrays in training sets and test sets"""
    indx_from = int(np.round(X.shape[0] * train_size))
    x_matrix, y_matrix = shuffle_arrays_in_unison(X, y)

    training_x_matrix = x_matrix[:indx_from, :]
    test_x_matrix = x_matrix[indx_from:, :]

    training_y_vector = y_matrix[:indx_from]
    test_y_vector = y_matrix[indx_from:]

    return [training_x_matrix, test_x_matrix, training_y_vector, test_y_vector]
