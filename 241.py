"""
    Problem 241
    ===========
    
    For a positive integer n, let σ(n) be the sum of all divisors of n, so
    e.g. σ(6) = 1 + 2 + 3 + 6 = 12.
    
    A perfect number, as you probably know, is a number with σ(n) = 2n.
    
    Let us define the perfection quotient of a positive integer p(n) =  σ(n) .
    as                                                                   n
    
    Find the sum of all positive integers n ≤ 10^18 for which p(n) has the
    form k + ^1⁄[2], where k is an integer.
    
    Answer: 556bfef2cacd1eff8af9126c5c13dcbc
    
"""
from common import check

PROBLEM_NUMBER = 241
ANSWER_HASH = "556bfef2cacd1eff8af9126c5c13dcbc"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
