#!/usr/bin/python3
"""Calculate the minimum operations needed to reach n characters."""


def minOperations(n):
    """Return the fewest Copy All and Paste operations."""
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
