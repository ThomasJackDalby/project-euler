# COMPLETED
"""
    Problem 1
    =========

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
   
    Answer: e1edf9d1967ca96767dcc2b2d6df69f4
"""
from common import check, is_factor

PROBLEM_NUMBER = 1
ANSWER_HASH = "e1edf9d1967ca96767dcc2b2d6df69f4"

sum = 0
for i in range(1, 1000):
    if is_factor(i, 3) or is_factor(i, 5):
        sum = sum + i  

check(sum, PROBLEM_NUMBER, ANSWER_HASH)