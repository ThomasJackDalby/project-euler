"""
    Problem 60
    ==========
    
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be
    prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
    sum of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.
    
    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    
    Answer: a4b5a70ca8cf24d0eb4330748d1e72e5
    
"""
from common import check

PROBLEM_NUMBER = 60
ANSWER_HASH = "a4b5a70ca8cf24d0eb4330748d1e72e5"

# need to find 5 primes which can be prime in any concatenated configuration.

def concatenate(a, b):
    # expecting a, b to be integers
    return int(str(a)+str(b))

print(concatenate(1, 23))

check(None, PROBLEM_NUMBER, ANSWER_HASH)
