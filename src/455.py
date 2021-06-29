"""
    Problem 455
    ===========
    
    Let f(n) be the largest positive integer x less than 10^9 such that the
    last 9 digits of n^x form the number x (including leading zeros), or zero
    if no such integer exists.
    
    For example:
    
    • f(4) = 411728896 (4^411728896 = ...490411728896)
    • f(10) = 0
    • f(157) = 743757 (157^743757 = ...567000743757)
    • Σf(n), 2 ≤ n ≤ 10^3 = 442530011399
    
    Find Σf(n), 2 ≤ n ≤ 10^6.
    
    Answer: 22d6cf30a29e14e5c78dca980edc2796
    
"""
from common import check

PROBLEM_NUMBER = 455
ANSWER_HASH = "22d6cf30a29e14e5c78dca980edc2796"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
