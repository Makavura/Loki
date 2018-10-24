from flask import Flask
from instance.config import *


def create_app(config_by_name):
    app = Flask(__name__)
    return app
