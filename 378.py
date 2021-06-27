"""
    Problem 378
    ===========
    
    Let T(n) be the n^th triangle number, so T(n) = n (n+1) .
    2
    
    Let dT(n) be the number of divisors of T(n).
    E.g.:T(7) = 28 and dT(7) = 6.
    
    Let Tr(n) be the number of triples (i, j, k) such that 1 ≤ i < j < k ≤ n
    and dT(i) > dT(j) > dT(k).
    Tr(20) = 14, Tr(100) = 5772 and Tr(1000) = 11174776.
    
    Find Tr(60 000 000).
    Give the last 18 digits of your answer.
    
    Answer: 336745dc9d90928596237c4b471a8927
    
"""
from common import check

PROBLEM_NUMBER = 378
ANSWER_HASH = "336745dc9d90928596237c4b471a8927"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
