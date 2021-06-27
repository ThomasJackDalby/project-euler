import hashlib

def check(result, problem_number, answer_hash):
    success = hashlib.md5(f"{result}".encode()).hexdigest() == answer_hash
    print(f"Problem {problem_number} - {'Pass' if success else 'Fail'}")

def is_factor(number, factor):
    return number % factor == 0

def is_prime(number):
    for i in range(2, number):
        if is_factor(number, i):
            return False
    return True