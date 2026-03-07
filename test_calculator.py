import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 3), -2)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_non_integer_input(self):
        with self.assertRaises(TypeError):
            add(5, 3.5)

    def test_add_non_integer_input_type(self):
        with self.assertRaises(TypeError):
            add("five", 3)

    def test_add_non_integer_string_input(self):
        with self.assertRaises(TypeError):
            add("five", "three")

if __name__ == '__main__':
    unittest.main()