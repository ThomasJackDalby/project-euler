"""
    Problem 86
    ==========
    
    A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
    and a fly, F, sits in the opposite corner. By travelling on the surfaces
    of the room the shortest "straight line" distance from S to F is 10 and
    the path is shown on the diagram.
    
    However, there are up to three "shortest" path candidates for any given
    cuboid and the shortest route doesn't always have integer length.
    
    By considering all cuboid rooms with integer dimensions, up to a maximum
    size of M by M by M, there are exactly 2060 cuboids for which the shortest
    route has integer length when M=100, and this is the least value of M for
    which the number of solutions first exceeds two thousand; the number of
    solutions is 1975 when M=99.
    
    Find the least value of M such that the number of solutions first exceeds
    one million.
    
    p_086.gif
    Answer: f5c3dd7514bf620a1b85450d2ae374b1
    
"""
from common import check

PROBLEM_NUMBER = 86
ANSWER_HASH = "f5c3dd7514bf620a1b85450d2ae374b1"

check(None, PROBLEM_NUMBER, ANSWER_HASH)