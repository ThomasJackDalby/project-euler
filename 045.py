"""
    Problem 45
    ==========
    
    Triangle, pentagonal, and hexagonal numbers are generated by the following
    formulae:
    
    Triangle     T[n]=n(n+1)/2    1, 3, 6, 10, 15, ...
    Pentagonal   P[n]=n(3n−1)/2   1, 5, 12, 22, 35, ...
    Hexagonal    H[n]=n(2n−1)     1, 6, 15, 28, 45, ...
    
    It can be verified that T[285] = P[165] = H[143] = 40755.
    
    Find the next triangle number that is also pentagonal and hexagonal.
    
    Answer: 30dfe3e3b286add9d12e493ca7be63fc
    
"""
from common import check

PROBLEM_NUMBER = 45
ANSWER_HASH = "30dfe3e3b286add9d12e493ca7be63fc"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
