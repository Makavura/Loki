import json
import unittest

from app.views.sales_views import *

class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def teardown(self):
        self.app_context.pop()

    def test_create_sale(self):
        data = {
            "attendant": "cooper",
            "description": "bazingA!"
        }
        res = self.client.post(
            "/store/api/v1/sales",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_create_sale_message(self):
        data = {
            "attendant": "cooper",
            "description": "bazingA!!"
        }
        res = self.client.post(
            "/store/api/v1/sales",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result["message"], "Sale record created successfully")