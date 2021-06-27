"""
    Problem 197
    ===========
    
    Given is the function f(x) = ⌊2^30.403243784-x^2⌋ × 10^-9 ( ⌊ ⌋ is the
    floor-function),
    the sequence u[n] is defined by u[0] = -1 and u[n+1] = f(u[n]).
    
    Find u[n] + u[n+1] for n = 10^12.
    Give your answer with 9 digits after the decimal point.
    
    Answer: c98cbf87636906f2465d481be815e454
    
"""
from common import check

PROBLEM_NUMBER = 197
ANSWER_HASH = "c98cbf87636906f2465d481be815e454"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
