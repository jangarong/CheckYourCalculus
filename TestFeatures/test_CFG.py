import unittest
from CFG.contextFree import Grammar


class TestGrammar(unittest.TestCase):

    def test_1s(self):
        g = Grammar({'S': ['', 'S1']}, 'S')
        res = ()
        res += (g.is_accepting(''),)
        res += (g.is_accepting('1'),)
        res += (g.is_accepting('11111111111111111111111'),)
        res += (g.is_accepting('00110abxe'),)
        self.assertEqual(res, (True, True, True, False))

    def test_palindrome(self):
        g = Grammar({'S': ['', '1', '0', '1S1', '0S0']}, 'S')
        res = ()
        res += (g.is_accepting('0011'),)
        res += (g.is_accepting('11100100111'),)
        res += (g.is_accepting('0110110'),)
        self.assertEqual(res, (False, True, True))

    def test_palindrome2(self):
        g = Grammar({'S': ['A', '2S2'], 'A': ['', '1', '1A1', '0A0']}, 'S')
        res = ()
        res += (g.is_accepting('2201111022'),)
        res += (g.is_accepting('11100100111'),)
        res += (g.is_accepting('0110110'),)
        self.assertEqual(res, (True, True, False))

    def test_ABC(self):
        g = Grammar({'S': ['0A', '1B', '2C', '0S0', '1S1', '2S2'],
                     'A': ['', 'B1', 'C2'],
                     'B': ['', 'A0', 'C2'],
                     'C': ['', 'A0', 'B1']}, 'S')
        res = ()
        res += (g.is_accepting('01X10'),)
        res += (g.is_accepting('0'),)
        res += (g.is_accepting('20012012021212'),)
        res += (g.is_accepting('201121'),)
        self.assertEqual(res, (False, True, True, False))


if __name__ == '__main__':
    unittest.main()
