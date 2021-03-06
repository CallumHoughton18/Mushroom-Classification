"""Prediction routes controller"""
from flask import Blueprint, request, jsonify, current_app as app
from api.custom_route_decorators import validate_prediction_json, log_request
from api.helpers import create_error_response
from api.prediction.services.user_prediction_service import UserPredictionService

PREDICTION = Blueprint('PREDICTION', __name__)

@PREDICTION.route('/submit')
@log_request
@validate_prediction_json
def submit():
    """Handles user prediction submission, returns poisonous prediction"""
    #raise Exception("oops!")
    if not hasattr(request, 'verified_json'):
        return create_error_response("JSON could not be verified", 500)

    user_prediction_verified = request.verified_json
    pred_service = UserPredictionService(app.DATA_CLEANER, app.MODEL)
    unseen_pred = pred_service.make_prediction(user_prediction_verified)
    return jsonify({"poisonous": bool(unseen_pred)})
