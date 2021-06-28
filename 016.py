"""
    Problem 16
    ==========
    
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    
    What is the sum of the digits of the number 2^1000?
    
    Answer: 6a5889bb0190d0211a991f47bb19a777
    
"""
from common import check
p013 = __import__('013')

PROBLEM_NUMBER = 16
ANSWER_HASH = "6a5889bb0190d0211a991f47bb19a777"

def square(a):
    p013.add()

check(None, PROBLEM_NUMBER, ANSWER_HASH)
