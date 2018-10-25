from flask import make_response, jsonify, Flask, request
from app.models.products_models import products, Products

app = Flask(__name__)

new_product_info = Products('product_name', 'product_quantity', 'product_price', 'product_id')


@app.route('/store/api/v1/products', methods=['POST'])
def create_product():
        new_product = new_product_info.create_product()
        response_message = {
            "status": "success",
            "message": "Product entity successfully created"
        }
        return jsonify(new_product, response_message), 201


@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
        response = new_product_info.get_products()
        return jsonify(response), 200


@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
        return jsonify(products[product_id])

