"""Contains test helper methods for testing the API application"""

def generate_json_with_missing_keys(features_definition: dict):
    """Generates a list of dictionaries with keys from the given features_definitions, each dictionary is missing a key"""
    mock_requests = []
    def_keys = list(features_definition.keys())

    for def_key in def_keys:
        mock_request = {key: value[0] for key, value in features_definition.items() if key is not def_key}
        mock_requests.append(mock_request)

    return mock_requests

def generate_json_with_incorrect_prediction_value(features_definition: dict):
    """
    Generates a list of dictonaries with keys from the given features_definitions, key in the dictionary
    has a corresponding value not allowed by the given definition
    """
    mock_requests = []
    def_keys = list(features_definition.keys())

    for def_key in def_keys:
        mock_request = {key: value[0] for key, value in features_definition.items()}
        # Replace given keys, based on enumeration step, value with invalid prediction value
        mock_request[def_key] = 'q'
        mock_requests.append(mock_request)

    return mock_requests
