"""
    Problem 47
    ==========
    
    
    The first two consecutive numbers to have two distinct prime factors are:
    
    14 = 2 × 7
    15 = 3 × 5
    
    The first three consecutive numbers to have three distinct prime factors
    are:
    
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
    
    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?
    
    
    Answer: 748f517ecdc29106e2738f88aa7530f4
"""
from common import check, is_prime, get_factors
from itertools import count

PROBLEM_NUMBER = 47
ANSWER_HASH = "748f517ecdc29106e2738f88aa7530f4"

def get_prime_factors(n):
    return [f for f in get_factors(n) if is_prime(f) and f != 1 and f != n]

def find(number):
    factors = [None] * number
    for i in count(1):
        for l, d in enumerate(reversed(factors)):
            if l == 0:
                continue
            factors[number-l] = d
        factors[0] = get_prime_factors(i)

        if i < number or any(len(f) != number for f in factors):
            continue

        all_factors = [f for factor in factors for f in factor]
        unique_factors = set(all_factors)
        if len(all_factors) == len(unique_factors):
            for j in range(i, i-number, -1):
                
            print(f"{i=} {all_factors=} {unique_factors=}")
            return i-number+1
           
print(find(2))

check(None, PROBLEM_NUMBER, ANSWER_HASH)