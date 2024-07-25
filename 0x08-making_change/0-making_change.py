#!/usr/bin/python3
"""
This calculates the fewest number of coins
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
        
    if total < 0:
        return -1
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    num_coins = 0
    remaining_total = total
    
    for coin in coins:
        if remaining_total <= 0:
            break
        num_coins += remaining_total // coin
        remaining_total %= coin
    
    return num_coins if remaining_total == 0 else -1
