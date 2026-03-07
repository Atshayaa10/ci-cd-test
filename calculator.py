def add(a, b):
    """
    Returns the sum of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    return a + b

# Test the add function
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_with_non_integer(self):
        with self.assertRaises(TypeError):
            add(5, 3.5)

if __name__ == "__main__":
    unittest.main()