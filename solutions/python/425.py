"""
    Problem 425
    ===========
    
    Two positive numbers A and B are said to be connected (denoted by "A ↔ B")
    if one of these conditions holds:
    (1) A and B have the same length and differ in exactly one digit; for
    example, 123 ↔ 173.
    (2) Adding one digit to the left of A (or B) makes B (or A); for example,
    23 ↔ 223 and 123 ↔ 23.
    
    We call a prime P a 2's relative if there exists a chain of connected
    primes between 2 and P and no prime in the chain exceeds P.
    
    For example, 127 is a 2's relative. One of the possible chains is shown
    below:
    2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
    However, 11 and 103 are not 2's relatives.
    
    Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
    We can verify that F(10^3) = 431 and F(10^4) = 78728.
    
    Find F(10^7).
    
    Answer: 3d229894ba4c585138125e802af2d06e
    
"""
from math import e
from common import check, is_prime
from functools import cache 
from rich import pretty
pretty.install()

PROBLEM_NUMBER = 425
ANSWER_HASH = "3d229894ba4c585138125e802af2d06e"
# DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGITS = "0123456789"

@cache
def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

@cache
def get_connections(ni):
    n = str(ni)
    relatives = set()

    def add(v):
        if len(v) == 0:
            return
        v = int(v)
        relatives.add(int(v))

    add(n[1:])
    for j in DIGITS:
        add(j + n)

    for i in range(len(n)):
        for j in DIGITS:
            if i == 0 and j == "0":
                continue
            add(n[:i] + j + n[i+1:])
    return [v for v in relatives if v != ni and is_prime(v)]

# there is no point continuing a chain which is already being explored for the current value of p (duplicate)
# we do need to explore chains for higher values of p
# for lower values of p, do we need to process them individually, or can we just run 10^7
# some values might not be linked, but will be linked if >p are allowed in the chain

# once we have confirmed that n can be reached from 2, we don't need to do that again. We can terminate any chains that also reach n


def calculate(max_value):
    relatives = [False] * max_value
    queue = [[2]]
    values = set()
    while len(queue) > 0:
        chain = queue.pop()
        print(chain)
        connections = get_connections(chain[-1])
        for value in connections:
            if value < max_value and value not in chain:
                if not relatives[value] and max(chain) < value:
                    if value == 11:
                        a = 0
                    relatives[value]=True
                if value not in values:
                    values.add(value)
                    queue.append(chain + [value])
    total = 0
    for i, v in enumerate(relatives):
        if v or not is_prime(i):
            continue
        else:
            print(i)
        total += i

    return sum((i for i, v in enumerate(relatives) if not v and is_prime(i)))

total = calculate(10**3)

print("total:", total)
check(total, PROBLEM_NUMBER, ANSWER_HASH)
