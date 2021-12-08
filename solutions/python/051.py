"""
    Problem 51
    ==========


    By replacing the 1^st digit of the 2-digit number *3, it turns out that
    six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all
    prime.

    By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight
    prime value family.


    Answer: e2a8daa5eb919905dadd795593084c22
"""
from common import check, is_prime
from itertools import combinations, permutations, count

PROBLEM_NUMBER = 51
ANSWER_HASH = "e2a8daa5eb919905dadd795593084c22"
DIGITS = sorted(list(range(0, 10)) * 4)
FAMILY_SIZE = 8

# 

def get_pattern(swaps, numbers):
    pattern = []
    j = 0
    for i in range(len(swaps) + len(numbers)):
        if i in swaps:
            pattern.append(None)
        else:
            pattern.append(numbers[j])
            j += 1
    return pattern

def get_set(pattern):
    digits = range(1, 10) if pattern[0] == None else range(0, 10)
    return [int("".join(str(d) if d is not None else str(i) for d in pattern)) for i in digits]

def get_sets(digits, replacements):
    for swaps in combinations(range(digits), replacements):
        print(swaps, "".join("X" if i in swaps else "." for i in range(digits)))
        for numbers in combinations(DIGITS, digits-replacements):
            pattern = get_pattern(swaps, numbers)
            if numbers[0] != 0 or 0 in swaps:
                yield get_set(pattern)

if __name__ == "__main__":
    min_prime = None
    for digits in count(2, 1):
        if min_prime is not None:
            check(min_prime, PROBLEM_NUMBER, ANSWER_HASH)
            exit()
        for replacements in range(2, digits):
            print(f"{digits=} {replacements=}")
            for pattern_set in get_sets(digits, replacements):
                primes = [number for number in pattern_set if is_prime(number)]
                if len(primes) == FAMILY_SIZE and (min_prime is None or min(primes) < min_prime):
                    min_prime = min(primes)
