import sympy as sm
import random


def get_polynomial(degree: int, no_zero: bool = False):
    """
    ------------------------------------------------------------------
    get_polynomial: Generates a polynomial with integer constants -9
    to 9 of the given degree.
    ------------------------------------------------------------------
    Parameters:
        degree: Degree of polynomial
        no_zero: If function can be 0 or not.
    Returns:
        Polynomial function.
    ------------------------------------------------------------------
    """
    x = sm.Symbol('x')
    expr = 0
    for i in range(degree + 1):
        if (i == degree and degree != 0) or (degree == 0 and no_zero):
            expr += sm.simplify([1, -1][random.randint(0, 1)] * random.randint(1, 9) * pow(x, i))
        else:
            expr += sm.simplify([1, -1][random.randint(0, 1)] * random.randint(0, 9) * pow(x, i))

    return expr


def get_rational(num_degree: int, denom_degree: int):
    """
    ------------------------------------------------------------------
    get_rational: Generates a rational function with the given degrees
    for the numerator and the denominator
    ------------------------------------------------------------------
    Parameters:
        num_degree: Degree of the numerator
        denom_degree: Degree of the denominator
    Returns:
        Rational function.
    ------------------------------------------------------------------
    """
    return get_polynomial(num_degree) / get_polynomial(denom_degree, no_zero=True)

