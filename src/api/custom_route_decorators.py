"""Contains custom decorators for routes"""
import json
from functools import wraps

from flask import request, current_app as app

from api.prediction.utils import verify_user_prediction
from api.helpers import create_error_response

def validate_prediction_json(func):
    """validates json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_prediction_json_string = request.args.get('values')
        if user_prediction_json_string is None:
            return create_error_response("missing get parameter: values", 400)
        try:
            prediction_dic = json.loads(user_prediction_json_string)
        except json.JSONDecodeError:
            return create_error_response("Could not decode JSON parameter \'values\'", 400)

        user_predictions_dic = verify_user_prediction(prediction_dic[0], app.PREDICTION_DEFINITIONS)
        if user_predictions_dic is False:
            return create_error_response("Given values does not match predictions definition", 400)

        request.verified_json = prediction_dic
        return func(*args, **kwargs)

    return decorated_function
