import numpy as np
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        self.test_X = np.ndarray(shape=(2,2), dtype=int, buffer=np.array([[1,2],[3,4]]))
        self.test_y = np.ndarray(shape=(2,), dtype=int, buffer=np.array([1, 0]))
        self.test_theta = np.zeros(self.test_X.shape[1])

    def get_x_and_theta_with_intercept(self):
        intercept = np.ones((self.test_X.shape[0], 1))
        x_with_intercept = np.concatenate((intercept, self.test_X), axis=1)
        theta_with_intercept = np.zeros(x_with_intercept.shape[1])
        
        return [x_with_intercept, theta_with_intercept]