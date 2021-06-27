"""
    Problem 398
    ===========
    
    Inside a rope of length n, n-1 points are placed with distance 1 from each
    other and from the endpoints. Among these points, we choose m-1 points at
    random and cut the rope at these points to create m segments.
    
    Let E(n, m) be the expected length of the second-shortest segment.For
    example, E(3, 2) = 2 and E(8, 3) = 16/7.Note that if multiple segments
    have the same shortest length the length of the second-shortest segment is
    defined as the same as the shortest length.
    
    Find E(10^7, 100).Give your answer rounded to 5 decimal places behind the
    decimal point.
    
    Answer: fa0a25d62fa225e05fd8736713a9bfc0
    
"""
from common import check

PROBLEM_NUMBER = 398
ANSWER_HASH = "fa0a25d62fa225e05fd8736713a9bfc0"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
