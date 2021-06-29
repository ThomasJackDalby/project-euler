# COMPLETED
"""
    Problem 14
    ==========
    
    The following iterative sequence is defined for the set of positive
    integers:
    
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    
    Using the rule above and starting with 13, we generate the following
    sequence:
    
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.
    
    Which starting number, under one million, produces the longest chain?
    
    NOTE: Once the chain starts the terms are allowed to go above one million.
    
    Answer: 5052c3765262bb2c6be537abd60b305e
    
"""
from common import check, is_even

PROBLEM_NUMBER = 14
ANSWER_HASH = "5052c3765262bb2c6be537abd60b305e"

def calculate(n):
    if is_even(n):
        return int(n/2)
    else:
        return 3*n+1

cache = { }
def get_length(n):
    if n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        m = calculate(n)
        length = get_length(m) + 1
        cache[n] = length
        return length

max_length = 0
best_n = None
for n in range(1, 1000000):
    length = get_length(n)
    if length > max_length:
        best_n = n
        max_length = length

check(best_n, PROBLEM_NUMBER, ANSWER_HASH)
