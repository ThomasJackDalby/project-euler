"""
    Problem 235
    ===========
    
    Given is the arithmetic-geometric sequence u(k) = (900-3k)r^k-1.
    Let s(n) = Σ[k=1...n]u(k).
    
    Find the value of r for which s(5000) = -600,000,000,000.
    
    Give your answer rounded to 12 places behind the decimal point.
    
    Answer: 41b13508789be1001308e065d4f83ea2
    
"""
from common import check

PROBLEM_NUMBER = 235
ANSWER_HASH = "41b13508789be1001308e065d4f83ea2"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
