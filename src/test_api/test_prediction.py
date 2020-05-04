"""Prediction Controller Tests"""

import unittest
import json
from os import environ

import api
from test_api.utils import generate_json_with_missing_keys

class PredictionControllerTests(unittest.TestCase):
    """Contains integration tests for prediction controller"""
    def setUp(self):
        api.APP.testing = True
        self.client = api.APP.test_client()
        feature_definition_path = environ.get('FEATURE_DEFINITION_PATH')
        self.definitions = json.load(open(feature_definition_path, 'rb'))

    def test_should_return_400_response_if_missing_values(self):
        """Should return 400 error message if values JSON parameter missing"""
        res = self.client.get('/api/prediction/submit', json={})
        json_data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(json_data['msg'], 'Missing get parameter: values')

    def test_should_return_400_response_if_values_missing_key(self):
        """Should return 400 error message if values JSON missing key from feature-definitions"""
        dics_with_missing_key = generate_json_with_missing_keys(self.definitions)
        for dic in dics_with_missing_key:
            values_string = json.dumps([dic])
            
            res = self.client.get(f'/api/prediction/submit?values={values_string}')
            json_data = res.get_json()

            self.assertEqual(res.status_code, 400)
            self.assertEqual(json_data['msg'], 'Given values does not match predictions definition')

if __name__ == '__main__':
    unittest.main()
