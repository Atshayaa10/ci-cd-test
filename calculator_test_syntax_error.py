import unittest

class TestCalculator(unittest.TestCase):
    def test_calculator_syntax_error(self):
        with self.assertRaises(SyntaxError):
            exec('calculator.py')

if __name__ == '__main__':
    unittest.main()