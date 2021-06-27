"""
    Problem 386
    ===========
    
    Let n be an integer and S(n) be the set of factors of n.
    
    A subset A of S(n) is called an antichain of S(n) if A contains only one
    element or if none of the elements of A divides any of the other elements
    of A.
    
    For example: S(30) = {1, 2, 3, 5, 6, 10, 15, 30}
    {2, 5, 6} is not an antichain of S(30).
    {2, 3, 5} is an antichain of S(30).
    
    Let N(n) be the maximum length of an antichain of S(n).
    
    Find ΣN(n) for 1 ≤ n ≤ 10^8
    
    Answer: d1d893f7c50910aa10daec5e9352e86d
    
"""
from common import check

PROBLEM_NUMBER = 386
ANSWER_HASH = "d1d893f7c50910aa10daec5e9352e86d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
