"""
    Problem 32
    ==========
    
    
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.
    
    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.
    
    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.
    
    HINT: Some products can be obtained in more than one way so be sure to
    only include it once in your sum.
    
    Answer: 100f6e37d0b0564490a2ee27eff0660d
"""
from common import check
from itertools import permutations
PROBLEM_NUMBER = 32
ANSWER_HASH = "100f6e37d0b0564490a2ee27eff0660d"

def convert(t):
    return int("".join(str(d) for d in t))

values = set()
for p in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    for i in range(1, 7):
        for j in range(i+1, 8):
            a = convert(p[:i])
            b = convert(p[i:j])
            c = convert(p[j:])
            if a * b == c:
                print(f"{a} x {b} = {c}")
                values.add(c)

result = sum(values)

check(result, PROBLEM_NUMBER, ANSWER_HASH)
