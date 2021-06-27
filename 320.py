"""
    Problem 320
    ===========
    
    Let N(i) be the smallest integer n such that n! is divisible by
    (i!)^1234567890
    
    Let S(u)=∑N(i) for 10 ≤ i ≤ u.
    
    S(1000)=614538266565663.
    
    Find S(1 000 000) mod 10^18.
    
    Answer: 8426f939c3ee410a8c4d43886ef77ccb
    
"""
from common import check

PROBLEM_NUMBER = 320
ANSWER_HASH = "8426f939c3ee410a8c4d43886ef77ccb"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
