"""
    Problem 442
    ===========
    
    An integer is called eleven-free if its decimal expansion does not contain
    any substring representing a power of 11 except 1.
    
    For example, 2404 and 13431 are eleven-free, while 911 and 4121331 are
    not.
    
    Let E(n) be the nth positive eleven-free integer. For example, E(3) = 3,
    E(200) = 213 and E(500 000) = 531563.
    
    Find E(10^18).
    
    Answer: c31bb13db787bce9a169dce600aec863
    
"""
from common import check

PROBLEM_NUMBER = 442
ANSWER_HASH = "c31bb13db787bce9a169dce600aec863"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
