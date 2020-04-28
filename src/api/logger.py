"""Helper methods that help setup a flask application"""
from logging.config import fileConfig

def setup_logger(setup_file_path):
    """Sets up logger, using given config within setup_file_path .yaml file"""
    # fileConfig(setup_file_path)
