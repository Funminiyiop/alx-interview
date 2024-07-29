#!/usr/bin/python3
"""
ALX SE Project to calculate the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed.
    If total is 0 or less, return 0.
    If total not met by any number of coins, return -1.

    Hint:
    coins is a list
    coin value = an integer greater than 0
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    dup_total = total
    len_coins = len(coins)

    while(i < len_coins and dup_total > 0):
        if (dup_total - coins[i]) >= 0:
            dup_total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = dup_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins
