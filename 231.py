"""
    Problem 231
    ===========
    
    The binomial coefficient ^10C[3] = 120.
    120 = 2^3 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
    So the sum of the terms in the prime factorisation of ^10C[3] is 14.
    
    Find the sum of the terms in the prime factorisation of
    ^20000000C[15000000].
    
    Answer: ef8bc4d9a843e71126bd10b5065132a5
    
"""
from common import check

PROBLEM_NUMBER = 231
ANSWER_HASH = "ef8bc4d9a843e71126bd10b5065132a5"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
