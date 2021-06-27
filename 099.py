"""
    Problem 99
    ==========
    
    Comparing two numbers written in index form like 2^11 and 3^7 is not
    difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
    
    However, confirming that 632382^518061 > 519432^525806 would be much more
    difficult, as both numbers contain over three million digits.
    
    Using [1]base_exp.txt, a 22K text file containing one thousand lines with
    a base/exponent pair on each line, determine which line number has the
    greatest numerical value.
    
    NOTE: The first two lines in the file represent the numbers in the example
    given above.
    
    Visible links
    1. base_exp.txt
    Answer: 1ecfb463472ec9115b10c292ef8bc986
    
"""
from common import check

PROBLEM_NUMBER = 99
ANSWER_HASH = "1ecfb463472ec9115b10c292ef8bc986"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
