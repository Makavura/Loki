from flask import make_response, jsonify, Flask, request
from app.models.sales_models import sales, Sales

app = Flask(__name__)

new_sale_info = Sales('attendant', 'sale_id')


@app.route('/store/api/v1/sales', methods=['POST'])
def create_sale():
        new_sale = new_sale_info.create_sale()
        response_message = {
            "status": "success",
            "message": "Sale record successfully created"
        }
        return jsonify(new_sale, response_message), 201


@app.route('/store/api/v1/sales', methods=['GET'])
def get_sales():
        response = new_sale_info.get_sales()
        return jsonify(response), 200


@app.route('/store/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
        return jsonify(sales[sale_id]), 200
