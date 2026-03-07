import unittest
from calculator import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_with_non_integer(self):
        with self.assertRaises(TypeError):
            add(5, 3.5)

if __name__ == "__main__":
    unittest.main()