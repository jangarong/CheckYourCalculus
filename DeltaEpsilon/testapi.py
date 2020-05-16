import sympy as sm
from sympy.core.relational import Relational
from sympy.parsing.latex import parse_latex

# x = sm.Symbol("x", positive=True)
# f = Relational(abs(x - 2), x, "<")
# print(sm.solve(f))
# f = f.subs(abs(y), y)
# print(f.subs(abs(y), y))
# print(y in parse_latex("\\epsilon + 2"))

# x = sm.Symbol("x")
# f1 = 2 * abs(x - 4)
# f2 = abs(2*x - 8)
# print(f1 - (parse_latex("\\infty")))
# print(sm.simplify(parse_latex("2|x - 4|")) == sm.simplify(parse_latex("|2x - 8|")))
# epsilon = sm.Symbol("epsilon")
# delta = sm.Symbol("delta")
# equation = sm.Eq(delta, epsilon/2)
# print(sm.solve(equation, epsilon))
