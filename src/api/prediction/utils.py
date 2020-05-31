"""Utility methods for prediction functionality"""

def verify_user_prediction(user_inputs_dic: dict, correct_definition_dic: dict):
    """
    Verifies user prediction json against correct json definition
    returns true if correct format, false if not
    """

    if user_inputs_dic.keys() != correct_definition_dic.keys():
        return False

    for user_key, user_value in user_inputs_dic.items():
        possible_values = correct_definition_dic[user_key].keys()
        if user_value not in possible_values:
            return False

    return True
