"""Initialization file for API, bootstrapping the API"""
from pickle import load
from os.path import join

from flask import Flask
import pandas as pd

from api.prediction.controllers import PREDICTION
from api.weights.controllers import WEIGHTS

from mushroom_classifier.path_constants import CURRENT_MODEL_DIR, DATASET_DIR
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.logisticregression import LogisticRegression

APP = Flask(__name__)

MODEL_FILE_PATH = join(CURRENT_MODEL_DIR, "model.sav")
COLUMNS_FILE_PATH = join(CURRENT_MODEL_DIR, "columns_for_index.sav")

APP.MODEL = load(open(MODEL_FILE_PATH, 'rb'))
# Datacleaner doesn't need dataset for prediction when model loaded, so None can be passed in
APP.DATA_CLEANER = DataCleaner(None, 'class', 'p')
LOADED_COLUMNS = load(open(COLUMNS_FILE_PATH, 'rb'))
APP.DATA_CLEANER.columns_for_index = LOADED_COLUMNS

APP.register_blueprint(PREDICTION, url_prefix='/api/prediction')
APP.register_blueprint(WEIGHTS, url_prefix='/api/weights')
