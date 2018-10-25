from flask import Flask
from instance.config import *
from app.models.users_models import users, Users

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

username_table = {u.username: u for u in users}
user_id_table = {u.id: u for u in users}


def authenticate(user_name, user_password):
    user = username_table.get(user_name, None)
    if user and safe_str_cmp(user.user_password.encode('utf-8'), user_password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_table.get(user_id, None)


app = Flask(__name__)


jwt = JWT(app, authenticate, identity)


@jwt_required()
def protected():
    return '%s' % current_identity
