def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float or None: The average of the numbers, or None if the input list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty
    total = sum(numbers)
    return total / len(numbers)

result = calculate_average([10, 20, 30])
if result is not None:
    print(f"The average is: {result}")
else:
    print("Cannot calculate average")