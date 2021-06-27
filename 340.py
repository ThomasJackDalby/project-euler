"""
    Problem 340
    ===========
    
    For fixed integers a, b, c, define the crazy function F(n) as follows:
    F(n) = n - c for all n > b
    F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.
    
    Also, define S(a, b, c) = .
    
    For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000)
    = 2040.
    Also, S(50, 2000, 40) = 5204240.
    
    Find the last 9 digits of S(21^7, 7^21, 12^7).
    
    p_340_formula.gif
    Answer: fc838afe9ecde39bbe230923d7b50775
    
"""
from common import check

PROBLEM_NUMBER = 340
ANSWER_HASH = "fc838afe9ecde39bbe230923d7b50775"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
