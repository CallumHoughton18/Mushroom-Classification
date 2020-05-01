"""Contains error handler functions which can be registered to the flask application"""
from logging import getLogger
from api.helpers import create_error_response

def unhandled_exception_handler(error):
    """
    Handles all uncaught exceptions, should be registered to the app
    upon initialization
    """
    original = getattr(error, "original_exception", error)
    getLogger().critical('Unhandled Exception: %s', original) 
    return create_error_response("Unhandled Internal Server Error...", 500)
