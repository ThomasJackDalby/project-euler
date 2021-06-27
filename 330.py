"""
    Problem 330
    ===========
    
    An infinite sequence of real numbers a(n) is defined for all integers n as
    follows:
    
    For example,
    
    a(0) = 1  + 1  + 1  + ... = e − 1
    1!   2!   3!
    
    a(1) = e − 1 + 1  + 1  + ... = 2e − 3
    1!      2!   3!
    
    a(2) = 2e − 3 + e − 1 + 1  + ... = 7 e − 6
    1!       2!      3!         2
    
    with e = 2.7182818... being Euler's constant.
    
    It can be shown that a(n) is of  A(n) e + B(n) for integers A(n) and B(n).
    the form                         n!
    
    For example a(10) = 328161643 e − 652694486 .
    10!
    
    Find A(10^9) + B(10^9) and give your answer mod 77 777 777.
    
    p_330_formula.gif
    Answer: d385d3fe0995b48a782a91477525b154
    
"""
from common import check

PROBLEM_NUMBER = 330
ANSWER_HASH = "d385d3fe0995b48a782a91477525b154"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
