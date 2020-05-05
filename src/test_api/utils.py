"""Contains test helper methods for testing the API application"""

def generate_json_with_missing_keys(features_definition: dict):
    """Generates a list of dictionaries with keys from the given features_definitions, each dictionary is missing a key"""
    mock_requests = []
    def_keys = list(features_definition.keys())

    for i in range(len(def_keys)):
        mock_request = {}
        current_keys = def_keys.copy()
        current_keys.pop(i)
        for key in current_keys:
            first_value_in_def = features_definition[key][0]
            mock_request[key] = first_value_in_def
        mock_requests.append(mock_request)

    return mock_requests

def generate_json_with_incorrect_prediction_value(features_definition: dict):
    """
    Generates a list of dictonaries with keys from the given features_definitions, key in the dictionary
    has a corresponding value not allowed by the given definition
    """
    mock_requests = []
    def_keys = list(features_definition.keys())

    for i in range(len(def_keys)):
        mock_request = {}
        current_keys = def_keys.copy()
        for key in current_keys:
            mock_request[key] = features_definition[key][0]

        # Replace one keys value with invalid prediction value
        mock_request[current_keys[i]] = 'q'
        mock_requests.append(mock_request)

    return mock_requests
