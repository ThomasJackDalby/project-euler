"""
    Problem 383
    ===========
    
    Let f[5](n) be the largest integer x for which 5^x divides n.
    For example, f[5](625000) = 7.
    
    Let T[5](n) be the number of integers i which satisfy f[5]((2·i-1)!) <
    2·f[5](i!) and 1 ≤ i ≤ n.
    It can be verified that T[5](10^3) = 68 and T[5](10^9) = 2408210.
    
    Find T[5](10^18).
    
    Answer: c1bc7c945344e1967bfaced9ade895a0
    
"""
from common import check

PROBLEM_NUMBER = 383
ANSWER_HASH = "c1bc7c945344e1967bfaced9ade895a0"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
