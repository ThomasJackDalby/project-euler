# COMPLETED
"""
    Problem 3
    =========
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143 ?
    
    Answer: 94c4dd41f9dddce696557d3717d98d82
"""
from common import check, is_factor, is_prime, get_primes

PROBLEM_NUMBER = 3
ANSWER_HASH = "94c4dd41f9dddce696557d3717d98d82"
STARTING_VALUE = 600851475143

primes = get_primes()

value = STARTING_VALUE
while value != 1:            
    prime = next(primes)
    if is_factor(value, prime):
        value = value / prime           

check(prime, PROBLEM_NUMBER, ANSWER_HASH)