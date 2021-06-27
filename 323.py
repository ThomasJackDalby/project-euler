"""
    Problem 323
    ===========
    
    Let y[0], y[1], y[2],... be a sequence of random unsigned 32 bit integers
    (i.e. 0 ≤ y[i] < 2^32, every value equally likely).
    
    For the sequence x[i] the following recursion is given:
    
    • x[0] = 0 and
    • x[i] = x[i-1] | y[i-1], for i > 0. ( | is the bitwise-OR operator)
    
    It can be seen that eventually there will be an index N such that x[i] =
    2^32 -1 (a bit-pattern of all ones) for all i ≥ N.
    
    Find the expected value of N.
    Give your answer rounded to 10 digits after the decimal point.
    
    Answer: c8f8a7ab17a87f1b17a1f4a86c984ea7
    
"""
from common import check

PROBLEM_NUMBER = 323
ANSWER_HASH = "c8f8a7ab17a87f1b17a1f4a86c984ea7"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
