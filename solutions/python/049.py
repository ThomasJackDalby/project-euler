"""
    Problem 49
    ==========
    
    
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.
    
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.
    
    What 12-digit number do you form by concatenating the three terms in this
    sequence?
    
    
    Answer: 0b99933d3e2a9addccbb663d46cbb592
"""
from common import check, is_prime
from itertools import combinations, permutations

PROBLEM_NUMBER = 49
ANSWER_HASH = "0b99933d3e2a9addccbb663d46cbb592"

# Allow multiples of each digit
DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
DIGITS += DIGITS
DIGITS += DIGITS

all_combinations = list(sorted(set(tuple(sorted(c)) for c in combinations(DIGITS, 4))))

for c in all_combinations:
    all_permutations = list(set(p for p in (int("".join(str(i) for i in p)) for p in permutations(c)) if p > 999 and p < 10000))
    all_primes = list(sorted(p for p in all_permutations if is_prime(p)))

    if len(all_primes) < 3:
        continue
    
    # print(f"---- {c} --- {all_primes} [{len(all_primes)}]")
    
    for i, a in enumerate(all_primes[:-2]):
        for j, b in enumerate(all_primes[i+1:-1]):
            c = 2 * b - a
            if c in all_primes[j+1:]:
                result = f"{a}{b}{c}"
                if result != "148748178147":
                    check(result, PROBLEM_NUMBER, ANSWER_HASH)
                    exit()
