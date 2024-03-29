# COMPLETED
"""
    Problem 12
    ==========
    
    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7^th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
    28. The first ten terms would be:
    
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    
    Let us list the factors of the first seven triangle numbers:
    
    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    
    We can see that 28 is the first triangle number to have over five
    divisors.
    
    What is the value of the first triangle number to have over five hundred
    divisors?
    
    Answer: 8091de7d285989bbfa9a2f9f3bdcc7c0
    
"""
from common import check, get_factors

PROBLEM_NUMBER = 12
ANSWER_HASH = "8091de7d285989bbfa9a2f9f3bdcc7c0"

def calculate(minimum_number_of_factors):
    i = 1
    previous = 0
    while True:
        current = previous + i
        if current > minimum_number_of_factors and len(get_factors(current)) > minimum_number_of_factors:
            return current
        previous = current
        i += 1
        
def main():
    result = calculate(500)
    check(result, PROBLEM_NUMBER, ANSWER_HASH)

if __name__ == "__main__":
    main()