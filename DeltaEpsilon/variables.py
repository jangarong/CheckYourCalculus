import copy
from sympy.core.relational import Relational
from DeltaEpsilon.absolute_checkers import *


class Variables:
    """
    ------------------------------------------------------------------
    DeltaEpsilon.Variables: Stores and handles variables that are used
    in the Delta Epsilon proof structure.
    ------------------------------------------------------------------
    """

    def sub_exps(self, exp1, exp2) -> list:
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
        return [sm.simplify(copy.copy(exp1).subs(self.sub_format_list).subs(self.sub_list)),
                sm.simplify(copy.copy(exp2).subs(self.sub_format_list).subs(self.sub_list))]

    def bound_expression(self):
        """
        ------------------------------------------------------------------
        bound_expression: Bounds the center expression that is currently
        in bounding_equations by whichever constant is greater on either
        side.
        ------------------------------------------------------------------
        """
        eq_parts = self.bounding_equations[len(self.bounding_equations) - 1].split("\\leq")
        self.bounded_exp = (abs(parse_latex(eq_parts[1])).subs(self.sub_format_list),
                            max(parse_latex(eq_parts[0]), parse_latex(eq_parts[2])))
        self.sub_list.append(self.bounded_exp)

    def init_bound_delta(self, k: str):
        """
        ------------------------------------------------------------------
        bound_delta: Bounds delta from above by constant.
        ------------------------------------------------------------------
        Parameters:
            k: Constant in string.
        ------------------------------------------------------------------
        """
        self.delta_bound = parse_latex(k)  # this is >= delta
        self.curr_bounding_equation = abs_to_x(self.given.lhs, parse_latex(k))
        self.bounding_equations.append(sm.latex(self.delta) + " \\leq " + k)
        self.bounding_equations.append(sm.latex(self.given.lhs) + " \\leq " + k)

    def insert_bound_equation(self, latex_equation: str):
        """
        ------------------------------------------------------------------
        insert_bound_equation: Bounds delta from above by constant.
        ------------------------------------------------------------------
        Parameters:
            latex_equation: Double inequality that is equivalent to the
            current bounding equation.
        ------------------------------------------------------------------
        """
        exps = latex_equation.split("\\leq")  # should be length 3
        curr_isolate_x = double_inequality_to_x(parse_latex(exps[0]),
                                                parse_latex(exps[1]),
                                                parse_latex(exps[2]))

        if self.curr_bounding_equation == curr_isolate_x:
            self.curr_bounding_equation = curr_isolate_x
            self.bounding_equations.append(latex_equation)
        else:
            print(latex_equation + " is not a valid expression!")

    def choose_delta(self, latex_expression: str):
        """
        ------------------------------------------------------------------
        choose_delta: Uses the equation (which contains epsilon) to choose
        what delta is.
        ------------------------------------------------------------------
        Parameters:
            latex_expression: The expression (in LaTeX) that delta is now
            going to be equal to.
        ------------------------------------------------------------------
        """
        # add the substitution list
        delta_equation = sm.Eq(self.delta, parse_latex(latex_expression).subs(self.sub_format_list))
        epsilon_expression = (sm.solve(delta_equation, self.epsilon) +
                              sm.solve(delta_equation, str(self.epsilon)))[0]
        self.sub_list.append((self.epsilon, epsilon_expression))
        self.sub_list.reverse()

        # add element
        if self.delta_bound != 0:
            self.delta_exp = str(self.delta) + " = " + latex_expression
        else:
            self.delta_exp = (str(self.delta) + " = " +
                              {"M": "max", "epsilon": "min"}[str(self.epsilon)] +
                              "(" + latex_expression + ", " +
                              str(self.delta_bound) + ")")

    def __init__(self, fx, x0, direction="+-"):
        """
        ------------------------------------------------------------------
        __init__: Initializes variables for Delta Epsilon Proof.
        ------------------------------------------------------------------
        Parameters:
            fx: The given function we're taking the limit of.
            x0: What x is approaching.
            direction: In which direction x is approaching.
        ------------------------------------------------------------------
        """
        if direction in ["+", "-"]:
            limit = sm.limit(fx, sm.Symbol('x'), x0, direction)
        else:
            limit = sm.limit(fx, sm.Symbol('x'), x0)

        # setup x
        self.x = (sm.Symbol("x", real=True, positive=True) if x0 == sm.oo else
                  sm.Symbol("x", real=True, negative=True) if x0 == - sm.oo else
                  sm.Symbol("x", real=True))

        # setup the other variables
        self.delta = sm.Symbol("N" if x0 == sm.oo or x0 == - sm.oo else "delta",
                               positive=True)
        self.epsilon = sm.Symbol("M" if limit == sm.oo or limit == - sm.oo else "epsilon",
                                 positive=True)

        # possible givens
        givens = [[Relational(abs(self.x - x0), self.delta, "<"),
                   Relational(self.x - x0, self.delta, "<"),
                   Relational(x0 - self.x, self.delta, "<")],
                  [Relational(self.x, self.delta, ">")],
                  [Relational(-self.x, self.delta, ">")]]

        # possible starting equations
        str_starting_equations = [["|" + sm.latex(fx) + "-" + sm.latex(limit) + "|",
                                   sm.latex(fx) + "-" + sm.latex(limit),
                                   sm.latex(limit) + "-" + sm.latex(fx)],
                                  [sm.latex(fx)] * 3,
                                  [sm.latex(-fx)] * 3]

        # possible starting equations
        starting_equations = [[abs(fx - limit),
                              fx - limit,
                              limit - fx],
                              [fx] * 3,
                              [-fx] * 3]

        # dictionary for side
        side_dict = {"+-": 0,
                     "+": 1,
                     "-": 2}
        side = side_dict[direction]
        x0_inf = 1 if x0 == sm.oo else 2 if x0 == - sm.oo else 0
        fx_inf = 1 if limit == sm.oo else 2 if limit == - sm.oo else 0

        # setup equations
        self.given = givens[x0_inf][side]
        self.starting_equation = starting_equations[fx_inf][side]
        self.str_starting_equation = str_starting_equations[fx_inf][side]

        # setup substitutions
        self.sub_format_list = [(str(self.epsilon), self.epsilon),
                                (str(self.delta), self.delta),
                                ("x", self.x)]
        self.sub_list = [(self.delta, self.given.lhs)]

        # store what delta is
        self.delta_exp = ""
        self.delta_bound = 0
        self.curr_bounding_equation = None
        self.bounded_exp = (None, None)
        self.bounding_equations = []



