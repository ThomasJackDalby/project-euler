"""
    Problem 428
    ===========
    
    Let a, b and c be positive numbers.
    Let W, X, Y, Z be four collinear points where |WX| = a, |XY| = b, |YZ| = c
    and |WZ| = a + b + c.
    Let C[in] be the circle having the diameter XY.
    Let C[out] be the circle having the diameter WZ.
    
    The triplet (a, b, c) is called a necklace triplet if you can place k ≥ 3
    distinct circles C[1], C[2], ..., C[k] such that:
    
    • C[i] has no common interior points with any C[j] for 1 ≤ i, j ≤ k and
    i ≠ j,
    • C[i] is tangent to both C[in] and C[out] for 1 ≤ i ≤ k,
    • C[i] is tangent to C[i+1] for 1 ≤ i < k, and
    • C[k] is tangent to C[1].
    
    For example, (5, 5, 5) and (4, 3, 21) are necklace triplets, while it can
    be shown that (2, 2, 5) is not.
    
    Let T(n) be the number of necklace triplets (a, b, c) such that a, b and c
    are positive integers, and b ≤ n.For example, T(1) = 9, T(20) = 732 and
    T(3000) = 438106.
    
    Find T(1 000 000 000).
    
    Answer: c6010c109b66b34bf3594e63eb58b446
    
"""
from common import check

PROBLEM_NUMBER = 428
ANSWER_HASH = "c6010c109b66b34bf3594e63eb58b446"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
