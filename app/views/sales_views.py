from flask import make_response, jsonify, Flask, request, Blueprint
from app.models.sales_models import sales, Sales

cales = Blueprint('cales', __name__, url_prefix='/store/api/v1')

new_sale_info = Sales('attendant', 'sale_id')


@cales.route('/cales', methods=['POST'])
def create_sale():
        new_sale = new_sale_info.create_sale()
        response_message = {
            "status": "success",
            "message": "Sale record successfully created"
        }
        return jsonify(new_sale, response_message), 201


@cales.route('/cales', methods=['GET'])
def get_sales():
        response = new_sale_info.get_sales()
        return jsonify(response), 200


@cales.route('/cales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
        return jsonify(sales[sale_id]), 200
