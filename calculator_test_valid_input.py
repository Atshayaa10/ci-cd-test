import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(10, -5), 5)
        self.assertEqual(add(-10, -5), -15)
        self.assertEqual(add(10, 10), 20)

    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add('a', 3)
        with self.assertRaises(TypeError):
            add(3, 'a')
        with self.assertRaises(TypeError):
            add('a', 'b')

if __name__ == '__main__':
    unittest.main()