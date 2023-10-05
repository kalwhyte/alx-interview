#!/usr/bin/python3
""" prime game """
from math import sqrt


def is_prime(n, nums):
    """ Where x is the number of rounds,
    and nums is an array of n.
    """
    if n < 2:
        return False
    if n in nums:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """ Where x is the number of rounds and nums is an array of n
    """
    if not nums or x < 1:
        return None
    Maria = 0
    Ben = 0
    for i in range(len(nums)):
        if is_prime(i, nums):
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return "Maria"
    elif Maria < Ben:
        return "Ben"
    else:
        return None
