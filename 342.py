"""
    Problem 342
    ===========
    
    Consider the number 50.
    50^2 = 2500 = 2^2 × 5^4, so φ(2500) = 2 × 4 × 5^3 = 8 × 5^3 = 2^3 × 5^3.
    ^1
    So 2500 is a square and φ(2500) is a cube.
    
    Find the sum of all numbers n, 1 < n < 10^10 such that φ(n^2) is a cube.
    
    ^1 φ denotes Euler's totient function.
    
    Answer: 0e9add0383d4116c7c5cb3dc73fc0536
    
"""
from common import check

PROBLEM_NUMBER = 342
ANSWER_HASH = "0e9add0383d4116c7c5cb3dc73fc0536"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
