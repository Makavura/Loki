from flask import Flask, make_response, jsonify
from app.models.users_models import users, Users

app = Flask(__name__)


@app.route('/store/api/v1/users', methods=['POST'])
def create_user():
        user_id = len(users) + 1
        user = {
            'id': user_id,
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
        return make_response(jsonify(response_message))


@app.route('/store/api/v1/users', methods=['GET'])
def get_users():
        return make_response(jsonify({'users': users}), 200)


@app.route('/store/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return make_response(jsonify({'user': user[0]}), 200)
