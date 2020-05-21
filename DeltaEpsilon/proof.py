import sympy as sm
from sympy.parsing.latex import parse_latex
from DeltaEpsilon.variables import Variables


class DeltaEpsilonProof(Variables):
    """
    ------------------------------------------------------------------
    DeltaEpsilon.DeltaEpsilonProof: Proof structure for Delta Epsilon
    proofs.
    ------------------------------------------------------------------
    """

    def print_all(self):
        """
        ------------------------------------------------------------------
        print_all: Prints all expressions stored in the proof.
        ------------------------------------------------------------------
        """
        print("===== PROOF: =====")
        for equation in self.equations:
            print(sm.latex(equation))

        if len(self.bounding_equations) > 0:
            print("===== ASIDE: =====")
            for equation in self.bounding_equations:
                print(sm.latex(equation))

    def is_less_than(self, exp1, exp2):
        """
        ------------------------------------------------------------------
        is_more_than: Checks if exp1 > ex2, or if exp1 >= exp2, if ex2
        contains delta and exp1 does not.
        ------------------------------------------------------------------
        Parameters:
            exp1: First expression
            exp2: Second expression
        Returns:
            True if exp1 > exp2 (False otherwise)
        ------------------------------------------------------------------
        """

        # check zero case (0 < epsilon)
        if sm.simplify(exp1) == 0 and sm.simplify(exp2) == sm.latex(self.epsilon):
            return True

        exps = self.sub_exps(exp1, exp2)
        # if first eq does not contain delta but the 2nd equation does OR gets bounded by assumption
        if ((str(self.delta) not in sm.latex(exp1) and str(self.delta) in sm.latex(exp2)) or
                (sm.latex(self.bounded_exp[0]) is not None and sm.latex(self.bounded_exp[0]) in
                 sm.latex(exp1) and sm.latex(self.bounded_exp[0]) not in sm.latex(exp2))):
            return sm.Or(sm.simplify(exps[0] - exps[1]) == 0,
                         sm.simplify(exps[0]) < sm.simplify(exps[1]))
        else:
            return sm.simplify(exps[0]) < sm.simplify(exps[1])

    def is_more_than(self, exp1, exp2):
        """
        ------------------------------------------------------------------
        is_more_than: Checks if exp1 < ex2, or if exp1 <= exp2, if ex2
        contains delta and exp1 does not.
        ------------------------------------------------------------------
        Parameters:
            exp1: First expression
            exp2: Second expression
        Returns:
            True if exp1 < exp2 (False otherwise)
        ------------------------------------------------------------------
        """

        # if first eq does not contain delta but the 2nd equation does
        exps = self.sub_exps(exp1, exp2)
        if str(self.delta) not in sm.latex(exp1) and str(self.delta) in sm.latex(exp2):
            return sm.Or(sm.simplify(exps[0] - exps[1]) == 0,
                         sm.simplify(exps[0]) > sm.simplify(exps[1]))
        else:
            return sm.simplify(exps[0]) > sm.simplify(exps[1])

    def is_equal_to(self, exp1, exp2):
        """
        ------------------------------------------------------------------
        is_equal_to: Checks if exp1 = exp2 after substitution.
        ------------------------------------------------------------------
        Parameters:
            exp1: First expression
            exp2: Second expression
        ------------------------------------------------------------------
        """
        exps = self.sub_exps(exp1, exp2)
        return sm.simplify(exps[0] - exps[1]) == 0

    def insert(self, latex_expression: str):
        """
        ------------------------------------------------------------------
        insert: Inserts given expression only if the expression is
        the same
        ------------------------------------------------------------------
        Parameters:
            latex_expression: The expression that we want to insert.
        ------------------------------------------------------------------
        """
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

    def __init__(self, latex_expression: str):
        """
        ------------------------------------------------------------------
        __init__: Initializes Delta Epsilon proof structure.
        ------------------------------------------------------------------
        Parameters:
            latex_expression: The limit expressed in LaTeX.
        ------------------------------------------------------------------
        """

        # setup variables for proof structure
        Variables.__init__(self, latex_expression)

        # store equations in a list
        self.current_equation = self.starting_equation
        self.equations = [sm.latex(self.starting_equation)]
