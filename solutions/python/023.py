"""
    Problem 23
    ==========
    
    
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.
    
    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.
    
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers is
    24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it
    is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.
    
    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    
    
    Answer: 2c8258c0604152962f7787571511cf28
"""
from common import check, get_factors

PROBLEM_NUMBER = 23
ANSWER_HASH = "2c8258c0604152962f7787571511cf28"
UPPER_LIMIT = 28123

# find all abundent numbers below limit
abundant_numbers = set()
for number in range(1, UPPER_LIMIT):
    factors = get_factors(number)
    total = sum(factors) - number
    if total > number:
        abundant_numbers.add(number)

numbers_to_sum = []
for number in range(1, UPPER_LIMIT):
    found = False
    for a in abundant_numbers:
        b = number - a
        if b in abundant_numbers:
            found = True
            break
    if not found:
        numbers_to_sum.append(number)

result = sum(numbers_to_sum)

check(result, PROBLEM_NUMBER, ANSWER_HASH)
