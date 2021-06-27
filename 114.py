"""
    Problem 114
    ===========
    
    A row measuring seven units in length has red blocks with a minimum length
    of three units placed on it, such that any two red blocks (which are
    allowed to be different lengths) are separated by at least one black
    square. There are exactly seventeen ways of doing this.
    
    ┌┬┬┬┬┬┬┐  ┌──┬┬┬┬┐  ┌┬──┬┬┬┐
    └┴┴┴┴┴┴┘  └──┴┴┴┴┘  └┴──┴┴┴┘
    ┌┬┬──┬┬┐  ┌┬┬┬──┬┐  ┌┬┬┬┬──┐
    └┴┴──┴┴┘  └┴┴┴──┴┘  └┴┴┴┴──┘
    ┌──┬┬──┐  ┌───┬┬┬┐  ┌┬───┬┬┐
    └──┴┴──┘  └───┴┴┴┘  └┴───┴┴┘
    ┌┬┬───┬┐  ┌┬┬┬───┐  ┌────┬┬┐
    └┴┴───┴┘  └┴┴┴───┘  └────┴┴┘
    ┌┬────┬┐  ┌┬┬────┐  ┌─────┬┐
    └┴────┴┘  └┴┴────┘  └─────┴┘
    ┌┬─────┐  ┌──────┐
    └┴─────┘  └──────┘
    
    How many ways can a row measuring fifty units in length be filled?
    
    NOTE: Although the example above does not lend itself to the possibility,
    in general it is permitted to mix block sizes. For example, on a row
    measuring eight units in length you could use red (3), black (1), and red
    (4).
    
    Answer: de48ca72bf252a8be7e0aad762eadcf8
    
"""
from common import check

PROBLEM_NUMBER = 114
ANSWER_HASH = "de48ca72bf252a8be7e0aad762eadcf8"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
