import json
import unittest

from app.auth.auth import *

class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def teardown(self):
        self.app_context.pop()

