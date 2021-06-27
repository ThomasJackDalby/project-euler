"""
    Problem 119
    ===========
    
    The number 512 is interesting because it is equal to the sum of its digits
    raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a
    number with this property is 614656 = 28^4.
    
    We shall define a[n] to be the nth term of this sequence and insist that a
    number must contain at least two digits to have a sum.
    
    You are given that a[2] = 512 and a[10] = 614656.
    
    Find a[30].
    
    Answer: 72fddfa6c52a120892ade628f3819da4
    
"""
from common import check

PROBLEM_NUMBER = 119
ANSWER_HASH = "72fddfa6c52a120892ade628f3819da4"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
