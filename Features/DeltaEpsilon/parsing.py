import sympy as sm
from sympy.parsing.latex import parse_latex


def latex_to_limit(latex_limit):
    """
    ------------------------------------------------------------------
    latex_to_limit: Breaks the latex limit into sympy objects.
    ------------------------------------------------------------------
    Parameters:
        latex_limit: latex string
    Returns:
        function, x0 and direction (in that order).
    ------------------------------------------------------------------
    """
    # split latex limit into different parts (except the limit since we already know what it is
    str_function = latex_limit.split("}", 1)[1].split("=")[0][1:]
    str_approaching = latex_limit.split("\\to")[1].split("}")[0][1:].split("^")

    # check if x0 is approaching infinity
    inf_dict = {"\\infty": sm.oo, "-\\infty": - sm.oo}
    if "\\infty" in str_approaching[0]:
        x0 = inf_dict[str_approaching[0]]
    else:
        x0 = parse_latex(str_approaching[0])

    # check which side the limit is on
    if len(str_approaching) > 1:
        direction = str_approaching[1]
    else:
        direction = "+-"

    return parse_latex(str_function), x0, direction


def insert_expr_latex(latex_expr):
    """
    ------------------------------------------------------------------
    insert_expr_latex: Splits into inequality sign and function.
    ------------------------------------------------------------------
    Parameters:
        latex_expr: latex string
    Returns:
        inequality sign, latex function.
    ------------------------------------------------------------------
    """
    latex_split = latex_expr.split(' ', 1)
    return latex_split[0], parse_latex(latex_split[1])


def insert_bound_eq_latex(latex_expr):
    """
    ------------------------------------------------------------------
    insert_bound_eq_latex: Converts the latex triple inequality into
    functions.
    ------------------------------------------------------------------
    Parameters:
        latex_expr: latex string
    Returns:
        f1, f2, f3 such that f1 <= f2 <= f3
    ------------------------------------------------------------------
    """
    latex_split = latex_expr.split("\\leq")
    return parse_latex(latex_split[0]), parse_latex(latex_split[1]), parse_latex(latex_split[2])


