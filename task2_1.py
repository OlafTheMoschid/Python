import unittest
from math import sqrt
from roots import roots


class RootsTest(unittest.TestCase):
    def test_a_iszero(self):
        self.assertEqual(roots(0, 1, 2), None)

    def test_b_iszero(self):
        self.assertEqual(roots(2, 0, -8), (-2, 2))

    def test_b_iszero_err(self):
        self.assertEqual(roots(2, 0, 8), None)

    def test_c_iszero(self):
        self.assertEqual(roots(1, -4, 0), (0, 4))

    def test_discriminant_iszero(self):
        self.assertEqual(roots(1, 2, 1), (-1, -1))

    def test_discriminant_isnegative(self):
        self.assertEqual(roots(1, 2, 6), None)

    def test_some_nums_are_float(self):
        x1 = (5 - 2 * sqrt(15)) / 7
        x2 = (5 + 2 * sqrt(15)) / 7
        self.assertEqual(roots(2.1, -3, -1.5), (x1, x2))

    def test_output_float(self):
        x1 = (14 - 16) / 6
        x2 = (14 + 16) / 6
        self.assertEqual(roots(3, -14, -5), (x1, x2))

    def test_wrong_type(self):
        self.assertEqual(roots('1', [4], 3), None)


if __name__ == '__main__':
    unittest.main()
