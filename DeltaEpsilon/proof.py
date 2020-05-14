import sympy as sm
from sympy.parsing.latex import parse_latex
import copy


def in_equation(latex_symbol, equation):
    return latex_symbol in sm.latex(equation)


"""
DEProof - Delta Epsilon Proof
"""


class DEProof:
    """Determines what epsilon is in terms of delta"""

    def derive_epsilon(self):
        delta = sm.Symbol("delta")
        epsilon = sm.Symbol("epsilon")
        self.epsilon_in_delta = sm.solve(sm.Eq(delta, self.delta), epsilon)[0]

    """Set delta to something in terms of epsilon"""

    def let_delta_be(self, raw_equation):
        self.delta = parse_latex(raw_equation)
        self.derive_epsilon()

    """Prints all equations stored in LaTeX"""

    def print_all_equations(self):
        for equation in self.equations:
            print(sm.latex(equation))

    """Substitutes epsilons and deltas in terms of the original function to verify equation"""

    def sub_variables(self, eq1, eq2) -> list:
        # substitute deltas and epsilons into each equation
        eqs = [copy.copy(eq1), copy.copy(eq2)]
        for i in range(len(eqs)):
            if self.epsilon_in_delta is not None:
                eqs[i] = eqs[i].subs(self.epsilon, self.epsilon_in_delta)
            if self.delta_inequality is not None:
                eqs[i] = eqs[i].subs(self.delta, self.delta_inequality)
        return eqs

    """Check if equation1 < equation2"""

    def is_less_than(self, eq1, eq2):
        eqs = self.sub_variables(eq1, eq2)

        # if first eq does not contain delta but the 2nd equation does
        if not in_equation("\\delta", eq1) and in_equation("\\delta", eq2):
            return sm.simplify(eqs[0]) <= sm.simplify(eqs[1])
        else:
            return sm.simplify(eqs[0]) < sm.simplify(eqs[1])

    """Check if equation1 = equation2"""

    def is_equal_to(self, eq1, eq2):
        eqs = self.sub_variables(eq1, eq2)
        return sm.simplify(eqs[0] - eqs[1]) == 0

    """Inserts equation into the proof if it is valid."""

    def insert_equation(self, raw_equation):
        equation = parse_latex(raw_equation[2:])  # assuming "< equation" or "= equation"

        # check if current equation < input equation
        if raw_equation[0] == "<" and self.is_less_than(self.equations[len(self.equations) - 1],
                                                        equation):
            self.equations[len(self.equations) - 1] = (sm.latex(self.equations[len(self.equations)
                                                                               - 1]) + " <")
            self.equations.append(equation)

        # check if current equation = input equation
        elif raw_equation[0] == "=" and self.is_equal_to(self.equations[len(self.equations) - 1],
                                                         equation):
            self.equations[len(self.equations) - 1] = (sm.latex(self.equations[len(self.equations)
                                                                               - 1]) + " =")
            self.equations.append(equation)
        else:
            print(str(raw_equation) + " is not a valid equation!")

    """Creates Delta Epsilon Proof"""

    def __init__(self, raw_limit):

        # parse values
        str_limit = raw_limit.split("=")[1][1:]
        str_function = raw_limit.split("}", 1)[1].split("=")[0][1:]
        str_approaching = raw_limit.split("\\to")[1].split("}")[0][1:].split("^")
        self.limit = parse_latex(str_limit)
        self.approaching = parse_latex(str_approaching[0])
        self.function = parse_latex(str_function)
        self.equations = []

        # formulate equations for the proof (assume no infinity limits for now

        # this is < /delta
        self.delta_inequality = parse_latex("|" + "x - " + str_approaching[0] + "|")

        # WTP: this is < /epsilon
        self.equations.append(parse_latex("|" + str_function + " - " + str_limit + "|"))

        # variables that we need to set
        self.delta = sm.Symbol("delta")
        self.epsilon = sm.Symbol("epsilon")
        self.epsilon_in_delta = None
