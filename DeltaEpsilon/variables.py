import sympy as sm
from sympy.parsing.latex import parse_latex
from sympy.core.relational import Relational
import copy


class Variables:
    """
    DeltaEpsilon.Variables: Stores and handles variables that are used
    in the Delta Epsilon proof structure.
    """

    """
    ------------------------------------------------------------------
    sub_exps: Checks if exp1 < exp2, or if exp1 <= exp2, if exp2 
    contains delta and exp1 does not.
    ------------------------------------------------------------------
    Parameters:
        exp1: First expression.
        exp2: Second expression.
    Returns:
        List that contains a copy of the two expressions.
    ------------------------------------------------------------------
    """

    def sub_exps(self, exp1, exp2) -> list:
        return [sm.simplify(copy.copy(exp1)).subs(self.sub_format_list).subs(self.sub_list),
                sm.simplify(copy.copy(exp2)).subs(self.sub_format_list).subs(self.sub_list)]

    """
    ------------------------------------------------------------------
    choose_delta: Uses the equation (which contains epsilon) to choose
    what delta is.
    ------------------------------------------------------------------
    Parameters:
        latex_equation: The expression (in LaTeX) that delta is now 
        going to be equal to.
    ------------------------------------------------------------------
    """

    def choose_delta(self, latex_expression: str):
        delta_equation = sm.Eq(self.delta, parse_latex(latex_expression).subs(self.sub_format_list))
        epsilon_expression = (sm.solve(delta_equation, self.epsilon) +
                              sm.solve(delta_equation, str(self.epsilon)))[0]
        self.sub_list.append((self.epsilon, epsilon_expression))
        self.sub_list.reverse()

    """
    ------------------------------------------------------------------
    __init__: Initializes variables for Delta Epsilon Proof.
    ------------------------------------------------------------------
    Parameters:
        latex_limit: The limit expressed in LaTeX
    ------------------------------------------------------------------
    """

    def __init__(self, latex_limit):
        # parse and setup variables
        # split latex limit into different parts
        str_limit = latex_limit.split("=")[1][1:]
        str_function = latex_limit.split("}", 1)[1].split("=")[0][1:]
        str_approaching = latex_limit.split("\\to")[1].split("}")[0][1:].split("^")

        # check if x0 is approaching infinity
        inf_dict = {"\\infty": 1, "-\\infty": 2}
        if "\\infty" in str_approaching[0]:
            x0_inf = inf_dict[str_approaching[0]]
        else:
            x0_inf = 0

        # check if f(x)'s limit is infinity
        if "\\infty" in str_limit:
            fx_inf = inf_dict[str_limit]
        else:
            fx_inf = 0

        # check which side the limit is on
        if len(str_approaching) > 1:
            sign_dict = {"+": 1, "-": 2}
            side = sign_dict[str_approaching[1]]
        else:
            side = 0

        # parse to latex
        x0 = parse_latex(str_approaching[0])
        limit = parse_latex(str_limit)
        fx = parse_latex(str_function)

        # setup x
        possible_xs = [sm.Symbol("x", real=True),
                       sm.Symbol("x", real=True, positive=True),
                       sm.Symbol("x", real=True, negative=True)]
        self.x = possible_xs[x0_inf]

        # setup the other variables
        str_delta = ["delta", "N", "N"]
        str_epsilon = ["epsilon", "M", "M"]
        self.delta = sm.Symbol(str_delta[x0_inf], positive=True)
        self.epsilon = sm.Symbol(str_epsilon[fx_inf], positive=True)

        # possible givens
        givens = [[Relational(abs(self.x - x0), self.delta, "<"),
                   Relational(self.x - x0, self.delta, "<"),
                   Relational(x0 - self.x, self.delta, "<")],
                  [Relational(self.x, self.delta, ">")],
                  [Relational(-self.x, self.delta, ">")]]

        # possible conclusions
        conclusions = [[Relational(abs(fx - limit), self.epsilon, "<"),  # automatically simplifies?
                        Relational(fx - limit, self.epsilon, "<"),
                        Relational(limit - fx, self.epsilon, "<")],
                       [Relational(fx, self.epsilon, ">")] * 3,
                       [Relational(-fx, self.epsilon, ">")] * 3]

        # possible starting equations (simplify this if possible)
        starting_equations = [[parse_latex("| " + str_function + " - " + str_limit + " |"),
                              parse_latex(str_function + " - " + str_limit),
                              parse_latex(str_limit + " - " + str_function)],
                              [Relational(fx, self.epsilon, ">").lhs] * 3,
                              [Relational(-fx, self.epsilon, ">").lhs] * 3]

        # setup equations
        self.given = givens[x0_inf][side]
        self.conclusion = conclusions[fx_inf][side]
        self.starting_equation = starting_equations[fx_inf][side]

        # setup substitutions
        self.sub_format_list = [(str_epsilon[fx_inf], self.epsilon),
                                (str_delta[x0_inf], self.delta),
                                ("x", self.x)]
        self.sub_list = [(self.delta, self.given.lhs)]

