"""
    Problem 316
    ===========
    
    Let p = p[1] p[2] p[3] ... be an infinite sequence of random digits,
    selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
    It can be seen that p corresponds to the real number 0.p[1] p[2] p[3] ....
    It can also be seen that choosing a random real number from the interval
    [0,1) is equivalent to choosing an infinite sequence of random digits
    selected from {0,1,2,3,4,5,6,7,8,9} with equal probability.
    
    For any positive integer n with d decimal digits, let k be the smallest
    index such that
    p[k, ]p[k+1], ...p[k+d-1] are the decimal digits of n, in the same order.
    Also, let g(n) be the expected value of k; it can be proven that g(n) is
    always finite and, interestingly, always an integer number.
    
    For example, if n = 535, then
    for p = 31415926535897...., we get k = 9
    for p = 355287143650049560000490848764084685354..., we get k = 36
    etc and we find that g(535) = 1008.
    
    Given that , find
    
    Note: represents the floor function.
    
    p_316_decexp1.gif
    p_316_decexp2.gif
    p_316_decexp3.gif
    Answer: 2495e8f6e9d4cdadbf0411144e7180b9
    
"""
from common import check

PROBLEM_NUMBER = 316
ANSWER_HASH = "2495e8f6e9d4cdadbf0411144e7180b9"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
