import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_floats(self):
        self.assertEqual(add(5.5, 3.3), 8.8)

    def test_add_mismatched_types(self):
        with self.assertRaises(TypeError):
            add(5, '3')

    def test_add_invalid_input(self):
        with self.assertRaises(TypeError) as cm:
            add('5', '3')
        self.assertEqual(str(cm.exception), "Both inputs must be numbers, but got str and str")

    def test_add_invalid_input_type(self):
        with self.assertRaises(TypeError) as cm:
            add(5, None)
        self.assertEqual(str(cm.exception), "Both inputs must be numbers, but got int and NoneType")

    def test_add_invalid_input_value(self):
        with self.assertRaises(TypeError) as cm:
            add(5, True)
        self.assertEqual(str(cm.exception), "Both inputs must be numbers, but got int and bool")

if __name__ == '__main__':
    unittest.main()