"""
    Problem 125
    ===========
    
    The palindromic number 595 is interesting because it can be written as the
    sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
    
    There are exactly eleven palindromes below one-thousand that can be
    written as consecutive square sums, and the sum of these palindromes is
    4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is
    concerned with the squares of positive integers.
    
    Find the sum of all the numbers less than 10^8 that are both palindromic
    and can be written as the sum of consecutive squares.
    
    Answer: 1b5635e8ab723e01570ca783129493dd
    
"""
from common import check

PROBLEM_NUMBER = 125
ANSWER_HASH = "1b5635e8ab723e01570ca783129493dd"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
