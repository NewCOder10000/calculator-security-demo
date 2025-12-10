import os

# Read environment variable (default to "normal")
CALC_MODE = os.environ.get("CALC_MODE", "normal")


def apply_mode(result):
    """Modify result based on environment variable CALC_MODE."""
    if CALC_MODE == "double":
        return result * 2
    return result


def add(a, b):
    """Return the sum of two numbers."""
    return apply_mode(a + b)


def subtract(a, b):
    """Return the difference of two numbers."""
    return apply_mode(a - b)


def multiply(a, b):
    """Return the product of two numbers."""
    return apply_mode(a * b)


def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return apply_mode(a / b)


def power(a, b):
    """Return the exponential product of two numbers."""
    return apply_mode(a ** b)
