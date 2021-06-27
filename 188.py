"""
    Problem 188
    ===========
    
    The hyperexponentiation or tetration of a number a by a positive integer
    b, denoted by a↑↑b or ^ba, is recursively defined by:
    
    a↑↑1 = a,
    a↑↑(k+1) = a^(a↑↑k).
    
    Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and
    3↑↑4 is roughly 10^3.6383346400240996*10^12.
    
    Find the last 8 digits of 1777↑↑1855.
    
    Answer: 62746b4d40a2b87c3dd6caee5d33e6a1
    
"""
from common import check

PROBLEM_NUMBER = 188
ANSWER_HASH = "62746b4d40a2b87c3dd6caee5d33e6a1"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
