# Completed
"""
    Problem 28
    ==========
    
    
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:
    
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    
    It can be verified that the sum of the numbers on the diagonals is 101.
    
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
    
    
    Answer: 0d53425bd7c5bf9919df3718c8e49fa6
"""
from common import check
from functools import cache

PROBLEM_NUMBER = 28
ANSWER_HASH = "0d53425bd7c5bf9919df3718c8e49fa6"
EDGE_SIZE = 1001

@cache
def get_square(n):
    if n == 1:
        return 1, 1, 1, 1
    else:
        edge = 2 * (n - 1)
        inside_square = get_square(n-1)
        a = inside_square[3] + edge
        b = a + edge
        c = b + edge
        end = c + edge

        return a, b, c, end

N = (EDGE_SIZE + 1) // 2
result = sum(sum(get_square(n)) for n in range(2, N+1)) + 1

check(result, PROBLEM_NUMBER, ANSWER_HASH)
