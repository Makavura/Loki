from flask import make_response, jsonify, Flask, request
from app.models.products_models import products, Products

app = Flask(__name__)


@app.route('/store/api/v1/products', methods=['POST'])
def create_product():
        product_id = len(products) + 1
        product = {
            'id': product_id,
            'description': request.json.get('description', "",),
            'price': "" ,
            'quantity': ""
        }

        products.append(product)
        response_message = {
            "status": "success",
            "message": "Product entity successfully created"
        }
        return make_response(jsonify(response_message))


@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
        return make_response(jsonify({'products': products}), 200)


@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
        product = [product for product in products if product['id'] == product_id]
        if len(product) == 0:
            abort(404)
        return make_response(jsonify({'product': product[0]}), 200)
