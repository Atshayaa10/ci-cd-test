import unittest
from calculator import calculate_average

class TestCalculator(unittest.TestCase):
    def test_average_of_non_empty_list(self):
        numbers = [10, 20, 30]
        self.assertAlmostEqual(calculate_average(numbers), 20)

    def test_average_of_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            calculate_average(numbers)

    def test_average_of_list_with_single_element(self):
        numbers = [10.5]  # Test with a float value
        self.assertAlmostEqual(calculate_average(numbers), 10.5)

if __name__ == '__main__':
    unittest.main()