"""
    Problem 266
    ===========
    
    The divisors of 12 are: 1,2,3,4,6 and 12.
    The largest divisor of 12 that does not exceed the square root of 12 is 3.
    We shall call the largest divisor of an integer n that does not exceed the
    square root of n the pseudo square root (PSR) of n.
    It can be seen that PSR(3102)=47.
    
    Let p be the product of the primes below 190.
    Find PSR(p) mod 10^16.
    
    Answer: 32da1d501e539ab509f104e2db68d57a
    
"""
from common import check

PROBLEM_NUMBER = 266
ANSWER_HASH = "32da1d501e539ab509f104e2db68d57a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
