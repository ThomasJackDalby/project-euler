import hashlib, os
from functools import cache
from math import sqrt, floor
from .prime_sieve import PrimeSieve

_sieve = PrimeSieve()

def check(result, problem_number, answer_hash):
    success = hashlib.md5(f"{result}".encode()).hexdigest() == answer_hash
    print(f"Problem {problem_number} - {result} - {'Pass' if success else 'Fail'}")

def get_relative_file_path(source_file_path, relative_file_path):
    folder_path = os.path.dirname(source_file_path)
    return os.path.join(folder_path, relative_file_path)

def is_even(number):
    return is_factor(number, 2)

def is_factor(number, factor):
    return number % factor == 0

def is_palindrome(text):
    if not isinstance(text, str):
        text = str(text)
    for i in range(floor(len(text) / 2.0)):
        if text[i] != text[-1-i]:
            return False
    return True

@cache
def is_prime(number):
    return _sieve.is_prime(number)

def get_primes():
    return _sieve.get_primes()

def get_prime(index):
    return _sieve.get_prime(index)


# def is_prime(number):
#     if number != 2 and number % 2 == 0:
#         return False

#     m = 0
#     d = number - 1
#     while d % 2 == 0:
#         d //= 2
#         m += 1
    
#     if number < 1373653:

# def mod_pow(n, p, m):
#     result = 1
#     for _ in range(n):
#         result *= n
#         result %= d
#     return result


@cache
def get_factors(number):
    """Returns a set of the factors of a number"""

    if number < 0:
        raise Exception()

    factors = set([1, number])
    step = 2 if number % 2 else 1
    for factor in range(1, int(sqrt(number))+1, step):
        if not number % factor:
            factors.add(factor)
            factors.add(number // factor)
    return factors