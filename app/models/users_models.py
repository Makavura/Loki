
users = []

class Users(object):
    def __init__(self, user_name, user_type, user_password, user_id):
        self.user_name = user_name
        self.user_type = user_type
        self.user_password = user_password
        self.user_id = user_id

    def create_user(self):
        new_user_info= {}
        new_user_info['product_id'] = len(users) + 1
        new_user_info['user_name'] = self.user_name
        new_user_info['user_type'] = self.user_type
        new_user_info['user_password'] = self.user_password
        users.append(new_user_info)
        return new_user_info

    def get_users(self):
        return users

    def get_user(self, user_id):
        user = [user for user in users if user['user_id'] == user_id]
        return make_response(jsonify({'user': user[0]}), 200)
