# Completed
"""
    Problem 25
    ==========
    
    
    The Fibonacci sequence is defined by the recurrence relation:
    
    F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.
    
    Hence the first 12 terms will be:
    
    F[1] = 1
    F[2] = 1
    F[3] = 2
    F[4] = 3
    F[5] = 5
    F[6] = 8
    F[7] = 13
    F[8] = 21
    F[9] = 34
    F[10] = 55
    F[11] = 89
    F[12] = 144
    
    The 12th term, F[12], is the first term to contain three digits.
    
    What is the first term in the Fibonacci sequence to contain 1000 digits?
    
    
    Answer: a376802c0811f1b9088828288eb0d3f0
"""
from common import check

PROBLEM_NUMBER = 25
ANSWER_HASH = "a376802c0811f1b9088828288eb0d3f0"

def get_first_term(length):
    fn_2 = 1
    fn_1 = 1
    t = 3
    while True:
        fn = fn_1 + fn_2

        if len(str(fn)) >= length:
            return t

        t += 1
        fn_2 = fn_1
        fn_1 = fn

result = get_first_term(1000)
check(result, PROBLEM_NUMBER, ANSWER_HASH)
