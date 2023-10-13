#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H
    """
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
