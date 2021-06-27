"""
    Problem 360
    ===========
    
    Given two points (x[1],y[1],z[1]) and (x[2],y[2],z[2]) in three
    dimensional space, the Manhattan distance between those points is defined
    as
    |x[1]-x[2]|+|y[1]-y[2]|+|z[1]-z[2]|.
    
    Let C(r) be a sphere with radius r and center in the origin O(0,0,0).
    Let I(r) be the set of all points with integer coordinates on the surface
    of C(r).
    Let S(r) be the sum of the Manhattan distances of all elements of I(r) to
    the origin O.
    
    E.g. S(45)=34518.
    
    Find S(10^10).
    
    Answer: 82ec91527315eafb7e3acc139eeeb8eb
    
"""
from common import check

PROBLEM_NUMBER = 360
ANSWER_HASH = "82ec91527315eafb7e3acc139eeeb8eb"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
