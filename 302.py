"""
    Problem 302
    ===========
    
    A positive integer n is powerful if p^2 is a divisor of n for every prime
    factor p in n.
    
    A positive integer n is a perfect power if n can be expressed as a power
    of another positive integer.
    
    A positive integer n is an Achilles number if n is powerful but not a
    perfect power. For example, 864 and 1800 are Achilles numbers: 864 =
    2^5·3^3 and 1800 = 2^3·3^2·5^2.
    
    We shall call a positive integer S a Strong Achilles number if both S and
    φ(S) are Achilles numbers.^1
    For example, 864 is a Strong Achilles number: φ(864) = 288 = 2^5·3^2.
    However, 1800 isn't a Strong Achilles number because: φ(1800) = 480 =
    2^5·3^1·5^1.
    
    There are 7 Strong Achilles numbers below 10^4 and 656 below 10^8.
    
    How many Strong Achilles numbers are there below 10^18?
    
    ^1 φ denotes Euler's totient function.
    
    Answer: 1ea8b8d64cead5149721a128b0de378c
    
"""
from common import check

PROBLEM_NUMBER = 302
ANSWER_HASH = "1ea8b8d64cead5149721a128b0de378c"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
