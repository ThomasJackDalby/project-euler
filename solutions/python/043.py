"""
    Problem 43
    ==========
    
    
    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.
    
    Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
    way, we note the following:
    
    • d[2]d[3]d[4]=406 is divisible by 2
    • d[3]d[4]d[5]=063 is divisible by 3
    • d[4]d[5]d[6]=635 is divisible by 5
    • d[5]d[6]d[7]=357 is divisible by 7
    • d[6]d[7]d[8]=572 is divisible by 11
    • d[7]d[8]d[9]=728 is divisible by 13
    • d[8]d[9]d[10]=289 is divisible by 17
    
    Find the sum of all 0 to 9 pandigital numbers with this property.
    
    
    Answer: 115253b7721af0fdff25cd391dfc70cf
"""
from common import check
from itertools import permutations

PROBLEM_NUMBER = 43
ANSWER_HASH = "115253b7721af0fdff25cd391dfc70cf"
PRIMES = [2, 3, 5, 7, 11, 13, 17]

result = 0
for perm in permutations("1234567890"):
    d_str = "".join(perm)
    if d_str[0] == "0":
        continue
    
    valid = True
    for i, prime in enumerate(PRIMES):
        d_i = int(d_str[i+1]+d_str[i+2]+d_str[i+3])
        if d_i % prime != 0:
            valid = False
            break
    
    if valid:
        result += int(d_str)

check(result, PROBLEM_NUMBER, ANSWER_HASH)
