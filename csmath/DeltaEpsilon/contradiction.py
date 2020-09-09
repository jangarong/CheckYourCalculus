import sympy as sm

from csmath.DeltaEpsilon.absolute_checkers import double_inequality_to_x


class Contradiction:
    """
    ------------------------------------------------------------------
    DeltaEpsilon.Contradiction: Proof structure for Delta Epsilon
    proofs.
    ------------------------------------------------------------------
    """

    def choose_epsilon(self, expr):
        """
        ------------------------------------------------------------------
        choose_epsilon: Uses the equation to set what epsilon will be.
        ------------------------------------------------------------------
        Parameters:
            expr: The expression that epsilon is now going to be equal to.
        ------------------------------------------------------------------
        """

        # bound epsilon
        self.epsilon = expr
        self.curr_bound_epsilon = double_inequality_to_x(0, self.less_than_epsilon, self.epsilon)

    def insert_bound_epsilon(self, f1, f2, f3):
        """
        ------------------------------------------------------------------
        insert_bound_epsilon: Bounds epsilon from above and below.
        ------------------------------------------------------------------
        Parameters:
            f1: Function that is less than f2.
            f2: Function that is between f1 and f3.
            f3: Function that is greater than f2.
            Or f1 < f2 < f3 for all x.
        ------------------------------------------------------------------
        """
        curr_isolate_x = double_inequality_to_x(f1,
                                                f2,
                                                f3)
        latex_equation = sm.latex(f1) + " \\leq " + sm.latex(f2) + " \\leq " + sm.latex(f3)
        if self.curr_bound_epsilon == curr_isolate_x:
            self.curr_bound_epsilon = curr_isolate_x
            self.bound_epsilon_eqs.append(latex_equation)
        else:
            print(latex_equation + " is not a valid expression!")


    def __init__(self, fx, x0):
        """
        ------------------------------------------------------------------
        __init__: Proof structure to prove that the limit does not exist.
        ------------------------------------------------------------------
        Parameters:
            fx: The given function we're taking the limit of.
            x0: What x is approaching.
        ------------------------------------------------------------------
        """

        # create arbitrary variables
        self.x = sm.Symbol("x", real=True)
        self.L = sm.Symbol("L", real=True)
        self.delta = sm.Symbol("\\delta", real=True, positive=True)

        # set up equations
        self.less_than_epsilon = abs(fx - self.L)
        self.less_than_delta = abs(self.x - x0)

        # create variables to set later
        self.epsilon = None
        self.curr_bound_epsilon = None
        self.bound_epsilon_eqs = []



