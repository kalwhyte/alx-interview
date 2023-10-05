#!/usr/bin/python3
""" prime game """
from math import sqrt


def is_prime(n):
    """ checks if a number is prime """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


def isWinner(x, nums):
    """ returns name of player that won most rounds """
    if not nums or x < 1:
        return None

    maria = 0
    ben = 0

    for round in range(x):
        prime_count = 0
        for num in nums:
            if is_prime(num):
                prime_count += 1
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
