#!/usr/bin/python3
"""
Coin Change Algorithm
"""


def makeChange(coins, total):
    """Calculate the fewest number needed to meet,
    needed to meet a given total amount.
    Args:
        coins ([list]): A list of coin values available.
        total ([number]): The target amount
    Return: The fewest number of coins needed to reach the total,
    or -1 if not possible.
    """
    
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change