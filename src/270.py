"""
    Problem 270
    ===========
    
    A square piece of paper with integer dimensions N×N is placed with a
    corner at the origin and two of its sides along the x- and y-axes. Then,
    we cut it up respecting the following rules:
    
    • We only make straight cuts between two points lying on different sides
    of the square, and having integer coordinates.
    • Two cuts cannot cross, but several cuts can meet at the same border
    point.
    • Proceed until no more legal cuts can be made.
    
    Counting any reflections or rotations as distinct, we call C(N) the number
    of ways to cut an N×N square. For example, C(1) = 2 and C(2) = 30 (shown
    below).
    
    What is C(30) mod 10^8 ?
    
    p_270_CutSquare.gif
    Answer: 2a592dfd1e9e3e9e38578affa7c72605
    
"""
from common import check

PROBLEM_NUMBER = 270
ANSWER_HASH = "2a592dfd1e9e3e9e38578affa7c72605"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
