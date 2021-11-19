"""
    Problem 27
    ==========
    
    
    Euler discovered the remarkable quadratic formula:
    
    n² + n + 41
    
    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.
    
    The incredible formula  n² − 79n + 1601 was discovered, which produces 80
    primes for the consecutive values n = 0 to 79. The product of the
    coefficients, −79 and 1601, is −126479.
    
    Considering quadratics of the form:
    
    n² + an + b, where |a| < 1000 and |b| < 1000
    
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4
    
    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n = 0.
    
    
    Answer: 69d9e3218fd7abb6ff453ea96505183d
"""
from common import check, is_prime

PROBLEM_NUMBER = 27
ANSWER_HASH = "69d9e3218fd7abb6ff453ea96505183d"

max_length = 0
max_a = None
max_b = None

for a, b in ((a, b) for a in range(-1000, 1001) for b in range(-1000, 1001)):
    n = 0
    while True:
        p = n * n + a * n + b
        if p < 0 or not is_prime(p):
            break
        n += 1
    
    if n > max_length:
        max_length = n
        max_a = a
        max_b = b
        print(a, b, max_length)

check(max_a * max_b, PROBLEM_NUMBER, ANSWER_HASH)
