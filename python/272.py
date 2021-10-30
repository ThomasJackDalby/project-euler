"""
    Problem 272
    ===========
    
    For a positive number n, define C(n) as the number of the integers x, for
    which 1<x<n and
    x^3≡1 mod n.
    
    When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53,
    74, 79, 81.
    Thus, C(91)=8.
    
    Find the sum of the positive numbers n≤10^11 for which C(n)=242.
    
    Answer: d84d2020055b3e8867dc359e739e0312
    
"""
from common import check

PROBLEM_NUMBER = 272
ANSWER_HASH = "d84d2020055b3e8867dc359e739e0312"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
