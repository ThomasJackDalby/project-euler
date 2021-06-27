"""
    Problem 7
    =========
    
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.
    
    What is the 10 001st prime number?
    
    Answer: 8c32ab09ec0210af60d392e9b2009560
"""
from common import check, is_factor

PROBLEM_NUMBER = 7
ANSWER_HASH = "8c32ab09ec0210af60d392e9b2009560"

primes = [2]
num_of_primes = 1
num = 1
not_found = True
while not_found:
    num = num + 1
    is_prime = True
    for prime in primes:
        if is_factor(num, prime):
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        num_of_primes = num_of_primes + 1
        if num_of_primes == 10001:
            not_found = False

check(primes.pop(), PROBLEM_NUMBER, ANSWER_HASH)