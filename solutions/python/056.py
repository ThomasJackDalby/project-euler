"""
    Problem 56
    ==========
    
    
    A googol (10^100) is a massive number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.
    
    Considering natural numbers of the form, a^b, where a, b < 100, what is
    the maximum digital sum?
    
    
    Answer: c22abfa379f38b5b0411bc11fa9bf92f
"""
from common import check

PROBLEM_NUMBER = 56
ANSWER_HASH = "c22abfa379f38b5b0411bc11fa9bf92f"

def pow(a, b):
    total = 1
    for _ in range(b):
        total *= a
    return total

for a in range(1, 10):
    for b in range(1, 4):
        result = pow(a, b)
        print(a, b, result)

check(None, PROBLEM_NUMBER, ANSWER_HASH)
