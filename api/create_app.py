from flask import Flask
from api.compute import compute
from api.cfg import cfg


def create_app():
    app = Flask(__name__)
    compute(app)
    cfg(app)
    return app
