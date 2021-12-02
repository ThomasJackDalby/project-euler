"""
    Problem 41
    ==========
    
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.
    
    What is the largest n-digit pandigital prime that exists?
    
    Answer: d0a1bd6ab4229b2d0754be8923431404
    
"""
from common import check, is_prime
from itertools import permutations

PROBLEM_NUMBER = 41
ANSWER_HASH = "d0a1bd6ab4229b2d0754be8923431404"

# n must be a digit 1 - 9
# must also be prime
# could brute force?

def is_pandigital(number):
    text = str(number)
    n = len(text)
    occurances = [0] * n
    for i in range(n):
        digit = int(text[i])
        if digit > n:
            return False
        occurances[digit-1] += 1
        if occurances[digit-1] > 1:
            return False
    return sum(occurances) == n

max_p = -1

for p in permutations("7654321"):
    p = int("".join(p))
    if is_prime(p):
        check(p, PROBLEM_NUMBER, ANSWER_HASH)
        exit()
