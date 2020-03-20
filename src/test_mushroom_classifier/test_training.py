import unittest
from test_mushroom_classifier.base_test import TestBase
from os import path
import numpy as np
from mushroom_classifier.logisticregression import LogisticRegression
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.trainingdiagnostics import TrainingDiagnostics
from mushroom_classifier.modelstorage import ModelStorage

import pandas as pd

class TrainingTests(TestBase):
    
    @classmethod
    def setUpClass(cls):
        currentdir = path.dirname(path.realpath(__file__))
        cls.test_dump_path = path.join(currentdir,"test_dump")
        cls.test_dataset_path = path.join(currentdir, "test_files/mushrooms_small_sample.csv")

    def test_training_correct_shapes(self):
        test_iters = 500
        test_dataset = pd.read_csv(self.test_dataset_path)
        data_cleaner = DataCleaner(test_dataset,"class","p")
        [train_X, test_X, train_y, test_y]  = data_cleaner.clean()
        self.assertTrue(train_X.shape == (169,59), f"train_X shape expected:(169,59), actual{train_X.shape}")
        self.assertTrue(test_X.shape == (30,59),  f"test_X shape expected:(30,59), actual{test_X.shape}")
        self.assertTrue(train_y.shape == (169,),  f"train_y shape expected:(169,), actual{train_y.shape}")
        self.assertTrue(test_y.shape == (30,),  f"test_y shape expected:(30,), actual{test_y.shape}")


        model = LogisticRegression(learning_rate=1, num_iter=test_iters, fit_intercept=True)

        model.setup_logger(self.mock_log)
        [thetas, costs] = model.train(train_X, train_y)

        #60 as the intercept has been added to X matrix during training process
        self.assertTrue(thetas.shape == (60,), f"Weight amount expected:60, actual{thetas.shape}")
        self.assertTrue(len(costs) == test_iters, f"Costs amount expected:{test_iters}, actual {len(costs)}")

        
    def mock_log(self, message):
        return None
        
if __name__ == "__main__":
    unittest.main()