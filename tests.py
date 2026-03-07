import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
        self.assertEqual(add(0.5, 0.5), 1.0)
        self.assertEqual(add(1e308, 1e308), float('inf'))
        self.assertEqual(add(-1e308, -1e308), float('-inf'))

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-1000000000, -2000000000), -3000000000)
        self.assertEqual(add(-0.5, -0.5), -1.0)
        self.assertEqual(add(-1e308, -1e308), float('-inf'))
        self.assertEqual(add(1e308, 1e308), float('inf'))

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-1000000000, 2000000000), -2000000000)
        self.assertEqual(add(-0.5, 0.5), 0.0)

    def test_add_non_numeric_input(self):
        with self.assertRaises(TypeError):
            add('a', 3)
        with self.assertRaises(TypeError):
            add(5, 'b')
        with self.assertRaises(TypeError):
            add('a', 'b')

    def test_add_too_large_input(self):
        with self.assertRaises(ValueError):
            add(2**31, 1)
        with self.assertRaises(ValueError):
            add(-2**31 - 1, 1)

if __name__ == '__main__':
    unittest.main()