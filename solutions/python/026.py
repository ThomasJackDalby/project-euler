# COMPLETED
"""
    Problem 26
    ==========
    
    
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:
    
    1/2  =  0.5
    1/3  =  0.(3)
    1/4  =  0.25
    1/5  =  0.2
    1/6  =  0.1(6)
    1/7  =  0.(142857)
    1/8  =  0.125
    1/9  =  0.(1)
    1/10 =  0.1
    
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.
    
    Find the value of d < 1000 for which ^1/[d] contains the longest recurring
    cycle in its decimal fraction part.
    
    
    Answer: 6aab1270668d8cac7cef2566a1c5f569
"""
from typing import DefaultDict
from common import check

PROBLEM_NUMBER = 26
ANSWER_HASH = "6aab1270668d8cac7cef2566a1c5f569"
DECIMALS = 2000
MAX_NUMBER = 1000

def accurate_divide(d, decimals):
    return f"0.{10 ** decimals // d}"

def calculate(d):
    decimal = accurate_divide(d, DECIMALS)
    for i, c_i in enumerate(decimal):
        if i == 0:
            continue

        for j, c_j in enumerate(decimal[:i]):
            if c_j == c_i:
                pattern = decimal[j:i]
                if len(pattern) > len(decimal) - i:
                    continue

                valid = True
                for k, c_k in enumerate(decimal[i:]):
                    if c_k != pattern[k % len(pattern)]:
                        valid = False
                        break
                if valid:
                    return pattern
    return None

max_d = None
max_length = 0
max_pattern = None
for d in range(1, MAX_NUMBER):
    pattern = calculate(d)
    if pattern is None:
        continue
    if len(pattern) > max_length:
        max_length = len(pattern)
        max_d = d
        max_pattern = pattern

check(max_d, PROBLEM_NUMBER, ANSWER_HASH)
