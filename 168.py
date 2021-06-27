"""
    Problem 168
    ===========
    
    Consider the number 142857. We can right-rotate this number by moving the
    last digit (7) to the front of it, giving us 714285.
    It can be verified that 714285=5×142857.
    This demonstrates an unusual property of 142857: it is a divisor of its
    right-rotation.
    
    Find the last 5 digits of the sum of all integers n, 10 < n < 10^100, that
    have this property.
    
    Answer: 39e7aab76650b018578830bc6dba007a
    
"""
from common import check

PROBLEM_NUMBER = 168
ANSWER_HASH = "39e7aab76650b018578830bc6dba007a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
