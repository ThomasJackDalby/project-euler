"""
    Problem 402
    ===========
    
    It can be shown that the polynomial n^4 + 4n^3 + 2n^2 + 5n is a multiple
    of 6 for every integer n. It can also be shown that 6 is the largest
    integer satisfying this property.
    
    Define M(a, b, c) as the maximum m such that n^4 + an^3 + bn^2 + cn is a
    multiple of m for all integers n. For example, M(4, 2, 5) = 6.
    
    Also, define S(N) as the sum of M(a, b, c) for all 0 < a, b, c ≤ N.
    
    We can verify that S(10) = 1972 and S(10000) = 2024258331114.
    
    Let F[k] be the Fibonacci sequence:
    F[0] = 0, F[1] = 1 and
    F[k] = F[k-1] + F[k-2] for k ≥ 2.
    
    Find the last 9 digits of Σ S(F[k]) for 2 ≤ k ≤ 1234567890123.
    
    Answer: fa7ae8e9243f01b0eac10ec5aaff1f42
    
"""
from common import check

PROBLEM_NUMBER = 402
ANSWER_HASH = "fa7ae8e9243f01b0eac10ec5aaff1f42"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
