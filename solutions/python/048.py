"""
    Problem 48
    ==========
    
    
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
    
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    
    
    Answer: 0829124724747ae1c65da8cae5263346
"""
from common import check

PROBLEM_NUMBER = 48
ANSWER_HASH = "0829124724747ae1c65da8cae5263346"

def mod_pow(x, n, d):
    total = 1
    for _ in range(n):
        total *= x
        total %= d
    return total

mod = 10_000_000_000
total = 0
for i in range(1, 1001):
    total += mod_pow(i, i, mod)
    total %= mod

check(total, PROBLEM_NUMBER, ANSWER_HASH)
