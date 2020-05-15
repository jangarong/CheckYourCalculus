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

# test case 4 - approaches infinite limit
print("\nPROOF 4:")
pf = DEProof("\\lim_{x \\to -\\infty} 1 = 14")

