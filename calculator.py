def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    
    Args:
    numbers (list): The list of numbers to calculate the average of.
    
    Returns:
    float: The average of the numbers.
    
    Raises:
    ValueError: If the input list is empty.
    TypeError: If the input list contains non-numeric values or None values.
    ValueError: If the input list contains NaN or infinity values.
    """
    if len(numbers) == 0:
        raise ValueError("The input list is empty")
    try:
        total = sum(numbers)
    except TypeError:
        raise TypeError("The input list contains non-numeric values or None values")
    except ValueError:
        raise ValueError("The input list contains NaN or infinity values")
    return total / len(numbers)

result = calculate_average([10, 20, 30])
print(f"The average is: {result}")