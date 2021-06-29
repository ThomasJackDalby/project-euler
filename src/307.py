"""
    Problem 307
    ===========
    
    k defects are randomly distributed amongst n integrated-circuit chips
    produced by a factory (any number of defects may be found on a chip and
    each defect is independent of the other defects).
    
    Let p(k,n) represent the probability that there is a chip with at least 3
    defects.
    For instance p(3,7) ≈ 0.0204081633.
    
    Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal
    places in the form 0.abcdefghij
    
    Answer: 0c49094fa750365e13bb20ec4a158b6d
    
"""
from common import check

PROBLEM_NUMBER = 307
ANSWER_HASH = "0c49094fa750365e13bb20ec4a158b6d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
