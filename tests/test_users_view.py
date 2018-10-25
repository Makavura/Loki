import json
import unittest
from run import app

from app.views.users_views import *


class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        self.data = {
            "user_name": "rickiestrick",
            "user_password": "mortyb@#%",
            "user_type": "rikitikitavi"
        }

    def test_create_user(self):
        res = self.client.post(
            "/store/api/v1/users",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_user_message(self):
        res = self.client.post(
            "/store/api/v1/users",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertIn("User account successfully created", str(res.data))

    def test_get_users(self):
        res = self.client.get(
            "/store/api/v1/users",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_user(self):
        res = self.client.get(
            "/store/api/v1/users/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def teardown(self):
        self.app_context.pop()
