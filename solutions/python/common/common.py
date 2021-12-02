import hashlib, os
from functools import cache
from math import sqrt
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

@cache
def is_prime(number):
    return _sieve.is_prime(number)

def get_primes():
    return _sieve.get_primes()

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