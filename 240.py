"""
    Problem 240
    ===========
    
    There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can
    be rolled so that the top three sum to 15. Some examples are:
    
    D[1],D[2],D[3],D[4],D[5] = 4,3,6,3,5
    D[1],D[2],D[3],D[4],D[5] = 4,3,3,5,6
    D[1],D[2],D[3],D[4],D[5] = 3,3,3,6,6
    D[1],D[2],D[3],D[4],D[5] = 6,6,3,3,3
    
    In how many ways can twenty 12-sided dice (sides numbered 1 to 12) be
    rolled so that the top ten sum to 70?
    
    Answer: cb31a3106db3876e77cd160664cd683e
    
"""
from common import check

PROBLEM_NUMBER = 240
ANSWER_HASH = "cb31a3106db3876e77cd160664cd683e"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
