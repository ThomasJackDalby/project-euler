"""
    Problem 3
    =========
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143 ?
    
    Answer: 94c4dd41f9dddce696557d3717d98d82
"""
from common import check

PROBLEM_NUMBER = 3
ANSWER_HASH = "94c4dd41f9dddce696557d3717d98d82"

STARTING_VALUE = 600851475143

def is_factor(number, factor):
    return number % factor == 0

def is_prime(number):
    for i in range(2,number):
        if is_factor(number, i):
            return False
    return True

def get_next_prime(number):
    while True:
        number = number + 1
        if is_prime(number):
            return number

value = STARTING_VALUE
prime = 2
max_prime = prime
while value != 1:            
    if is_factor(value, prime):
        value = value / prime           
        prime = 2
    else:
        prime = get_next_prime(prime)
        if prime > max_prime:
            max_prime = prime

check(max_prime, PROBLEM_NUMBER, ANSWER_HASH)