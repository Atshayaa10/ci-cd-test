def calculate_average(numbers)
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

result = calculate_average([10, 20, 30])
print(f"The average is: {result}")
