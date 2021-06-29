"""
    Problem 355
    ===========
    
    Define Co(n) to be the maximal possible sum of a set of mutually co-prime
    elements from {1, 2, ..., n}.
    For example Co(10) is 30 and hits that maximum on the subset
    {1, 5, 7, 8, 9}.
    
    You are given that Co(30) = 193 and Co(100) = 1356.
    
    Find Co(200000).
    
    Answer: 41cb97b6d02878d79f8b2e3b6c74920a
    
"""
from common import check

PROBLEM_NUMBER = 355
ANSWER_HASH = "41cb97b6d02878d79f8b2e3b6c74920a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
