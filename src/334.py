"""
    Problem 334
    ===========
    
    In Plato's heaven, there exist an infinite number of bowls in a straight
    line.
    Each bowl either contains some or none of a finite number of beans.
    A child plays a game, which allows only one kind of move: removing two
    beans from any bowl, and putting one in each of the two adjacent bowls.
    The game ends when each bowl contains either one or no beans.
    
    For example, consider two adjacent bowls containing 2 and 3 beans
    respectively, all other bowls being empty. The following eight moves will
    finish the game:
    
    You are given the following sequences:
    
    t[0] = 123456.
    
    t[i-1] ,         if t[i-1] is even
    t[i] =   2
    t[i-1]   926252, if t[i-1] is odd
    2
    where ⌊x⌋ is the floor function
    and is the bitwise XOR operator.
    
    b[i] = ( t[i] mod 2^11) + 1.
    
    The first two terms of the last sequence are b[1] = 289 and b[2] = 145.
    If we start with b[1] and b[2] beans in two adjacent bowls, 3419100 moves
    would be required to finish the game.
    
    Consider now 1500 adjacent bowls containing b[1], b[2],..., b[1500] beans
    respectively, all other bowls being empty. Find how many moves it takes
    before the game ends.
    
    p_334_beans.gif
    p_334_cases.gif
    p_334_lfloor.gif
    p_334_rfloor.gif
    p_334_oplus.gif
    Answer: 71851da3058acf6b74e90251bdf4aa8f
    
"""
from common import check

PROBLEM_NUMBER = 334
ANSWER_HASH = "71851da3058acf6b74e90251bdf4aa8f"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
