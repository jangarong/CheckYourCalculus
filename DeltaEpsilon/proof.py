import sympy as sm
from sympy.parsing.latex import parse_latex
from DeltaEpsilon.variables import Variables


class DeltaEpsilonProof(Variables):
    """
    DeltaEpsilonProof
    """

    """
    ------------------------------------------------------------------
    print_all: Prints all expressions stored in the proof.
    ------------------------------------------------------------------
    """

    def print_all(self):
        for equation in self.equations:
            print(sm.latex(equation))

    """
    ------------------------------------------------------------------
    is_less_than: Checks if ex1 > ex2, or if ex1 >= ex2, if ex2 
    contains delta and ex1 does not.
    ------------------------------------------------------------------
    Parameters:
        ex1: First expression
        ex2: Second expression
    Returns:
        True if ex1 > ex2 (False otherwise)
    ------------------------------------------------------------------
    """

    def is_less_than(self, exp1, exp2):

        # check zero case (0 < epsilon)
        if sm.simplify(exp1) == 0 and sm.simplify(exp2) == sm.latex(self.epsilon):
            return True

        exps = self.sub_exps(exp1, exp2)
        # if first eq does not contain delta but the 2nd equation does
        if str(self.delta) not in sm.latex(exp1) and str(self.delta) in sm.latex(exp2):
            return sm.simplify(exps[0] - exps[1]) == 0  # or sm.simplify(exps[0]) <
            # sm.simplify(exps[1])
        else:
            return sm.simplify(exps[0]) < sm.simplify(exps[1])

    """
    ------------------------------------------------------------------
    is_more_than: Checks if ex1 < ex2, or if ex1 <= ex2, if ex2 
    contains delta and ex1 does not.
    ------------------------------------------------------------------
    Parameters:
        ex1: First expression
        ex2: Second expression
    Returns:
        True if ex1 < ex2 (False otherwise)
    ------------------------------------------------------------------
    """

    def is_more_than(self, exp1, exp2):

        # if first eq does not contain delta but the 2nd equation does
        exps = self.sub_exps(exp1, exp2)
        if str(self.delta) not in sm.latex(exp1) and str(self.delta) in sm.latex(exp2):
            return sm.simplify(exps[0] - exps[1]) == 0  # or sm.simplify(exps[0]) >
            # sm.simplify(exps[1])
        else:
            return sm.simplify(exps[0]) > sm.simplify(exps[1])

    """
    ------------------------------------------------------------------
    is_equal_to: Checks if ex1 = ex2 after substitution.
    ------------------------------------------------------------------
    Parameters:
        ex1: First expression
        ex2: Second expression
    ------------------------------------------------------------------
    """

    def is_equal_to(self, exp1, exp2):
        exps = self.sub_exps(exp1, exp2)
        return sm.simplify(exps[0] - exps[1]) == 0

    """
    ------------------------------------------------------------------
    insert: Inserts given expression only if the expression is
    the same 
    ------------------------------------------------------------------
    Parameters:
        latex_expression: The expression that we want to insert.
    ------------------------------------------------------------------
    """

    def insert(self, latex_expression: str):
        expression = parse_latex(latex_expression[2:]).subs(self.sub_format_list)

        # check if current expression <, > or = input expression
        if ((latex_expression[0] == "<" and self.is_less_than(self.current_equation, expression)) or
                (latex_expression[0] == ">" and self.is_more_than(self.current_equation,
                                                                  expression)) or
                (latex_expression[0] == "=" and self.is_equal_to(self.current_equation,
                                                                 expression))):
            self.equations.append(latex_expression)
            self.current_equation = parse_latex(latex_expression[2:])
        else:
            print(latex_expression + " is not a valid expression!")

    """
    ------------------------------------------------------------------
    __init__: Initializes Delta Epsilon proof structure.
    ------------------------------------------------------------------
    Parameters:
        latex_expression: The limit expressed in LaTeX.
    ------------------------------------------------------------------
    """

    def __init__(self, latex_expression: str):

        # setup variables for proof structure
        Variables.__init__(self, latex_expression)

        # store equations in a list
        self.current_equation = self.starting_equation
        self.equations = [sm.latex(self.starting_equation)]
