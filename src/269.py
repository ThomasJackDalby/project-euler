"""
    Problem 269
    ===========
    
    A root or zero of a polynomial P(x) is a solution to the equation P(x) =
    0.
    Define P[n] as the polynomial whose coefficients are the digits of n.
    For example, P[5703](x) = 5x^3 + 7x^2 + 3.
    
    We can see that:
    
    • P[n](0) is the last digit of n,
    • P[n](1) is the sum of the digits of n,
    • P[n](10) is n itself.
    
    Define Z(k) as the number of positive integers, n, not exceeding k for
    which the polynomial P[n] has at least one integer root.
    
    It can be verified that Z(100 000) is 14696.
    
    What is Z(10^16)?
    
    Answer: f7ba868cb52a9b9c7e58b1b92e230be8
    
"""
from common import check

PROBLEM_NUMBER = 269
ANSWER_HASH = "f7ba868cb52a9b9c7e58b1b92e230be8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
