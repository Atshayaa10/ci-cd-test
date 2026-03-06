def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if len(numbers) == 0:
        raise ValueError(f"Cannot calculate average of an empty list: {numbers}")
    if len(numbers) == 1:
        return float(numbers[0])  # Return the single number as a float
    return sum(numbers) / len(numbers)

result = calculate_average([10, 20, 30])
print(f"The average is: {result}")