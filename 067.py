"""
    Problem 67
    ==========
    
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
    
    3
    7 4
    2 4 6
    8 5 9 3
    
    That is, 3 + 7 + 4 + 9 = 23.
    
    Find the maximum total from top to bottom in [1]triangle.txt, a 15K text
    file containing a triangle with one-hundred rows.
    
    NOTE: This is a much more difficult version of [2]Problem 18. It is not
    possible to try every route to solve this problem, as there are 2^99
    altogether! If you could check one trillion (10^12) routes every second it
    would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)
    
    Visible links
    1. triangle.txt
    2. problem=18
    Answer: 9d702ffd99ad9c70ac37e506facc8c38
    
"""
from common import check

PROBLEM_NUMBER = 67
ANSWER_HASH = "9d702ffd99ad9c70ac37e506facc8c38"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
