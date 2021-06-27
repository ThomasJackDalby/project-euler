"""
    Problem 418
    ===========
    
    Let n be a positive integer. An integer triple (a, b, c) is called a
    factorisation triple of n if:
    
    • 1 ≤ a ≤ b ≤ c
    • a·b·c = n.
    
    Define f(n) to be a + b + c for the factorisation triple (a, b, c) of n
    which minimises c / a. One can show that this triple is unique.
    
    For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.
    
    Find f(43!).
    
    Answer: b032468ddb4847d8a2273789379753f5
    
"""
from common import check

PROBLEM_NUMBER = 418
ANSWER_HASH = "b032468ddb4847d8a2273789379753f5"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
