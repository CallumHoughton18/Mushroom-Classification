import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataCleaner:
    train = None

    """Encodes the given dataset"""
    def __init__(self, csvData, classification_column_name, truth_value):
        self.train = pd.read_csv(csvData)
        self.classification_column_name = classification_column_name
        self.truth_value = truth_value

    def clean(self):
        X = self.__onehot_encode(self.classification_column_name)
        y = self.__extract_y_values(self.classification_column_name, self.truth_value)
        return train_test_split(X, y, train_size=0.85, test_size=0.15)

    def __onehot_encode(self, classification_column_name):
        X = pd.get_dummies(self.train.drop(classification_column_name, axis=1))
        return X.values

    def __extract_y_values(self, classification_column_name, truth_value):
        y = (self.train[classification_column_name].T == truth_value).astype(int)
        return y
