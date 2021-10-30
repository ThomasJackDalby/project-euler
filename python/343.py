"""
    Problem 343
    ===========
    
    For any positive integer k, a finite sequence a[i] of fractions x[i]/y[i]
    is defined by:
    a[1] = 1/k and
    a[i] = (x[i-1]+1)/(y[i-1]-1) reduced to lowest terms for i>1.
    When a[i] reaches some integer n, the sequence stops. (That is, when
    y[i]=1.)
    Define f(k) = n.
    For example, for k = 20:
    
    1/20 → 2/19 → 3/18 = 1/6 → 2/5 → 3/4 → 4/3 → 5/2 → 6/1 = 6
    
    So f(20) = 6.
    
    Also f(1) = 1, f(2) = 2, f(3) = 1 and Σf(k^3) = 118937 for 1 ≤ k ≤ 100.
    
    Find Σf(k^3) for 1 ≤ k ≤ 2×10^6.
    
    Answer: 0e10bd111425ad8e1343ac79dac7bb0e
    
"""
from common import check

PROBLEM_NUMBER = 343
ANSWER_HASH = "0e10bd111425ad8e1343ac79dac7bb0e"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
