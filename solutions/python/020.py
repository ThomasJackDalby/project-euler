# COMPLETED
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
from math import factorial

PROBLEM_NUMBER = 20
ANSWER_HASH = "443cb001c138b2561a0d90720d6ce111"
FACTORIAL_NUMBER = 100

# manual approach
value = 1
for i in range(1, FACTORIAL_NUMBER):
    value *= i

# built in function
value = factorial(FACTORIAL_NUMBER)

total = sum(int(c) for c in str(value))
check(total, PROBLEM_NUMBER, ANSWER_HASH)
