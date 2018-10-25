import json
import unittest
from run import app

from app.views.products_views import *


class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        self.data = {
            "product_name": "residentjoke",
            "product_description": "sanchezium",
            "product_price": "777",
            "product_quantity": "4"

        }

    def test_create_product(self):
        res = self.client.post(
            "/store/api/v1/products",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_product_message(self):
        res = self.client.post(
            "/store/api/v1/products",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertIn("Product entity successfully created", str(res.data))

    def test_get_products(self):
        res = self.client.get(
            "/store/api/v1/products",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_product(self):
        res = self.client.get(
            "/store/api/v1/products/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def teardown(self):
        self.app_context.pop()

    '''
        def test_if_requested_product_is_in_products(self):
        res = self.client.get(
            "/store/api/v1/products/1",
            headers={"content-type": "application/json"}
        )
        self.assertIn('{"product_name": "residentjoke","product_description": "sanchezium","product_price": "777","product_quantity": "4"}',str(res.data))
    '''