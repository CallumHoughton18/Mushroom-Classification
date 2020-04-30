"""Contains custom decorators for routes"""
import json
from functools import wraps
import logging

from flask import request, current_app as app

from api.prediction.utils import verify_user_prediction
from api.helpers import create_error_response

LOGGER = logging.getLogger(__name__)

def validate_prediction_json(func):
    """validates json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_prediction_json_string = request.args.get('values')
        app.logger.info(f'({request.remote_addr}) - submitted prediction request')
        if user_prediction_json_string is None:
            err = create_error_response("missing get parameter: values", 400)
            app.logger.info(f'({request.remote_addr}) - submitted prediction request failed: {err[0].data}')
            return err
        try:
            prediction_dic = json.loads(user_prediction_json_string)
        except json.JSONDecodeError:
            err = create_error_response("Could not decode JSON parameter \'values\'", 400)
            app.logger.info(f'({request.remote_addr}) - submitted prediction request failed: {err[0].data}')
            return err

        user_predictions_dic = verify_user_prediction(prediction_dic[0], app.PREDICTION_DEFINITIONS)
        if user_predictions_dic is False:
            err = create_error_response("Given values does not match predictions definition", 400)
            app.logger.info(f'({request.remote_addr}) - submitted prediction request failed: {err[0].data}')
            return err

        request.verified_json = prediction_dic
        return func(*args, **kwargs)

    return decorated_function
