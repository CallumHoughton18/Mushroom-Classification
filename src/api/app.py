"""
Main app file for RESTful API to expose mushroom classifier model
"""
from pickle import load
from os.path import join

from flask import Flask
import pandas as pd

from mushroom_classifier.path_constants import CURRENT_MODEL_DIR
from mushroom_classifier.datacleaner import DataCleaner

APP = Flask(__name__)

MODEL_FILE_PATH = join(CURRENT_MODEL_DIR, "model.sav")
COLUMNS_FILE_PATH = join(CURRENT_MODEL_DIR, "columns_for_index.sav")

MODEL = load(open(MODEL_FILE_PATH, 'rb'))
LOADED_COLUMNS = load(open(COLUMNS_FILE_PATH, 'rb'))

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
    mock_header = "cap-shape,cap-surface,cap-color,bruises,odor,gill-attachment,gill-spacing,gill-size,gill-color,stalk-shape,stalk-root,stalk-surface-above-ring,stalk-surface-below-ring,stalk-color-above-ring,stalk-color-below-ring,veil-type,veil-color,ring-number,ring-type,spore-print-color,population,habitat"   
    mock_predictions = "c,y,e,f,n,f,c,n,w,e,b,s,w,w,p,w,t,s,w,v,d"
    # data_cleaner = DataCleaner(dataset, 'class', 'p')
    # data_cleaner.columns_for_index = loaded_columns
    # unseen_test_data_path = path.join(DATASET_DIR, 'unseen_mushrooms.csv')

    # unseen_test_data = pd.read_csv(unseen_test_data_path)
    # unseen_test_data_cleaned = data_cleaner.clean_new_unseen_data(unseen_test_data)

    # unseen_preds = loaded_model.predict(unseen_test_data_cleaned)



# ROUTE: /api/weights
# method: GET
# returns: jsonified prediction set of loaded model, fully formatted and cleaned
@APP.route('/api/weights')
def get_weights():
    """Returns the weights, with column names, of the model"""
    return ""
