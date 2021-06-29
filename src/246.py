"""
    Problem 246
    ===========
    
    A definition for an ellipse is:
    Given a circle c with centre M and radius r and a point G such that
    d(G,M)<r, the locus of the points that are equidistant from c and G form
    an ellipse.
    
    The construction of the points of the ellipse is shown below.
    
    Given are the points M(-2000,1500) and G(8000,1500).
    Given is also the circle c with centre M and radius 15000.
    The locus of the points that are equidistant from G and c form an ellipse
    e.
    From a point P outside e the two tangents t[1] and t[2] to the ellipse are
    drawn.
    Let the points where t[1] and t[2] touch the ellipse be R and S.
    
    For how many lattice points P is angle RPS greater than 45 degrees?
    
    p_246_anim.gif
    p_246_ellipse.gif
    Answer: 94c521ffeb906391d161b66fec433827
    
"""
from common import check

PROBLEM_NUMBER = 246
ANSWER_HASH = "94c521ffeb906391d161b66fec433827"

check(None, PROBLEM_NUMBER, ANSWER_HASH)