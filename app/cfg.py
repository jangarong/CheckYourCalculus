from flask import request, jsonify
import json
from csmath.CFG.contextFree import Grammar


def cfg(app):

    response = {'string': '',
            'accept': False,
            'cfg_map': {}}

    @app.route('/api/cfg', methods=['GET'])
    def get_grammar():
        return jsonify(response)

    @app.route('/api/cfg', methods=['POST'])
    def is_accepting():

        # compute whether the string gets accepted or not
        data = json.loads(request.data)
        text = data['string']
        cfg_map = data['cfg_map']
        cfg = Grammar(cfg_map, 'S')

        #TODO: Not sure if this will behave well with null/empty data/text/cfg_map


        # output to API
        response['string'] = text
        response['cfg_map'] = cfg_map
        response['accept'] = cfg.is_accepting(text)
        return jsonify(response)
