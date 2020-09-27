from flask import Flask
from app.compute import compute
from app.cfg import cfg
from app.logicequiv import logicequiv

app = Flask(__name__)
compute(app)
cfg(app)
logicequiv(app)


