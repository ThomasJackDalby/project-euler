"""
    Problem 83
    ==========
    
    NOTE: This problem is a significantly more challenging version of
    [1]Problem 81.
    
    In the 5 by 5 matrix below, the minimal path sum from the top left to the
    bottom right, by moving left, right, up, and down, is indicated in bold
    red and is equal to 2297.
    
    131 673 234 103 18
    201 96  342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524 37  331
    
    Find the minimal path sum, in [2]matrix.txt, a 31K text file containing a
    80 by 80 matrix, from the top left to the bottom right by moving left,
    right, up, and down.
    
    Visible links
    1. problem=81
    2. matrix.txt
    Answer: 61b28c4fbe8560003ee50fa5619d7a1e
    
"""
from common import check

PROBLEM_NUMBER = 83
ANSWER_HASH = "61b28c4fbe8560003ee50fa5619d7a1e"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
