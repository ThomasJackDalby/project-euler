"""
    Problem 469
    ===========
    
    In a room N chairs are placed around a round table.
    Knights enter the room one by one and choose at random an available empty
    chair.
    To have enough elbow room the knights always leave at least one empty
    chair between each other.
    
    When there aren't any suitable chairs left, the fraction C of empty chairs
    is determined.
    We also define E(N) as the expected value of C.
    We can verify that E(4) = 1/2 and E(6) = 5/9.
    
    Find E(10^18). Give your answer rounded to fourteen decimal places in the
    form 0.abcdefghijklmn.
    
    Answer: 3c2b641262880db5b735cfa4d4c957bc
    
"""
from common import check

PROBLEM_NUMBER = 469
ANSWER_HASH = "3c2b641262880db5b735cfa4d4c957bc"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
