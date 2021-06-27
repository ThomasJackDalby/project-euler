"""
    Problem 346
    ===========
    
    The number 7 is special, because 7 is 111 written in base 2, and 11
    written in base 6
    (i.e. 7[10] = 11[6] = 111[2]). In other words, 7 is a repunit in at least
    two bases b > 1.
    
    We shall call a positive integer with this property a strong repunit. It
    can be verified that there are 8 strong repunits below 50:
    {1,7,13,15,21,31,40,43}.
    Furthermore, the sum of all strong repunits below 1000 equals 15864.
    
    Find the sum of all strong repunits below 10^12.
    
    Answer: a17874b5a9ec9d7fc8c6489ab8ff29b9
    
"""
from common import check

PROBLEM_NUMBER = 346
ANSWER_HASH = "a17874b5a9ec9d7fc8c6489ab8ff29b9"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
