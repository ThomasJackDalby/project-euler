# COMPLETED
"""
    Problem 18
    ==========
    
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
    
    3
    7 4
    2 4 6
    8 5 9 3
    
    That is, 3 + 7 + 4 + 9 = 23.
    
    Find the maximum total from top to bottom of the triangle below:
    
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    
    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, [1]Problem 67, is the same challenge with
    a triangle containing one-hundred rows; it cannot be solved by brute
    force, and requires a clever method! ;o)
    
    Visible links
    1. problem=67
    Answer: 708f3cf8100d5e71834b1db77dfa15d6
    
"""
from common import check

PROBLEM_NUMBER = 18
ANSWER_HASH = "708f3cf8100d5e71834b1db77dfa15d6"

triangle = [
    "75",
    "95 64",
    "17 47 82",
    "18 35 87 10",
    "20 04 82 47 65",
    "19 01 23 75 03 34",
    "88 02 77 73 07 63 67",
    "99 65 04 28 06 16 70 92",
    "41 41 26 56 83 40 80 70 33",
    "41 48 72 33 47 32 37 16 94 29",
    "53 71 44 65 25 43 91 52 97 51 14",
    "70 11 33 28 77 73 17 78 39 68 17 57",
    "91 71 52 38 17 14 91 43 58 50 27 29 48",
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
]
triangle = [[int(c) for c in row.split()] for row in triangle]

cache = { }

def calculate(row, column):
    if row == len(triangle)-1:
        return triangle[row][column]
    elif (row, column) in cache:
        return cache[(row, column)]
    else:
        a = triangle[row][column]
        b = calculate(row+1, column)
        c = calculate(row+1, column+1)
        value = a + max(b, c)
        cache[(row, column)] = value
        return value

result = calculate(0, 0)
check(result, PROBLEM_NUMBER, ANSWER_HASH)
