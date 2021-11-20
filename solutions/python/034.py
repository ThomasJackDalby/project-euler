# Completed
"""
    Problem 34
    ==========
    
    
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    
    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.
    
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    
    
    Answer: 60803ea798a0c0dfb7f36397d8d4d772
"""
from common import check
from math import factorial

PROBLEM_NUMBER = 34
ANSWER_HASH = "60803ea798a0c0dfb7f36397d8d4d772"

result = 0
for n in range(10, 100000):

    total = 0
    n_str = str(n)
    for c_str in n_str:
        c = int(c_str)
        total += factorial(c)
    
    if total == n:
        result += n

check(result, PROBLEM_NUMBER, ANSWER_HASH)
