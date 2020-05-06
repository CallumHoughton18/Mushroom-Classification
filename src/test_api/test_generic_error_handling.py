"""Generic API Error Handling Tests"""
import unittest
from test_api.base_test import TestBase

class GenericErrorHandlingTests(TestBase):
    """Contains integration tests for generic error handling, ie invalid route"""

    # def setUp(self):
    #     super(GenericErrorHandlingTests, self).setUp()

    def test_should_return_404(self):
        """Performs get request test to route that does not exist"""
        res = self.client.get(f'/api/prediction//erotu/ef/e//')

        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
