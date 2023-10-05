#!/usr/bin/python3
""" prime game """
from math import sqrt


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    def get_primes(n):
        if n <= 2:
            return True
        return n % 2 == 0
    
    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        if get_primes(n):
            winner_count["Maria"] += 1
        else:
            winner_count["Ben"] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return None
    