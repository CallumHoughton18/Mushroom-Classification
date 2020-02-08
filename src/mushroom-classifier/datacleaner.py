import pandas as pd
import numpy as np

class DataCleaner:
    train = None

    """Encodes the given dataset"""
    def __init__(self, csvData):
        mushroom_df= pd.read_csv(csvData)
        self.train = mushroom_df

    def onehot_encode(self):
        train_onehot = pd.get_dummies(self.train)
        return train_onehot

def segment_data(df):
    train = df.sample(frac=0.8, random_state=0)
    test = df.drop(train.index)
    return[train, test]
        