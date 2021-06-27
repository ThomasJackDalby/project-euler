"""
    Problem 5
    =========
    
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    
    Answer: bc0d0a22a7a46212135ed0ba77d22f3a
    
"""
from common import check

PROBLEM_NUMBER = 5
ANSWER_HASH = "bc0d0a22a7a46212135ed0ba77d22f3a"

def is_factor(number, factor):
    return number % factor== 0

FACTORS = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

number = 2520
not_found_answer = True
while not_found_answer:
    found_answer = True
    for factor in FACTORS:
        if not is_factor(number, factor):
            found_answer = False
            break
    if found_answer:
        not_found_answer = False
    else:
        number += 1

check(number, PROBLEM_NUMBER, ANSWER_HASH)