from flask import Flask
from api.compute import compute


def create_app():
    app = Flask(__name__)
    compute(app)
    return app
