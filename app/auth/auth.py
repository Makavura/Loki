from flask import make_response, jsonify
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
'''
@auth.get_password
def get_password(username):
    if username == 'rickiestrick':
        return 'mortyb@#%'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
'''