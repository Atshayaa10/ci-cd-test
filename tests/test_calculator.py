import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    
    def test_add_non_integer(self):
        with self.assertRaises(TypeError):
            add(5, 3.5)

if __name__ == '__main__':
    unittest.main()