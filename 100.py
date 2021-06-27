"""
    Problem 100
    ===========
    
    If a box contains twenty-one coloured discs, composed of fifteen blue
    discs and six red discs, and two discs were taken at random, it can be
    seen that the probability of taking two blue discs, P(BB) =
    (15/21)×(14/20) = 1/2.
    
    The next such arrangement, for which there is exactly 50% chance of taking
    two blue discs at random, is a box containing eighty-five blue discs and
    thirty-five red discs.
    
    By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
    discs in total, determine the number of blue discs that the box would
    contain.
    
    Answer: 21156e3acc4ca35b7a318c541a0648d5
    
"""
from common import check

PROBLEM_NUMBER = 100
ANSWER_HASH = "21156e3acc4ca35b7a318c541a0648d5"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
