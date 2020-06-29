from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/derivatives')
    def delta_epsilon():
        return render_template('derivatives.html', equation="")

    @app.route('/derivatives', methods=['POST'])
    def delta_epsilon_input():
        text = request.form['text']
        return render_template('derivatives.html', equation=text)

    return app

