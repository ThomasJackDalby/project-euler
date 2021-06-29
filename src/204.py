"""
    Problem 204
    ===========
    
    A Hamming number is a positive number which has no prime factor larger
    than 5.
    So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
    There are 1105 Hamming numbers not exceeding 10^8.
    
    We will call a positive number a generalised Hamming number of type n, if
    it has no prime factor larger than n.
    Hence the Hamming numbers are the generalised Hamming numbers of type 5.
    
    How many generalised Hamming numbers of type 100 are there which don't
    exceed 10^9?
    
    Answer: 4118ffb9edc56a033b5b27ca0bf34366
    
"""
from common import check

PROBLEM_NUMBER = 204
ANSWER_HASH = "4118ffb9edc56a033b5b27ca0bf34366"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
