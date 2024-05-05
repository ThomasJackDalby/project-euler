"""
    Problem 60
    ==========
    
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be
    prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
    sum of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.
    
    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    
    Answer: a4b5a70ca8cf24d0eb4330748d1e72e5
    
"""
from common import check, is_prime, get_prime
from functools import cache
from itertools import count, takewhile

PROBLEM_NUMBER = 60
ANSWER_HASH = "a4b5a70ca8cf24d0eb4330748d1e72e5"
GROUP_SIZE = 5

def check_pair(a, b):
    a = str(a)
    b = str(b)
    if not is_prime(int(a + b)):
        return False
    if not is_prime(int(b + a)):
        return False
    return True

def get_indexes(number):
    current = list(range(number))
    yield current
    for _ in count(1):
        for i in range(number):
            if i == number-1 or current[i] != current[i+1]-1:
                current[i] += 1
                for j in range(i):
                    current[j] = j+1
                break
        yield current

## attempt 1
generators = {}
cached_groups = []
def get_group(number, i):
    if len(cached_groups[number-2]) <= i:
        for _ in takewhile(lambda p: len(cached_groups[number-2]) <= i, generators[number]):
            pass
    return cached_groups[number-2][i]

def get_groups(number):
    for indexes in get_indexes(number):
        if number == 2:
            primes = [get_prime(i) for i in indexes]
            if check_pair(primes[0], primes[1]):
                prime_set = set(primes)
                print(",".join((str(len(g)) for g in cached_groups)), prime_set)
                cached_groups[number-2].append(prime_set)
                yield prime_set
        else:
            group = [get_group(number-1, i) for i in indexes]
            group_set = set(prime for primes in group for prime in primes)
            if len(group_set) == number:
                print(",".join((str(len(g)) for g in cached_groups)), group_set)
                cached_groups[number-2].append(group_set)
                yield group_set

if __name__ == "__main__":
    for i in range(GROUP_SIZE):
        generators[i] = get_groups(i)
        cached_groups.append([])

    for group in get_groups(GROUP_SIZE):
        exit()
