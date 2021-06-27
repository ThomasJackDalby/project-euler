"""
    Problem 422
    ===========
    
    Let H be the hyperbola defined by the equation 12x^2 + 7xy - 12y^2 = 625.
    
    Next, define X as the point (7, 1). It can be seen that X is in H.
    
    Now we define a sequence of points in H, {P[i] : i ≥ 1}, as:
    
    • P[1] = (13, 61/4).
    • P[2] = (-43/6, -4).
    • For i > 2, P[i] is the unique point in H that is different from P[i-1]
    and such that line P[i]P[i-1] is parallel to line P[i-2]X. It can be
    shown that P[i] is well-defined, and that its coordinates are always
    rational.
    
    You are given that P[3] = (-19/2, -229/24), P[4] = (1267/144, -37/12) and
    P[7] = (17194218091/143327232, 274748766781/1719926784).
    
    Find P[n] for n = 11^14 in the following format:
    If P[n] = (a/b, c/d) where the fractions are in lowest terms and the
    denominators are positive, then the answer is (a + b + c + d) mod
    1 000 000 007.
    
    For n = 7, the answer would have been: 806236837.
    
    Answer: 7034610688a8851f742f912143c1becf
    
"""
from common import check

PROBLEM_NUMBER = 422
ANSWER_HASH = "7034610688a8851f742f912143c1becf"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
