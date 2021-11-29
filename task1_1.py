import unittest
from reverse import reverse


class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_single(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrom(self):
        self.assertEqual(reverse('level'), 'level')

    def test_usual_str(self):
        self.assertEqual(reverse('Hello'), 'olleH')

    def test_wrong_type_not_iter(self):
        with self.assertRaises(TypeError):
            reverse(55)

    def test_wrong_type_iter(self):
        with self.assertRaises(TypeError):
            reverse(['He', 'll', 'o!'])


if __name__ == '__main__':
    unittest.main()
