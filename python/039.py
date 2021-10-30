"""
    Problem 39
    ==========
    
    If p is the perimeter of a right angle triangle with integral length
    sides, {a,b,c}, there are exactly three solutions for p = 120.
    
    {20,48,52}, {24,45,51}, {30,40,50}
    
    For which value of p ≤ 1000, is the number of solutions maximised?
    
    Answer: fa83a11a198d5a7f0bf77a1987bcd006
    
"""
from common import check

PROBLEM_NUMBER = 39
ANSWER_HASH = "fa83a11a198d5a7f0bf77a1987bcd006"

solutions = [0] * 1001
for a in range(1, 1000):
    a2 = a**2
    for b in range(1, 1000):
        c2 = a2 + b**2

        c = int(c2**0.5)
        if not c**2 == c2:
            continue
        
        p = a + b + c
        if p > 1000:
            continue

        solutions[p] += 1

result = solutions.index(max(solutions))
print(result)
check(result, PROBLEM_NUMBER, ANSWER_HASH)
