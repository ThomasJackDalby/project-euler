"""
    Problem 190
    ===========
    
    Let S[m] = (x[1], x[2], ... , x[m]) be the m-tuple of positive real
    numbers with x[1] + x[2] + ... + x[m] = m for which P[m] = x[1] * x[2]^2 *
    ... * x[m]^m is maximised.
    
    For example, it can be verified that [P[10]] = 4112 ([ ] is the integer
    part function).
    
    Find Σ[P[m]] for 2 ≤ m ≤ 15.
    
    Answer: 40cfcabd9b30d79ec81151fc756e9946
    
"""
from common import check

PROBLEM_NUMBER = 190
ANSWER_HASH = "40cfcabd9b30d79ec81151fc756e9946"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
