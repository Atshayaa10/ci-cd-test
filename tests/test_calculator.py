import unittest
from calculator import calculate_average

class TestCalculator(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20.0)

    def test_average_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_average([0])

    def test_average_with_non_numeric_values_and_zero(self):
        with self.assertRaises(ValueError):
            calculate_average([10, 'a', 0])

    def test_average_with_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

if __name__ == '__main__':
    unittest.main()