"""
    Problem 215
    ===========
    
    Consider the problem of building a wall out of 2×1 and 3×1 bricks
    (horizontal×vertical dimensions) such that, for extra strength, the gaps
    between horizontally-adjacent bricks never line up in consecutive layers,
    i.e. never form a "running crack".
    
    For example, the following 9×3 wall is not acceptable due to the running
    crack shown in red:
    
    There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.
    
    Calculate W(32,10).
    
    p_215_crackfree.gif
    Answer: 60212c9ec4a6cd1d14277c32b6adf2d8
    
"""
from common import check

PROBLEM_NUMBER = 215
ANSWER_HASH = "60212c9ec4a6cd1d14277c32b6adf2d8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
