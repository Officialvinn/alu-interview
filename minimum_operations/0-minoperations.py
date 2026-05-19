#!/usr/bin/python3
"""Module that calculates the minimum number of operations."""


def minOperations(n):
    """Return the fewest Copy All / Paste operations to reach n 'H' chars.

    Works by summing the prime factors of n, since each multiplication
    by a factor f costs f operations and primes give the smallest sum.

    Args:
        n (int): the target number of characters.

    Returns:
        int: the minimum number of operations, or 0 if n is unreachable.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
