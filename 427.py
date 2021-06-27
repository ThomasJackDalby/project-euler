"""
    Problem 427
    ===========
    
    A sequence of integers S = {s[i]} is called an n-sequence if it has n
    elements and each element s[i] satisfies 1 ≤ s[i] ≤ n. Thus there are n^n
    distinct n-sequences in total.For example, the sequence S = {1, 5, 5, 10,
    7, 7, 7, 2, 3, 7} is a 10-sequence.
    
    For any sequence S, let L(S) be the length of the longest contiguous
    subsequence of S with the same value.For example, for the given sequence S
    above, L(S) = 3, because of the three consecutive 7's.
    
    Let f(n) = ∑ L(S) for all n-sequences S.
    
    For example, f(3) = 45, f(7) = 1403689 and f(11) = 481496895121.
    
    Find f(7 500 000) mod 1 000 000 009.
    
    Answer: ecb4da2c940b517c63d8d256814dd511
    
"""
from common import check

PROBLEM_NUMBER = 427
ANSWER_HASH = "ecb4da2c940b517c63d8d256814dd511"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
