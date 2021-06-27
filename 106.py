"""
    Problem 106
    ===========
    
    Let S(A) represent the sum of elements in set A of size n. We shall call
    it a special sum set if for any two non-empty disjoint subsets, B and C,
    the following properties are true:
    
    i. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    ii. If B contains more elements than C then S(B) > S(C).
    
    For this problem we shall assume that a given set contains n strictly
    increasing elements and it already satisfies the second rule.
    
    Surprisingly, out of the 25 possible subset pairs that can be obtained
    from a set for which n = 4, only 1 of these pairs need to be tested for
    equality (first rule). Similarly, when n = 7, only 70 out of the 966
    subset pairs need to be tested.
    
    For n = 12, how many of the 261625 subset pairs that can be obtained need
    to be tested for equality?
    
    NOTE: This problem is related to [1]Problem 103 and [2]Problem 105.
    
    Visible links
    1. problem=103
    2. problem=105
    Answer: c8fd9e36fdeb06bcc93a0732c667b6d8
    
"""
from common import check

PROBLEM_NUMBER = 106
ANSWER_HASH = "c8fd9e36fdeb06bcc93a0732c667b6d8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
