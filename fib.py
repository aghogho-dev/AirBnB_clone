#!/usr/bin/python3
"""Inside the module."""


def fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
