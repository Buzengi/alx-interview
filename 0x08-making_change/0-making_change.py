#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount.
"""

import sys


def makeChange(coins, total):
    """
    Module tries to give exact change given a list of coins with a 
    specified values if unable to do so returns -1
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
