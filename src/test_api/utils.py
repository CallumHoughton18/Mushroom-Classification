"""Contains test helper methods for testing the API application"""

def generate_json_with_missing_keys(features_definition: dict):
    """Generates a dictionary from the given features_definitions, missing the first key"""
    mock_request = {}
    def_keys = list(features_definition.keys())
    def_keys.pop(0)

    for key in def_keys:
        first_value_in_def = features_definition[key][0]
        mock_request[key] = first_value_in_def

    return mock_request
