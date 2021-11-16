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
import time

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

def get_primes(max_prime):
    def create_wheel(primes, wheel_end):
        wheel_start = primes[-1] + 1
        wheel_size = wheel_end - wheel_start + 1
        digits = [True] * wheel_size
        for i in primes + list(range(wheel_start, wheel_size)):
            j = 2
            while True:
                value = i * j
                if value > wheel_end:
                    break
                digits[value - wheel_start] = False
                j += 1
        return primes + [i+wheel_start for i, is_prime in enumerate(digits) if is_prime]

    primes = [2]
    wheel_end = 10
    start_time = time.perf_counter()
    while primes[-1] < max_prime:
        primes = create_wheel(primes, wheel_end)
        wheel_end *= 2
        print(f"{time.perf_counter() - start_time:.3f}", f"{wheel_end:#9d}", f"{len(primes):#9d}")

    return primes
    
# largest n digit pandigital prime

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True





print(get_primes(999999999))

check(None, PROBLEM_NUMBER, ANSWER_HASH)
