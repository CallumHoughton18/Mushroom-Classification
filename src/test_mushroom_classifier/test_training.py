"""
Contains end to end training tests
"""

import unittest
from os import path

import pandas as pd

from test_mushroom_classifier.base_test import TestBase
from mushroom_classifier.logisticregression import LogisticRegression
from mushroom_classifier.datacleaner import DataCleaner

class TrainingTests(TestBase):
    """Training tests"""
    @classmethod
    def setUpClass(cls):
        currentdir = path.dirname(path.realpath(__file__))
        cls.test_dump_path = path.join(currentdir, 'test_dump')
        cls.test_dataset_path = path.join(currentdir, 'test_files/mushrooms_small_sample.csv')

    def test_training_correct_shapes(self):
        """Checks shapes of cleaned data, and returned costs/thetas"""
        test_iters = 500
        test_dataset = pd.read_csv(self.test_dataset_path)
        data_cleaner = DataCleaner(test_dataset, "class", "p")
        [train_x_matrix, test_x_matrix, train_y_vector, test_y_vector] = data_cleaner.clean()
        self.assertTrue(train_x_matrix.shape == (159, 59),
                        f'train_X shape expected:(169,59), actual{train_x_matrix.shape}')
        self.assertTrue(test_x_matrix.shape == (40, 59),
                        f'test_X shape expected:(30,59), actual{test_x_matrix.shape}')
        self.assertTrue(train_y_vector.shape == (159,),
                        f'train_y shape expected:(169,), actual{train_y_vector.shape}')
        self.assertTrue(test_y_vector.shape == (40,),
                        f'test_y shape expected:(30,), actual{test_y_vector.shape}')


        model = LogisticRegression(learning_rate=1, num_iter=test_iters, fit_intercept=True)

        model.setup_logger(self.mock_log)
        [thetas, costs] = model.train(train_x_matrix, train_y_vector)

        #60 as the intercept has been added to X matrix during training process
        self.assertTrue(thetas.shape == (60,), f'Weight amount expected:60, actual{thetas.shape}')
        self.assertTrue(len(costs) == test_iters,
                        f'Costs amount expected:{test_iters}, actual {len(costs)}')

    def mock_log(self):
        """Mock log method"""
        return None

if __name__ == '__main__':
    unittest.main()
