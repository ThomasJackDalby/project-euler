"""
    Problem 113
    ===========
    
    Working from left-to-right if no digit is exceeded by the digit to its
    left it is called an increasing number; for example, 134468.
    
    Similarly if no digit is exceeded by the digit to its right it is called a
    decreasing number; for example, 66420.
    
    We shall call a positive integer that is neither increasing nor decreasing
    a "bouncy" number; for example, 155349.
    
    As n increases, the proportion of bouncy numbers below n increases such
    that there are only 12951 numbers below one-million that are not bouncy
    and only 277032 non-bouncy numbers below 10^10.
    
    How many numbers below a googol (10^100) are not bouncy?
    
    Answer: a9e504ee704c87f9bddad6d3ffe39532
    
"""
from common import check

PROBLEM_NUMBER = 113
ANSWER_HASH = "a9e504ee704c87f9bddad6d3ffe39532"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
