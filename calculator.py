def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Notes:
        Both inputs must be integers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    print("The sum of {} and {} is: {}".format(a, b, a + b))
    return a + b

# Test the function
add(5, 3)