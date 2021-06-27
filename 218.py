"""
    Problem 218
    ===========
    
    Consider the right angled triangle with sides a=7, b=24 and c=25.The area
    of this triangle is 84, which is divisible by the perfect numbers 6 and
    28.
    Moreover it is a primitive right angled triangle as gcd(a,b)=1 and
    gcd(b,c)=1.
    Also c is a perfect square.
    
    We will call a right angled triangle perfect if
    -it is a primitive right angled triangle
    -its hypotenuse is a perfect square
    
    We will call a right angled triangle super-perfect if
    -it is a perfect right angled triangle and
    -its area is a multiple of the perfect numbers 6 and 28.
    
    How many perfect right-angled triangles with c≤10^16 exist that are not
    super-perfect?
    
    Answer: cfcd208495d565ef66e7dff9f98764da
    
"""
from common import check

PROBLEM_NUMBER = 218
ANSWER_HASH = "cfcd208495d565ef66e7dff9f98764da"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
