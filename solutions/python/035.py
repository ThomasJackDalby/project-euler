"""
    Problem 35
    ==========
    
    
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.
    
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.
    
    How many circular primes are there below one million?
    
    
    Answer: b53b3a3d6ab90ce0268229151c9bde11
"""
from common import check, is_prime

PROBLEM_NUMBER = 35
ANSWER_HASH = "b53b3a3d6ab90ce0268229151c9bde11"

circular_primes = set()
for n in range(2, 1000000):
    if n in circular_primes or not is_prime(n):
        continue

    n_str = str(n)
    primes = { int(n_str[i:] + n_str[:i]) for i in range(1, len(n_str)) }
    if all((is_prime(p) for p in primes)):
        circular_primes.add(n)
        circular_primes.update(primes)

result = len(circular_primes)
check(result, PROBLEM_NUMBER, ANSWER_HASH)
