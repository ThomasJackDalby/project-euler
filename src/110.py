"""
    Problem 110
    ===========
    
    In the following equation x, y, and n are positive integers.
    
    1   1   1
    ─ + ─ = ─
    x   y   n
    
    It can be verified that when n = 1260 there are 113 distinct solutions and
    this is the least value of n for which the total number of distinct
    solutions exceeds one hundred.
    
    What is the least value of n for which the number of distinct solutions
    exceeds four million?
    
    NOTE: This problem is a much more difficult version of [1]Problem 108 and
    as it is well beyond the limitations of a brute force approach it requires
    a clever implementation.
    
    Visible links
    1. problem=108
    Answer: 591a7a92f10322866e6a02f3b2386a1c
    
"""
from common import check

PROBLEM_NUMBER = 110
ANSWER_HASH = "591a7a92f10322866e6a02f3b2386a1c"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
