#!/usr/bin/python3
"""
This is to determine the fewest
number of coins needed to meet a given amount total.

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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
