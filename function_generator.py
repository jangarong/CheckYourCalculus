import sympy as sm
import random


def get_polynomial(degree: int):
    """
    ------------------------------------------------------------------
    get_polynomial: Generates a polynomial with integer constants -9
    to 9 of the given degree.
    ------------------------------------------------------------------
    Parameters:
        degree: Degree of polynomial
    Returns:
        Polynomial
    ------------------------------------------------------------------
    """
    x = sm.Symbol('x')
    expr = 0
    for i in range(degree + 1):
        if i == degree:
            expr += sm.simplify([1, -1][random.randint(0, 1)] * random.randint(1, 9) * pow(x, i))
        else:
            expr += sm.simplify([1, -1][random.randint(0, 1)] * random.randint(0, 9) * pow(x, i))

    return expr
