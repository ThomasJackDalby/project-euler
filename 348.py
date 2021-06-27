"""
    Problem 348
    ===========
    
    Many numbers can be expressed as the sum of a square and a cube. Some of
    them in more than one way.
    
    Consider the palindromic numbers that can be expressed as the sum of a
    square and a cube, both greater than 1, in exactly 4 different ways.
    For example, 5229225 is a palindromic number and it can be expressed in
    exactly 4 different ways:
    
    2285^2 + 20^3
    2223^2 + 66^3
    1810^2 + 125^3
    1197^2 + 156^3
    
    Find the sum of the five smallest such palindromic numbers.
    
    Answer: f286f9159fc20aeb97a8bf8396ba64de
    
"""
from common import check

PROBLEM_NUMBER = 348
ANSWER_HASH = "f286f9159fc20aeb97a8bf8396ba64de"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
