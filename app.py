def add(a, b
    return a + b

# The issue was caused by an unclosed parenthesis in this line
# The correct fix is to remove the unclosed parenthesis and the function call
result = add(5, 3)
print("The sum of 5 and 3 is:", result
