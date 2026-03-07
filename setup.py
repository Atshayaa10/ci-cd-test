# Removed the test_add function as it was redundant and not a valid test case
import unittest
from calculator import add

class TestSetup(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

if __name__ == '__main__':
    unittest.main()