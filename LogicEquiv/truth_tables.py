class LESymbol:

    def __init__(self, char, truth_table: dict):
        self.truth_table = truth_table
        self.char = char

"""
Examples of truth tables:
AND
{'11': '1', '10': '0', '01': '0', '00': '0'}
OR
{'11': '1', '10': '1', '01': '1', '00': '0'}
NOT
{'1': '0', '0': '1'}
"""


class TruthTables:

    def __init__(self):
        self.le_not = LESymbol('\\neg', {'1': '0', '0': '1'})
        self.le_and = LESymbol('\\wedge', {'11': '1', '10': '0', '01': '0', '00': '0'})
        self.le_and = LESymbol('\\vee', {'11': '1', '10': '1', '01': '1', '00': '0'})
        self.le_implies = LESymbol('\\rightarrow', {'11': '1', '10': '0', '01': '1', '00': '1'})
        self.le_implies = LESymbol('\\leftrightarrow', {'11': '1', '10': '0', '01': '0', '00': '1'})
