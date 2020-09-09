from Automata.NFSA import NonDeterministic
import unittest


class TestNFSA(unittest.TestCase):
    """Test cases for class NFSA.NonDeterministic.
    """

    def setUp(self):
        # accept: {(5+7)(57)* delete zero or more 7)}
        n = NonDeterministic({('q0', '5'): ['q1'],
                              ('q0', '7'): ['q2'],
                              ('q0', ''): ['q2'],
                              ('q1', ''): ['q3'],
                              ('q2', ''): ['q3'],
                              ('q3', '5'): ['q4'],
                              ('q4', '7'): ['q3'],
                              ('q4', ''): ['q3']
                              }, 'q0', ['q3'])
        self.nfsa = n

    def test_00_empty_input(self):
        string = ''
        actual = self.nfsa.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)

    def test_01_single_five(self):
        string = '5'
        actual = self.nfsa.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_02_single_seven(self):
        string = '7'
        actual = self.nfsa.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_03_not_delete_seven(self):
        string = '757575757'
        actual = self.nfsa.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_04_delete_seven(self):
        string = '557557557'
        actual = self.nfsa.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_05_rejected(self):
        string = '555775'
        actual = self.nfsa.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)


if __name__ == '__main__':
    unittest.main()
