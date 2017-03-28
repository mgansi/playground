# import os
from platformMonitor import app
# import tempfile
# from flask_testing import TestCase

import unittest
from flask import Flask


class PlatformMonitorTestCase(unittest.TestCase):
    """Testing for platform monitor"""
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_get_index(self):
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_equal_numbers(self):
        self.assertEqual(2, 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
