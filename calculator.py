def add(a, b):
    """
    Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer, float, complex, or None.
    """
    if not isinstance(a, (int, float, complex, type(None))) or not isinstance(b, (int, float, complex, type(None))):
        raise TypeError("Both inputs must be integers, floats, complex numbers, or None")
    if a is None or b is None:
        raise TypeError("Both inputs must be integers, floats, complex numbers, or None")
    return a + b