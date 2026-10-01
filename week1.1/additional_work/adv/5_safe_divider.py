"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

# TODO: wrap the risky operations in a try/except block
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds

try:
    numerator = int(numerator_input)
    denominator = int(denominator_input)
    result = numerator / denominator
    print(f"The result is: {result}")
except ValueError:
    print("Error: both inputs must be numbers.")
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
