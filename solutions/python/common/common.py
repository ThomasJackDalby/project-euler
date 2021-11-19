import hashlib, os
from functools import cache
from math import sqrt

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
    return len(get_factors(number)) == 2

    # for i in range(2, number):
    #     if is_factor(number, i):
    #         return False
    # return True

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

class PrimeGenerator:
    def __init__(self) -> None:
        self.wheel_size = 10

    def calculate(self):
        primes = [2]
        factors = [2]
        wheel = [False] * self.wheel_size
        wheel_start = 2

        def wheel_forward_prime(prime, i):
            factor = factors[i]
            while factor - wheel_start < self.wheel_size:
                wheel[factor - wheel_start] = True
                factor += prime
                factors[i] = factor

        while True:
            for i in range(len(primes)):
                prime = primes[i]
                wheel_forward_prime(prime, i)

            for i in range(self.wheel_size):
                is_prime = not wheel[i]
                if not is_prime:
                    continue

                prime = i + wheel_start
                primes.Add(prime)
                factors.Add(prime)

                wheel_forward_prime(prime, len(primes) - 1)

            # extend the wheel
            wheel_start += self.wheel_size
            for i in range(self.wheel_size):
                wheel[i] = False

if __name__ == "__main__":
    print("factors")
    factors = get_factors(100000000)
    print(len(factors), factors)