import unittest
from mushroom_classifier.mlutils import add_intercept
import numpy as np
from test_mushroom_classifier.base_test import TestBase

class Add_InterceptTests(TestBase):
    def test_add_intercept_should_return_matrix_with_ones(self):
        expected_X_with_intercept = np.ndarray(shape=(2,3), dtype=int, buffer=np.array([[1,1,2],[1,3,4]]))

        actual_X_with_intercept = add_intercept(self.test_X)

        np.testing.assert_array_equal(expected_X_with_intercept, actual_X_with_intercept)

if __name__ == "__main__":
    unittest.main()