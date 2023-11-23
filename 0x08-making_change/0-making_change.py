#!/usr/bin/python3
"""0. Change comes from within
"""


def makeChange(coins, total):
    """determines the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    if total in coins:
        return 1

    nbr_coin = 0
    coins.sort(reverse=True)

    for i in coins:
        if total % i == 0:
            return total / i
        elif total - i >= 0:
            if int(total / i) > 1:
                nbr_coin += int(total / i)
                total = total % i
            else:
                nbr_coin += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return nbr_coin
