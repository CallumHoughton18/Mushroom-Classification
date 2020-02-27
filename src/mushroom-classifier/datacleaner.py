import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataCleaner:
    train = None

    """Encodes the given dataset"""
    def __init__(self, csvData):
        mushroom_df= pd.read_csv(csvData)
        self.train = mushroom_df

    def onehot_encode(self):
        mushroom_x = pd.get_dummies(self.train.drop('class', axis=1))
        mushroom_x = mushroom_x.values
        mushroom_y = (np.atleast_2d(self.train['class']).T == 'p').astype(int)
        return train_test_split(mushroom_x, mushroom_y, train_size=0.85, test_size=0.15)