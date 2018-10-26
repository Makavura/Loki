from flask import make_response, jsonify, Flask, request, Blueprint, make_response
from app.models.users_models import users, Users

uzers = Blueprint('uzers', __name__, url_prefix='/store/api/v1')



@uzers.route('/uzers', methods=['POST'])
def create_user():
        data = request.get_json()
        user_name = data['user_name']
        user_type = data['user_type']
        user_password = data['user_password']
        new_user_info = Users(user_name, user_type, user_password)
        new_user = new_user_info.create_user()
        response_message = {
            "status": "success",
            "message": "User account successfully created"
        }
        return jsonify(new_user, response_message), 201


@uzers.route('/uzers', methods=['GET'])
def get_uzers():
        return jsonify(users), 200


@uzers.route('/uzers/<int:user_id>', methods=['GET'])
def get_uzer(user_id):
        return jsonify(users[int(user_id)-1])

