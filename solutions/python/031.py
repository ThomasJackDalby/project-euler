"""
    Problem 31
    ==========
    
    
    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:
    
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    
    It is possible to make £2 in the following way:
    
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    
    How many different ways can £2 be made using any number of coins?
    
    
    Answer: 142dfe4a33d624d2b830a9257e96726d
"""
from common import check

PROBLEM_NUMBER = 31
ANSWER_HASH = "142dfe4a33d624d2b830a9257e96726d"
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def get_permutations(value, coins):
    if len(coins) == 0:
        return None
    coin = coins[0]
    if len(coins) == 1:
        if value % coin == 0:
            yield { coin : value // coin } 
        else:
            return None
    else:
        amount = 0
        while value >= 0:
            for permutation in (p for p in get_permutations(value, coins[1:]) if p is not None):
                permutation.update({ coin : amount })
                yield permutation
            amount += 1
            value -= coin

result = len(list(get_permutations(200, COINS)))
check(result, PROBLEM_NUMBER, ANSWER_HASH)
