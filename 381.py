"""
    Problem 381
    ===========
    
    For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.
    
    For example, if p=7,
    (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! =
    720+120+24+6+2 = 872.
    As 872 mod(7) = 4, S(7) = 4.
    
    It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.
    
    Find ∑S(p) for 5 ≤ p < 10^8.
    
    Answer: 80c84973a9643e46d49d79d7284e7ff3
    
"""
from common import check

PROBLEM_NUMBER = 381
ANSWER_HASH = "80c84973a9643e46d49d79d7284e7ff3"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
