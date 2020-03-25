#pylint: disable=unused-argument
"""
Contains gradientdescent Tests
"""
import unittest

import numpy as np

from mushroom_classifier.gradientdescent import GradientDescent
from test_mushroom_classifier.base_test import TestBase

class GradientDescentTests(TestBase):
    """GradientDescent tests"""
    def mock_cost_function(self, hyp, y_vector):
        """Mock model cost function"""
        return 1

    def mock_hypothesis(self, x_matrix, theta):
        """Mock model hypothesis"""
        return 1

    def test_calculate_happypath(self):
        """Should calculate theta values from gradient descent"""
        expected_costs = [1, 1, 1, 1, 1]
        expected_theta = np.ndarray(shape=(2,), dtype=float, buffer=np.array([-2.90625, -3.875]))

        self.calculate_assertion(self.test_x_matrix, self.test_theta,
                                 expected_costs, expected_theta, add_intercept=False)

    def test_calculate_intercepted_added(self):
        """Should calculate, taking into account intercept"""
        expected_costs = [1, 1, 1, 1, 1]
        [test_x_with_intercept, test_theta_with_intercept] = self.get_x_and_theta_with_intercept()
        expected_theta = np.ndarray(shape=(3,), dtype=float,
                                    buffer=np.array([-2.5, -2.90625, -3.875]))

        self.calculate_assertion(test_x_with_intercept, test_theta_with_intercept,
                                 expected_costs, expected_theta, add_intercept=True)

    def calculate_assertion(self, test_x_matrix,
                            test_theta, expected_costs, expected_theta, add_intercept):
        """helper method for creating sut, executing calculation method"""
        sut = GradientDescent(self.mock_hypothesis, self.mock_cost_function,
                              test_x_matrix, self.test_y_vector, test_theta,
                              intercept_added=add_intercept)

        [actual_theta, actual_costs] = sut.calculate(5)

        np.testing.assert_array_equal(expected_costs, actual_costs)
        np.testing.assert_array_equal(expected_theta, actual_theta)

if __name__ == '__main__':
    unittest.main()
