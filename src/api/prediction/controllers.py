"""Prediction routes controller"""

import json
from flask import Blueprint, request, current_app as app
import pandas as pd

from api.custom_route_decorators import check_prediction_json
from api.prediction.utils import verify_user_prediction

PREDICTION = Blueprint('PREDICTION', __name__)

@PREDICTION.route('/')
def index():
    """Root test"""
    return "prediction route"

@PREDICTION.route('/submit')
@check_prediction_json
def submit():
    """Handles user prediction submission, returns edible prediction"""
    # maybe do error handling in decorator? mimicking route 'middleware' type pattern
    user_prediction_json_string = request.args.get('values')
    if user_prediction_json_string is None:
        return "Missing parameter: values!"
    try:
        prediction_dic = json.loads(user_prediction_json_string)
    except json.JSONDecodeError:
        return "Could not decode param: values json..."

    user_predictions_dic = verify_user_prediction(prediction_dic[0], app.PREDICTION_DEFINITIONS)
    if user_predictions_dic is False:
        return "Given values does not match definition for predictions"

    mock_predictions = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"e\",\"bruises\":\"f\",\"odor\":\"n\",\"gill-attachment\":\"f\",\"gill-spacing\":\"c\",\"gill-size\":\"n\",\"gill-color\":\"w\",\"stalk-shape\":\"e\",\"stalk-root\":\"b\",\"stalk-surface-above-ring\":\"s\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"s\",\"spore-print-color\":\"w\",\"population\":\"v\",\"habitat\":\"d\"}]"
    prediction_df = pd.read_json(mock_predictions)
    prediction_cleaned = app.DATA_CLEANER.clean_new_unseen_data(prediction_df)
    unseen_pred = app.MODEL.predict(prediction_cleaned)[0]
    return {"poisonous": bool(unseen_pred)}
