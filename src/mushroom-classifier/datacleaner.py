import pandas as pd
import numpy as np

class DataCleaner:
    train = None

    """Encodes the given dataset"""
    def __init__(self, csvData):
        mushroom_df= pd.read_csv(csvData)
        self.train = mushroom_df

    def onehot_encode(self):
        #return pd.get_dummies(self.train)
        train_onehot = pd.get_dummies(self.train)
        return train_onehot