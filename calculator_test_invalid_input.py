import unittest

class TestCalculator(unittest.TestCase):
    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add('a', 3)
        with self.assertRaises(TypeError):
            add(3, 'a')
        with self.assertRaises(TypeError):
            add('a', 'b')

if __name__ == '__main__':
    unittest.main()