"""
    Problem 138
    ===========
    
    Consider the isosceles triangle with base length, b = 16, and legs, L =
    17.
    
    By using the Pythagorean theorem it can be seen that the height of the
    triangle, h = √(17^2 − 8^2) = 15, which is one less than the base length.
    
    With b = 272 and L = 305, we get h = 273, which is one more than the base
    length, and this is the second smallest isosceles triangle with the
    property that h = b ± 1.
    
    Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1
    and b, L are positive integers.
    
    p_138.gif
    Answer: f7524f4d0d6d042c0f92a0d6469aff85
    
"""
from common import check

PROBLEM_NUMBER = 138
ANSWER_HASH = "f7524f4d0d6d042c0f92a0d6469aff85"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
