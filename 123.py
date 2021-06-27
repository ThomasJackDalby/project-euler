"""
    Problem 123
    ===========
    
    Let p[n] be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder
    when (p[n]−1)^n + (p[n]+1)^n is divided by p[n]^2.
    
    For example, when n = 3, p[3] = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.
    
    The least value of n for which the remainder first exceeds 10^9 is 7037.
    
    Find the least value of n for which the remainder first exceeds 10^10.
    
    Answer: 71497f728b86b55d965edbf1849cca8d
    
"""
from common import check

PROBLEM_NUMBER = 123
ANSWER_HASH = "71497f728b86b55d965edbf1849cca8d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
