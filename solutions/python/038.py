"""
    Problem 38
    ==========
    
    
    Take the number 192 and multiply it by each of 1, 2, and 3:
    
    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)
    
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).
    
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    
    
    Answer: f2a29ede8dc9fae7926dc7a4357ac25e
"""
from common import check

PROBLEM_NUMBER = 38
ANSWER_HASH = "f2a29ede8dc9fae7926dc7a4357ac25e"

# largest pandigital is 987654321

# acheive by concatanation

# K x 1 = 987
# K x 2 = 654

DIGITS = "123456789"

k = 1
keep_searching = True
results = []
while keep_searching:
    P = ""
    n = 1
    if len(str(k)) >= 5:
        keep_searching = False

    while True:
        p = k * n
        n += 1
        p_str = str(p)
        P += p_str
        if len(P) == 9:
            if all((d in P for d in DIGITS)):
                print(f"{k} : 1..{n-1} : {P}")
                results.append(int(P))
            break
        elif len(P) > 9:
            if n == 2:
                keep_searching = False
            break
    k += 1

check(max(results), PROBLEM_NUMBER, ANSWER_HASH)
