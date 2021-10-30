"""
    Problem 98
    ==========
    
    By replacing each of the letters in the word CARE with 1, 2, 9, and 6
    respectively, we form a square number: 1296 = 36^2. What is remarkable is
    that, by using the same digital substitutions, the anagram, RACE, also
    forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square
    anagram word pair and specify further that leading zeroes are not
    permitted, neither may a different letter have the same digital value as
    another letter.
    
    Using [1]words.txt, a 16K text file containing nearly two-thousand common
    English words, find all the square anagram word pairs (a palindromic word
    is NOT considered to be an anagram of itself).
    
    What is the largest square number formed by any member of such a pair?
    
    NOTE: All anagrams formed must be contained in the given text file.
    
    Visible links
    1. words.txt
    Answer: 36b3b5f54143786b7ab2ebb6bcd06e75
    
"""
from common import check

PROBLEM_NUMBER = 98
ANSWER_HASH = "36b3b5f54143786b7ab2ebb6bcd06e75"

check(None, PROBLEM_NUMBER, ANSWER_HASH)
