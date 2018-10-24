from flask import make_response, jsonify, Flask
from app.models.sales_models import sales, Sales

app = Flask(__name__)


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
        products.append(product)
        response_message = {
            "status": "success",
            "message": "Sale record entity created successfully"
        }

    return jsonify({'sale': sales}), 201, make_response(jsonify({response_message}))


@app.route('/store/api/v1/sales', methods=['GET'])
def get_sales(self):
    return jsonify(self.sales), 200


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
        abort(404)
    return make_response(jsonify({'sale': sale[0]}), 200)

