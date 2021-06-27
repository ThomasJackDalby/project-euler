"""
    Problem 233
    ===========
    
    Let f(N) be the number of points with integer coordinates that are on a
    circle passing through (0,0), (N,0),(0,N), and (N,N).
    
    It can be shown that f(10000) = 36.
    
    What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
    
    Answer: 7e80b27798170abb493e3b4671bd82ca
    
"""
from common import check

PROBLEM_NUMBER = 233
ANSWER_HASH = "7e80b27798170abb493e3b4671bd82ca"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
