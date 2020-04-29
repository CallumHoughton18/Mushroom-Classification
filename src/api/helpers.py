"""Contains helper methods for mushroom prediction application"""
import re
from os import environ
from flask import jsonify
import yaml

def create_error_response(msg, status_code: int):
    """Returns reponse object with given error message as json and status code"""
    res = jsonify({"msg":msg}), status_code
    return res

def generate_enviroment_variable_yaml_loader(tag):
    """Generates loader, to handle given tag in yaml"""
    pattern = re.compile('.*?\\${(\\w+)}.*?')
    loader = yaml.SafeLoader

    loader.add_implicit_resolver(tag, pattern, None)

    def constructor_env_variables(loader, node):
        """
        Extracts the environment variable from the node's value
        """
        value = loader.construct_scalar(node)
        match = pattern.findall(value)  # to find all env variables in line
        if match:
            full_value = value
            for env_var in match:
                full_value = full_value.replace(
                    f'${{{env_var}}}', environ.get(env_var, env_var)
                )
            return full_value
        return value

    loader.add_constructor(tag, constructor_env_variables)
    return loader
