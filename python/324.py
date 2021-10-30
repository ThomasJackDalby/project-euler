"""
    Problem 324
    ===========
    
    Let f(n) represent the number of ways one can fill a 3×3×n tower with
    blocks of 2×1×1.
    You're allowed to rotate the blocks in any way you like; however,
    rotations, reflections etc of the tower itself are counted as distinct.
    
    For example (with q = 100000007) :
    f(2) = 229,
    f(4) = 117805,
    f(10) mod q = 96149360,
    f(10^3) mod q = 24806056,
    f(10^6) mod q = 30808124.
    
    Find f(10^10000) mod 100000007.
    
    Answer: b8d91b06d43a2ef98a6fcb0be4a6d617
    
"""
from common import check

PROBLEM_NUMBER = 324
ANSWER_HASH = "b8d91b06d43a2ef98a6fcb0be4a6d617"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
