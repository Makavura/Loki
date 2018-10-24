from flask import Flask, make_response, jsonify
from app.models.users_models import users, Users

app = Flask(__name__)


@app.route('/store/api/v1/users', methods=['POST'])
def create_user():
        user = {
            'user_id': users[-1]['id'] + 1,
            'user_name':  "",
            'user_email': "" ,
            'user_password': "",
            'user_type': ""
        }

        users.append(user)
        response_message = {
            "status": "success",
            "message": "user account successfully created"
        }
        return jsonify({users}), 201, make_response(jsonify({response_message}))


@app.route('/store/api/v1/users', methods=['GET'])
def get_users():
        return make_response(jsonify({'users': users}), 200)


@app.route('store/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for i, users in enumerate(self.users):
        if user['id'] == user_id:
            return make_response(jsonify(user))
        elif user['id'] != user_id:
                print("access error")
                response_message = {
                    "status": "fail",
                    "message": "non-existent user account "
                }
        return make_response(jsonify(response_message))
