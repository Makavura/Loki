from flask import make_response, jsonify, Flask, request
from app.models.products_models import products, Products

app = Flask(__name__)


@app.route('/store/api/v1/products', methods=['POST'])
def create_product():
        data = request.json()
        new_product = data.create_products()
        response_message = {
            "status": "success",
            "message": "Product entity successfully created"
        }
        return make_response(jsonify(response_message)), jsonify({'product': new_product})


@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
        response = get_products()
        return make_response(jsonify({'products': response}), 200)


@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product():
        response = get_product()
        return make_response(jsonify({'product': response}), 200)

