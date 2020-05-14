import sympy as sm
from sympy.parsing.latex import parse_latex

y = sm.Symbol("epsilon")
f = parse_latex("\\epsilon + 2")
print(f.subs(y, parse_latex("y + 3")))
print(y in parse_latex("\\epsilon + 2"))
