"""
    Problem 275
    ===========
    
    Let us define a balanced sculpture of order n as follows:
    
    • A polyomino made up of n+1 tiles known as the blocks (n tiles)
    and the plinth (remaining tile);
    • the plinth has its centre at position (x = 0, y = 0);
    • the blocks have y-coordinates greater than zero (so the plinth is the
    unique lowest tile);
    • the centre of mass of all the blocks, combined, has x-coordinate equal
    to zero.
    
    When counting the sculptures, any arrangements which are simply
    reflections about the y-axis, are not counted as distinct. For example,
    the 18 balanced sculptures of order 6 are shown below; note that each pair
    of mirror images (about the y-axis) is counted as one sculpture:
    
    There are 964 balanced sculptures of order 10 and 360505 of order 15.
    How many balanced sculptures are there of order 18?
    
    p_275_sculptures2.gif
    Answer: a2a192f9790dcbfe4b450a82c4461d4a
    
"""
from common import check

PROBLEM_NUMBER = 275
ANSWER_HASH = "a2a192f9790dcbfe4b450a82c4461d4a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
