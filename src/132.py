"""
    Problem 132
    ===========
    
    A number consisting entirely of ones is called a repunit. We shall define
    R(k) to be a repunit of length k.
    
    For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these
    prime factors is 9414.
    
    Find the sum of the first forty prime factors of R(10^9).
    
    Answer: 5df3a36faa173a393a04a022b2d5d49d
    
"""
from common import check

PROBLEM_NUMBER = 132
ANSWER_HASH = "5df3a36faa173a393a04a022b2d5d49d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)