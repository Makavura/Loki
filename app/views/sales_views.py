from flask import make_response, jsonify, Flask, request
from app.models.sales_models import sales, Sales

app = Flask(__name__)


@app.route('/store/api/v1/sales', methods=['POST'])
def create_sale():
        sale_id = len(sales) + 1
        sale = {
            'id': sale_id,
            'attendant': request.json.get('attendant', ""),
            'description': request.json.get('description', "")
            }

        sales.append(sale)
        response_message = {
            "status": "success",
            "message": "Sale record created successfully"
        }
        return make_response(jsonify(response_message))


@app.route('/store/api/v1/sales', methods=['GET'])
def get_sales():
    return make_response(jsonify({'sales': sales}), 200)


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
        abort(404)
    return make_response(jsonify({'sale': sale[0]}), 200)
