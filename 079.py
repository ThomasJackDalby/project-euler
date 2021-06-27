"""
    Problem 79
    ==========
    
    A common security method used for online banking is to ask the user for
    three random characters from a passcode. For example, if the passcode was
    531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
    reply would be: 317.
    
    The text file, [1]keylog.txt, contains fifty successful login attempts.
    
    Given that the three characters are always asked for in order, analyse the
    file so as to determine the shortest possible secret passcode of unknown
    length.
    
    Visible links
    1. keylog.txt
    Answer: 3ccc6e16d99b21d42948f6d49b90fa30
    
"""
from common import check

PROBLEM_NUMBER = 79
ANSWER_HASH = "3ccc6e16d99b21d42948f6d49b90fa30"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
