from flask import request, jsonify
from csmath.CFG.contextFree import Grammar

# note to self: test {var: [var+str+var+str, str]}


def cfg(app):

    data = {'string': '',
            'accept': False,
            'cfg_map': {}}

    @app.route('/api/cfg/', methods=['GET'])
    def get_grammar():
        return jsonify(data)

    @app.route('/api/cfg/', methods=['POST'])
    def is_accepting():

        # compute whether the string gets accepted or not
        text = request.form['string']
        cfg_map = request.form['cfg_map']
        cfg = Grammar(cfg_map, 'S')

        # output to API
        data['string'] = text
        data['cfg_map'] = cfg_map
        data['accept'] = cfg.is_accepting(text)
        return jsonify(data)
