"""Prediction Controller Tests"""
# pylint: disable=C0301
import unittest
import json
from os import environ
import api

from api.custom_logger import disable_custom_logging
from test_api.utils import generate_json_with_missing_keys

class PredictionControllerTests(unittest.TestCase):
    """Contains integration tests for prediction controller"""
    def setUp(self):
        disable_custom_logging()
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

    def test_should_return_400_if_values_json_malformed(self):
        """Should return 400 error message if values json cannot be deserialized"""
        malformed_json = "[{\"cap-shape\":,\"cap-surface\":\"y\",\"cap-color\":\"e\",\"bruises\":\"f\",\"odor\":\"n\",\"gill-attachment\":\"f\",\"gill-spacing\":\"c\",\"gill-size\":\"n\",\"gill-color\":\"w\",\"stalk-shape\":\"e\",\"stalk-root\":\"b\",\"stalk-surface-above-ring\":\"s\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"s\",\"spore-print-color\":\"w\",\"population\":\"v\",\"habitat\":\"d\"}]"

        res = self.client.get(f'/api/prediction/submit?values={malformed_json}')
        json_data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(json_data['msg'], 'Could not decode JSON parameter \'values\'')

    def test_should_return_true_for_poisonous_values(self):
        """Should return 200 response with poisonous field set to True"""
        correct_json = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"e\",\"bruises\":\"f\",\"odor\":\"n\",\"gill-attachment\":\"f\",\"gill-spacing\":\"c\",\"gill-size\":\"n\",\"gill-color\":\"w\",\"stalk-shape\":\"e\",\"stalk-root\":\"b\",\"stalk-surface-above-ring\":\"s\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"s\",\"spore-print-color\":\"w\",\"population\":\"v\",\"habitat\":\"d\"}]"

        res = self.client.get(f'/api/prediction/submit?values={correct_json}')
        json_data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['poisonous'], True)

    def test_should_return_false_for_poisonous_values(self):
        """Should return 200 response with poisonous field set to False"""
        #correct_json = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"w\",\"bruises\":\"f\",\"odor\":\"n\",\"gill-attachment\":\"f\",\"gill-spacing\":\"w\",\"gill-size\":\"n\",\"gill-color\":\"n\",\"stalk-shape\":\"e\",\"stalk-root\":\"s\",\"stalk-surface-above-ring\":\"s\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"u\",\"veil-color\":\"w\",\"ring-number\":\"n\",\"ring-type\":\"n\",\"spore-print-color\":\"n\",\"population\":\"c\",\"habitat\":\"w\"}]"
        correct_json = "[{\"cap-shape\":\"c\",\"cap-surface\":\"y\",\"cap-color\":\"w\",\"bruises\":\"f\",\"odor\":\"n\",\"gill-attachment\":\"f\",\"gill-spacing\":\"w\",\"gill-size\":\"n\",\"gill-color\":\"n\",\"stalk-shape\":\"e\",\"stalk-root\":\"e\",\"stalk-surface-above-ring\":\"s\",\"stalk-surface-below-ring\":\"s\",\"stalk-color-above-ring\":\"w\",\"stalk-color-below-ring\":\"w\",\"veil-type\":\"p\",\"veil-color\":\"w\",\"ring-number\":\"t\",\"ring-type\":\"n\",\"spore-print-color\":\"n\",\"population\":\"v\",\"habitat\":\"d\"}]"

        res = self.client.get(f'/api/prediction/submit?values={correct_json}')
        json_data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['poisonous'], False)

if __name__ == '__main__':
    unittest.main()
