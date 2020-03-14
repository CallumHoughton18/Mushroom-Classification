import numpy as np
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        self.test_X = np.ndarray(shape=(2,2), dtype=int, buffer=np.array([[1,2],[3,4]]))
        self.test_y = np.ndarray(shape=(2,), dtype=int, buffer=np.array([1, 0]))
        self.test_theta = [0.2, 0.8]
