"""
    Problem 337
    ===========
    
    Let {a[1], a[2],..., a[n]} be an integer sequence of length n such that:
    
    • a[1] = 6
    • for all 1 ≤ i < n : φ(a[i]) < φ(a[i+1]) < a[i] < a[i+1] ^1
    
    Let S(N) be the number of such sequences with a[n] ≤ N.
    For example, S(10) = 4: {6}, {6, 8}, {6, 8, 9} and {6, 10}.
    We can verify that S(100) = 482073668 and S(10 000) mod 10^8 = 73808307.
    
    Find S(20 000 000) mod 10^8.
    
    ^1 φ denotes Euler's totient function.
    
    Answer: a60bbbe1b90254043fb92820492a2f96
    
"""
from common import check

PROBLEM_NUMBER = 337
ANSWER_HASH = "a60bbbe1b90254043fb92820492a2f96"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
