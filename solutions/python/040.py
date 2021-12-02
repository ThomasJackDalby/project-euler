"""
    Problem 40
    ==========
    
    
    An irrational decimal fraction is created by concatenating the positive
    integers:
    
    0.123456789101112131415161718192021...
    
    It can be seen that the 12^th digit of the fractional part is 1.
    
    If d[n] represents the n^th digit of the fractional part, find the value
    of the following expression.
    
    d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]
    
    
    Answer: 6f3ef77ac0e3619e98159e9b6febf557
"""
from common import check
from itertools import takewhile, count

PROBLEM_NUMBER = 40
ANSWER_HASH = "6f3ef77ac0e3619e98159e9b6febf557"

def generate():
    for i in count(1):
        for c in str(i):
            yield int(c)

def d(n):
    for i, v in enumerate(generate()):
        if i >= n - 1:
            return v

result = d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
check(result, PROBLEM_NUMBER, ANSWER_HASH)
