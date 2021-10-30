"""
    Problem 396
    ===========
    
    For any positive integer n, the nth weak Goodstein sequence {g[1], g[2],
    g[3], ...} is defined as:
    
    • g[1] = n
    • for k > 1, g[k] is obtained by writing g[k-1] in base k, interpreting
    it as a base k + 1 number, and subtracting 1.
    
    The sequence terminates when g[k] becomes 0.
    
    For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:
    
    • g[1] = 6.
    • g[2] = 11 since 6 = 110[2], 110[3] = 12, and 12 - 1 = 11.
    • g[3] = 17 since 11 = 102[3], 102[4] = 18, and 18 - 1 = 17.
    • g[4] = 25 since 17 = 101[4], 101[5] = 26, and 26 - 1 = 25.
    
    and so on.
    
    It can be shown that every weak Goodstein sequence terminates.
    
    Let G(n) be the number of nonzero elements in the nth weak Goodstein
    sequence.
    It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
    It can also be verified that ΣG(n) = 2517 for 1 ≤ n < 8.
    
    Find the last 9 digits of ΣG(n) for 1 ≤ n < 16.
    
    Answer: 4665c73fdca473ccc0643fc982f24e06
    
"""
from common import check

PROBLEM_NUMBER = 396
ANSWER_HASH = "4665c73fdca473ccc0643fc982f24e06"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
