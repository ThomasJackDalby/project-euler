# COMPLETED
"""
    Problem 36
    ==========
    
    The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
    bases.
    
    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, may not include
    leading zeros.)
    
    Answer: 0e175dc2f28833885f62e7345addff03
    
"""
from common import check
import math

PROBLEM_NUMBER = 36
ANSWER_HASH = "0e175dc2f28833885f62e7345addff03"

def is_palindrome(text):
    length = len(text)
    i = 0
    while i < length / 2.0:
        a = text[i]
        b = text[length - 1 - i]
        if a != b:
            return False
        i = i + 1
    return True

def to_binary(number):
    bits = []
    previous = number
    while previous != 0:
        current = int(math.floor(previous / 2))
        remainder = previous - (current * 2)
        bits.append(remainder)
        previous = current
    return "".join((str(c) for c in reversed(bits)))

total = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
        total += i

check(total, PROBLEM_NUMBER, ANSWER_HASH)
