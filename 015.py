"""
    Problem 15
    ==========
    
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.
    
    How many such routes are there through a 20×20 grid?
    
    p_015.gif
    Answer: 928f3957168ac592c4215dcd04e0b678
    
"""
from common import check

PROBLEM_NUMBER = 15
ANSWER_HASH = "928f3957168ac592c4215dcd04e0b678"

cache = {}

def calculate(x, y):
    if (x, y) == (1, 1):
        return 2
    elif (x, y) in cache:
        return cache[(x, y)]
    else:
        right = calculate(x-1, y) if x > 1 else 1
        down = calculate(x, y-1) if y > 1 else 1
        total = right + down
        cache[(x, y)] = total
        return total

result = calculate(20, 20)
check(result, PROBLEM_NUMBER, ANSWER_HASH)