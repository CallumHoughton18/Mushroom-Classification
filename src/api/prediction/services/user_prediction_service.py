"""Service for handling given prediction data against given model"""
import pandas as pd

class UserPredictionService:
    """Class for using user data against a given model for forming predictions"""
    def __init__(self, data_cleaner, model):
        self.data_cleaner = data_cleaner
        self.model = model

    def make_prediction(self, dic_for_prediction):
        """
        Uses model to make prediction on if given user prediction data
        indicates a poisonous mushroom
        returns true, if poisonous, false if edible
        """
        prediction_df = pd.DataFrame.from_dict(dic_for_prediction)
        prediction_cleaned = self.data_cleaner.clean_new_unseen_data(prediction_df)
        unseen_pred = self.model.predict(prediction_cleaned)[0]
        return unseen_pred
