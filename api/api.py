from flask import Flask, render_template, request, jsonify
from Computations.compute import Computation


def create_app():

    data = {'equation': '',
            'correct': 'yes'}
    comps = Computation()
    app = Flask(__name__)

    @app.route('/api/eqs', methods=['GET'])
    def get_eqs():
        return jsonify(data)

    # the below functions are there to test the API
    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def display_eqs():
        text = request.form['text']
        data['equation'] = text

        # insert equation in computation object
        if comps.current_equation is None:
            comps.new(text)
            data['correct'] = 'yes'
        else:
            valid = comps.insert(text)
            if valid:
                data['correct'] = 'yes'
            else:
                data['correct'] = 'no'

        return render_template('index.html', equation=data['equation'], correct=data['correct'])

    return app

