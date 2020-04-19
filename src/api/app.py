"""
Main app file for RESTful API to expose mushroom classifier model
"""
from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def root():
    """Test route for API"""
    return 'Mushroom Classifier API'

# ROUTE: /api/predict?
# method: GET
# params: features(JSON object with user chosen features to predict against model)
# returns: edible or none edible classification response

# ROUTE: /api/weights
# method: GET
# returns: jsonified prediction set of loaded model, fully formatted and cleaned
