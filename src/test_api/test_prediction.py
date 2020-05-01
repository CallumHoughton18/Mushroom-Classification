"""Prediction Controller Tests"""

import unittest
import api

class PredictionControllerTests(unittest.TestCase):
    """Contains integration tests for prediction controller"""
    def setUp(self):
        api.APP.testing = True
        self.client = api.APP.test_client()

    def test_should_return_missing_values_response(self):
        """Should return 400 error message if values JSON parameter missing"""
        res = self.client.get('/api/prediction/submit', json={})
        json_data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(json_data['msg'], 'Missing get parameter: values')

if __name__ == '__main__':
    unittest.main()
