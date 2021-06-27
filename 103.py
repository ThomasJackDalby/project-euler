"""
    Problem 103
    ===========
    
    Let S(A) represent the sum of elements in set A of size n. We shall call
    it a special sum set if for any two non-empty disjoint subsets, B and C,
    the following properties are true:
    
    i. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    ii. If B contains more elements than C then S(B) > S(C).
    
    If S(A) is minimised for a given n, we shall call it an optimum special
    sum set. The first five optimum special sum sets are given below.
    
    n = 1: {1}
    n = 2: {1, 2}
    n = 3: {2, 3, 4}
    n = 4: {3, 5, 6, 7}
    n = 5: {6, 9, 11, 12, 13}
    
    It seems that for a given optimum set, A = {a[1], a[2], ... , a[n]}, the
    next optimum set is of the form B = {b, a[1]+b, a[2]+b, ... ,a[n]+b},
    where b is the "middle" element on the previous row.
    
    By applying this "rule" we would expect the optimum set for n = 6 to be A
    = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the
    optimum set, as we have merely applied an algorithm to provide a near
    optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25},
    with S(A) = 115 and corresponding set string: 111819202225.
    
    Given that A is an optimum special sum set for n = 7, find its set string.
    
    NOTE: This problem is related to [1]Problem 105 and [2]Problem 106.
    
    Visible links
    1. problem=105
    2. problem=106
    Answer: af8c238336c2a79bb81a24b3fef3330d
    
"""
from common import check

PROBLEM_NUMBER = 103
ANSWER_HASH = "af8c238336c2a79bb81a24b3fef3330d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
