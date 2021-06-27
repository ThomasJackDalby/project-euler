"""
    Problem 377
    ===========
    
    There are 16 positive integers that do not have a zero in their digits and
    that have a digital sum equal to 5, namely:
    5, 14, 23, 32, 41, 113, 122, 131, 212, 221, 311, 1112, 1121, 1211, 2111
    and 11111.
    Their sum is 17891.
    
    Let f(n) be the sum of all positive integers that do not have a zero in
    their digits and have a digital sum equal to n.
    
    Find .
    Give the last 9 digits as your answer.
    
    Answer: a915ccbae49de15208c88affba84d206
    
"""
from common import check

PROBLEM_NUMBER = 377
ANSWER_HASH = "a915ccbae49de15208c88affba84d206"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
