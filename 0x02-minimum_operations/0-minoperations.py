#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H
    """
    p = 0

    if n <= 1:
        return p

    for i in range(2, n + 1):
        while (0 == n % i):
            p = p + i
            n = n / i
            if n < i:
                break
    return p
