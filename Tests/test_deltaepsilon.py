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
pf.plot('../samples/open.png', 5)

# test case 5 - x approaches infinity limit
print("\nPROOF 5:")
pf = Proof(*latex_to_limit("\\lim_{x \\to \\infty} \\frac{x + 1}{x} = 1"))
pf.insert(*insert_expr_latex("= |\\frac{x + 1}{x} - \\frac{x}{x}|"))  # automatic simplifcation?!
pf.insert(*insert_expr_latex("= |\\frac{x + 1 - x}{x}|"))
pf.insert(*insert_expr_latex("= |\\frac{1}{x}|"))
pf.insert(*insert_expr_latex("< |\\frac{1}{N}|")) # problem
pf.choose_delta(parse_latex("\\frac{1}{\\epsilon}"))
pf.insert(*insert_expr_latex("= |\\frac{1}{\\frac{1}{\\epsilon}}|"))
pf.insert(*insert_expr_latex("= |\\epsilon|"))
pf.insert(*insert_expr_latex("= \\epsilon"))
pf.print_all()

# test case 6 - limit is infinity
print("\nPROOF 6:")
pf = Proof(*latex_to_limit("\\lim_{x \\to 0^+} \\frac{1}{x} = \\infty"))
pf.choose_delta(parse_latex("\\frac{1}{M}"))
pf.insert(*insert_expr_latex("> \\frac{1}{\\delta}"))
pf.insert(*insert_expr_latex("= \\frac{1}{\\frac{1}{M}}"))
pf.insert(*insert_expr_latex("= M"))
pf.print_all()

# test case 7 - limit is infinity, x approaches infinity
print("\nPROOF 7:")
pf = Proof(*latex_to_limit("\\lim_{x \\to \\infty} 2(x + 2) = \\infty"))
pf.insert(*insert_expr_latex("= 2x + 4"))
pf.insert(*insert_expr_latex("> 2x"))
pf.insert(*insert_expr_latex("> 2N"))
pf.choose_delta(parse_latex("\\frac{M}{2}"))
pf.insert(*insert_expr_latex("= 2\\frac{M}{2}"))
pf.insert(*insert_expr_latex("= M"))
pf.print_all()

# test case 10 - delta assumption
print("\nPROOF 10:")
pf = Proof(*latex_to_limit("\\lim_{x \\to 2} x^2 = 4"))
pf.insert(*insert_expr_latex("= |x + 2||x - 2|"))
pf.init_bound_delta(parse_latex("1"))
pf.insert_bound_equation(*insert_bound_eq_latex("-1 \\leq x - 2 \\leq 1"))
pf.insert_bound_equation(*insert_bound_eq_latex("1 \\leq x \\leq 3"))
pf.insert_bound_equation(*insert_bound_eq_latex("3 \\leq x + 2 \\leq 5"))
pf.bound_expression()
pf.insert(*insert_expr_latex("< 5|x - 2|"))
pf.choose_delta(parse_latex("\\frac{\\epsilon}{5}"))
pf.insert(*insert_expr_latex("< 5\\delta"))
pf.insert(*insert_expr_latex("= 5\\frac{\\epsilon}{5}"))
pf.insert(*insert_expr_latex("= \\epsilon"))
pf.print_all()
pf.plot('../samples/open2.png', 6)
