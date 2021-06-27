"""
    Problem 365
    ===========
    
    The binomial coeffient C(10^18,10^9) is a number with more than 9 billion
    (9×10^9) digits.
    
    Let M(n,k,m) denote the binomial coefficient C(n,k) modulo m.
    
    Calculate ∑M(10^18,10^9,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.
    
    Answer: 53addf69042b0cefbeb94f3bd3224918
    
"""
from common import check

PROBLEM_NUMBER = 365
ANSWER_HASH = "53addf69042b0cefbeb94f3bd3224918"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
