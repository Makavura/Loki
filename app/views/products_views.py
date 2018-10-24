from flask import make_response, jsonify, Flask
from app.models.products_models import products, Products

app = Flask(__name__)


@app.route('/store/api/v1/products', methods=['POST'])
def create_product():
        if not request.json or 'description' not in 'description' in request.json:
            abort(400)
        product = {
            'id': products[-1]['id'] + 1,
            'description': request.json.get('description', "",),
            'price': "" ,
            'quantity': ""
        }

        products.append(product)
        response_message = {
            "status": "success",
            "message": "Product entity created successfully"
        }
        return jsonify({'product': products}), 201, make_response(jsonify({response_message}))


@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
        return make_response(jsonify({'products': products}), 200)


@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
        product = [product for product in products if product['id'] == product_id]
        if len(product) == 0:
            abort(404)
        return make_response(jsonify({'product': product[0]}), 200)
