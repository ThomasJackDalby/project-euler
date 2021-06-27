"""
    Problem 432
    ===========
    
    Let S(n,m) = ∑φ(n × i) for 1 ≤ i ≤ m. (φ is Euler's totient function)
    You are given that S(510510,10^6 )= 45480596821125120.
    
    Find S(510510,10^11).
    Give the last 9 digits of your answer.
    
    Answer: e171c2872d650e47589842faa80f5707
    
"""
from common import check

PROBLEM_NUMBER = 432
ANSWER_HASH = "e171c2872d650e47589842faa80f5707"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
