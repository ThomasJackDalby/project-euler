"""
    Problem 438
    ===========
    
    For an n-tuple of integers t = (a[1], ..., a[n]), let (x[1], ..., x[n]) be
    the solutions of the polynomial equation x^n + a[1]x^n-1 + a[2]x^n-2 + ...
    + a[n-1]x + a[n] = 0.
    
    Consider the following two conditions:
    
    • x[1], ..., x[n] are all real.
    • If x[1], ..., x[n] are sorted, ⌊x[i]⌋ = i for 1 ≤ i ≤ n. (⌊·⌋: floor
    function.)
    
    In the case of n = 4, there are 12 n-tuples of integers which satisfy both
    conditions.
    We define S(t) as the sum of the absolute values of the integers in t.
    For n = 4 we can verify that ∑S(t) = 2087 for all n-tuples t which satisfy
    both conditions.
    
    Find ∑S(t) for n = 7.
    
    Answer: ?
    
"""
from common import check

PROBLEM_NUMBER = 438
ANSWER_HASH = "?"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
