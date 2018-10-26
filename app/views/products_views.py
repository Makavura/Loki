from flask import make_response, jsonify, Flask, request, Blueprint, make_response
from app.models.products_models import products, Products
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from app.auth.auth import *

produkts = Blueprint('produkts', __name__, url_prefix='/store/api/v1')



@produkts.route('/produkts', methods=['POST'])
def create_product():
        data = request.get_json()
        product_name = data['product_name']
        product_quantity = data['product_quantity']
        product_price = data['product_price']
        new_product_info = Products(product_name, product_quantity, product_price)
        new_product = new_product_info.create_product()
        response_message = {
            "status": "success",
            "message": "Product entity successfully created"
        }
        return jsonify(new_product, response_message), 201


@produkts.route('/produkts', methods=['GET'])
def get_products():
        return jsonify(products), 200


@produkts.route('/produkts/<int:product_id>', methods=['GET'])
def get_product(product_id):
        return jsonify(products[int(product_id)-1])

