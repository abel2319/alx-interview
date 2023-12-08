#!/usr/bin/python3
""" Prime Game
"""


def isPrime(nbr):
    """ check if nbr is Prime or not
    return True or False
    """
    for i in range(2, int(nbr / 2)):
        if nbr % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
        where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
    """
    scores = {
        'Maria': 0,
        'Ben': 0
    }

    if x is None or nums is None:
        return None

    if x < 1 or len(nums) == 0:
        return None

    nbr_of_primes = 0
    for round in range(x):
        nbr_of_primes = 0
        if nums[round] == 1:
            scores['Ben'] += 1
        else:
            for i in range(2, nums[round] + 1):
                if isPrime(i):
                    nbr_of_primes = nbr_of_primes + 1

            if nbr_of_primes % 2 == 0:
                scores['Ben'] += 1
            else:
                scores['Maria'] += 1

    if scores['Ben'] == scores['Maria']:
        return None

    return 'Ben' if scores['Ben'] > scores['Maria'] else 'Maria'
