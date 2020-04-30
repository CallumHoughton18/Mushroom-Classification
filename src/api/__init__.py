"""Initialization file for API, bootstrapping the API"""
from pickle import load
from os import environ
from os.path import join, dirname, abspath
import logging
import json
import sys

from flask import Flask
import pandas as pd

from api import logger
from api.prediction.controllers import PREDICTION
from api.weights.controllers import WEIGHTS

from mushroom_classifier.path_constants import CURRENT_MODEL_DIR, DATASET_DIR
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.logisticregression import LogisticRegression

try:
    # Logging needs to be done in separate setup file, reduce bloat of this bootstrapper file
    LOG_CONFIG_PATH = join(dirname(abspath(__file__)), 'logger-config.yaml')
    LOG_FILE_PATH = environ.get('LOGS_DIRECTORY')
    logger.setup_logging(LOG_CONFIG_PATH, LOG_FILE_PATH)

    APP = Flask(__name__)

    MODEL_FILE_PATH = join(CURRENT_MODEL_DIR, 'model.sav')
    COLUMNS_FILE_PATH = join(CURRENT_MODEL_DIR, 'columns_for_index.sav')
    FEATURES_DEFINITION_PATH = environ.get('FEATURE_DEFINITION_PATH')

    APP.MODEL = load(open(MODEL_FILE_PATH, 'rb'))
    # Datacleaner doesn't need dataset for prediction when model loaded, so None can be passed in
    APP.DATA_CLEANER = DataCleaner(None, 'class', 'p')
    LOADED_COLUMNS = load(open(COLUMNS_FILE_PATH, 'rb'))
    APP.DATA_CLEANER.columns_for_index = LOADED_COLUMNS
    APP.PREDICTION_DEFINITIONS = json.load(open(FEATURES_DEFINITION_PATH, 'rb'))
    APP.register_blueprint(PREDICTION, url_prefix='/api/prediction')
    APP.register_blueprint(WEIGHTS, url_prefix='/api/weights')
    raise Exception("Oh oh!!")

except Exception as exc:
    logging.critical('Init error: %s', exc, exc_info=True)
    # Initialisation as failed, so rethrow exception
    raise exc
