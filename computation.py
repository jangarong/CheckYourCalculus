import sympy as sm
from sympy.parsing.latex import parse_latex


class Computation:
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
            latex_expression: This is the starting equation, with "= " in
            front of it.
        ------------------------------------------------------------------
        """
        expr = parse_latex(latex_expression.split("= ", 1)[1])
        if (sm.simplify(expr) - self.current_equation) == 0:
            self.current_equation = expr
            self.equations.append(latex_expression)
        else:
            print(latex_expression + " is not a valid expression!")

    def __init__(self, latex_expression: str) -> None:
        """
        ------------------------------------------------------------------
        __init__: initializes computation module.
        ------------------------------------------------------------------
        Parameters:
            latex_expression: This is the starting equation.
        ------------------------------------------------------------------
        """
        self.equations = []  # this stores raw input latex strings
        self.equations.append(latex_expression)
        self.current_equation = parse_latex(latex_expression)
