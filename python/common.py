import hashlib, os

def check(result, problem_number, answer_hash):
    success = hashlib.md5(f"{result}".encode()).hexdigest() == answer_hash
    print(f"Problem {problem_number} - {'Pass' if success else 'Fail'}")

def get_relative_file_path(source_file_path, relative_file_path):
    folder_path = os.path.dirname(source_file_path)
    return os.path.join(folder_path, relative_file_path)

def is_even(number):
    return is_factor(number, 2)

def is_factor(number, factor):
    return number % factor == 0

def is_prime(number):
    for i in range(2, number):
        if is_factor(number, i):
            return False
    return True

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