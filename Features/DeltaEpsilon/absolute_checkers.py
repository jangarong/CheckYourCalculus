import sympy as sm
from sympy.parsing.latex import parse_latex


def abs_to_x(lhs_abs_exp, rhs_exp) -> list:
    """
    ------------------------------------------------------------------
    abs_to_x: Simplifies expression from lhs_abs_exp <= rhs_exp to
    ... <= x <= ...
    ------------------------------------------------------------------
    Parameters:
        lhs_abs_exp: Left hand side expression (must have absolute
        value bars)
        rhs_exp: Right hand expression.
    Returns:
        List in the form [lhs <= x, x <= rhs]
    ------------------------------------------------------------------
    """
    # remove absolute value bars
    center_exp = parse_latex(sm.latex(lhs_abs_exp).replace('\\left|', '').replace('\\right|', ''))
    return double_inequality_to_x(-rhs_exp, center_exp, rhs_exp)


def double_inequality_to_x(lhs_exp, center_exp, rhs_exp) -> list:
    """
    ------------------------------------------------------------------
    simplify_double_inequality: Simplifies expression lhs <= center <=
    rhs to ... <= x <= ...
    ------------------------------------------------------------------
    Parameters:
        lhs_exp: Left hand side expression
        center_exp: Center expression (should not have absolute value in
        it).
        rhs_exp: Right hand expression.
    Returns:
        List in the form [lhs <= x, x <= rhs]
    ------------------------------------------------------------------
    """
    # setup equations
    left_eq = sm.Eq(center_exp, lhs_exp)
    right_eq = sm.Eq(center_exp, rhs_exp)

    # solve for x
    x = sm.Symbol("x")
    left_exp = sm.solve(left_eq, x)[0]
    right_exp = sm.solve(right_eq, x)[0]
    return [left_exp <= x, x <= right_exp]
