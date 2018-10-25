from flask import make_response, jsonify, Flask, request, Blueprint
from app.models.products_models import products, Products

produkts = Blueprint('produkts', __name__, url_prefix='/store/api/v1')

new_product_info = Products('product_name', 'product_quantity', 'product_price', 'product_id')


@produkts.route('/produkts', methods=['POST'])
def create_product():
        new_product = new_product_info.create_product()
        response_message = {
            "status": "success",
            "message": "Product entity successfully created"
        }
        return jsonify(new_product, response_message), 201


@produkts.route('/produkts', methods=['GET'])
def get_products():
        response = new_product_info.get_products()
        return jsonify(response), 200


@produkts.route('/produkts/<int:product_id>', methods=['GET'])
def get_product(product_id):
        return jsonify(products[product_id])

