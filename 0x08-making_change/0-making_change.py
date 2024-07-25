#!/usr/bin/python3
"""
This is to determine the fewest number of coins
needed to meet a given amount total.

Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1

Hint:
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
assume an infinite number of each denomination of coin in the list
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total amount.

    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    """
    
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    cpy_total = total
    len_coins = len(coins)

    while(i < len_coins and cpy_total > 0):
        if (cpy_total - coins[i]) >= 0:
            cpy_total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = cpy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins