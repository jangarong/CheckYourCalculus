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

    def init_bound_delta(self, k):
        """
        ------------------------------------------------------------------
        bound_delta: Bounds delta from above by constant.
        ------------------------------------------------------------------
        Parameters:
            k: Constant (from sympy module)
        ------------------------------------------------------------------
        """
        self.delta_bound = k  # this is >= delta
        self.curr_bounding_equation = abs_to_x(self.given.lhs, k)
        self.bounding_equations.append(sm.latex(self.delta) + " \\leq " + sm.latex(k))
        self.bounding_equations.append(sm.latex(self.given.lhs) + " \\leq " + sm.latex(k))

    def insert_bound_equation(self, f1, f2, f3):
        """
        ------------------------------------------------------------------
        insert_bound_equation: Bounds delta from above by constant.
        ------------------------------------------------------------------
        Parameters:
            f1: Function that is less than or equal to f2.
            f2: Function that is between f1 and f3.
            f3: Function that is greater than or equal to f2.
            Or f1 <= f2 <= f3 for all x.
        ------------------------------------------------------------------
        """
        curr_isolate_x = double_inequality_to_x(f1,
                                                f2,
                                                f3)
        latex_equation = sm.latex(f1) + " \\leq " + sm.latex(f2) + " \\leq " + sm.latex(f3)
        if self.curr_bounding_equation == curr_isolate_x:
            self.curr_bounding_equation = curr_isolate_x
            self.bounding_equations.append(latex_equation)
        else:
            print(latex_equation + " is not a valid expression!")

    def choose_delta(self, expr):
        """
        ------------------------------------------------------------------
        choose_delta: Uses the equation (which contains epsilon) to choose
        what delta is.
        ------------------------------------------------------------------
        Parameters:
            expr: The expression that delta is now going to be equal to.
        ------------------------------------------------------------------
        """
        # add the substitution list
        delta_equation = sm.Eq(self.delta, expr.subs(self.sub_format_list))
        epsilon_expression = (sm.solve(delta_equation, self.epsilon) +
                              sm.solve(delta_equation, str(self.epsilon)))[0]
        self.sub_list.append((self.epsilon, epsilon_expression))
        self.sub_list.reverse()

        # add element
        if self.delta_bound == 0:
            self.delta_exp_latex = str(self.delta) + " = " + sm.latex(expr)
        else:
            self.delta_exp_latex = (str(self.delta) + " = " +
                              {"M": "max", "epsilon": "min"}[str(self.epsilon)] +
                              "(" + sm.latex(expr) + ", " +
                              str(self.delta_bound) + ")")
        self.delta_exp = expr.subs(self.sub_format_list)

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
        # evaluate limit
        try:
            limit = sm.limit(fx, sm.Symbol('x'), x0, dir=direction)

        # limit does not exist
        except ValueError:
            self.L = sm.Symbol("l")
            limit = self.L

        # save variables
        self.fx = fx
        self.x0 = x0
        self.direction = direction
        self.limit = limit

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
        self.delta_exp_latex = ""
        self.delta_exp = None
        self.delta_bound = 0
        self.curr_bounding_equation = None
        self.bounded_exp = (None, None)
        self.bounding_equations = []

