"""
    Problem 258
    ===========
    
    A sequence is defined as:
    
    • g[k] = 1, for 0 ≤ k ≤ 1999
    • g[k] = g[k-2000] + g[k-1999], for k ≥ 2000.
    
    Find g[k] mod 20092010 for k = 10^18.
    
    Answer: 18eca0138f3acbde20dcc24ed06627ea
    
"""
from common import check

PROBLEM_NUMBER = 258
ANSWER_HASH = "18eca0138f3acbde20dcc24ed06627ea"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
