"""
    Problem 89
    ==========
    
    The rules for writing Roman numerals allow for many ways of writing each
    number (see [1]About Roman Numerals...). However, there is always a "best"
    way of writing a particular number.
    
    For example, the following represent all of the legitimate ways of writing
    the number sixteen:
    
    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI
    
    The last example being considered the most efficient, as it uses the least
    number of numerals.
    
    The 11K text file, [2]roman.txt, contains one thousand numbers written in
    valid, but not necessarily minimal, Roman numerals; that is, they are
    arranged in descending units and obey the subtractive pair rule (see
    [3]About Roman Numerals... for the definitive rules for this problem).
    
    Find the number of characters saved by writing each of these in their
    minimal form.
    
    Note: You can assume that all the Roman numerals in the file contain no
    more than four consecutive identical units.
    
    Visible links
    1. about=roman_numerals
    2. roman.txt
    3. about=roman_numerals
    Answer: 5c572eca050594c7bc3c36e7e8ab9550
    
"""
from common import check

PROBLEM_NUMBER = 89
ANSWER_HASH = "5c572eca050594c7bc3c36e7e8ab9550"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
