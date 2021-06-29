"""
    Problem 41
    ==========
    
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.
    
    What is the largest n-digit pandigital prime that exists?
    
    Answer: d0a1bd6ab4229b2d0754be8923431404
    
"""
from common import check

PROBLEM_NUMBER = 41
ANSWER_HASH = "d0a1bd6ab4229b2d0754be8923431404"

# n must be a digit 1 - 9
# must also be prime
# could brute force?

def is_pandigital(number):
    text = str(number)
    n = len(text)
    occurances = [0] * n
    for i in range(n):
        digit = int(text[i])
        if digit > n:
            return False
        occurances[digit-1] += 1
        if occurances[digit-1] > 1:
            return False
    return sum(occurances) == n

# work backwards for primes?

# need to write a prime wheel

def get_primes(max_prime):
    primes = []

    def create_wheel(wheel_start, wheel_end):
        wheel_size = wheel_end - wheel_start
        digits = [True] * wheel_size
        for i in primes + list(range(wheel_start, wheel_size)):
            print("i:", i)
            j = 2
            while True:
                value = (i * j) - 1
                if value > wheel_end:
                    print(f"End: {i} x {j} = {value}")
                    break
                digits[value - wheel_start] = False
                j += 1
        return [i+wheel_start for i, is_prime in enumerate(digits) if is_prime]

    primes = create_wheel(2, 10)

    return primes
    
print(get_primes(10))

check(None, PROBLEM_NUMBER, ANSWER_HASH)
