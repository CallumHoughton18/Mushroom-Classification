"""Contains custom decorators for routes"""
from functools import wraps
# from flask import flash, redirect, url_for

def check_prediction_json(func):
    """Verifies json in parameter matches expected json from features-definition.json"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # get loaded .json definition file
        # if def.keys.count ==  param.keys.count and has valid values within def range
        # continue, passing parsed json to function
        # else, redirect to error page
        return func(*args, **kwargs)
    return decorated_function
