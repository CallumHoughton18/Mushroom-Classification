"""Utility methods for prediction functionality"""

def verify_user_prediction(user_inputs_dic, correct_definition_dic):
    """
    Verifies user prediction json against correct json definition
    returns true if correct format, false if not
    """
    print(set(correct_definition_dic.keys()).difference(user_inputs_dic.keys()))

    if user_inputs_dic.keys() == correct_definition_dic.keys():
        return True
    return False
