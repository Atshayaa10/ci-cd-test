def add(a, b):
    return a + b

# Define constants for the numbers
NUM1 = 5
NUM2 = 3

# Fix the syntax error by closing the parenthesis
print(f"The sum of {NUM1} and {NUM2} is:", add(NUM1, NUM2))

# Additional check to ensure parenthesis is closed correctly
try:
    print(f"The sum of {NUM1} and {NUM2} is:", add(NUM1, NUM2))
except SyntaxError as e:
    print(f"Syntax error detected: {e}")
except TypeError as e:
    print(f"Type error detected: {e}")