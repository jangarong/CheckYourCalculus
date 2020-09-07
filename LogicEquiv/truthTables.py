class LESymbol:

    def __init__(self, char: str, truth_table: dict):
        self.truth_table = truth_table
        self.char = char
        if len(truth_table.keys()) > 4:
            print("Symbols that take more than 2 variables have not"
                  "been implemented yet for Truth Tables.")

        # note to self: should display an error if the char is ' ', '(' or ')'


def to_binary(n: int, num_digits: int):

    # get binary string
    binary_str = ''
    while n > 0:
        remainder = n % 2
        n = n // 2
        binary_str = str(remainder) + binary_str

    # add trailing zeros according to num_digits
    while len(binary_str) < num_digits:
        binary_str = '0' + binary_str

    return binary_str


class TruthTables:

    def get_vars(self, predicate: str):

        # get rid of non-variable characters
        temp_predicate = predicate
        for symbol in self.symbols:
            temp_predicate = temp_predicate.replace(symbol.char, '')
        temp_predicate = temp_predicate.replace('(', '').replace(')', '')
        vars_lst = temp_predicate.split(' ')

        # get rid of whitespace
        vars_lst = list(set(vars_lst))
        vars_lst.remove('')
        vars_lst.sort()
        return vars_lst

    def evaluate(self, predicate: str, var_list: list, parameters: str):
        print(predicate, var_list, parameters)

    def generate(self, predicate: str):
        var_lst = self.get_vars(predicate)
        n = 2 ** len(var_lst)
        for i in range(0, n):
            self.evaluate(predicate, var_lst, to_binary(i, len(var_lst)))

    def new_symbol(self, char: str, truth_table: dict):
        self.symbols.append(LESymbol(char, truth_table))

    def __init__(self):
        self.symbols = [LESymbol('\\neg', {'1': '0', '0': '1'}),
                        LESymbol('\\wedge', {'11': '1', '10': '0', '01': '0', '00': '0'}),
                        LESymbol('\\vee', {'11': '1', '10': '1', '01': '1', '00': '0'}),
                        LESymbol('\\rightarrow', {'11': '1', '10': '0', '01': '1', '00': '1'}),
                        LESymbol('\\leftrightarrow', {'11': '1', '10': '0', '01': '0', '00': '1'})]
