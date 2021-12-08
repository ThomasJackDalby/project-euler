"""
    Problem 52
    ==========
    
    
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.
    
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    
    
    Answer: a420384997c8a1a93d5a84046117c2aa
"""
from common import check
from itertools import count

PROBLEM_NUMBER = 52
ANSWER_HASH = "a420384997c8a1a93d5a84046117c2aa"

def check_factor(number, factor):
    factored_number = number * factor
    factored_number_set = set(str(factored_number))
    number_set = set(str(number))
    return number_set == factored_number_set

def check_number(number):
    for factor in range(2, 7):
        if not check_factor(number, factor):
            return False
    return True

for number in count(1):
    if check_number(number):
        check(number, PROBLEM_NUMBER, ANSWER_HASH)
        exit()
