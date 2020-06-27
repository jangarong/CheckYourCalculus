from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Something about the app...'

    @app.route('/deltaepsilon')
    def delta_epsilon():
        return 'Delta epsilon proofs go here...'

    return app
