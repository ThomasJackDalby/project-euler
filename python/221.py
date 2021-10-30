"""
    Problem 221
    ===========
    
    We shall call a positive integer A an "Alexandrian integer", if there
    exist integers p, q, r such that:
    
    A = p · q · r    and   1 = 1 + 1 + 1
    A   p   q   r
    
    For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18).In
    fact, 630 is the 6^th Alexandrian integer, the first 6 Alexandrian
    integers being: 6, 42, 120, 156, 420 and 630.
    
    Find the 150000^th Alexandrian integer.
    
    Answer: cb000c24f653d9c8f78b74123e6515ab
    
"""
from common import check

PROBLEM_NUMBER = 221
ANSWER_HASH = "cb000c24f653d9c8f78b74123e6515ab"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
