"""
Contains mlutils tests
"""
import unittest

import numpy as np

from mushroom_classifier.mlutils import add_intercept
from test_mushroom_classifier.base_test import TestBase

class AddInterceptTests(TestBase):
    """
    Tests add_intercept mlutils method
    """
    def test_add_intercept_should_return_matrix_with_ones(self):
        """Should return matrix with ones inserted correctly"""
        expected_x_matrix_with_intercept = np.ndarray(shape=(2, 3), dtype=int,
                                                      buffer=np.array([[1, 1, 2], [1, 3, 4]]))

        actual_x_matrix_with_intercept = add_intercept(self.test_x_matrix)

        np.testing.assert_array_equal(expected_x_matrix_with_intercept,
                                      actual_x_matrix_with_intercept)

if __name__ == "__main__":
    unittest.main()
