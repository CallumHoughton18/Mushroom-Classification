"""Contains helper methods for mushroom prediction API"""
from flask import jsonify

def create_error_response(msg, status_code: int):
    """Returns reponse object with given error message as json and status code"""
    res = jsonify({"msg":msg}), status_code
    return res
