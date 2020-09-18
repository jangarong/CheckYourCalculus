from flask import Flask
from app.compute import compute
from app.cfg import cfg

app = Flask(__name__)

compute(app)
cfg(app)


