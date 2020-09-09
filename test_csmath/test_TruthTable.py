from csmath.LogicEquiv.truthTables import TruthTables
tt = TruthTables()
print(tt.dnf('((\\neg x) \\vee x)'))
print(tt.cnf('((\\neg x) \\vee x)'))
print(tt.generate_truth_table('\\neg ((\\neg x) \\vee x)'))
print(tt.generate_truth_table('(x \\rightarrow y)'))
print(tt.generate_truth_table('(((\\neg x) \\vee y) \\rightarrow z)'))
print(tt.dnf('(((\\neg x) \\vee y) \\rightarrow z)'))
print(tt.cnf('(((\\neg x) \\vee y) \\rightarrow z)'))

# all three of these have to be equal
print(tt.generate_truth_table('((\\neg x) \\leftrightarrow y)'))
print(tt.generate_truth_table(tt.dnf('((\\neg x) \\leftrightarrow y)')))
# print(tt.generate_truth_table(tt.cnf('((\\neg x) \\leftrightarrow y)')))
# the above commented code causes an error when parsing
