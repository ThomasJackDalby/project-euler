"""
    Problem 404
    ===========
    
    E[a] is an ellipse with an equation of the form x^2 + 4y^2 = 4a^2.
    E[a]' is the rotated image of E[a] by θ degrees counterclockwise around
    the origin O(0, 0) for 0° < θ < 90°.
    
    b is the distance to the origin of the two intersection points closest to
    the origin and c is the distance of the two other intersection points.
    We call an ordered triplet (a, b, c) a canonical ellipsoidal triplet if a,
    b and c are positive integers.
    For example, (209, 247, 286) is a canonical ellipsoidal triplet.
    
    Let C(N) be the number of distinct canonical ellipsoidal triplets (a, b,
    c) for a ≤ N.
    It can be verified that C(10^3) = 7, C(10^4) = 106 and C(10^6) = 11845.
    
    Find C(10^17).
    
    p_404_c_ellipse.gif
    Answer: 2d1bc4b93bbc19d9e70c5b04338dea2e
    
"""
from common import check

PROBLEM_NUMBER = 404
ANSWER_HASH = "2d1bc4b93bbc19d9e70c5b04338dea2e"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
