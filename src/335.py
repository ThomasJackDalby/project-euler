"""
    Problem 335
    ===========
    
    Whenever Peter feels bored, he places some bowls, containing one bean
    each, in a circle. After this, he takes all the beans out of a certain
    bowl and drops them one by one in the bowls going clockwise. He repeats
    this, starting from the bowl he dropped the last bean in, until the
    initial situation appears again. For example with 5 bowls he acts as
    follows:
    
    So with 5 bowls it takes Peter 15 moves to return to the initial
    situation.
    
    Let M(x) represent the number of moves required to return to the initial
    situation, starting with x bowls. Thus, M(5) = 15. It can also be verified
    that M(100) = 10920.
    
    Find M(2^k+1). Give your answer modulo 7^9.
    
    p_335_mancala.gif
    p_335_sum.gif
    Answer: 9a519cfa0ebdd4d1dd318f14b5799eea
    
"""
from common import check

PROBLEM_NUMBER = 335
ANSWER_HASH = "9a519cfa0ebdd4d1dd318f14b5799eea"

check(None, PROBLEM_NUMBER, ANSWER_HASH)