import json
import unittest
from run import app

from app.views.sales_views import *


class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        self.data = {
            "attendant": "ulalala"
        }

    def test_create_sale(self):
        res = self.client.post(
            "/store/api/v1/cales",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_sale_message(self):
        res = self.client.post(
            "/store/api/v1/cales",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertIn("Sale record successfully created", str(res.data))

    def test_get_sales(self):
        res = self.client.get(
            "/store/api/v1/cales",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_sale(self):
        res = self.client.get(
            "/store/api/v1/cales/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_if_requested_sale_is_in_sales(self):
        res = self.client.get(
            "/store/api/v1/cales/1",
            headers={"content-type": "application/json"}
        )
        self.assertIn('{"attendant":"ulalala","sale_id":"1"}',str(res.data))

    def teardown(self):
        self.app_context.pop()
