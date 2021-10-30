"""
    Problem 92
    ==========
    
    A number chain is created by continuously adding the square of the digits
    in a number to form a new number until it has been seen before.
    
    For example,
    
    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
    
    Therefore any chain that arrives at 1 or 89 will become stuck in an
    endless loop. What is most amazing is that EVERY starting number will
    eventually arrive at 1 or 89.
    
    How many starting numbers below ten million will arrive at 89?
    
    Answer: 6cee918c0612bccc2dac03d05e07035f
    
"""
from common import check

PROBLEM_NUMBER = 92
ANSWER_HASH = "6cee918c0612bccc2dac03d05e07035f"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
