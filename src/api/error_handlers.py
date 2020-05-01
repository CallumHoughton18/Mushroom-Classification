"""Contains error handler functions which can be registered to the flask application"""
from werkzeug.exceptions import HTTPException

from api.custom_logger import get_custom_logger, LoggerType
from api.helpers import create_error_response

def unhandled_exception_handler(error: Exception):
    """
    Handles all uncaught exceptions, should be registered to the app
    upon initialization
    """
    original = getattr(error, "original_exception", error)
    get_custom_logger(LoggerType.FAILURE).critical('Unhandled Exception: %s', original)
    return create_error_response("Unhandled Internal Server Error...", 500)

def http_error_as_json(error: HTTPException):
    """
    Turns the given error into a json response containing the error message
    """
    get_custom_logger(LoggerType.BASIC).error('(%s)-%s', error.code, error.description)
    return create_error_response(error.description, error.code)
