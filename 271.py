"""
    Problem 271
    ===========
    
    For a positive number n, define S(n) as the sum of the integers x, for
    which 1<x<n and
    x^3≡1 mod n.
    
    When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53,
    74, 79, 81.
    Thus, S(91)=9+16+22+29+53+74+79+81=363.
    
    Find S(13082761331670030).
    
    Answer: c4157aab542bd0dfa465c890e1286cc5
    
"""
from common import check

PROBLEM_NUMBER = 271
ANSWER_HASH = "c4157aab542bd0dfa465c890e1286cc5"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
