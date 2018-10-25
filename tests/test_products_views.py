import json
import unittest

from app.views.products_views import *


class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def teardown(self):
        self.app_context.pop()

    def test_create_product(self):
        data = {
            "description": "sanchezium",
            "price": "777",
            "quantity": "4"
        }
        res = self.client.post(
            "/store/api/v1/products",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_product_message(self):
        data = {
            "description": "sanchezium",
            "price": "777",
            "quantity": "4"
        }
        res = self.client.post(
            "/store/api/v1/products",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result["message"], "Product entity successfully created")

