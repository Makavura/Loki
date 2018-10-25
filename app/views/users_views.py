from flask import make_response, jsonify, Flask, request
from app.models.users_models import users, Users

app = Flask(__name__)

new_user_info = Users('user_name', 'user_type', 'user_password', 'user_id')


@app.route('/store/api/v1/users', methods=['POST'])
def create_user():
        new_user = new_user_info.create_user()
        response_message = {
            "status": "success",
            "message": "User account successfully created"
        }
        return jsonify(new_user, response_message), 201


@app.route('/store/api/v1/users', methods=['GET'])
def get_users():
        response = new_user_info.get_users()
        return jsonify(response), 200


@app.route('/store/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
        return jsonify(users[user_id])
