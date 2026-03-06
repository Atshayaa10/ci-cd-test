import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
        self.assertEqual(add(-1000000000, -2000000000), -3000000000)

    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add('a', 3)
        with self.assertRaises(TypeError):
            add(5, 'b')
        with self.assertRaises(TypeError):
            add('a', 'b')

    def test_add_invalid_input_message(self):
        with self.assertRaises(TypeError) as e:
            add('a', 3)
        self.assertEqual(str(e.exception), "Both inputs must be numbers")

if __name__ == '__main__':
    unittest.main()