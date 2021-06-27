"""
    Problem 171
    ===========
    
    For a positive integer n, let f(n) be the sum of the squares of the digits
    (in base 10) of n, e.g.
    
    f(3) = 3^2 = 9,
    f(25) = 2^2 + 5^2 = 4 + 25 = 29,
    f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36
    
    Find the last nine digits of the sum of all n, 0 < n < 10^20, such that
    f(n) is a perfect square.
    
    Answer: ff586db8c4a5699ec78c645fcb27db7b
    
"""
from common import check

PROBLEM_NUMBER = 171
ANSWER_HASH = "ff586db8c4a5699ec78c645fcb27db7b"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
