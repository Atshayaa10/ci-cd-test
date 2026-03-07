import unittest

class TestCalculator(unittest.TestCase):
    """
    Test class for the calculator module.
    """
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
        self.assertEqual(add(-1000000000, -2000000000), -3000000000)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(5, 0), 5)
        with self.assertRaises(TypeError):
            add('a', 3)
        with self.assertRaises(TypeError):
            add(3.5, 'b')
        with self.assertRaises(TypeError):
            add('a', 'b')
        with self.assertRaises(TypeError):
            add([1, 2], 3)
        with self.assertRaises(TypeError):
            add(3.5, [1, 2])

if __name__ == '__main__':
    unittest.main()