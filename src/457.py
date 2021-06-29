"""
    Problem 457
    ===========
    
    Let f(n) = n^2 - 3n - 1.
    Let p be a prime.
    Let R(p) be the smallest positive integer n such that f(n) mod p^2 = 0 if
    such an integer n exists, otherwise R(p) = 0.
    
    Let SR(L) be &Sum;R(p) for all primes not exceeding L.
    
    Find SR(10^7).
    
    Answer: 5eae79c2f4887f6cf08c099840317a51
    
"""
from common import check

PROBLEM_NUMBER = 457
ANSWER_HASH = "5eae79c2f4887f6cf08c099840317a51"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
