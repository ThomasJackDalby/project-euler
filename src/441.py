"""
    Problem 441
    ===========
    
    For an integer M, we define R(M) as the sum of 1/(p·q) for all the integer
    pairs p and q which satisfy all of these conditions:
    
    • 1 ≤ p < q ≤ M
    • p + q ≥ M
    • p and q are coprime.
    
    We also define S(N) as the sum of R(i) for 2 ≤ i ≤ N.
    We can verify that S(2) = R(2) = 1/2, S(10) ≈ 6.9147 and S(100) ≈ 58.2962.
    
    Find S(10^7). Give your answer rounded to four decimal places.
    
    Answer: 152cc265f5461c5055db95a122280416
    
"""
from common import check

PROBLEM_NUMBER = 441
ANSWER_HASH = "152cc265f5461c5055db95a122280416"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
