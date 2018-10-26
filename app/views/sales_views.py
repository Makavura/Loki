from flask import make_response, jsonify, Flask, request, Blueprint, make_response
from app.models.sales_models import sales, Sales

cales = Blueprint('cales', __name__, url_prefix='/store/api/v1')



@cales.route('/cales', methods=['POST'])
def create_sale():
        data = request.get_json()
        attendant = data['attendant']
        new_sale_info = Sales(attendant)
        new_sale = new_sale_info.create_sale()
        response_message = {
            "status": "success",
            "message": "Sale record successfully created"
        }
        return jsonify(new_sale, response_message), 201


@cales.route('/cales', methods=['GET'])
def get_sales():
        return jsonify(sales), 200


@cales.route('/cales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
        return jsonify(sales[int(sale_id)-1])

