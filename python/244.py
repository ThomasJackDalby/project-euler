"""
    Problem 244
    ===========
    
    You probably know the game Fifteen Puzzle. Here, instead of numbered
    tiles, we have seven red tiles and eight blue tiles.
    
    A move is denoted by the uppercase initial of the direction (Left, Right,
    Up, Down) in which the tile is slid, e.g. starting from configuration (S),
    by the sequence LULUR we reach the configuration (E):
    
    (S)                   , (E)
    
    For each path, its checksum is calculated by (pseudocode):
    checksum = 0
    checksum = (checksum × 243 + m[1]) mod 100 000 007
    checksum = (checksum × 243 + m[2]) mod 100 000 007
    …
    checksum = (checksum × 243 + m[n]) mod 100 000 007
    where m[k] is the ASCII value of the k^th letter in the move sequence and
    the ASCII values for the moves are:
    
    ┌──────┬─────┐
    │L     │76   │
    ├──────┼─────┤
    │R     │82   │
    ├──────┼─────┤
    │U     │85   │
    ├──────┼─────┤
    │D     │68   │
    └──────┴─────┘
    
    For the sequence LULUR given above, the checksum would be 19761398.
    
    Now, starting from configuration (S),find all shortest ways to reach
    configuration (T).
    
    (S)                   , (T)
    
    What is the sum of all checksums for the paths having the minimal length?
    
    p_244_start.gif
    p_244_example.gif
    p_244_start.gif
    p_244_target.gif
    Answer: f8fd502ec1d0084a79d43d9dc5bd3a3d
    
"""
from common import check

PROBLEM_NUMBER = 244
ANSWER_HASH = "f8fd502ec1d0084a79d43d9dc5bd3a3d"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
