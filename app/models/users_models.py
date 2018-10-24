
users = []


class Users(object):
    def __init__(self, user_id, user_name, user_email, user_password, user_type):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_type = user_type
        self.user_id = user_id
