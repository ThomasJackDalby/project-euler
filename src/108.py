"""
    Problem 108
    ===========
    
    In the following equation x, y, and n are positive integers.
    
    1   1   1
    ─ + ─ = ─
    x   y   n
    
    For n = 4 there are exactly three distinct solutions:
    
    1   1    1
    ─ + ─  = ─
    5   20   4
    1   1    1
    ─ + ─  = ─
    6   12   4
    1   1    1
    ─ + ─  = ─
    8   8    4
    
    What is the least value of n for which the number of distinct solutions
    exceeds one-thousand?
    
    NOTE: This problem is an easier version of [1]Problem 110; it is strongly
    advised that you solve this one first.
    
    Visible links
    1. problem=110
    Answer: 765ba18edd2844db2db95fba25d2f3e7
    
"""
from common import check

PROBLEM_NUMBER = 108
ANSWER_HASH = "765ba18edd2844db2db95fba25d2f3e7"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
