from app.models.sales_models import sales, Sales


@app.route('/store/api/v1/sales/', methods=['POST'])
def create_sale():
    if not request.json or 'description' not in 'description' in request.json:
        abort(400)
        sale = {
            'id': sales[-1]['id'] + 1,
            'attendant': request.json.get('attendant', ""),
            'description': request.json.get('description', "")
            }
        sales.append(sale)
    return jsonify({'sale': sale}), 201


@app.route('/store/api/v1/sales', methods=['GET'])
def get_sales(self):
    return jsonify(self.sales), 200


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
        abort(404)
    return make_response(jsonify({'sale': sale[0]}), 200)


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'attendant' in request.json and type(request.json['attendant']) != unicode:
        abort(404)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(404)
    sale[0]['attendant'] = request.json.get('attendant', sale[0]['attendant'])
    sale[0]['description'] = request.json.get('description', sale[0]['description'])
    return jsonify({'sale': sale}), 201


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id   ]
    sales.remove(sale[0])
    return jsonify({}), 200
