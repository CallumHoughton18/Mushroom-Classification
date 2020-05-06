"""TestBase class for API testing"""
from unittest import TestCase

from api import APP
from api.custom_logger import disable_custom_logging

class TestBase(TestCase):
    """Base class for api tests"""
    def setUp(self):
        disable_custom_logging()
        APP.testing = True
        self.client = APP.test_client()
