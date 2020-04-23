"""Prediction routes controller"""

from flask import Blueprint, current_app as app
import pandas as pd

from api.custom_route_decorators import check_prediction_json

PREDICTION = Blueprint('PREDICTION', __name__)

@PREDICTION.route('/')
def index():
    """Root test"""
    return "prediction route"

@PREDICTION.route('/submit')
@check_prediction_json
def submit():
    """Handles user prediction submission, returns edible prediction"""
    mock_predictions = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"e\",\"bruises\":\"f\",\"odor,gill-attachment\":\"n\",\"gill-spacing\":\"f\",\"gill-size\":\"c\",\"gill-color\":\"n\",\"stalk-shape\":\"w\",\"stalk-root\":\"e\",\"stalk-surface-above-ring\":\"b\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"s\",\"spore-print-color\":\"w\",\"population\":\"v\",\"habitat\":\"d\"}]"
    prediction_df = pd.read_json(mock_predictions)
    prediction_cleaned = app.DATA_CLEANER.clean_new_unseen_data(prediction_df)
    unseen_pred = app.MODEL.predict(prediction_cleaned)[0]
    return {"poisonous": bool(unseen_pred)}
