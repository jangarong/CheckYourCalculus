from flask import request, jsonify
from csmath.Computations.compute import Compute


def compute(app):

    data = {'equation': '',
            'correct': 'yes'}
    comps = Compute()

    @app.route('/app/compute', methods=['GET'])
    def get_eqs():
        return jsonify(data)

    @app.route('/app/compute', methods=['POST'])
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

        return jsonify(data)
