"""
    Problem 117
    ===========
    
    Using a combination of black square tiles and oblong tiles chosen from:
    red tiles measuring two units, green tiles measuring three units, and blue
    tiles measuring four units, it is possible to tile a row measuring five
    units in length in exactly fifteen different ways.
    
    ┌╥╥╥╥┐  ┌─╥╥╥┐  ┌╥─╥╥┐  ┌╥╥─╥┐
    └╨╨╨╨┘  └─╨╨╨┘  └╨─╨╨┘  └╨╨─╨┘
    
    ┌╥╥╥─┐  ┌─╥─╥┐  ┌─╥╥─┐  ┌╥─╥─┐
    └╨╨╨─┘  └─╨─╨┘  └─╨╨─┘  └╨─╨─┘
    
    ┌──╥╥┐  ┌╥──╥┐  ┌╥╥──┐  ┌─╥──┐
    └──╨╨┘  └╨──╨┘  └╨╨──┘  └─╨──┘
    
    ┌──╥─┐  ┌───╥┐  ┌╥───┐
    └──╨─┘  └───╨┘  └╨───┘
    
    How many ways can a row measuring fifty units in length be tiled?
    
    NOTE: This is related to [1]Problem 116.
    
    Visible links
    1. problem=116
    Answer: 542612809b3dd08cf518b85450fce8d6
    
"""
from common import check

PROBLEM_NUMBER = 117
ANSWER_HASH = "542612809b3dd08cf518b85450fce8d6"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
