"""
    Problem 145
    ===========
    
    Some positive integers n have the property that the sum [ n + reverse(n) ]
    consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
    409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409,
    and 904 are reversible. Leading zeroes are not allowed in either n or
    reverse(n).
    
    There are 120 reversible numbers below one-thousand.
    
    How many reversible numbers are there below one-billion (10^9)?
    
    Answer: 705e8444ad9c92e9a7589fb97515a9b6
    
"""
from common import check

PROBLEM_NUMBER = 145
ANSWER_HASH = "705e8444ad9c92e9a7589fb97515a9b6"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
