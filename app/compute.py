from flask import request, jsonify
import json
from csmath.Computations.compute import Compute


def compute(app):

    response = {'equation': '',
            'correct': 'yes'}
    comps = Compute()

    @app.route('/api/compute', methods=['GET'])
    def get_eqs():
        return jsonify(response)

    @app.route('/api/compute', methods=['POST'])
    def display_eqs():
        data = json.loads(request.data)
        text = data['equation']
        response['equation'] = text
        if text == "":
            return jsonify(response)
        # insert equation in computation object
        if comps.current_equation is None:
            comps.new(text)
            response['correct'] = 'yes'
        else:
            valid = comps.insert(text)
            if valid:
                response['correct'] = 'yes'
            else:
                response['correct'] = 'no'
        #To see response:
        #print(response['equation'], response['correct'])
        return jsonify(response)
