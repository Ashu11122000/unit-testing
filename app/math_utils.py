# Import Union from typing module
# Union allows us to specify that a variable can have multiple types
from typing import Union

# Define a custom type "Number"
# This means Number can be either an integer (int) or a floating-point number(float)
Number = Union[int, float]

# Function to add two numbers
def add(a: Number, b: Number) -> Number:
    # a and b are inputs of type Number (int or float)
    # Returns the sum of a and b
    return a+b

# Function to subtract two numbers
def subtract(a: Number, b: Number) -> Number:
    # Subtracts b from a
    return a-b

# Function to multiply two numbers
def multiply(a: Number, b: Number) -> Number:
    # Multiplies a and b
    return a*b

# Function to divide two numbers
def divide(a: Number, b: Number) -> float:
    # Check if denominator (b) is zero
    # Division by zero is undefined and causes runtime error
    if b == 0:
        # Raise a ValueError with a custom message
        # This prevents the program from crashing unexpectedly
        raise ValueError("Cannot divide by zero")
    
    # Perform normal division
    # Always returns float in Python
    return a / b


# Function for floor division
def floor_divide(a: Number, b: Number) -> Number:
    # Check for division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    # Floor division returns the largest integer less than or equal to the result
    return a // b


# Function to calculate modulus (remainder)
def modulus(a: Number, b: Number) -> Number:
    # Check for division by zero
    if b == 0:
        # Modulus by zero is not allowed
        raise ValueError("Cannot perform modulus by zero")
    
    # Returns remainder after division
    return a % b


# Function to calculate power (exponentiation)
def power(a: Number, b: Number) -> Number:
    # Raises a to the power of b
    return a ** b


# Function to get absolute value
def absolute(a: Number) -> Number:
    # abs() is a built-in Python function
    # Converts negative numbers to positive
    return abs(a)