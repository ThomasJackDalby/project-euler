"""
    Problem 305
    ===========
    
    Let's call S the (infinite) string that is made by concatenating the
    consecutive positive integers (starting from 1) written down in base 10.
    Thus, S = 1234567891011121314151617181920212223242...
    
    It's easy to see that any number will show up an infinite number of times
    in S.
    
    Let's call f(n) the starting position of the n^th occurrence of n in S.
    For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365.
    
    Find ∑f(3^k) for 1≤k≤13.
    
    Answer: 9def85298f598867d361e4afca8cdd96
    
"""
from common import check

PROBLEM_NUMBER = 305
ANSWER_HASH = "9def85298f598867d361e4afca8cdd96"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
