from Automata.PDA import PushDown
import unittest


class TestPDA(unittest.TestCase):
    """Test cases for class PDA.PushDown.
    """

    def setUp(self):
        # accept: palindrome
        p = PushDown({('q0', '0', ''): [('q0', 'X'), ('q1', '')],
                      ('q0', '1', ''): [('q0', 'Y'), ('q1', '')],
                      ('q0', '', ''): [('q1', '')],
                      ('q1', '0', 'X'): [('q1', '')],
                      ('q1', '1', 'Y'): [('q1', '')]
                      }, 'q0', ['q1'])
        self.pda = p

    def test_00_empty_input(self):
        string = ''
        actual = self.pda.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_01_length_one(self):
        string = '0'
        actual = self.pda.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_02_length_two_palindrome(self):
        string = '11'
        actual = self.pda.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_03_length_two_not_palindrome(self):
        string = '10'
        actual = self.pda.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)

    def test_04_even_length_palindrome(self):
        string = '011101101110'
        actual = self.pda.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_05_odd_length_palindrome(self):
        string = '1011010101101'
        actual = self.pda.is_accepting(string)
        msg = "Expected True, but returned {}".format(actual)
        self.assertTrue(actual, msg)

    def test_06_even_length_not_palindrome(self):
        string = '1001101101'
        actual = self.pda.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)

    def test_07_odd_length_not_palindrome(self):
        string = '101101001'
        actual = self.pda.is_accepting(string)
        msg = "Expected False, but returned {}".format(actual)
        self.assertFalse(actual, msg)


if __name__ == '__main__':
    unittest.main()
