'''try:
    x = 1 / 0  # This will cause a ZeroDivisionError
    raise ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError("Custom error message: Division by zero detected.") from e
'''
#2
# Define a custom exception
class MyCustomError(Exception):
    pass

# Raise the custom exception
try:
    raise MyCustomError("This is a custom error message.")
except MyCustomError as e:
    print(f"Caught an error: {e}")
