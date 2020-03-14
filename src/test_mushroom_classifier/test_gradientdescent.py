import unittest
from mushroom_classifier.gradientdescent import GradientDescent
import numpy as np
from test_mushroom_classifier.base_test import TestBase

class GradientDescentTests(TestBase):
    def mock_cost_function(self, h, y):
        return 1

    def mock_hypothesis(self, X, theta):
        return 1

    def test_hypothesis_happypath(self):
        expected_costs=[1, 1, 1, 1, 1]
        expected_theta=np.ndarray(shape=(2,),dtype=float, buffer=np.array([-2.9 , -3.85]))
        sut = GradientDescent(self.mock_hypothesis, self.mock_cost_function, self.test_X, self.test_y, self.test_theta, intercept_added=False)

        [actual_theta, actual_costs] = sut.calculate(5)

        np.testing.assert_array_equal(expected_costs, actual_costs)
        np.testing.assert_array_equal(expected_theta, actual_theta)


        
if __name__ == "__main__":
    unittest.main()