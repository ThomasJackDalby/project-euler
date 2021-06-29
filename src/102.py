"""
    Problem 102
    ===========
    
    Three distinct points are plotted at random on a Cartesian plane, for
    which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
    
    Consider the following two triangles:
    
    A(-340,495), B(-153,-910), C(835,-947)
    
    X(-175,41), Y(-421,-714), Z(574,-645)
    
    It can be verified that triangle ABC contains the origin, whereas triangle
    XYZ does not.
    
    Using [1]triangles.txt, a 27K text file containing the co-ordinates of one
    thousand "random" triangles, find the number of triangles for which the
    interior contains the origin.
    
    NOTE: The first two examples in the file represent the triangles in the
    example given above.
    
    Visible links
    1. triangles.txt
    Answer: 74db120f0a8e5646ef5a30154e9f6deb
    
"""
from common import check

PROBLEM_NUMBER = 102
ANSWER_HASH = "74db120f0a8e5646ef5a30154e9f6deb"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
