"""
    Problem 388
    ===========
    
    Consider all lattice points (a,b,c) with 0 ≤ a,b,c ≤ N.
    
    From the origin O(0,0,0) all lines are drawn to the other lattice points.
    Let D(N) be the number of distinct such lines.
    
    You are given that D(1 000 000) = 831909254469114121.
    
    Find D(10^10). Give as your answer the first nine digits followed by the
    last nine digits.
    
    Answer: 2bab886c7d98d802d9249c9e12d72c25
    
"""
from common import check

PROBLEM_NUMBER = 388
ANSWER_HASH = "2bab886c7d98d802d9249c9e12d72c25"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
