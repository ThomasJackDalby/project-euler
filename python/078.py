"""
    Problem 78
    ==========
    
    Let p(n) represent the number of different ways in which n coins can be
    separated into piles. For example, five coins can separated into piles in
    exactly seven different ways, so p(5)=7.
    
    OOOOO
    
    OOOO   O
    
    OOO   OO
    
    OOO   O   O
    
    OO   OO   O
    
    OO   O   O   O
    
    O   O   O   O   O
    
    Find the least value of n for which p(n) is divisible by one million.
    
    Answer: ef2a8695e428116131cc94c651d0e566
    
"""
from common import check

PROBLEM_NUMBER = 78
ANSWER_HASH = "ef2a8695e428116131cc94c651d0e566"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
