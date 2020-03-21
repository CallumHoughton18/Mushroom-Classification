import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataCleaner:
    train = None

    """Encodes and splits the given dataset"""
    def __init__(self, dataset_df, classification_column_name, truth_value):
        self.train = dataset_df
        self.classification_column_name = classification_column_name
        self.truth_value = truth_value

    def clean(self):
        X = self.__onehot_encode(self.classification_column_name)
        y = self.__extract_y_values(self.classification_column_name, self.truth_value)
        return train_test_split(X, y, train_size=0.85, test_size=0.15)

    def clean_new_unseen_data(self, new_data):
        new_X = pd.get_dummies(new_data)
        return new_X.reindex(columns=self.train_encoded.columns,fill_value=0)

    def __onehot_encode(self, classification_column_name):
        X = pd.get_dummies(self.train.drop(classification_column_name, axis=1))
        self.train_encoded = X
        return X.values

    def __extract_y_values(self, classification_column_name, truth_value):
        y = (self.train[classification_column_name].T == truth_value).astype(int)
        return y

    # def __train_test_split(X, y, train_size=0.85, test_size=0.15):
    #     full_set = np.concatenate((X, y), axis=1)
    #     np.random.shuffle(full_set)
    #     np.split(full_set, 2, )
