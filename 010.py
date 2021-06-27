"""
    Problem 10
    ==========
    
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    
    Find the sum of all the primes below two million.
    
    Answer: d915b2a9ac8749a6b837404815f1ae25 
"""
from common import check

PROBLEM_NUMBER = 10
ANSWER_HASH = "d915b2a9ac8749a6b837404815f1ae25"

number_of_primes = 2000000
primes = []
numbers = []
for i in range(0,number_of_primes):
    numbers.append(True)

for i in range(1,number_of_primes):
    if numbers[i]:
        primes.append(i+1)
        j = 2
        while True:
            factor = j * (i + 1)
            if factor > number_of_primes:
                break
            numbers[factor-1] = False
            j += 1

sum = 0
for prime in primes:
    sum = sum + prime

check(sum, PROBLEM_NUMBER, ANSWER_HASH)