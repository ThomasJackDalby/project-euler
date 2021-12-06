"""
    Problem 50
    ==========
    
    
    The prime 41, can be written as the sum of six consecutive primes:
    
    41 = 2 + 3 + 5 + 7 + 11 + 13
    
    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.
    
    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.
    
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
    
    
    Answer: 73229bab6c5dc1c7cf7a4fa123caf6bc
"""
from common import check, get_primes, is_prime
from itertools import takewhile

PROBLEM_NUMBER = 50
ANSWER_HASH = "73229bab6c5dc1c7cf7a4fa123caf6bc"
MAX_VALUE = 1_000_000

def find_max_prime_longest_chain(max_value):
    primes = list(takewhile(lambda p: p < max_value, get_primes()))
    prime_set = set(primes)
    max_prime = None
    max_length = 0
    for i, s in enumerate(primes):
        total = s
        for j, v in enumerate(primes[i+1:]):
            total += v
            if total > max_value:
                break

            if total in prime_set:
                if j+1 > max_length:
                    max_prime = total
                    max_length = j+1
                    print(f"{total} : {primes[i:i+j+2]} [{max_length}]")
    return max_prime

result = find_max_prime_longest_chain(MAX_VALUE)

check(result, PROBLEM_NUMBER, ANSWER_HASH)
