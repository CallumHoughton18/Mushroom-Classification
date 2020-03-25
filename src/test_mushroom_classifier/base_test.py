"""
Imports for TestBase
"""
from unittest import TestCase
import numpy as np

class TestBase(TestCase):
    """Base class for mushroom_classifier tests"""
    def setUp(self):
        self.test_x_matrix = np.ndarray(shape=(2, 2), dtype=int, buffer=np.array([[1, 2], [3, 4]]))
        self.test_y_vector = np.ndarray(shape=(2,), dtype=int, buffer=np.array([1, 0]))
        self.test_theta = np.zeros(self.test_x_matrix.shape[1])

    def get_x_and_theta_with_intercept(self):
        """returns theta and test_x_matrix with intercept added"""
        intercept = np.ones((self.test_x_matrix.shape[0], 1))
        x_with_intercept = np.concatenate((intercept, self.test_x_matrix), axis=1)
        theta_with_intercept = np.zeros(x_with_intercept.shape[1])
        return [x_with_intercept, theta_with_intercept]
