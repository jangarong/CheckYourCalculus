from DeltaEpsilon.proof import DEProof

# test case 1 - straight proof
print("PROOF 1:")
pf = DEProof("\\lim_{x \\to 2} (x + 3) = 5")
pf.insert_equation("= |x - 2|")
pf.insert_equation("< \\delta")
pf.let_delta_be("\\epsilon")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 2 - delta with a multiple
print("\nPROOF 2:")
pf = DEProof("\\lim_{x \\to 4} 2(x + 3) = 14")
pf.insert_equation("= |2x + 6 - 14|")
pf.insert_equation("= |2x - 8|")
pf.insert_equation("= 2|x - 4|")
pf.insert_equation("< 2\\delta")
pf.let_delta_be("\\frac{\\epsilon}{2}")
pf.insert_equation("= 2\\frac{\\epsilon}{2}")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 3 - one sided limit
print("\nPROOF 3:")
pf = DEProof("\\lim_{x \\to 4^-} 2(x + 3) = 14")
pf.insert_equation("= -(2x + 6 - 14)")
pf.insert_equation("= -(2x - 8)")
pf.insert_equation("= -2x + 8)")
pf.insert_equation("= 2(4 - x)")
pf.insert_equation("< 2\\delta")
pf.let_delta_be("\\frac{\\epsilon}{2}")
pf.insert_equation("= 2\\frac{\\epsilon}{2}")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 4 - x approaches infinity limit
print("\nPROOF 4:")
pf = DEProof("\\lim_{x \\to \\infty} \\frac{3}{x^2} = 0")
pf.insert_equation("< |\\frac{3}{N^2}|")
pf.let_delta_be("\\sqrt{\\frac{3}{\\epsilon}}")
pf.insert_equation("= |\\frac{3}{(\\sqrt{\\frac{3}{\\epsilon}})^2}|")
pf.insert_equation("= |\\epsilon|")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 5 - x approaches infinity limit
print("\nPROOF 5:")
pf = DEProof("\\lim_{x \\to \\infty} \\frac{x + 1}{x} = 1")
pf.insert_equation("= |\\frac{x + 1}{x} - \\frac{x}{x}|")
pf.insert_equation("= |\\frac{x + 1 - x}{x}|")
pf.insert_equation("= |\\frac{1}{x}|")
pf.insert_equation("< |\\frac{1}{N}|") # problem
pf.let_delta_be("\\frac{1}{\\epsilon}")
pf.insert_equation("= |\\frac{1}{\\frac{1}{\\epsilon}}|")
pf.insert_equation("= |\\epsilon|")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 6 - limit is infinity
print("\nPROOF 6:")
pf = DEProof("\\lim_{x \\to 0^+} \\frac{1}{x} = \\infty")
pf.let_delta_be("\\frac{1}{M}")
pf.insert_equation("> \\frac{1}{\\delta}")
pf.insert_equation("= \\frac{1}{\\frac{1}{M}}")
pf.insert_equation("= M")
pf.print_all_equations()