"""
    Problem 425
    ===========
    
    Two positive numbers A and B are said to be connected (denoted by "A ↔ B")
    if one of these conditions holds:
    (1) A and B have the same length and differ in exactly one digit; for
    example, 123 ↔ 173.
    (2) Adding one digit to the left of A (or B) makes B (or A); for example,
    23 ↔ 223 and 123 ↔ 23.
    
    We call a prime P a 2's relative if there exists a chain of connected
    primes between 2 and P and no prime in the chain exceeds P.
    
    For example, 127 is a 2's relative. One of the possible chains is shown
    below:
    2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
    However, 11 and 103 are not 2's relatives.
    
    Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
    We can verify that F(10^3) = 431 and F(10^4) = 78728.
    
    Find F(10^7).
    
    Answer: 3d229894ba4c585138125e802af2d06e
    
"""
from common import check

PROBLEM_NUMBER = 425
ANSWER_HASH = "3d229894ba4c585138125e802af2d06e"

check(None, PROBLEM_NUMBER, ANSWER_HASH)