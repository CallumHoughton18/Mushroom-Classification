"""Weights route controller"""
from flask import Blueprint

WEIGHTS = Blueprint('WEIGHTS', __name__)

@WEIGHTS.route('/')
def index():
    """Root route test"""
    return "Weights route"
