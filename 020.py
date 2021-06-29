"""
    Problem 20
    ==========
    
    n! means n × (n − 1) × ... × 3 × 2 × 1
    
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
    27.
    
    Find the sum of the digits in the number 100!
    
    Answer: 443cb001c138b2561a0d90720d6ce111
    
"""
from common import check

PROBLEM_NUMBER = 20
ANSWER_HASH = "443cb001c138b2561a0d90720d6ce111"

value = 1
for i in range(1, 100):
    value *= i

total = sum(int(c) for c in str(value))
check(total, PROBLEM_NUMBER, ANSWER_HASH)
