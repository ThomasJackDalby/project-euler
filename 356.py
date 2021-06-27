"""
    Problem 356
    ===========
    
    Let a[n] be the largest real root of a polynomial g(x) = x^3 - 2^n·x^2 +
    n.
    For example, a[2] = 3.86619826...
    
    Find the last eight digits of.
    
    Note: represents the floor function.
    
    p_356_cubicpoly1.gif
    p_356_cubicpoly2.gif
    Answer: ab2104e80fa7da630ce7fd835d8006ee
    
"""
from common import check

PROBLEM_NUMBER = 356
ANSWER_HASH = "ab2104e80fa7da630ce7fd835d8006ee"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
