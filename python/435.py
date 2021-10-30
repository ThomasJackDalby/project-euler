"""
    Problem 435
    ===========
    
    The Fibonacci numbers {f[n], n ≥ 0} are defined recursively as f[n] =
    f[n-1] + f[n-2] with base cases f[0] = 0 and f[1] = 1.
    
    Define the polynomials {F[n], n ≥ 0} as F[n](x) = ∑f[i]x^i for 0 ≤ i ≤ n.
    
    For example, F[7](x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7, and
    F[7](11) = 268357683.
    
    Let n = 10^15. Find the sum [∑[0≤x≤100] F[n](x)] mod 1307674368000 (=
    15!).
    
    Answer: 0f08231a97e872f565a085de75743a1c
    
"""
from common import check

PROBLEM_NUMBER = 435
ANSWER_HASH = "0f08231a97e872f565a085de75743a1c"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
