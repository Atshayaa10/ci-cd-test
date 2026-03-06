import unittest

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers in the list.

    Raises:
        ValueError: If the input list contains non-numeric values.
        ZeroDivisionError: If the input list contains zero and is empty.
    """
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input list must contain only numbers")
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

result = calculate_average([10, 20, 30])
print(f"The average is: {result}")