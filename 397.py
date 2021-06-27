"""
    Problem 397
    ===========
    
    On the parabola y = x^2/k, three points A(a, a^2/k), B(b, b^2/k) and C(c,
    c^2/k) are chosen.
    
    Let F(K, X) be the number of the integer quadruplets (k, a, b, c) such
    that at least one angle of the triangle ABC is 45-degree, with 1 ≤ k ≤ K
    and -X ≤ a < b < c ≤ X.
    
    For example, F(1, 10) = 41 and F(10, 100) = 12492.
    Find F(10^6, 10^9).
    
    Answer: 07f769df9543bc05e6318878c34d074d
    
"""
from common import check

PROBLEM_NUMBER = 397
ANSWER_HASH = "07f769df9543bc05e6318878c34d074d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
