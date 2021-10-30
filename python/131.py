"""
    Problem 131
    ===========
    
    There are some prime values, p, for which there exists a positive integer,
    n, such that the expression n^3 + n^2p is a perfect cube.
    
    For example, when p = 19, 8^3 + 8^2×19 = 12^3.
    
    What is perhaps most surprising is that for each prime with this property
    the value of n is unique, and there are only four such primes below
    one-hundred.
    
    How many primes below one million have this remarkable property?
    
    Answer: f7e6c85504ce6e82442c770f7c8606f0
    
"""
from common import check

PROBLEM_NUMBER = 131
ANSWER_HASH = "f7e6c85504ce6e82442c770f7c8606f0"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
