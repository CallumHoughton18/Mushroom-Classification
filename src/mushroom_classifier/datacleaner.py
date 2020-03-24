"""
Required to work with data as dataframe, and onehot encode
"""
import pandas as pd
from mushroom_classifier.mlutils import train_test_split

class DataCleaner:
    """Cleans the classification dataset, providing the ability to onehot encode it"""
    def __init__(self, dataset_df, classification_column_name, truth_value):
        self.train = dataset_df
        self.classification_column_name = classification_column_name
        self.truth_value = truth_value
        self.columns_for_index = None
        self.train_encoded = None

    def clean(self):
        """Splits the encoded dataset into training and test sets"""
        x_matrix = self.__onehot_encode(self.classification_column_name)
        y_vector = self.__extract_y_values(
            self.classification_column_name, self.truth_value)
        return train_test_split(x_matrix, y_vector)

    def clean_new_unseen_data(self, new_data):
        """Splits and encodes unseen data, reindexing it"""
        new_x_matrix = pd.get_dummies(new_data)
        return new_x_matrix.reindex(columns=self.columns_for_index, fill_value=0)

    def __onehot_encode(self, classification_column_name):
        x_matrix = pd.get_dummies(self.train.drop(classification_column_name, axis=1))
        self.train_encoded = x_matrix
        self.columns_for_index = self.train_encoded.columns
        return x_matrix.values

    def __extract_y_values(self, classification_column_name, truth_value):
        y_vector = (self.train[classification_column_name].T ==
                    truth_value).astype(int)
        return y_vector
