"""
    Problem 372
    ===========
    
    Let R(M, N) be the number of lattice points (x, y) which satisfy M<x≤N,
    M<y≤N and is odd.
    We can verify that R(0, 100) = 3019 and R(100, 10000) = 29750422.
    Find R(2·10^6, 10^9).
    
    Note: represents the floor function.
    
    p_372_pencilray1.jpg
    p_372_pencilray2.gif
    Answer: 5fdeda0dca23d12ae3eb1763b2c6f5ea
    
"""
from common import check

PROBLEM_NUMBER = 372
ANSWER_HASH = "5fdeda0dca23d12ae3eb1763b2c6f5ea"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
