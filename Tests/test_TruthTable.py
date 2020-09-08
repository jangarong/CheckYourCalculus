from LogicEquiv.truthTables import TruthTables
tt = TruthTables()
print(tt.dnf('((\\neg x) \\vee x)'))
print(tt.generate_truth_table('\\neg ((\\neg x) \\vee x)'))
print(tt.generate_truth_table('(x \\rightarrow y)'))
print(tt.generate_truth_table('(((\\neg x) \\vee y) \\rightarrow z)'))
print(tt.dnf('(((\\neg x) \\vee y) \\rightarrow z)'))
