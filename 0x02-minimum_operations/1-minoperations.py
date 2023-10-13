#!/usr/bin/python3
"""Minimum Operations
"""
import math


def is_prime(n):
    """Check if a number is prime
    Args:
        n(int): number to check
    Return: True or False
    """
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True


def biggest_prime_divisor(n):
    """Find the biggest prime number of n
    Args:
        n(int): number
    Return: the biggest prime divisor of n
    """
    for i in range(int(n / 2), 1, -1):
        if n % i == 0 and is_prime(i):
            return i


def minOperations(n):
    """method that calculates the fewest number of
    operations needed to result in exactly n H
    Args:
        n(int): number of H wished
    Return: number of operations
    """
    if n and n > 1:
        if is_prime(n):
            return n
        else:
            div1 = biggest_prime_divisor(n)
            div2 = n / div1
            return int(div1 + div2)
    return 0
