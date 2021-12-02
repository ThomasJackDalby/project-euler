"""
    Problem 46
    ==========
    
    
    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.
    
    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2
    
    It turns out that the conjecture was false.
    
    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?
    
    
    Answer: 89abe98de6071178edb1b28901a8f459
"""
from common import check, get_primes, is_prime
from itertools import count, islice

PROBLEM_NUMBER = 46
ANSWER_HASH = "89abe98de6071178edb1b28901a8f459"

def is_possible(i):
    for p in get_primes():
        if p >= i:
            return False

        for j in count(1):
            k = p + 2 * j**2
            if k == i:
                print(f"{p} + 2 * {j}**2 = {i}")
                return True
            elif k > i:
                break

result = next(i for i in count(3, 2) if not is_prime(i) and not is_possible(i))
check(result, PROBLEM_NUMBER, ANSWER_HASH)
