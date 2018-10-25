from flask import make_response, jsonify, Flask, request, Blueprint
from app.models.users_models import users, Users

uzers = Blueprint('uzers', __name__, url_prefix='/store/api/v1')

new_user_info = Users('user_name', 'user_type', 'user_password', 'user_id')


@uzers.route('/uzers', methods=['POST'])
def create_user():
        new_user = new_user_info.create_user()
        response_message = {
            "status": "success",
            "message": "User account successfully created"
        }
        return jsonify(new_user, response_message), 201


@uzers.route('/uzers', methods=['GET'])
def get_users():
        response = new_user_info.get_users()
        return jsonify(response), 200


@uzers.route('/uzers/<int:user_id>', methods=['GET'])
def get_user(user_id):
        return jsonify(users[user_id])
