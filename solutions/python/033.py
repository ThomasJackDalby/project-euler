"""
    Problem 33
    ==========
    
    
    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    
    We shall consider fractions like, 30/50 = 3/5, to be trivial
    examples.
    
    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.
    
    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.
    
    
    Answer: f899139df5e1059396431415e770c6dd
"""
from common import check, get_factors
from functools import reduce

PROBLEM_NUMBER = 33
ANSWER_HASH = "f899139df5e1059396431415e770c6dd"

def check_it(f, order):
    n, d = f
    np, dp = order
    n_str = str(n)
    d_str = str(d)
    if n_str[np] == d_str[dp]:
        n_1 = int(n_str[abs(np-1)])
        d_1 = int(d_str[abs(dp)-1])
        if n_1 == 0 or d_1 == 0:
            return False
        n_f = n / n_1
        d_f = d / d_1
        if n_f != 10 and n_f == d_f:
            return True

fractions = ((n, d) for n in range(10, 100) for d in range(n+1, 100))
results = set()
for f in fractions:
    for order in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        if check_it(f, order):
            results.add(f)

def multiply_fractions(a, b):
    n = a[0] * b[0]
    d = a[1] * b[1]
    return simplify_fraction((n, d))

def simplify_fraction(a):
    n, d = a
    n_factors = get_factors(n)
    d_factors = get_factors(d)
    common_factors = n_factors.intersection(d_factors)
    if len(common_factors) == 0:
        return a
    largest_common_factor = max(common_factors)
    n //= largest_common_factor
    d //= largest_common_factor
    return n, d

result = reduce(multiply_fractions, results, (1, 1))
check(result[1], PROBLEM_NUMBER, ANSWER_HASH)
