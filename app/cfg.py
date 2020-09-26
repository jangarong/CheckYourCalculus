from flask import request, jsonify
from csmath.CFG.contextFree import Grammar


def cfg(app):

    data = {'input_string': '',
            'accept': False,
            'cfg_map': {}}

    @app.route('/api/cfg', methods=['GET'])
    def get_grammar():
        return jsonify(data)

    @app.route('/api/cfg', methods=['POST'])
    def is_accepting():

        # compute whether the string gets accepted or not
        text = request.form['input_string']
        cfg_map = request.form['cfg_map']
        g = Grammar(cfg_map, 'S')

        # output to API
        data['input_string'] = text
        data['cfg_map'] = cfg_map
        data['accept'] = g.is_accepting(text)
        return jsonify(data)
