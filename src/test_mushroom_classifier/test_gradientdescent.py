import unittest
from mushroom_classifier.gradientdescent import GradientDescent
import numpy as np
from test_mushroom_classifier.base_test import TestBase

class GradientDescentTests(TestBase):
    def mock_cost_function(self, h, y):
        return 1

    def mock_hypothesis(self, X, theta):
        return 1

    def test_calculate_happypath(self):
        expected_costs=[1, 1, 1, 1, 1]
        expected_theta=np.ndarray(shape=(2,),dtype=float, buffer=np.array([-2.90625 , -3.875]))

        self.calculate_assertion(self.test_X, self.test_theta ,expected_costs, expected_theta, add_intercept=False)

    def test_calculate_intercepted_added(self):
        expected_costs=[1, 1, 1, 1, 1]
        [test_x_with_intercept , test_theta_with_intercept] = self.get_x_and_theta_with_intercept()
        expected_theta=np.ndarray(shape=(3,),dtype=float, buffer=np.array([-2.5, -2.90625, -3.875]))

        self.calculate_assertion(test_x_with_intercept, test_theta_with_intercept ,expected_costs, expected_theta, add_intercept=True)

    def calculate_assertion(self, test_X, test_theta, expected_costs, expected_theta, add_intercept):
        sut = GradientDescent(self.mock_hypothesis, self.mock_cost_function, test_X, self.test_y, test_theta, intercept_added=add_intercept)

        [actual_theta, actual_costs] = sut.calculate(5)

        np.testing.assert_array_equal(expected_costs, actual_costs)
        np.testing.assert_array_equal(expected_theta, actual_theta)


        
if __name__ == "__main__":
    unittest.main()