"""
    Problem 87
    ==========
    
    The smallest number expressible as the sum of a prime square, prime cube,
    and prime fourth power is 28. In fact, there are exactly four numbers
    below fifty that can be expressed in such a way:
    
    28 = 2^2 + 2^3 + 2^4
    33 = 3^2 + 2^3 + 2^4
    49 = 5^2 + 2^3 + 2^4
    47 = 2^2 + 3^3 + 2^4
    
    How many numbers below fifty million can be expressed as the sum of a
    prime square, prime cube, and prime fourth power?
    
    Answer: e7fb7907f1af626cc42e787e367ec602
    
"""
from common import check

PROBLEM_NUMBER = 87
ANSWER_HASH = "e7fb7907f1af626cc42e787e367ec602"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
