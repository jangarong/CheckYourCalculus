from DeltaEpsilon.proof import Proof
from DeltaEpsilon.parsing import latex_to_limit
from DeltaEpsilon.parsing import insert_expr_latex
from DeltaEpsilon.parsing import insert_bound_eq_latex
from sympy.parsing.latex import parse_latex

# test case 2 - delta with a multiple
print("\nPROOF 2:")
pf = Proof(*latex_to_limit("\\lim_{x \\to 4} 2(x + 3) = 14"))
pf.insert(*insert_expr_latex("= |2x + 6 - 14|"))
pf.insert(*insert_expr_latex("= 2|x - 4|"))  # says this is not valid ?!
pf.insert(*insert_expr_latex("< 2\\delta"))
pf.choose_delta(parse_latex("\\frac{\\epsilon}{2}"))
pf.insert(*insert_expr_latex("= 2\\frac{\\epsilon}{2}"))  # epsilon auto simplifies
pf.insert(*insert_expr_latex("= \\epsilon"))
pf.print_all()
pf.plot('open.png', 1)

# # test case 10 - delta assumption
# print("\nPROOF 10:")
# pf = Proof(*latex_to_limit("\\lim_{x \\to 2} x^2 = 4"))
# pf.insert(*insert_expr_latex("= |x + 2||x - 2|"))
# pf.init_bound_delta(parse_latex("1"))
# pf.insert_bound_equation(*insert_bound_eq_latex("-1 \\leq x - 2 \\leq 1"))
# pf.insert_bound_equation(*insert_bound_eq_latex("1 \\leq x \\leq 3"))
# pf.insert_bound_equation(*insert_bound_eq_latex("3 \\leq x + 2 \\leq 5"))
# pf.bound_expression()
# pf.insert(*insert_expr_latex("< 5|x - 2|"))
# pf.choose_delta(parse_latex("\\frac{\\epsilon}{5}"))
# pf.insert(*insert_expr_latex("< 5\\delta"))
# pf.insert(*insert_expr_latex("= 5\\frac{\\epsilon}{5}"))
# pf.insert(*insert_expr_latex("= \\epsilon"))
# pf.print_all()
