"""
    Problem 4
    =========
    
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    Answer: d4cfc27d16ea72a96b83d9bdef6ce2ec
    
"""
from common import check

PROBLEM_NUMBER = 4
ANSWER_HASH = "d4cfc27d16ea72a96b83d9bdef6ce2ec"

def is_factor(number, factor):
    return number % factor== 0

def is_palindrome(number):
    numberString = str(number)
    length = len(numberString)
    i = 0
    while i < len(numberString) / 2.0:
        a = numberString[i]
        b = numberString[length - 1 - i]
        if a != b:
            return False
        i = i + 1
    return True

def next_smallest_palindrome(palindrone):
    palindrone -= 1
    while not is_palindrome(palindrone):
        palindrone -= 1
    return palindrone

palindrone = 999 * 999
not_found = True
while not_found:
    palindrone = next_smallest_palindrome(palindrone)
    factor_a = 999
    while factor_a > 1:
        if is_factor(palindrone, factor_a):
            if len(str(factor_a)) == 3:
                factor_b = int(palindrone / factor_a)
                if is_factor(palindrone, factor_b):
                    if len(str(factor_b)) == 3:
                        not_found = False
                        break
            if len(str(palindrone)) < 3:
                break
        factor_a = factor_a - 1

check(palindrone, PROBLEM_NUMBER, ANSWER_HASH)
