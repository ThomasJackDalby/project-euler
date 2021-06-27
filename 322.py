"""
    Problem 322
    ===========
    
    Let T(m, n) be the number of the binomial coefficients ^iC[n] that are
    divisible by 10 for n ≤ i < m(i, m and n are positive integers).
    You are given that T(10^9, 10^7-10) = 989697000.
    
    Find T(10^18, 10^12-10).
    
    Answer: a75af9d717fa592487fb45e7552204a8
    
"""
from common import check

PROBLEM_NUMBER = 322
ANSWER_HASH = "a75af9d717fa592487fb45e7552204a8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
