#!/usr/bin/python3
""" prime game """
from math import sqrt


def isWinner(x, nums):
    """ Where x is the number of rounds and nums is an array of n
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    sieve = [i for i, x in enumerate(sieve) if x]
    c = 0
    for n in nums:
        for i in range(len(sieve)):
            if sieve[i] > n:
                break
            c += 1
        if c % 2 == 0:
            return "Ben"
        else:
            return "Maria"
