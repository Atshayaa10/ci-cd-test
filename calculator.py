def add(a, b):
    return a + b

try:
    # Fix the syntax error by adding a closing parenthesis
    print("The sum of 5 and 3 is:", add(5, 3))
except TypeError as e:
    print(f"Invalid input: {e}")