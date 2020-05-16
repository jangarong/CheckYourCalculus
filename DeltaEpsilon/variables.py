import sympy as sm
from sympy.parsing.latex import parse_latex
from sympy.core.relational import Relational
import copy

"""
------------------------------------------------------------------
parse_limit: Breaks down the limit into variables used for 
initializing the Variables class.
------------------------------------------------------------------
Parameters:
    latex_limit: The expression (in LaTeX) of the limit.
Returns (in this order):
    x0: What x approaches
    fx: The function that we're taking the limit of.
    limit: The value in which the function approches
    x0_inf: Integer that determines whether x is approaching:
        0 - some finite value
        1 - infinity
        2 - negative infinity
    fx_inf: Integer that determines whether f(x) is approaching:
        0 - some finite value
        1 - infinity
        2 - negative infinity
    side: Integer that determines whether the limit is:
        0 - approaching both sides
        1 - approaches the right side
        2 - approaches the left side
------------------------------------------------------------------
"""


def parse_limit(latex_limit: str):

    # split latex limit into different parts
    str_limit = latex_limit.split("=")[1][1:]
    str_function = latex_limit.split("}", 1)[1].split("=")[0][1:]
    str_approaching = latex_limit.split("\\to")[1].split("}")[0][1:].split("^")

    # check if x0 is approaching infinity
    inf_dict = {"\\infty": 1, "-\\infty": 2}
    if "\\infty" in str_approaching[0]:
        approaches_inf = inf_dict[str_approaching[0]]
    else:
        approaches_inf = 0

    # check if f(x)'s limit is infinity
    if "\\infty" in str_limit:
        limit_inf = inf_dict[str_limit]
    else:
        limit_inf = 0

    # check which side the limit is on
    if len(str_approaching) > 1:
        sign_dict = {"+": 1, "-": 2}
        side = sign_dict[str_approaching[1]]
    else:
        side = 0

    return (parse_latex(str_approaching[0]), parse_latex(str_limit), parse_latex(str_function),
            approaches_inf, limit_inf, side)


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
    Issues:
        When called more than once it has a problem with 
        distinguishing "epsilon" and the symbol epsilon, thus causing
        a crash. This also happens when working with infinity.
    ------------------------------------------------------------------
    """
    def choose_delta(self, latex_expression: str):
        delta_equation = sm.Eq(self.delta, parse_latex(latex_expression).subs(self.sub_format_list))
        epsilon_expression = sm.solve(delta_equation, self.epsilon)[0]
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
        x0, limit, fx, x0_inf, fx_inf, side = parse_limit(latex_limit)

        # setup variable names
        self.x = sm.Symbol("x", real=True)
        str_delta = ["delta", "N", "N"]
        str_epsilon = ["epsilon", "M", "M"]
        self.delta = sm.Symbol(str_delta[x0_inf], positive=True)
        self.epsilon = sm.Symbol(str_epsilon[fx_inf], positive=True)

        # possible givens
        givens = [[Relational(abs(self.x - x0), self.delta, "<"),
                   Relational(self.x - x0, self.delta, "<"),
                   Relational(x0 - self.x, self.delta, "<")],
                  [Relational(abs(self.x), self.delta, ">")],
                  [Relational(-abs(self.x), self.delta, ">")]]

        # possible conclusions
        conclusions = [[Relational(abs(fx - limit), self.epsilon, "<"),  # automatically simplifies?
                        Relational(fx - limit, self.epsilon, "<"),
                        Relational(limit - fx, self.epsilon, "<")],
                       Relational(abs(fx), self.epsilon, ">"),
                       Relational(-abs(fx), self.epsilon, ">")]

        # possible starting equations (simplify this if possible)
        starting_equations = [parse_latex("| " + latex_limit.split("}", 1)[1].split("=")[0][1:]
                                             + " - " + latex_limit.split("=")[1][1:] + " |"),
                              parse_latex(latex_limit.split("}", 1)[1].split("=")[0][1:]
                                          + " - " + latex_limit.split("=")[1][1:]),
                              parse_latex(latex_limit.split("=")[1][1:] + " - " +
                                          latex_limit.split("}", 1)[1].split("=")[0][1:])]

        # setup equations
        self.given = givens[x0_inf][side]
        self.conclusion = conclusions[fx_inf][side]
        self.starting_equation = starting_equations[side]

        # setup substitutions
        self.sub_format_list = [(str_epsilon[x0_inf], self.epsilon),
                                (str_delta[fx_inf], self.delta),
                                ("x", self.x)]
        self.sub_list = [(self.delta, self.given.lhs)]
