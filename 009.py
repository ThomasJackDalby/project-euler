"""
    Problem 9
    =========
    
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,
    
    a^2 + b^2 = c^2
    
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    
    Answer: 24eaa9820350012ff678de47cb85b639
"""
from common import check

PROBLEM_NUMBER = 9
ANSWER_HASH = "24eaa9820350012ff678de47cb85b639"

def distance(a, b):
    return (a*a + b*b)**0.5

def is_triplet(a, b):
    if b < a:
        return False, None
    c = distance(a, b)
    return c == round(c), int(c)

a = 1
b = 1
not_found = True
while not_found:
    result, c = is_triplet(a, b)
    if result:
        sum = a + b + c
        if sum == 1000:
            not_found = False
            break
    if b < 400:
        b += 1
    else:
        b = 1
        a += 1 
result = a * b * c

check(result, PROBLEM_NUMBER, ANSWER_HASH)