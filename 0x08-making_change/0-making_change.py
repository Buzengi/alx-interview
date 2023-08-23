#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount.
"""

import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
            If total is 0 or less, return 0
            If total can't be met by any number of coins u have, return -1
    """

    if total == 0:
        return 0

    coins.sort(reverse=True)

    new_total = total
    total_change = 0
    total_value = 0

    for coin in coins:
        current_change = 0
        if coin == new_total:
            current_change = new_total // coin
            total_value += current_change * coin
            total_change += current_change
        elif total % coin > 0:
            current_change = new_total // coin
            new_total = new_total % coin
            total_value += current_change * coin
            total_change += current_change

    if total == total_value:
        return total_change
    else:
        return - 1
