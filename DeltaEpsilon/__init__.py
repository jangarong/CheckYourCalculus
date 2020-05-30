import sympy as sm
from sympy.parsing.latex import parse_latex


def latex_to_limit(latex_limit):
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


def __init__():
    pass
