from app.main import app
from flask_cors import CORS

CORS(app, support_credentials=True)

if __name__ == '__main__':
    app.run()
