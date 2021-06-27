"""
    Problem 433
    ===========
    
    Let E(x[0], y[0]) be the number of steps it takes to determine the
    greatest common divisor of x[0] and y[0] with Euclid's algorithm. More
    formally:
    x[1] = y[0], y[1] = x[0] mod y[0]
    x[n] = y[n-1], y[n] = x[n-1] mod y[n-1]
    E(x[0], y[0]) is the smallest n such that y[n] = 0.
    
    We have E(1,1) = 1, E(10,6) = 3 and E(6,10) = 4.
    
    Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
    We have S(1) = 1, S(10) = 221 and S(100) = 39826.
    
    Find S(5·10^6).
    
    Answer: 0eeca9fa5cf25a2bfae01f1f04d6cd35
    
"""
from common import check

PROBLEM_NUMBER = 433
ANSWER_HASH = "0eeca9fa5cf25a2bfae01f1f04d6cd35"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
