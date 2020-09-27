from flask import request, jsonify
from csmath.LogicEquiv.truthTables import TruthTables


def logicequiv(app):

    data = {'predicate': '',
            'truth_table': {},
            'cnf': '',
            'dnf': '',
            'symbols': []}
    tt = TruthTables()

    @app.route('/api/logicequiv', methods=['GET'])
    def get_le():
        return jsonify(data)

    @app.route('/api/logicequiv', methods=['POST'])
    def post_le():

        # get data from input
        p = request.form['predicate']
        data['symbols'] = request.form['symbols']
        tt.dicts_to_symbols(data['symbols'])

        # output to json
        data['truth_table'] = tt.generate_truth_table(p)
        data['cnf'] = tt.cnf(p)
        data['dnf'] = tt.dnf(p)
