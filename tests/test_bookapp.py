import unittest
from core.app import app


class BasicAppTest(unittest.TestCase):
    """Test the existence and basic behaviour of the app"""
    def setUp(self):
        # Used for creation of test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status(self):
        # Send a GET request to / and check status code
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
