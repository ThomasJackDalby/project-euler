"""
    Problem 160
    ===========
    
    For any N, let f(N) be the last five digits before the trailing zeroes in
    N!.
    For example,
    
    9! = 362880 so f(9)=36288
    10! = 3628800 so f(10)=36288
    20! = 2432902008176640000 so f(20)=17664
    
    Find f(1,000,000,000,000)
    
    Answer: e51ada1e23f810eb1b51a18bb6825f85
    
"""
from common import check

PROBLEM_NUMBER = 160
ANSWER_HASH = "e51ada1e23f810eb1b51a18bb6825f85"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
