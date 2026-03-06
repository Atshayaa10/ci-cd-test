def add(a, b):
    return a + b

# Fix the syntax error by closing the parenthesis
print("The sum of 5 and 3 is:", add(5, 3))  # Added closing parenthesis

# Additional check to ensure parenthesis is closed correctly
try:
    result = add(5, 3)  # Corrected syntax
    print("The sum of 5 and 3 is:", result)
except SyntaxError as e:
    print(f"Syntax error detected: {e}")