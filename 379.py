"""
    Problem 379
    ===========
    
    Let f(n) be the number of couples (x,y) with x and y positive integers, x
    ≤ y and the least common multiple of x and y equal to n.
    
    Let g be the summatory function of f, i.e.: g(n) = ∑ f(i) for 1 ≤ i ≤ n.
    
    You are given that g(10^6) = 37429395.
    
    Find g(10^12).
    
    Answer: de20f710cb6665c48795072197ad53e0
    
"""
from common import check

PROBLEM_NUMBER = 379
ANSWER_HASH = "de20f710cb6665c48795072197ad53e0"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
