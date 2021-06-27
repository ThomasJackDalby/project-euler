"""
    Problem 448
    ===========
    
    The function lcm(a,b) denotes the least common multiple of a and b.
    Let A(n) be the average of the values of lcm(n,i) for 1≤i≤n.
    E.g: A(2)=(2+2)/2=2 and A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32.
    
    Let S(n)=∑A(k) for 1≤k≤n.
    S(100)=122726.
    
    Find S(99999999019) mod 999999017.
    
    Answer: e6e7e87005c7b070cbc08ce727ae4e6a
    
"""
from common import check

PROBLEM_NUMBER = 448
ANSWER_HASH = "e6e7e87005c7b070cbc08ce727ae4e6a"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
