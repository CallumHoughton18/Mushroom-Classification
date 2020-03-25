"""
Contains logisticregression Tests
"""
import unittest

import numpy as np

from mushroom_classifier.logisticregression import LogisticRegression
from test_mushroom_classifier.base_test import TestBase

class LogisticRegressionTests(TestBase):
    """LogisticRegression tests"""
    def test_hypothesis_happypath(self):
        """Should calculate hypothesis correctly"""
        expected_hypothesis = [0.5, 0.5]
        sut = LogisticRegression()

        actual_hypothesis = sut.hypothesis(self.test_x_matrix, self.test_theta)

        np.testing.assert_array_almost_equal(expected_hypothesis, actual_hypothesis, decimal=1)

    def test_cost_function_happypath(self):
        """Should calculate cost correctly"""
        expected_cost = 0.22314355
        test_hypothesis = np.ndarray(shape=(1, 2), dtype=float, buffer=np.array([0.8, 0.2]))
        sut = LogisticRegression()

        actual_cost = sut.cost_function(test_hypothesis, self.test_y_vector)

        self.assertAlmostEqual(expected_cost, actual_cost, places=7)

if __name__ == '__main__':
    unittest.main()
