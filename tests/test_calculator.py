import unittest
from calculator import calculate_average

class TestCalculator(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20.0)
        self.assertIsNone(calculate_average([]))
        with self.assertRaises(TypeError):
            calculate_average("not a list")

    def test_calculate_average_with_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_average(123)  # Test with a single integer
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "3"])  # Test with a list containing a string

if __name__ == "__main__":
    unittest.main()