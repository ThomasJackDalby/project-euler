"""
    Problem 186
    ===========
    
    Here are the records from a busy telephone system with one million users:
    
    ┌─────────────────┬─────────┬─────────┐
    │RecNr            │ Caller  │ Called  │
    ├─────────────────┼─────────┼─────────┤
    │        1        │ 200007  │ 100053  │
    ├─────────────────┼─────────┼─────────┤
    │        2        │ 600183  │ 500439  │
    ├─────────────────┼─────────┼─────────┤
    │        3        │ 600863  │ 701497  │
    ├─────────────────┼─────────┼─────────┤
    │       ...       │   ...   │   ...   │
    └─────────────────┴─────────┴─────────┘
    
    The telephone number of the caller and the called number in record n are
    Caller(n) = S[2n-1] and Called(n) = S[2n] where S[1,2,3,...] come from the
    "Lagged Fibonacci Generator":
    
    For 1 ≤ k ≤ 55, S[k] = [100003 - 200003k + 300007k^3] (modulo 1000000)
    For 56 ≤ k, S[k] = [S[k-24] + S[k-55]] (modulo 1000000)
    
    If Caller(n) = Called(n) then the user is assumed to have misdialled and
    the call fails; otherwise the call is successful.
    
    From the start of the records, we say that any pair of users X and Y are
    friends if X calls Y or vice-versa. Similarly, X is a friend of a friend
    of Z if X is a friend of Y and Y is a friend of Z; and so on for longer
    chains.
    
    The Prime Minister's phone number is 524287. After how many successful
    calls, not counting misdials, will 99% of the users (including the PM) be
    a friend, or a friend of a friend etc., of the Prime Minister?
    
    Answer: b21d68f1871abf1d5bbcf1206b3f1643
    
"""
from common import check

PROBLEM_NUMBER = 186
ANSWER_HASH = "b21d68f1871abf1d5bbcf1206b3f1643"

check(None, PROBLEM_NUMBER, ANSWER_HASH)