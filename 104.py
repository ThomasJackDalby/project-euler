"""
    Problem 104
    ===========
    
    The Fibonacci sequence is defined by the recurrence relation:
    
    F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.
    
    It turns out that F[541], which contains 113 digits, is the first
    Fibonacci number for which the last nine digits are 1-9 pandigital
    (contain all the digits 1 to 9, but not necessarily in order). And
    F[2749], which contains 575 digits, is the first Fibonacci number for
    which the first nine digits are 1-9 pandigital.
    
    Given that F[k] is the first Fibonacci number for which the first nine
    digits AND the last nine digits are 1-9 pandigital, find k.
    
    Answer: c8771ddd4df191098d70a8e94dd1cde7
    
"""
from common import check

PROBLEM_NUMBER = 104
ANSWER_HASH = "c8771ddd4df191098d70a8e94dd1cde7"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
