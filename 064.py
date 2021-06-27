"""
    Problem 64
    ==========
    
    All square roots are periodic when written as continued fractions and can
    be written in the form:
    
    √N = a[0] +            1
    a[1] +         1
    a[2] +     1
    a[3] + ...
    
    For example, let us consider √23:
    
    √23 = 4 + √23 — 4 = 4 +    1    = 4 +       1
    1           1 +  √23 – 3
    √23—4                 7
    
    If we continue we would get the following expansion:
    
    √23 = 4 +          1
    1 +        1
    3 +      1
    1 +    1
    8 + ...
    
    The process can be summarised as follows:
    
    a[0] = 4,     1    =   √23+4    = 1 +  √23—3
    √23—4        7               7
    a[1] = 1,     7    =  7(√23+3)  = 3 +  √23—3
    √23—3        14              2
    a[2] = 3,     2    =  2(√23+3)  = 1 +  √23—4
    √23—3        14              7
    a[3] = 1,     7    =  7(√23+4)  = 8 +  √23—4
    √23—4        7
    a[4] = 8,     1    =   √23+4    = 1 +  √23—3
    √23—4        7               7
    a[5] = 1,     7    =  7(√23+3)  = 3 +  √23—3
    √23—3        14              2
    a[6] = 3,     2    =  2(√23+3)  = 1 +  √23—4
    √23—3        14              7
    a[7] = 1,     7    =  7(√23+4)  = 8 +  √23—4
    √23—4        7
    
    It can be seen that the sequence is repeating. For conciseness, we use the
    notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
    indefinitely.
    
    The first ten continued fraction representations of (irrational) square
    roots are:
    
    √2=[1;(2)], period=1
    √3=[1;(1,2)], period=2
    √5=[2;(4)], period=1
    √6=[2;(2,4)], period=2
    √7=[2;(1,1,1,4)], period=4
    √8=[2;(1,4)], period=2
    √10=[3;(6)], period=1
    √11=[3;(3,6)], period=2
    √12= [3;(2,6)], period=2
    √13=[3;(1,1,1,1,6)], period=5
    
    Exactly four continued fractions, for N ≤ 13, have an odd period.
    
    How many continued fractions for N ≤ 10000 have an odd period?
    
    Answer: dc960c46c38bd16e953d97cdeefdbc68
    
"""
from common import check

PROBLEM_NUMBER = 64
ANSWER_HASH = "dc960c46c38bd16e953d97cdeefdbc68"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
