"""
Contains tests for datacleaner
All tests are data driven using CSV data
"""
import unittest
from os import path

import pandas as pd
import numpy as np

from mushroom_classifier.datacleaner import DataCleaner
from test_mushroom_classifier.base_test import TestBase

class DataCleanerDataDrivenTests(TestBase):
    """Data Cleaner Data Driven Tests"""
    @classmethod
    def setUpClass(cls):
        currentdir = path.dirname(path.realpath(__file__))
        test_dataset_path = path.join(currentdir, "test_files/mushrooms_small_sample.csv")
        cls.test_dataset = pd.read_csv(test_dataset_path)
        unseen_test_data_path = path.join(currentdir, "test_files/unseen_data_examples.csv")
        cls.unseen_test_data = pd.read_csv(unseen_test_data_path)

    def test_clean_new_unseen_data(self):
        """Should clean new data correctly, applying correct index"""
        sut = DataCleaner(self.test_dataset, "class", truth_value="p")

        sut.clean()
        actual_new_encoded_data = sut.clean_new_unseen_data(self.unseen_test_data)

        np.testing.assert_array_equal(sut.train_encoded.columns, actual_new_encoded_data.columns)
        self.assertEqual(actual_new_encoded_data.shape, (1, 59))

if __name__ == "__main__":
    unittest.main()
