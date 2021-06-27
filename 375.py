"""
    Problem 375
    ===========
    
    Let S[n] be an integer sequence produced with the following pseudo-random
    number generator:
    
    S[0]   =[ ] 290797[ ]
    S[n+1] =[ ] S[n]^2 mod 50515093
    
    Let A(i, j) be the minimum of the numbers S[i], S[i+1], ... , S[j] for i ≤
    j.
    Let M(N) = ΣA(i, j) for 1 ≤ i ≤ j ≤ N.
    We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.
    
    Find M(2 000 000 000).
    
    Answer: 68a12e3f2e4ccbae9c8555e547fbe096
    
"""
from common import check

PROBLEM_NUMBER = 375
ANSWER_HASH = "68a12e3f2e4ccbae9c8555e547fbe096"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
