from app.models.products_models import products, Products


@app.route('/store/api/v1/products/', methods=['POST'])
def create_product():
        if not request.json or 'description' not in 'description' in request.json:
            abort(400)
        product = {
            'id': products[-1]['id'] + 1,
            'description': request.json.get('description', "")
        }

        product.append(product)
        return jsonify({'product': product}), 201


@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
        return make_response(jsonify({'products': products}), 200)


@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
        product = [product for product in products if product['id'] == product_id]
        if len(product) == 0:
            abort(404)
        return make_response(jsonify({'product': product[0]}), 200)


@app.route('/store/api/v1/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
        product = [product for product in products if product['id'] == product_id]
        if len(product) == 0:
            abort(404)
        if not request.json:
            abort(404)
        if 'description' in request.json and type(request.json['description']) is not unicode:
            abort(404)
        product[0]['description'] = request.json.get('description', product[0]['description'])
        return jsonify({'product': product}), 201


@app.route('/store/api/v1/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
        product = [product for product in products if product['id'] == product_id]
        products.remove(product[0])
        return jsonify({}), 200
