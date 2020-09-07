from Automata.DFSA import Deterministic
import unittest


class TestDFSA(unittest.TestCase):
    """Test cases for class DFSA.Deterministic.
    """

    def setUp(self):
        # accept: {|x|>=2, x start and end with 0}
        d = Deterministic({('q0', '0'): 'q1',
                           ('q1', '0'): 'q2',
                           ('q1', '1'): 'q3',
                           ('q2', '0'): 'q2',
                           ('q2', '1'): 'q3',
                           ('q3', '0'): 'q2',
                           ('q3', '1'): 'q3'}, 'q0', ['q2'])
        self.dfsa = d

    def test_00_empty_input(self):
        string = ''
        actual = self.dfsa.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)

    def test_01_length_one(self):
        string = '0'
        actual = self.dfsa.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)

    def test_02_length_greater_than_one_accepted(self):
        string = '0100'
        actual = self.dfsa.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_03_length_greater_than_one_rejected(self):
        string = '10011'
        actual = self.dfsa.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)


if __name__ == '__main__':
    unittest.main()
