def add(a, b):
    return a + b

# Fix the syntax error by closing the parenthesis
print("The sum of 5 and 3 is:", add(5, 3))  # Added closing parenthesis

# Additional check to ensure parenthesis is closed correctly
try:
    print("The sum of 5 and 3 is:", add(5, 3))
except SyntaxError as e:
    print(f"Syntax error detected: {e}")