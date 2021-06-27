"""
    Problem 6
    =========
    
    The sum of the squares of the first ten natural numbers is,
    
    1^2 + 2^2 + ... + 10^2 = 385
    
    The square of the sum of the first ten natural numbers is,
    
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.
    
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    
    Answer: 867380888952c39a131fe1d832246ecc
"""
from common import check

PROBLEM_NUMBER = 6
ANSWER_HASH = "867380888952c39a131fe1d832246ecc"

# First find sum of each squared
sum_individually_squared = 0
for i in range(1, 101):
    sum_individually_squared = sum_individually_squared + i * i

# Next find sum of all squared
sum_global_squared = 0
for i in range(1, 101):
    sum_global_squared += i
sum_global_squared = sum_global_squared * sum_global_squared

difference = sum_global_squared - sum_individually_squared

check(difference, PROBLEM_NUMBER, ANSWER_HASH)