import json
import unittest

from app.views.users_views import *

class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def teardown(self):
        self.app_context.pop()

    def test_create_user(self):
        data = {
            "user_name":  "rick",
            "user_email": "rickiestrick@ricks.com",
            "user_password": "mortyb@#%",
            "user_type": "admin"
        }
        res = self.client.post(
            "/store/api/v1/users",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_user_message(self):
        data = {
            "user_name":  "rick",
            "user_email": "rickiestrick@ricks.com",
            "user_password": "mortyb@#%",
            "user_type": "admin"
        }
        res = self.client.post(
            "/store/api/v1/users",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result["message"], "user account successfully created")

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
