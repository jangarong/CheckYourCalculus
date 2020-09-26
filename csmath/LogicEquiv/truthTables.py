from csmath.LogicEquiv.binaryTree import Node
from csmath.LogicEquiv.normalForms import NormalForms
from csmath.LogicEquiv.symbols import LESymbol


def to_binary(n: int, num_digits: int):
    """
    ------------------------------------------------------------------
    truthTables.to_binary: Generate a binary string based on n.
    ------------------------------------------------------------------
    Parameters:
        n: Number to convert to binary
        num_digits: Max number of digits.
    Returns:
        Binary string.
    ------------------------------------------------------------------
    """

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


def generate_parse_tree(predicate: str, var_lst: list):
    """
    ------------------------------------------------------------------
    truthTables.generate_parse_tree: Creates a parse tree of a
    predicate that contains only unary and binary operators.
    ------------------------------------------------------------------
    Parameters:
        predicate: Must be well formatted, no spaces and all order
        of operations are dictated by brackets (with all of them
        being present already).

        var_lst: List of variables in the predicate.
    ------------------------------------------------------------------
    """

    # split predicate and create tree
    predicate_split = predicate.replace(')', ' )').replace('(', '( ').split(' ')
    root = Node()
    curr_node = root
    for char in predicate_split:
        if char == '(':
            curr_node.left_node = Node(parent_node=curr_node)
            curr_node = curr_node.left_node

        # should go outside of brackets
        elif char == ')':
            curr_node = curr_node.parent_node

            # if we reach an operator rather than the outer brackets
            if curr_node is not None and curr_node.parent_node is not None and curr_node.char != '':
                curr_node = curr_node.parent_node

        # char is a variable (leaf branch)
        elif char in var_lst:
            curr_node.char = char
            curr_node = curr_node.parent_node

        # char is an operator
        else:
            curr_node.char = char
            curr_node.right_node = Node(parent_node=curr_node)
            curr_node = curr_node.right_node

    return root


class TruthTables(NormalForms):
    """
    ------------------------------------------------------------------
    truthTables.TruthTables: Generate truth tables with the given
    symbols.
    ------------------------------------------------------------------
    """

    def check_equiv(self, p1: str, p2: str):
        """
        ------------------------------------------------------------------
        check_equiv: Checks if p1 and p2 are logically equivalent via
        Truth Tables
        ------------------------------------------------------------------
        Parameters:
            p1: Predicate to compare with p2.
            p2: Predicate to compare with p1.
        Returns:
            True if both statements are logically equivalent. False
            otherwise.
        ------------------------------------------------------------------
        """
        return self.generate_truth_table(p1) == self.generate_truth_table(p2)

    def get_vars(self, predicate: str):
        """
        ------------------------------------------------------------------
        get_vars: Creates a parse tree of a predicate that
        contains only unary and binary operators.
        ------------------------------------------------------------------
        Parameters:
            predicate: Must be well formatted, no spaces and all order
            of operations are dictated by brackets (with all of them
            being present already).
        Returns:
            List of variables.
        ------------------------------------------------------------------
        """

        # get rid of non-variable characters
        temp_predicate = predicate
        for symbol in self.symbols:
            temp_predicate = temp_predicate.replace(symbol.char, '')
        temp_predicate = temp_predicate.replace('(', '').replace(')', '')
        vars_lst = temp_predicate.split(' ')

        # get rid of whitespace
        vars_lst = list(set(vars_lst))
        if '' in vars_lst:
            vars_lst.remove('')
        vars_lst.sort()
        return vars_lst

    def post_order_evaluation(self, node: Node, var_dict: dict, unary_symbols: list,
                              binary_symbols: list):
        """
        ------------------------------------------------------------------
        post_order_evaluation: Evaluates operations in post-order.
        ------------------------------------------------------------------
        Parameters:
            node: The node it is currently at.
            var_dict: Dictionary that maps variables to their truth value.
            unary_symbols: list of unary symbols available.
            binary_symbols: list of binary symbols available.
        Returns:
            result of the operation/variable ('1' or '0')
        ------------------------------------------------------------------
        """

        # post-order traversal
        left_val, right_val = None, None
        if node.left_node is not None:  # exists for binary operations
            left_val = self.post_order_evaluation(node.left_node, var_dict, unary_symbols,
                                                  binary_symbols)
        if node.right_node is not None:  # exists for both binary and unary operations
            right_val = self.post_order_evaluation(node.right_node, var_dict, unary_symbols,
                                                   binary_symbols)
        # evaluate the symbol
        if node.char in var_dict.keys():
            return var_dict[node.char]

        # search for binary symbol in list and evaluate via truth table
        elif node.char in binary_symbols:
            for symbol in self.symbols:
                if node.char == symbol.char:
                    return symbol.truth_table[left_val + right_val]

        # search for unary symbol in list and evaluate via truth table
        elif node.char in unary_symbols:
            for symbol in self.symbols:
                if node.char == symbol.char:
                    return symbol.truth_table[right_val]

        else:
            # one of these have to yield a 1 or 0; both of them can't be None and both of them can't
            # have values (2 Nones = empty string, 2 Values = illegal operation).
            if left_val is not None:
                return left_val
            else:
                return right_val

    def evaluate(self, root: Node, var_lst: list, parameters: str):
        """
        ------------------------------------------------------------------
        evaluate: Evaluates predicate tree with the given parameters
        ------------------------------------------------------------------
        Parameters:
            root: Root of predicate tree.
            var_lst: List of variables in the predicate.
            parameters: truth value of the var_lst (parameters[i] is the
                truth value of var_lst[i]).
        Returns:
            Truth value of the predicate.
        ------------------------------------------------------------------
        """

        # create mapping for variables and parameters
        var_dict = {}
        for i in range(len(var_lst)):
            var_dict[var_lst[i]] = parameters[i]

        # create binary/unary symbols list
        unary_symbols = []
        binary_symbols = []
        for symbol in self.symbols:
            if len(symbol.truth_table.keys()) == 2:
                unary_symbols.append(symbol.char)
            else:
                binary_symbols.append(symbol.char)

        # evaluate using post-order
        return self.post_order_evaluation(root, var_dict, unary_symbols, binary_symbols)

    # def clean_predicate(self, predicate: str):

    def generate_truth_table(self, predicate: str):
        """
        ------------------------------------------------------------------
        generate_truth_table: Creates truth table for the given predicate.
        ------------------------------------------------------------------
        Parameters:
            predicate: Predicate of truth table.
        Returns:
            Truth table of the predicate.
        ------------------------------------------------------------------
        """
        var_lst = self.get_vars(predicate)
        n = 2 ** len(var_lst)
        # TODO: Add brackets based on order of operations (and maybe remove excessive spacing?)
        # predicate = clean_predicate(predicate)
        root = generate_parse_tree(predicate, var_lst)
        truth_table = {}
        for i in range(0, n):
            binary_str = to_binary(i, len(var_lst))
            truth_table[binary_str] = self.evaluate(root, var_lst, binary_str)
        return truth_table

    def symbols_to_dicts(self) -> list:
        """
        ------------------------------------------------------------------
        tt_to_dict: Creates list of dictionaries from TruthTable's
        symbols.
        ------------------------------------------------------------------
        """
        res = []
        for symbol in self.symbols:
            symbol_dict = {'order': symbol.order,
                           'truth_table': symbol.truth_table,
                           'char': symbol.char}
            res.append(symbol_dict)
        return res

    def dicts_to_symbols(self, symbol_dicts: list):
        """
        ------------------------------------------------------------------
        dict_to_tt: Creates symbol ordering from list of dictionaries.
        ------------------------------------------------------------------
        Parameters:
            symbol_dicts: List of dictionaries containing the char, order
            and truth table of each symbol.
        ------------------------------------------------------------------
        """
        self.symbols = []
        for symbol_dict in symbol_dicts:
            self.symbols.append(LESymbol(symbol_dict['char'], symbol_dict['order'],
                                         symbol_dict['truth_table']))

    def __init__(self):

        # default symbols (note that this is also the order of evaluation).
        self.symbols = [LESymbol('\\neg', 0, {'1': '0', '0': '1'}),
                        LESymbol('\\wedge', 1, {'11': '1', '10': '0', '01': '0', '00': '0'}),
                        LESymbol('\\vee', 1, {'11': '1', '10': '1', '01': '1', '00': '0'}),
                        LESymbol('\\rightarrow', 2, {'11': '1', '10': '0', '01': '1', '00': '1'}),
                        LESymbol('\\leftrightarrow', 3,
                                 {'11': '1', '10': '0', '01': '0', '00': '1'})]
