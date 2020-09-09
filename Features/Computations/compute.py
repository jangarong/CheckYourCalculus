import sympy as sm
from sympy.parsing.latex import parse_latex


class Compute:
    """
    ------------------------------------------------------------------
    Computation: Stores equations used to compute an answer.
    ------------------------------------------------------------------
    """

    def print_all(self):
        """
        ------------------------------------------------------------------
        print_all: Prints all expressions stored.
        ------------------------------------------------------------------
        """
        print("===== COMPUTATIONS: =====")
        for equation in self.equations:
            print(sm.latex(equation))

    def insert(self, latex_expression: str):
        """
        ------------------------------------------------------------------
        insert: Inserts expression into the list only if it's equal to
        what was previously stated.
        ------------------------------------------------------------------
        Parameters:
            latex_expression: This is the equation we want to input.
        Returns:
            True if equations equal each other. False otherwise.
        ------------------------------------------------------------------
        """
        if self.current_equation is not None:
            expr = parse_latex(latex_expression)
            if (sm.simplify(expr) - self.current_equation) == 0:
                self.current_equation = expr
                self.equations.append(latex_expression)
                return True
            else:
                return False
        else:
            return False  # nothing to compare it to

    def new(self, latex_expression: str):
        self.equations.append(latex_expression)
        self.current_equation = parse_latex(latex_expression)

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: initializes computation module.
        ------------------------------------------------------------------
        Parameters:
            latex_expression: This is the starting equation.
        ------------------------------------------------------------------
        """
        self.equations = []  # this stores raw input latex strings
        self.current_equation = None
