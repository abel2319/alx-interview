#!/usr/bin/python3
"""0. Change comes from within
"""


def makeChange(coins, total):
    """determines the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    if coins == [] or coins is None:
        return -1

    if total in coins:
        return 1

    nbr_coin = 0
    coins.sort(reverse=True)

    for i in coins:
        while i <= total:
            total -= i
            nbr_coin += 1
        if (total == 0):
            return change
    return -1
