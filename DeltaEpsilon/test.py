from DeltaEpsilon.proof import DEProof

# test case 1
print("PROOF 1:")
pf = DEProof("\\lim_{x \\to 2} (x + 3) = 5")
pf.insert_equation("= |x - 2|")
pf.insert_equation("< \\delta")
pf.let_delta_be("\\epsilon")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()

# test case 2
print("PROOF 2:")
pf = DEProof("\\lim_{x \\to 4} 2(x + 3) = 14")
pf.insert_equation("= |2x + 6 - 14|")
pf.insert_equation("= |2x - 8|")
pf.insert_equation("= 2|x - 4|")
pf.insert_equation("< 2\\delta")
pf.let_delta_be("\\frac{\\epsilon}{2}")
pf.insert_equation("= 2\\frac{\\epsilon}{2}")
pf.insert_equation("= \\epsilon")
pf.print_all_equations()