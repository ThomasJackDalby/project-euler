"""
    Problem 368
    ===========
    
    The harmonic series 1 + 1 + 1 + 1 + ... is well known to be divergent.
    2   3   4
    
    If we however omit from this series every term where the denominator has a
    9 in it, the series remarkably enough converges to approximately
    22.9206766193.
    This modified harmonic series is called the Kempner series.
    
    Let us now consider another modified harmonic series by omitting from the
    harmonic series every term where the denominator has 3 or more equal
    consecutive digits.One can verify that out of the first 1200 terms of the
    harmonic series, only 20 terms will be omitted.
    These 20 omitted terms are:
    
    1   , 1   , 1   , 1   , 1   , 1   , 1   , 1   , 1   , 1    , 1    ,
    111   222   333   444   555   666   777   888   999   1000   1110
    
    1    , 1    , 1    , 1    , 1    , 1    , 1    , 1    and 1    .
    1111   1112   1113   1114   1115   1116   1117   1118     1119
    
    This series converges as well.
    
    Find the value the series converges to.
    Give your answer rounded to 10 digits behind the decimal point.
    
    Answer: bfb15c388f4721cbd5eb89f17be2eef2
    
"""
from common import check

PROBLEM_NUMBER = 368
ANSWER_HASH = "bfb15c388f4721cbd5eb89f17be2eef2"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
