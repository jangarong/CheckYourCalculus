import sympy as sm
from sympy.parsing.latex import parse_latex

# y = sm.Symbol("epsilon")
# f = parse_latex("\\epsilon + 2")
# print(f.subs(y, parse_latex("y + 3")))
# print(y in parse_latex("\\epsilon + 2"))

# x = sm.Symbol("x")
# f1 = 2 * abs(x - 4)
# f2 = abs(2*x - 8)
print(sm.simplify(parse_latex("2|x - 4| - |2x - 8|")) == 0)
#print(sm.simplify(parse_latex("2|x - 4|")) == sm.simplify(parse_latex("|2x - 8|")))
