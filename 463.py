"""
    Problem 463
    ===========
    
    The function $f$ is defined for all positive integers as follows:
    
    • $f(1)=1$
    • $f(3)=3$
    • $f(2n)=f(n)$
    • $f(4n + 1)=2f(2n + 1) - f(n)$
    • $f(4n + 3)=3f(2n + 1) - 2f(n)$
    
    The function $S(n)$ is defined as $\sum_{i=1}^{n}f(i)$.
    
    $S(8)=22$ and $S(100)=3604$.
    
    Find $S(3^{37})$. Give the last 9 digits of your answer.
    
    Answer: 95481696a65b0c1d9f73186a693686f5
    
"""
from common import check

PROBLEM_NUMBER = 463
ANSWER_HASH = "95481696a65b0c1d9f73186a693686f5"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
