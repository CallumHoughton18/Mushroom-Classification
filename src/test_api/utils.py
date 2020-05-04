"""Contains test helper methods for testing the API application"""

def generate_json_with_missing_keys(features_definition: dict):
    """Generates a dictionary from the given features_definitions, missing the first key"""
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
