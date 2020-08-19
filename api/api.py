from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def eq_input():
        text = request.form['text']
        return render_template('index.html', equation=text)

    return app

