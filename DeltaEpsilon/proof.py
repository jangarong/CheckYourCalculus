import sympy as sm
from sympy.parsing.latex import parse_latex
import copy


def in_equation(latex_symbol, equation):
    return latex_symbol in sm.latex(equation)


"""
DEProof - Delta Epsilon Proof
Notes:
parse_latex() removes useless zeros (i.e. |x - 0| turns into |x|)
"""


class DEProof:
    """Determines what epsilon is in terms of delta"""

    def derive_epsilon(self):
        self.epsilon_in_delta = sm.solve(sm.Eq(self.delta, self.delta_equation), self.epsilon)[0]

    """Set delta to something in terms of epsilon"""

    def let_delta_be(self, raw_equation):
        self.delta_equation = parse_latex(raw_equation).subs(self.str_to_symbol)  # delta = ???
        self.derive_epsilon()

    """Prints all equations stored in LaTeX"""

    def print_all_equations(self):
        for equation in self.equations:
            print(sm.latex(equation))

    """Substitutes epsilons and deltas in terms of the original function to verify equation"""

    def sub_variables(self, eq1, eq2) -> list:
        # substitute deltas and epsilons into each equation
        eqs = [sm.simplify(copy.copy(eq1)).subs(self.str_to_symbol),
               sm.simplify(copy.copy(eq2)).subs(self.str_to_symbol)]
        for i in range(len(eqs)):
            if self.epsilon_in_delta is not None:
                eqs[i] = eqs[i].subs(self.epsilon, self.epsilon_in_delta)
            if self.delta_inequality is not None:
                eqs[i] = eqs[i].subs(self.delta, self.delta_inequality)
        return eqs

    """Check if equation1 < equation2"""

    def is_less_than(self, eq1, eq2):
        eqs = self.sub_variables(eq1, eq2)

        # check zero case (0 < epsilon)
        if sm.simplify(eq1) == 0 and sm.simplify(eq2) == sm.latex(self.epsilon):
            return True

        # if first eq does not contain delta but the 2nd equation does
        if not in_equation(sm.latex(self.delta), eq1) and in_equation(sm.latex(self.delta), eq2):
            return sm.simplify(eqs[0] - eqs[1]) == 0  # or sm.simplify(eqs[1]) > sm.simplify(eqs[0])
        else:
            return sm.simplify(eqs[0]) < sm.simplify(eqs[1])

    def is_more_than(self, eq1, eq2):
        eqs = self.sub_variables(eq1, eq2)

        # check zero case (0 < epsilon)
        if sm.simplify(eq1) == 0 and sm.simplify(eq2) == sm.latex(self.epsilon):
            return True

        # if first eq does not contain delta but the 2nd equation does
        if not in_equation(sm.latex(self.delta), eq1) and in_equation(sm.latex(self.delta), eq2):
            return sm.simplify(eqs[0] - eqs[1]) == 0  # or sm.simplify(eqs[1]) > sm.simplify(eqs[0])
        else:
            return sm.simplify(eqs[0]) > sm.simplify(eqs[1])

    """Check if equation1 = equation2"""

    def is_equal_to(self, eq1, eq2):
        eqs = self.sub_variables(eq1, eq2)
        return sm.simplify(eqs[0] - eqs[1]) == 0

    """Inserts equation into the proof if it is valid."""

    def insert_equation(self, raw_equation):
        # assuming "< equation" or "= equation"
        equation = parse_latex(raw_equation[2:]).subs("x", self.x)

        # check if current equation < input equation
        if raw_equation[0] == "<" and self.is_less_than(self.equations[len(self.equations) - 1],
                                                        equation):
            self.equations[len(self.equations) - 1] = (sm.latex(self.equations[len(self.equations)
                                                                               - 1]) + " <")
            self.equations.append(parse_latex(raw_equation[2:]))

        # check if current equation > input equation
        elif raw_equation[0] == ">" and self.is_more_than(self.equations[len(self.equations) - 1],
                                                         equation):
            self.equations[len(self.equations) - 1] = (sm.latex(self.equations[len(self.equations)
                                                                               - 1]) + " >")
            self.equations.append(parse_latex(raw_equation[2:]))

        # check if current equation = input equation
        elif raw_equation[0] == "=" and self.is_equal_to(self.equations[len(self.equations) - 1],
                                                         equation):
            self.equations[len(self.equations) - 1] = (sm.latex(self.equations[len(self.equations)
                                                                               - 1]) + " =")
            self.equations.append(parse_latex(raw_equation[2:]))

        else:
            print(str(raw_equation) + " is not a valid equation!")

    """Creates Delta Epsilon Proof"""

    def __init__(self, raw_limit):

        # set math variables for parsing
        self.x = sm.Symbol("x", real=True)

        # parse values
        str_limit = raw_limit.split("=")[1][1:]
        str_function = raw_limit.split("}", 1)[1].split("=")[0][1:]
        str_approaching = raw_limit.split("\\to")[1].split("}")[0][1:].split("^")
        self.limit = parse_latex(str_limit)
        self.approaching = parse_latex(str_approaching[0])
        self.function = parse_latex(str_function)
        self.equations = []

        # status
        self.is_infinite = 0
        self.approaches_infinity = 0

        # check if x approaches negative infinity
        if "-\\infty" in str_approaching[0]:
            self.approaches_infinity = -1  # x < N
            self.delta_inequality = parse_latex("-|x|").subs("x", self.x)
            self.equations.append(parse_latex("| " + str_function + " - " + str_limit +
                                              " |"))

        # check if x approaches infinity
        elif "\\infty" in str_approaching[0]:
            self.approaches_infinity = 1  # x > N
            self.delta_inequality = parse_latex("|x|").subs("x", self.x)
            self.equations.append(parse_latex("| " + str_function + " - " + str_limit + " |"))

        elif len(str_approaching) > 1:
            self.approaches_infinity = 0

            # if it's a right sided limit
            if str_approaching[1] == "+":
                self.delta_inequality = parse_latex("x - " + str_approaching[0]).subs("x", self.x)
                self.equations.append(parse_latex(str_function + " - " +
                                                  str_limit))

            # if it's a left sided limit
            elif str_approaching[1] == "-":
                self.delta_inequality = parse_latex("-(" + "x - " + str_approaching[0] +
                                                    ")").subs("x", self.x)
                self.equations.append(parse_latex("-(" + str_function + " - " + str_limit + ")"))
        else:
            self.approaches_infinity = 0
            self.delta_inequality = parse_latex("| x - " + str_approaching[0] +
                                                "|").subs("x", self.x)
            self.equations.append(parse_latex("| " + str_function + " - " + str_limit + " |"))

        # check if f(x) approaches negative infinity
        if "-\\infty" == str_limit:
            self.is_infinite = -1  # f(x) > -M
            self.equations[0] = parse_latex(str_function)

        # check if f(x) approaches infinity
        elif "\\infty" == str_limit:
            self.is_infinite = 1  # f(x) > M
            self.equations[0] = parse_latex(str_function)

        # variables that we need to set
        self.str_to_symbol = {"x": self.x}
        if self.is_infinite != 0:
            self.epsilon = sm.Symbol("M", positive=True)  # > 0
            self.str_to_symbol["M"] = self.epsilon
        else:
            self.epsilon = sm.Symbol("epsilon", positive=True)  # > 0
            self.str_to_symbol["epsilon"] = self.epsilon

        # if it's an N-X proof
        if self.approaches_infinity != 0:
            self.delta = sm.Symbol("N", positive=True)  # < x
            self.str_to_symbol["N"] = self.delta

        # if it's an epsilon-X proof
        else:
            self.delta = sm.Symbol("delta", positive=True)  # > 0
            self.str_to_symbol["delta"] = self.delta

        # important equations
        self.epsilon_in_delta = None
        self.delta_equation = None
