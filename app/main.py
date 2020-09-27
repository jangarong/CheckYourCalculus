from flask import Flask
from app.compute import compute
from app.cfg import cfg
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
compute(app)
cfg(app)


