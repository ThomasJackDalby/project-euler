"""
    Problem 354
    ===========
    
    Consider a honey bee's honeycomb where each cell is a perfect regular
    hexagon with side length 1.
    
    One particular cell is occupied by the queen bee.
    For a positive real number L, let B(L) count the cells with distance L
    from the queen bee cell (all distances are measured from centre to
    centre); you may assume that the honeycomb is large enough to accommodate
    for any distance we wish to consider.
    For example, B(√3) = 6, B(√21) = 12 and B(111 111 111) = 54.
    
    Find the number of L ≤ 5·10^11 such that B(L) = 450.
    
    p_354_bee_honeycomb.png
    Answer: e36240897614dc46e83405ae8cdf198c
    
"""
from common import check

PROBLEM_NUMBER = 354
ANSWER_HASH = "e36240897614dc46e83405ae8cdf198c"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
