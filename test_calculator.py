import unittest

class TestCalculator(unittest.TestCase):

    def test_add_integers(self):
        """
        Test that the add function returns the correct result when both inputs are integers.
        """
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_integers(self):
        """
        Test that the add function returns the correct result when both inputs are negative integers.
        """
        self.assertEqual(add(-5, -3), -8)

    def test_add_zero(self):
        """
        Test that the add function returns the correct result when both inputs are zero.
        """
        self.assertEqual(add(0, 0), 0)

    def test_add_zero_and_positive(self):
        """
        Test that the add function returns the correct result when one input is zero and the other is a positive number.
        """
        self.assertEqual(add(0, 5), 5)

    def test_add_zero_and_negative(self):
        """
        Test that the add function returns the correct result when one input is zero and the other is a negative number.
        """
        self.assertEqual(add(0, -5), -5)

    def test_add_floats(self):
        """
        Test that the add function returns the correct result when both inputs are floats.
        """
        self.assertEqual(add(5.5, 3.3), 8.8)

    def test_add_integer_and_float(self):
        """
        Test that the add function returns the correct result when one input is a float and the other is an integer.
        """
        self.assertEqual(add(5, 3.3), 8.3)

    def test_add_integer_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a string and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add(5, "3")

    def test_add_string_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is an integer and the other is a string.
        """
        with self.assertRaises(TypeError):
            add("5", 3)

    def test_add_string_and_string(self):
        """
        Test that the add function raises a TypeError when both inputs are strings.
        """
        with self.assertRaises(TypeError):
            add("5", "3")

    def test_add_none(self):
        """
        Test that the add function raises a TypeError when either input is None.
        """
        with self.assertRaises(TypeError):
            add(None, 3)
        with self.assertRaises(TypeError):
            add(3, None)

    def test_add_list_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a list and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add([1, 2, 3], 3)

    def test_add_list_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a list and the other is a float.
        """
        with self.assertRaises(TypeError):
            add([1, 2, 3], 3.3)

    def test_add_list_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a list and the other is a string.
        """
        with self.assertRaises(TypeError):
            add([1, 2, 3], "3")

    def test_add_list_and_list(self):
        """
        Test that the add function raises a TypeError when both inputs are lists.
        """
        with self.assertRaises(TypeError):
            add([1, 2, 3], [4, 5, 6])

    def test_add_dict_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a dictionary and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add({"a": 1, "b": 2}, 3)

    def test_add_dict_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a dictionary and the other is a float.
        """
        with self.assertRaises(TypeError):
            add({"a": 1, "b": 2}, 3.3)

    def test_add_dict_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a dictionary and the other is a string.
        """
        with self.assertRaises(TypeError):
            add({"a": 1, "b": 2}, "3")

    def test_add_dict_and_dict(self):
        """
        Test that the add function raises a TypeError when both inputs are dictionaries.
        """
        with self.assertRaises(TypeError):
            add({"a": 1, "b": 2}, {"c": 3, "d": 4})

    def test_add_set_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a set and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add({1, 2, 3}, 3)

    def test_add_set_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a set and the other is a float.
        """
        with self.assertRaises(TypeError):
            add({1, 2, 3}, 3.3)

    def test_add_set_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a set and the other is a string.
        """
        with self.assertRaises(TypeError):
            add({1, 2, 3}, "3")

    def test_add_set_and_set(self):
        """
        Test that the add function raises a TypeError when both inputs are sets.
        """
        with self.assertRaises(TypeError):
            add({1, 2, 3}, {4, 5, 6})

    def test_add_tuple_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a tuple and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add((1, 2, 3), 3)

    def test_add_tuple_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a tuple and the other is a float.
        """
        with self.assertRaises(TypeError):
            add((1, 2, 3), 3.3)

    def test_add_tuple_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a tuple and the other is a string.
        """
        with self.assertRaises(TypeError):
            add((1, 2, 3), "3")

    def test_add_tuple_and_tuple(self):
        """
        Test that the add function raises a TypeError when both inputs are tuples.
        """
        with self.assertRaises(TypeError):
            add((1, 2, 3), (4, 5, 6))

    def test_add_boolean_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a boolean and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add(True, 3)

    def test_add_boolean_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a boolean and the other is a float.
        """
        with self.assertRaises(TypeError):
            add(True, 3.3)

    def test_add_boolean_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a boolean and the other is a string.
        """
        with self.assertRaises(TypeError):
            add(True, "3")

    def test_add_boolean_and_boolean(self):
        """
        Test that the add function raises a TypeError when both inputs are booleans.
        """
        with self.assertRaises(TypeError):
            add(True, True)

    def test_add_complex_and_integer(self):
        """
        Test that the add function raises a TypeError when one input is a complex number and the other is an integer.
        """
        with self.assertRaises(TypeError):
            add(3 + 4j, 3)

    def test_add_complex_and_float(self):
        """
        Test that the add function raises a TypeError when one input is a complex number and the other is a float.
        """
        with self.assertRaises(TypeError):
            add(3 + 4j, 3.3)

    def test_add_complex_and_string(self):
        """
        Test that the add function raises a TypeError when one input is a complex number and the other is a string.
        """
        with self.assertRaises(TypeError):
            add(3 + 4j, "3")

    def test_add_complex_and_complex(self):
        """
        Test that the add function returns the correct result when both inputs are complex numbers.
        """
        self.assertEqual(add(3 + 4j, 3 + 4j), 6 + 8j)

if __name__ == '__main__':
    unittest.main()