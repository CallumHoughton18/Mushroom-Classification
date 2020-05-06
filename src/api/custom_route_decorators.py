"""Contains custom decorators for routes"""
import json
from functools import wraps

from flask import request, current_app as app
from werkzeug.exceptions import BadRequest

from api.prediction.utils import verify_user_prediction
from api.custom_logger import get_custom_logger, LoggerType

def validate_prediction_json(func):
    """validates json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_prediction_json_string = request.args.get('values', type=str)
        if user_prediction_json_string is None:
            raise BadRequest('Missing get parameter: values')
        try:
            list_of_prediction_dics = json.loads(user_prediction_json_string)
        except json.JSONDecodeError:
            raise BadRequest('Could not decode JSON parameter \'values\'')

        if not isinstance(list_of_prediction_dics, list):
            raise BadRequest('values parameter must be a json array')

        user_predictions_dic = verify_user_prediction(list_of_prediction_dics[0], app.PREDICTION_DEFINITIONS)
        if user_predictions_dic is False:
            raise BadRequest('Given values does not match predictions definition')

        request.verified_json = list_of_prediction_dics
        return func(*args, **kwargs)

    return decorated_function

def log_request(func):
    """validates json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        msg = f'{request.remote_addr}-{request.url}'
        get_custom_logger(LoggerType.BASIC).info(msg)
        return func(*args, **kwargs)

    return decorated_function
