"""
    Problem 370
    ===========
    
    Let us define a geometric triangle as an integer sided triangle with sides
    a ≤ b ≤ c so that its sides form a geometric progression, i.e.
    b^2 = a · c .
    
    An example of such a geometric triangle is the triangle with sides a =
    144, b = 156 and c = 169.
    
    There are 861805 geometric triangles with perimeter ≤ 10^6 .
    
    How many geometric triangles exist with perimeter ≤ 2.5·10^13 ?
    
    Answer: 85b5048e25677205555a5308991c2e04
    
"""
from common import check

PROBLEM_NUMBER = 370
ANSWER_HASH = "85b5048e25677205555a5308991c2e04"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
