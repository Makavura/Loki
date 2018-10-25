from flask import Flask
from instance.config import *
from app.views.products_views import *
from app.views.sales_views import *
from app.views.users_views import *

def create_app(config_by_name):
    app = Flask(__name__)
    app.register_blueprint(produkts)
    app.register_blueprint(cales)
    app.register_blueprint(uzers)
    return app
