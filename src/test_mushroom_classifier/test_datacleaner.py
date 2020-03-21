import unittest
from mushroom_classifier.datacleaner import DataCleaner
import pandas as pd
import numpy as np
from test_mushroom_classifier.base_test import TestBase
from os import path

class DataCleanerTests(TestBase):

    @classmethod
    def setUpClass(cls):
        cls.test_df = pd.DataFrame({'cat':[1,0,1,1],'val':['a','b','c','d']})
        cls.test_new_data = pd.DataFrame({'val':['a']})

    def test_clean_new_unseen_data_happypath(self):
        expected_new_encoded_data = pd.DataFrame({'val_a':[1],'val_b':[0],'val_c':[0],'val_d':[0]})
        sut = DataCleaner(self.test_df, "cat", truth_value=1)

        sut.clean()
        actual_new_encoded_data = sut.clean_new_unseen_data(self.test_new_data)
        
        pd.testing.assert_frame_equal(expected_new_encoded_data, actual_new_encoded_data, check_dtype=False)  

    # TODO: Need to finalize the code for splitting of data, so the random component can be mocked out and 
    # proper assertions can be made
    # def test_clean_happypath(self):
    #     sut = DataCleaner(self.test_df, "cat", truth_value=1)
    #     expected_cleaned_train_X = np.ndarray(shape=(3,4),dtype=int, buffer=np.array([0, 1, 0, 0],[0, 0, 0, 1],[1, 0, 0, 0]))
    #     expected_cleaned_test_X = np.ndarray(shape=(3,4),dtype=int, buffer=np.array([0, 0, 1, 0]))


    #     [actual_cleaned_train_X, actual_cleaned_test_X, actual_cleaned_train_y, actual_cleaned_test_y] = sut.clean()
    #     print(actual_cleaned_train_X) 
    #     print(actual_cleaned_test_X)
               
if __name__ == "__main__":
    unittest.main()