def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both inputs must be numbers, but got {type(a).__name__} and {type(b).__name__}")
    return a + b
print("The sum of 5 and 3 is:", add(5, 3))