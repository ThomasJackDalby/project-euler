"""
    Problem 228
    ===========
    
    Let S[n] be the regular n-sided polygon – or shape – whose vertices v[k]
    (k = 1,2,…,n) have coordinates:
    
    x[k]   =   cos( ^2k-1/[n] ×180° )
    y[k]   =   sin( ^2k-1/[n] ×180° )
    
    Each S[n] is to be interpreted as a filled shape consisting of all points
    on the perimeter and in the interior.
    
    The Minkowski sum, S+T, of two shapes S and T is the result of adding
    every point in S to every point in T, where point addition is performed
    coordinate-wise: (u, v) + (x, y) = (u+x, v+y).
    
    For example, the sum of S[3] and S[4] is the six-sided shape shown in pink
    below:
    
    [1]picture showing S_3 + S_4
    
    How many sides does S[1864] + S[1865] + … + S[1909] have?
    
    Visible links
    p_228.png
    Answer: 35d0195ddaf58e52e12400de1c9333d8
    
"""
from common import check

PROBLEM_NUMBER = 228
ANSWER_HASH = "35d0195ddaf58e52e12400de1c9333d8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
