"""Initialization file for API, bootstrapping the API"""
from pickle import load
from os import environ
from os.path import join, dirname, abspath
from logging import getLogger
import json
import sys

from flask import Flask, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound
import pandas as pd

from api.custom_logger import setup_logging, get_custom_logger, LoggerType
from api.error_handlers import unhandled_exception_handler, http_error_as_json
from api.prediction.controllers import PREDICTION
from api.weights.controllers import WEIGHTS

from mushroom_classifier.path_constants import CURRENT_MODEL_DIR, DATASET_DIR
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.logisticregression import LogisticRegression
try:
    # Logging needs to be done in separate setup file, reduce bloat of this bootstrapper file
    LOG_CONFIG_PATH = join(dirname(abspath(__file__)), 'logger-config.yaml')
    LOG_FILE_PATH = environ.get('LOGS_DIRECTORY')
    setup_logging(LOG_CONFIG_PATH, LOG_FILE_PATH)

    APP = Flask(__name__)

    CORS = CORS(APP, resources={r"/api/*": {"origins": "*"}})

    APP.register_error_handler(BadRequest, http_error_as_json)
    APP.register_error_handler(NotFound, http_error_as_json)
    APP.register_error_handler(Exception, unhandled_exception_handler)

    MODEL_FILE_PATH = join(CURRENT_MODEL_DIR, 'model.sav')
    COLUMNS_FILE_PATH = join(CURRENT_MODEL_DIR, 'columns_for_index.sav')
    FEATURES_DEFINITION_PATH = environ.get('FEATURE_DEFINITION_PATH')
    # send_from_directory from Flask doesn't like relative paths
    # So relative path is converted to its absolute path
    STATIC_FILES_PATH = abspath(environ.get('DATASET_DIR'))

    APP.MODEL = load(open(MODEL_FILE_PATH, 'rb'))
    # Datacleaner doesn't need dataset for prediction when model loaded, so None can be passed in
    APP.DATA_CLEANER = DataCleaner(None, 'class', 'p')
    LOADED_COLUMNS = load(open(COLUMNS_FILE_PATH, 'rb'))
    APP.DATA_CLEANER.columns_for_index = LOADED_COLUMNS

    with open(FEATURES_DEFINITION_PATH, 'rb') as features_json:
        APP.PREDICTION_DEFINITIONS = json.load(features_json)

    APP.register_blueprint(PREDICTION, url_prefix='/api/prediction')
    APP.register_blueprint(WEIGHTS, url_prefix='/api/weights')

    @APP.route("/api/files/<path:filename>")
    def staticfiles(filename):
        """Route for serving static files from the files directory"""
        # This is purely done for flask dev server, in production static files
        # should be served by the web server, e.g nginx.
        return send_from_directory(STATIC_FILES_PATH, filename)

except Exception as exc:
    # Initialisation has failed, so rethrow exception
    get_custom_logger(LoggerType.FAILURE).critical('App Startup Error: %s', exc, exc_info=True)
    raise exc
