"""
Main app file for RESTful API to expose mushroom classifier model
"""
from pickle import load
from os.path import join

from flask import Flask
import pandas as pd

from mushroom_classifier.path_constants import CURRENT_MODEL_DIR, DATASET_DIR
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.logisticregression import LogisticRegression

APP = Flask(__name__)

MODEL_FILE_PATH = join(CURRENT_MODEL_DIR, "model.sav")
COLUMNS_FILE_PATH = join(CURRENT_MODEL_DIR, "columns_for_index.sav")

MODEL = load(open(MODEL_FILE_PATH, 'rb'))
DATASET_PATH = join(DATASET_DIR, 'mushrooms.csv')
DATASET = pd.read_csv(DATASET_PATH)
DATA_CLEANER = DataCleaner(DATASET, 'class', 'p')
LOADED_COLUMNS = load(open(COLUMNS_FILE_PATH, 'rb'))
DATA_CLEANER.columns_for_index = LOADED_COLUMNS

@APP.route('/')
def root():
    """Test route for API"""
    return 'Mushroom Classifier API'

# ROUTE: /api/predict?
# method: GET
# params: features(JSON object with user chosen features to predict against model)
# returns: edible or none edible classification response
@APP.route('/api/predict')
def predict():
    """Predicts whether given mushrooms features indicate an edible or none edible mushroom"""
    mock_predictions = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"e\",\"bruises\":\"f\",\"odor,gill-attachment\":\"n\",\"gill-spacing\":\"f\",\"gill-size\":\"c\",\"gill-color\":\"n\",\"stalk-shape\":\"w\",\"stalk-root\":\"e\",\"stalk-surface-above-ring\":\"b\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"s\",\"spore-print-color\":\"w\",\"population\":\"v\",\"habitat\":\"d\"}]"
    prediction_df = pd.read_json(mock_predictions)
    prediction_cleaned = DATA_CLEANER.clean_new_unseen_data(prediction_df)
    unseen_preds = MODEL.predict(prediction_cleaned)
    print(prediction_df.shape)
    print(DATASET.shape)
    return {"predictions":pd.Series(unseen_preds).to_json(orient='values')}



# ROUTE: /api/weights
# method: GET
# returns: jsonified prediction set of loaded model, fully formatted and cleaned
@APP.route('/api/weights')
def get_weights():
    """Returns the weights, with column names, of the model"""
    return ""
