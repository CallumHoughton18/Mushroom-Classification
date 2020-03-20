import unittest
from mushroom_classifier.datacleaner import DataCleaner
import pandas as pd
from test_mushroom_classifier.base_test import TestBase

class DataCleanerTests(TestBase):
    def test_clean_new_unseen_data_happypath(self):
        test_df = pd.DataFrame({'cat':[1,0,1,1],'val':['a','b','c','d']})
        test_new_data = pd.DataFrame({'val':['a']})
        expected_new_encoded_data = pd.DataFrame({'val_a':[1],'val_b':[0],'val_c':[0],'val_d':[0]})
        sut = DataCleaner(test_df, "cat", truth_value=1)

        sut.clean()
        actual_new_encoded_data = sut.clean_new_unseen_data(test_new_data)
        
        pd.testing.assert_frame_equal(expected_new_encoded_data, actual_new_encoded_data, check_dtype=False)

        
if __name__ == "__main__":
    unittest.main()