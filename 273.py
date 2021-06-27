"""
    Problem 273
    ===========
    
    Consider equations of the form: a^2 + b^2 = N, 0 ≤ a ≤ b, a, b and N
    integer.
    
    For N=65 there are two solutions:
    
    a=1, b=8 and a=4, b=7.
    
    We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N,
    0 ≤ a ≤ b, a, b and N integer.
    
    Thus S(65) = 1 + 4 = 5.
    
    Find ∑S(N), for all squarefree N only divisible by primes of the form 4k+1
    with 4k+1 < 150.
    
    Answer: 2b03731e58e9d60e559ee5fdce4f0d14
    
"""
from common import check

PROBLEM_NUMBER = 273
ANSWER_HASH = "2b03731e58e9d60e559ee5fdce4f0d14"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
