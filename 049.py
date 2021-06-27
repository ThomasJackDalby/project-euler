"""
    Problem 49
    ==========
    
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.
    
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.
    
    What 12-digit number do you form by concatenating the three terms in this
    sequence?
    
    Answer: 0b99933d3e2a9addccbb663d46cbb592
    
"""
from common import check

PROBLEM_NUMBER = 49
ANSWER_HASH = "0b99933d3e2a9addccbb663d46cbb592"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
