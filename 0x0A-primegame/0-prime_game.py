#!/usr/bin/python3
""" prime game """


def isWinner(x, nums):
    """ prime game """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i, x in enumerate(sieve) if x]
    c = 0
    for n in nums:
        for i in range(len(sieve)):
            if sieve[i] > n:
                break
        c += i % 2 == 1
    if c * 2 == len(nums):
        return None
    if c * 2 > len(nums):
        return "Maria"
    return "Ben"
