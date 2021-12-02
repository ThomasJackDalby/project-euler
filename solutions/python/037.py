"""
    Problem 37
    ==========
    
    
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.
    
    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.
    
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    
    
    Answer: cace46c61b00de1b60874936a093981d
"""
from common import check, is_prime

PROBLEM_NUMBER = 37
ANSWER_HASH = "cace46c61b00de1b60874936a093981d"

# starting with a single digit, we can add numbers to the left of it, and then check whether its trunckable

def check_truncatable(n):
    n_str = str(n)
    if len(n_str) == 1:
        return False
    for i in range(len(n_str)-1):
        p_str = n_str[:-i-1]
        p = int(p_str)
        if not is_prime(p):
            return False
    return True

queue = list((p for p in range(1, 10) if is_prime(p)))
results = []

while len(queue) > 0 and len(results) < 11:
    n = queue.pop(0)
    n_str = str(n)

    if check_truncatable(n):
        left = " ".join(reversed([n_str[:-i-1] for i in range(len(n_str)-1)]))
        right = " ".join([n_str[i+1:] for i in range(len(n_str)-1)])
        print(f"{left} | {n} | {right}")
        results.append(n)
    
    for i in range(1, 10):
        p_str = str(i) + n_str
        p = int(p_str)
        if is_prime(p):
            queue.append(p)

check(sum(results), PROBLEM_NUMBER, ANSWER_HASH)