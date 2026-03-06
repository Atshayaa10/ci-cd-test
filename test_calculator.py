import unittest
from calculator import calculate_average

class TestCalculator(unittest.TestCase):
    def test_average_of_numbers(self):
        self.assertAlmostEqual(calculate_average([10, 20, 30]), 20)

    def test_average_of_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_average_of_list_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            calculate_average([10, 'a', 30])

    def test_average_of_list_with_nan(self):
        with self.assertRaises(ValueError):
            calculate_average([10, float('nan'), 30])

    def test_average_of_list_with_infinity(self):
        with self.assertRaises(ValueError):
            calculate_average([10, float('inf'), 30])

    def test_average_of_list_with_negative_infinity(self):
        with self.assertRaises(ValueError):
            calculate_average([10, float('-inf'), 30])

    def test_average_of_list_with_single_none_value(self):
        with self.assertRaises(TypeError):
            calculate_average([10, None, 30])

    def test_average_of_list_with_empty_string(self):
        with self.assertRaises(TypeError):
            calculate_average([10, '', 30])

    def test_average_of_list_with_single_infinity_value(self):
        with self.assertRaises(ValueError):
            calculate_average([float('inf')])

    def test_average_of_list_with_single_negative_infinity_value(self):
        with self.assertRaises(ValueError):
            calculate_average([float('-inf')])

if __name__ == "__main__":
    unittest.main()