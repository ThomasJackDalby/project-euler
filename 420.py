"""
    Problem 420
    ===========
    
    A positive integer matrix is a matrix whose elements are all positive
    integers.
    Some positive integer matrices can be expressed as a square of a positive
    integer matrix in two different ways. Here is an example:
    
    We define F(N) as the number of the 2x2 positive integer matrices which
    have a trace less than N and which can be expressed as a square of a
    positive integer matrix in two different ways.
    We can verify that F(50) = 7 and F(1000) = 1019.
    
    Find F(10^7).
    
    p_420_matrix.gif
    Answer: e265e34e34fc54e8ceecd5e4b94b1381
    
"""
from common import check

PROBLEM_NUMBER = 420
ANSWER_HASH = "e265e34e34fc54e8ceecd5e4b94b1381"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
