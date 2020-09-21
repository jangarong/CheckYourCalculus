from csmath.LogicEquiv.truthTables import TruthTables
import unittest


class TestPDA(unittest.TestCase):

    def setUp(self):
        self.tt = TruthTables()

    def test_truth_01(self):
        self.assertDictEqual(self.tt.generate_truth_table('\\neg ((\\neg x) \\vee x)'),
                             {'0': '0', '1': '0'})

    def test_truth_02(self):
        self.assertDictEqual(self.tt.generate_truth_table('(x \\rightarrow y)'),
                             {'00': '1', '01': '1', '10': '0', '11': '1'})

    def test_truth_03(self):
        self.assertDictEqual(self.tt.generate_truth_table('(((\\neg x) \\vee y) \\rightarrow z)'),
                             {'000': '0', '001': '1', '010': '0', '011': '1', '100': '1',
                              '101': '1', '110': '0', '111': '1'})

    def test_truth_04(self):
        self.assertDictEqual(self.tt.generate_truth_table("(((\\neg (\\neg x)) \\vee (\\neg "
                                                          "(\\neg y))) \\wedge ((\\neg x) \\vee "
                                                          "(\\neg y)))"),
                             {'00': '0', '01': '1', '10': '1', '11': '0'})

    # def test_contradiction_dnf(self):
    #     self.assertEqual(self.tt.dnf('((\\neg x) \\vee x)'), "((\\neg x) \\wedge x)")

    def test_dnf_01(self):
        self.assertEqual(self.tt.dnf('(((\\neg x) \\vee y) \\rightarrow z)'),
                         "(((\\neg x) \\wedge (\\neg y) \\wedge z) \\vee ((\\neg x) \\wedge y "
                         "\\wedge z) \\vee (x \\wedge (\\neg y) \\wedge (\\neg z)) \\vee (x \\wedge"
                         " (\\neg y) \\wedge z) \\vee (x \\wedge y \\wedge z))")


if __name__ == '__main__':
    unittest.main()
