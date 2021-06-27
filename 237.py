"""
    Problem 237
    ===========
    
    Let T(n) be the number of tours over a 4 × n playing board such that:
    
    • The tour starts in the top left corner.
    • The tour consists of moves that are up, down, left, or right one
    square.
    • The tour visits each square exactly once.
    • The tour ends in the bottom left corner.
    
    The diagram shows one tour over a 4 × 10 board:
    
    T(10) is 2329. What is T(10^12) modulo 10^8?
    
    p_237.gif
    Answer: 0742988a3948491b15fb48e476c78a6a
    
"""
from common import check

PROBLEM_NUMBER = 237
ANSWER_HASH = "0742988a3948491b15fb48e476c78a6a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
