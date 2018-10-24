from flask import Flask
from instance.config import *
from app.views.products_views import *
from app.views.sales_views import *

def create_app(config_by_name):
    app = Flask(__name__)
    return app
