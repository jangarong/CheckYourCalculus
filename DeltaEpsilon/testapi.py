import sympy as sm
from sympy.parsing.latex import parse_latex

x = sm.Symbol("x", positive=True)
f = -abs(x - 2) + abs(x - 2)
print(sm.simplify(f))
# f = f.subs(abs(y), y)
# print(f.subs(abs(y), y))
# print(y in parse_latex("\\epsilon + 2"))

# x = sm.Symbol("x")
# f1 = 2 * abs(x - 4)
# f2 = abs(2*x - 8)
# print(sm.simplify(parse_latex("2|x - 4| - |2x - 8|")) == 0)
# print(sm.simplify(parse_latex("2|x - 4|")) == sm.simplify(parse_latex("|2x - 8|")))
