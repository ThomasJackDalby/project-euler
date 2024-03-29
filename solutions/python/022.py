"""
    Problem 22
    ==========
    
    Using names.txt, a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.
    
    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.
    
    What is the total of all the name scores in the file?
    
    Visible links
    1. names.txt
    Answer: f2c9c91cb025746f781fa4db8be3983f
"""
from common import check
import os

PROBLEM_NUMBER = 22
ANSWER_HASH = "f2c9c91cb025746f781fa4db8be3983f"
FILE_NAME = "p022_names.txt"

file_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def get_score(text):
    return sum((ord(c)-96 for c in text.lower()))

with open(file_path, "r") as file:
    lines = file.readlines()
    names = [name.strip("\"") for line in lines for name in line.split(",")]
    names.sort()

total = 0
for i, name in enumerate(names):
    score = get_score(name)
    total += score * (i+1)

check(total, PROBLEM_NUMBER, ANSWER_HASH)
