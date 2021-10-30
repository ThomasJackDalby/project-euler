"""
    Problem 409
    ===========
    
    Let n be a positive integer. Consider nim positions where:
    
    • There are n non-empty piles.
    • Each pile has size less than 2^n.
    • No two piles have the same size.
    
    Let W(n) be the number of winning nim positions satisfying the
    aboveconditions (a position is winning if the first player has a winning
    strategy). For example, W(1) = 1, W(2) = 6, W(3) = 168, W(5) = 19764360
    and W(100) mod 1 000 000 007 = 384777056.
    
    Find W(10 000 000) mod 1 000 000 007.
    
    Answer: 56c32e75a2656ec08ce177089bda2f53
    
"""
from common import check

PROBLEM_NUMBER = 409
ANSWER_HASH = "56c32e75a2656ec08ce177089bda2f53"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
