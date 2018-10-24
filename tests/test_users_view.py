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
