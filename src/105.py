"""
    Problem 105
    ===========
    
    Let S(A) represent the sum of elements in set A of size n. We shall call
    it a special sum set if for any two non-empty disjoint subsets, B and C,
    the following properties are true:
    
    i. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    ii. If B contains more elements than C then S(B) > S(C).
    
    For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set
    because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159,
    161, 139, 158} satisfies both rules for all possible subset pair
    combinations and S(A) = 1286.
    
    Using [1]sets.txt (right click and "Save Link/Target As..."), a 4K text
    file with one-hundred sets containing seven to twelve elements (the two
    examples given above are the first two sets in the file), identify all the
    special sum sets, A[1], A[2], ..., A[k], and find the value of S(A[1]) +
    S(A[2]) + ... + S(A[k]).
    
    NOTE: This problem is related to [2]Problem 103 and [3]Problem 106.
    
    Visible links
    1. sets.txt
    2. problem=103
    3. problem=106
    Answer: c87d30e494eff438fe37b4c810167da0
    
"""
from common import check

PROBLEM_NUMBER = 105
ANSWER_HASH = "c87d30e494eff438fe37b4c810167da0"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
