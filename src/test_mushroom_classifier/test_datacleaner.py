#pylint: disable=line-too-long
"""
Contains tests for datacleaner
using simple mock data
"""
import unittest
from unittest.mock import patch

import pandas as pd
import numpy as np

from mushroom_classifier.datacleaner import DataCleaner
from test_mushroom_classifier.base_test import TestBase

def side_effect_for_shuffling(x_matrix, y_vector):
    """removed random shuffling, just returns params"""
    return x_matrix, y_vector

class DataCleanerTests(TestBase):
    """DataCleaner tests, using simple mock data"""
    @classmethod
    def setUpClass(cls):
        cls.test_df = pd.DataFrame({'cat':[1, 0, 1, 1], 'val':['a', 'b', 'c', 'd']})
        cls.test_new_data = pd.DataFrame({'val':['a']})

    def test_clean_new_unseen_data_happypath(self):
        """Should encode and return expected clean data"""
        expected_new_encoded_data = pd.DataFrame({'val_a':[1], 'val_b':[0], 'val_c':[0], 'val_d':[0]})
        sut = DataCleaner(self.test_df, 'cat', truth_value=1)

        sut.clean()
        actual_new_encoded_data = sut.clean_new_unseen_data(self.test_new_data)

        pd.testing.assert_frame_equal(expected_new_encoded_data, actual_new_encoded_data,
                                      check_dtype=False)

    @patch('mushroom_classifier.mlutils.shuffle_arrays_in_unison')
    def test_clean_happypath(self, shuffle_arrays_in_unison_mock):
        """Should return cleaned encoded data, split correctly"""
        shuffle_arrays_in_unison_mock.side_effect = side_effect_for_shuffling
        sut = DataCleaner(self.test_df, 'cat', truth_value=1)
        expected_cleaned_train_x_matrix = np.ndarray(shape=(3, 4), dtype=int,
                                                     buffer=np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]))
        expected_cleaned_test_x_matrix = np.ndarray(shape=(1, 4), dtype=int, buffer=np.array([0, 0, 0, 1]))
        expected_cleaned_train_y_vector = np.ndarray(shape=(3,), dtype=int, buffer=np.array([[1], [0], [1]]))
        expected_cleaned_test_y_vector = np.ndarray(shape=(1,), dtype=int, buffer=np.array([1]))

        [actual_cleaned_train_x_matrix, actual_cleaned_test_x_matrix,
         actual_cleaned_train_y_vector, actual_cleaned_test_y_vector] = sut.clean()

        np.testing.assert_array_equal(actual_cleaned_train_x_matrix,
                                      expected_cleaned_train_x_matrix)
        np.testing.assert_array_equal(actual_cleaned_test_x_matrix, expected_cleaned_test_x_matrix)
        np.testing.assert_array_equal(actual_cleaned_train_y_vector,
                                      expected_cleaned_train_y_vector)
        np.testing.assert_array_equal(actual_cleaned_test_y_vector, expected_cleaned_test_y_vector)

if __name__ == "__main__":
    unittest.main()
