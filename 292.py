"""
    Problem 292
    ===========
    
    We shall define a pythagorean polygon to be a convex polygon with the
    following properties:
    
    • there are at least three vertices,
    • no three vertices are aligned,
    • each vertex has integer coordinates,
    • each edge has integer length.
    
    For a given integer n, define P(n) as the number of distinct pythagorean
    polygons for which the perimeter is ≤ n.
    Pythagorean polygons should be considered distinct as long as none is a
    translation of another.
    
    You are given that P(4) = 1, P(30) = 3655 and P(60) = 891045.
    Find P(120).
    
    Answer: 27f50f02ef10f170379b144435e0144b
    
"""
from common import check

PROBLEM_NUMBER = 292
ANSWER_HASH = "27f50f02ef10f170379b144435e0144b"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
