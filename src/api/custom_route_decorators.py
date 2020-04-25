"""Contains custom decorators for routes"""
import json
from functools import wraps

from flask import request, current_app as app

from api.prediction.utils import verify_user_prediction

def validate_prediction_json(func):
    """validates json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_prediction_json_string = request.args.get('values')
        if user_prediction_json_string is None:
            return "Missing get parameter: values", 400
        try:
            prediction_dic = json.loads(user_prediction_json_string)
        except json.JSONDecodeError:
            return "Could not decode param: values json...", 400

        user_predictions_dic = verify_user_prediction(prediction_dic[0], app.PREDICTION_DEFINITIONS)
        if user_predictions_dic is False:
            return "Given values does not match definition for predictions", 400

        request.verified_json = prediction_dic
        return func(*args, **kwargs)

    return decorated_function
